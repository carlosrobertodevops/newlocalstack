# Refactor Status — 2026-05-25

Status vivo do refactor "Pragmatic Restructure" (Opção B aprovada).

Plano completo: [`docs/internal/superpowers/plans/2026-05-25-folder-refactor.md`](../docs/internal/superpowers/plans/2026-05-25-folder-refactor.md).

## Estado atual

```
Branch: new-localstack-v1
Commits aplicados:
  044963b  F1 follow-up — update refs in moved files
  92fe34a  F1 — root cleanup (requirements/, docker/, .planning/)
  26fdc03  F0 — fix .gitignore + commit stubs/plan
```

## Divisão em 10 tasks (5 fases × 2 subtasks)

| #   | Task                                                    | Fase | Status     | Subagents                                                                          | Commit            |
| --- | ------------------------------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------- | ----------------- |
| T1a | F1 commit root cleanup (validações)                     | F1   | ✓ done     | 5 verify (Makefile, pyproject, .dockerignore, CI, git integrity)                   | 92fe34a + 044963b |
| T1b | F1 sweep refs legacy `requirements-`/`DOCKER.md`        | F1   | ✓ done     | 5 scan (CLAUDE, AGENTS, README, TESTING_LOCAL, plans) — sem alterações necessárias | —                 |
| T2a | F2 git mv `docs/` → `{user,dev,internal,legal}/`        | F2   | ⏳ next    | 5 map (user-facing, dev, internal, orphans, cross-links)                           | —                 |
| T2b | F2 sweep links após docs move                           | F2   | ⏳ pending | 5 scan (CLAUDE, README, AGENTS, internal refs, fix dead)                           | —                 |
| T3a | F3 mover 13 dev scripts de `bin/` → `scripts/`          | F3   | ⏳ pending | 5 verify (Dockerfile, Makefile, CLAUDE, docs, rationale)                           | —                 |
| T3b | F3 sweep paths `bin/` → `scripts/`                      | F3   | ⏳ pending | 5 sweep (Makefile, Dockerfile, Dockerfile.s3, CLAUDE, console-cli-bridge)          | —                 |
| T4a | F4 frontend `src/app/` + `src/shared/` + Vite alias     | F4   | ⏳ pending | 5 (map entries, classify lib, classify ui, sweep ~38 imports, validate alias)      | —                 |
| T4b | F4 `features/{aws,azure,gcp,stack}/` Clean Architecture | F4   | ⏳ pending | 5 (1 por feature + dep-rule validator)                                             | —                 |
| T5a | F5 build verify + smoke nav                             | F5   | ⏳ pending | 5 (build log, missing imports, dead code, bundle diff, route nav)                  | —                 |
| T5b | F5 `PROJECT-STRUCTURE.md` + update CLAUDE/AGENTS/README | F5   | ⏳ pending | 5 (draft, update CLAUDE, AGENTS, README, consistency review)                       | —                 |

## Mudanças aplicadas (F0 + F1)

### F0 — Stubs + plano + .gitignore fix

- Removido `**/lib/**` do `.gitignore` (escondia console stubs do VCS).
- Adicionado `localstack-ui/console/src/lib/` com 17 arquivos stub (utils, skins, queryClient, cloud-context, theme-context, i18n, service-icons, cli-bridge, iac-drawer-store, iac/generators, api/{\_client,aws,azure,gcp,stack,clouds}).
- Vite build agora gera `dist/` (1860 modules → nginx serve, 200 OK).

### F1 — Root cleanup

| Antes                                                             | Depois                                               | Refs atualizadas                                                  |
| ----------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| `requirements-{base-runtime,basic,dev,runtime,test,typehint}.txt` | `requirements/{X}.txt` (6 arquivos)                  | Makefile (12 linhas), `docker/Dockerfile`, `docker/Dockerfile.s3` |
| `Dockerfile`, `Dockerfile.s3`                                     | `docker/Dockerfile`, `docker/Dockerfile.s3`          | `scripts/docker-helper.sh` (`DOCKERFILE=docker/Dockerfile`)       |
| `DOCKER.md`                                                       | `docker/README.md`                                   | — (não referenciado em código)                                    |
| `prompts/` (13 arquivos)                                          | `.planning/prompts/`                                 | — (artefatos dev)                                                 |
| `tasks/` (5 arquivos)                                             | `.planning/tasks/`                                   | — (artefatos dev)                                                 |
| `.dockerignore`                                                   | + exclui `.planning/` + `docs/internal/superpowers/` | —                                                                 |

### Decisões mantidas

- `localstack-core/localstack/` permanece (parity upstream, namespace pkg).
- `docker-compose.yml` + `docker-compose-pro.yml` permanecem no root (UX cotidiano `docker compose up`).
- `bin/` mantém scripts shipped no container (`docker-entrypoint.sh`, `localstack-supervisor`, `hosts`). 13 dev-only serão movidos em T3a.
- `localstack-ui/console/src/` já adota `src/`; será reorganizado em T4 com Clean Architecture.

## Constraints duros (não negociáveis)

1. `localstack-core/localstack/__init__.py` PROIBIDO (`make lint` aborta — namespace pkg para `localstack-pro` plugins).
2. `pyproject.toml` `package-dir = {"": "localstack-core"}` — mover core quebra setuptools.
3. `plux.ini` 228 entries — module paths Python (`localstack.aws.services.providers:X`), independem de filesystem.
4. `localstack-core/localstack/aws/api/` regenerado por `make asf-regenerate` (botocore pinned).
5. Parity com upstream LocalStack — divergir layout = merge debt perpétuo.

## Clean Architecture aplicada ao Frontend (F4)

Cada feature em `src/features/<name>/` com 4 camadas e dependency rule (outer → inner):

```
src/features/aws/
├── domain/              # types puros, entidades, interfaces de repository
├── application/         # use cases, hooks orquestradores (react-query)
├── infrastructure/      # adapters concretos (fetch, SDK calls)
└── presentation/        # React components, routes, forms
```

`src/shared/`:

```
src/shared/
├── ui/              # design system primitivos
├── lib/             # cn, queryClient, type-helpers
├── http/            # apiClient base
├── i18n/, theme/, cloud-context/   # cross-cutting providers
└── domain/          # tipos compartilhados (CloudName, etc)
```

`src/app/`:

```
src/app/
├── App.tsx
├── router.tsx
├── main.tsx
└── providers/       # composição (Theme, I18n, Cloud, QueryClient)
```

**Regra:** presentation → application → domain ← infrastructure (infrastructure implementa interfaces do domain). Domain nunca importa de fora.

## Próximo passo

T2a — `git mv docs/*.md` para `docs/{user,dev,internal,legal}/`. Dispatch 5 subagents para categorização final.

## Verificação após cada task

- F1/F3: `make install-test` (dry-run OK) + `docker compose up` (smoke)
- F4: `bun run build` (1860+ modules) + `curl localhost:4577/` (200 OK)
- Cada commit precisa passar `make lint` (não rodado ainda — opcional pós-refactor).
