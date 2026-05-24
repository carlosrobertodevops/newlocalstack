#!/usr/bin/env bash
# Syncs post-image-build source patches into the running localstack-main
# container, patches the editable dist-info entry_points so plux discovers
# the ecr/ecs/eks/rds providers added in commit 23e3ec8, restarts the
# container, then commits the image so the changes survive `docker compose
# down && up` without bind-mounts.
#
# Run after editing:
#   - localstack-core/localstack/aws/api/{ecr,ecs,eks,rds}/
#   - localstack-core/localstack/aws/services/providers.py
#   - localstack-core/localstack/gcp/
#
# Usage:
#   bin/docker-sync.sh [container]
#
# Remove this script once the image is rebuilt via `make docker-build`.
set -euo pipefail

CONTAINER="${1:-localstack-main}"
IMAGE_TAG="${LOCALSTACK_IMAGE:-localstack/localstack-custom:dev}"
REPO_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
DEST=/opt/code/localstack/localstack-core/localstack
EP=/opt/code/localstack/.venv/lib/python3.13/site-packages/localstack_core-0.1.dev3.dist-info/entry_points.txt

if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
  echo "container ${CONTAINER} not running — start with: docker compose up -d localstack" >&2
  exit 1
fi

echo "[sync] copying ASF stubs ecr/ecs/eks/rds"
for svc in ecr ecs eks rds; do
  docker exec "${CONTAINER}" mkdir -p "${DEST}/aws/api/${svc}"
  docker cp "${REPO_ROOT}/localstack-core/localstack/aws/api/${svc}/." \
    "${CONTAINER}:${DEST}/aws/api/${svc}/"
done

echo "[sync] copying providers.py"
docker cp "${REPO_ROOT}/localstack-core/localstack/aws/services/providers.py" \
  "${CONTAINER}:${DEST}/aws/services/providers.py"

echo "[sync] copying gcp gateway + storage models"
docker cp "${REPO_ROOT}/localstack-core/localstack/gcp/gateway.py" \
  "${CONTAINER}:${DEST}/gcp/gateway.py"
docker cp "${REPO_ROOT}/localstack-core/localstack/gcp/services/storage/models.py" \
  "${CONTAINER}:${DEST}/gcp/services/storage/models.py"

echo "[sync] copying azure module (entra graph router, arm extras)"
docker cp "${REPO_ROOT}/localstack-core/localstack/azure/." \
  "${CONTAINER}:${DEST}/azure/"

echo "[sync] copying aws/handlers/multi_cloud.py (graph path routing)"
docker cp "${REPO_ROOT}/localstack-core/localstack/aws/handlers/multi_cloud.py" \
  "${CONTAINER}:${DEST}/aws/handlers/multi_cloud.py"

echo "[sync] patching entry_points (idempotent)"
docker exec "${CONTAINER}" python3 - <<PY
import re
path = "${EP}"
src = open(path).read()
add = (
    "ecr:default = localstack.aws.services.providers:ecr\n"
    "ecs:default = localstack.aws.services.providers:ecs\n"
    "eks:default = localstack.aws.services.providers:eks\n"
    "rds:default = localstack.aws.services.providers:rds\n"
)
if "ecr:default" in src:
    print("[entrypoints] already patched")
else:
    m = re.search(r"^\[localstack\.aws\.provider\]\n", src, re.M)
    if not m:
        raise SystemExit("[entrypoints] section not found")
    start = m.end()
    nxt = re.search(r"^\[", src[start:], re.M)
    end = start + nxt.start() if nxt else len(src)
    open(path, "w").write(src[:end] + add + src[end:])
    print("[entrypoints] applied")
PY

echo "[sync] purging __pycache__"
docker exec "${CONTAINER}" find ${DEST} -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null || true

echo "[sync] restarting container"
docker restart "${CONTAINER}" >/dev/null

echo "[sync] waiting for health"
for i in $(seq 1 30); do
  if curl -fsS -m 2 http://127.0.0.1:4566/_localstack/health 2>/dev/null \
      | grep -q '"ecr": "available"'; then
    echo "[sync] ecr available after ${i} polls"
    break
  fi
  sleep 2
done

echo "[sync] committing image ${IMAGE_TAG}"
docker commit "${CONTAINER}" "${IMAGE_TAG}" >/dev/null
docker tag "${IMAGE_TAG}" localstack/localstack-custom:latest

echo "[sync] done"
