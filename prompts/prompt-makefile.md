## Modelo padrão de um Makefile

- ABaixo temos um modelo padrão de arquivo Makefile

```bash
# Cloudinho / 0X3 CL0UD L4BS — Makefile
# OxeTech Academy · SECTI Alagoas
#
# Uso comum (aluno):
#   make             # mostra ajuda
#   make setup-labs  # cria .venv e instala libs dos labs
#   make lab         # sobe 0X3 CL0UD L4BS em http://localhost:8765
#   make clean       # remove caches e backups internos
#
# Targets do instrutor (slides/briefings/illustrations/...) exigem a pasta
# _instrutor/ — não distribuída no repo público.

VENV_LOCAL := .venv/bin/python3
PY := $(shell test -x $(VENV_LOCAL) && echo $(VENV_LOCAL) || command -v python3)
LESSONS := $(shell seq -w 1 20)

.PHONY: help
help:
	@echo "Cloudinho — alvos disponíveis (python: $(PY)):"
	@echo ""
	@echo "──── Para o aluno ──────────────────────────────────────────────────"
	@echo "  make setup-labs        cria .venv + instala deps dos labs"
	@echo "  make lab               inicia 0X3 CL0UD L4BS em http://localhost:8765"
	@echo "  make localstack-up     sobe containers LocalStack (AWS + Azure preview)"
	@echo "  make localstack-down   derruba LocalStack"
	@echo "  make localstack-logs   segue logs do LocalStack"
	@echo "  make clean             remove caches e backups internos"
	@echo ""
	@echo "──── Para o instrutor (requer pasta _instrutor/) ───────────────────"
	@echo "  make setup             cria .venv local + instala deps (todos)"
	@echo "  make slides            gera todos os 20 .pptx em _instrutor/material-aulas/slides/"
	@echo "  make briefings         gera todos os 20 PDFs em _instrutor/material-aulas/briefings/"
	@echo "  make all               slides + briefings"
	@echo "  make aula N=07         gera só a Aula 07 (slide + briefing)"
	@echo "  make slide N=07        gera só o .pptx da Aula 07"
	@echo "  make brief N=07        gera só o briefing PDF da Aula 07"
	@echo "  make illustrations     gera SVGs das aulas + dos labs (aws/azure/gcp)"
	@echo "  make illustrations-png SVGs + exporta PNGs 2× para slides/labs"
	@echo "  make preview           gera PPTX preview das 3 nuvens (aws/azure/gcp)"
	@echo "  make present           abertura whoami no terminal (antes da Aula 01)"
	@echo "  make slide-numbers     insere badge N/T em todos os slides"
	@echo "  make slide-numbers N=06   só a Aula 06"
	@echo ""

# ═════════════════════════════════════════════════════════════════════════════
# ALUNO — labs hands-on (não exige _instrutor/)
# ═════════════════════════════════════════════════════════════════════════════

.PHONY: setup-labs
setup-labs:
	@if [ ! -d .venv ]; then \
		echo "→ Criando .venv local…"; \
		python3 -m venv .venv; \
	fi
	@.venv/bin/pip install --quiet --upgrade pip
	@.venv/bin/pip install --quiet -r requirements.txt
	@echo "✓ .venv pronta com FastAPI + uvicorn (modo SIMULADO usa outputs estáticos)"

.PHONY: lab
lab: setup-labs
	@echo "☁  Iniciando 0X3 CL0UD L4BS…"
	@PYTHONUNBUFFERED=1 .venv/bin/python3 labs/lab_server.py

.PHONY: localstack-up localstack-down localstack-logs localstack
localstack-up:
	@echo "🐳 Subindo LocalStack (AWS + Azure preview)…"
	@cd labs && docker compose up -d
	@echo "✓ LocalStack AWS   → http://localhost:4566"
	@echo "✓ LocalStack Azure → http://localhost:4567 (preview, requer LOCALSTACK_AUTH_TOKEN)"

localstack-down:
	@echo "🐳 Derrubando LocalStack…"
	@cd labs && docker compose down

localstack-logs:
	@cd labs && docker compose logs -f --tail=100

# alias retrocompatível
localstack: localstack-up

# ═════════════════════════════════════════════════════════════════════════════
# INSTRUTOR — slides, briefings, ilustrações (requer _instrutor/)
# ═════════════════════════════════════════════════════════════════════════════

.PHONY: setup
setup:
	@if [ ! -d .venv ]; then \
		echo "→ Criando .venv local…"; \
		python3 -m venv .venv; \
	fi
	@.venv/bin/pip install -q --upgrade pip
	@.venv/bin/pip install -q -r requirements.txt
	@if [ -f _instrutor/requirements.txt ]; then \
		echo "→ Instalando deps adicionais do instrutor…"; \
		.venv/bin/pip install -q -r _instrutor/requirements.txt; \
	fi
	@echo "✓ setup pronto (.venv/bin/python3)"

.PHONY: slides
slides: _check-instrutor slides-dir
	@for i in $(LESSONS); do \
		if [ -f _instrutor/geradores/gerar_aula$$i.py ]; then \
			echo "→ Gerando Aula $$i (slide)"; \
			$(PY) _instrutor/geradores/gerar_aula$$i.py || exit 1; \
		else \
			echo "  ! _instrutor/geradores/gerar_aula$$i.py não existe — pulando"; \
		fi; \
	done

.PHONY: briefings
briefings: _check-instrutor briefings-dir
	@for i in $(LESSONS); do \
		if [ -f _instrutor/geradores/gerar_briefing_aula$$i.py ]; then \
			echo "→ Gerando Aula $$i (briefing)"; \
			$(PY) _instrutor/geradores/gerar_briefing_aula$$i.py || exit 1; \
		else \
			echo "  ! _instrutor/geradores/gerar_briefing_aula$$i.py não existe — pulando"; \
		fi; \
	done

.PHONY: all
all: slides briefings

.PHONY: aula
aula: _check-instrutor
ifndef N
	$(error "Use: make aula N=07")
endif
	@$(MAKE) slide N=$(N)
	@$(MAKE) brief N=$(N)

.PHONY: slide
slide: _check-instrutor slides-dir
ifndef N
	$(error "Use: make slide N=07")
endif
	@$(PY) _instrutor/geradores/gerar_aula$(N).py

.PHONY: brief
brief: _check-instrutor briefings-dir
ifndef N
	$(error "Use: make brief N=07")
endif
	@$(PY) _instrutor/geradores/gerar_briefing_aula$(N).py

slides-dir:
	@mkdir -p _instrutor/material-aulas/slides

briefings-dir:
	@mkdir -p _instrutor/material-aulas/briefings

.PHONY: illustrations
illustrations: _check-instrutor
	@echo "🎨 Gerando ilustrações didáticas das aulas (Aula 04: EC2 lifecycle, IAM)…"
	@$(PY) _instrutor/geradores/generate_illustrations.py
	@echo "🎨 Gerando ilustrações dos labs AWS (compute + storage)…"
	@$(PY) _instrutor/geradores/generate_illustrations_aws_extra.py
	@$(PY) _instrutor/geradores/generate_illustrations_aws_storage.py
	@echo "🎨 Gerando ilustrações dos labs Azure (compute + storage)…"
	@$(PY) _instrutor/geradores/generate_illustrations_azure.py
	@$(PY) _instrutor/geradores/generate_illustrations_azure_storage.py
	@echo "🎨 Gerando ilustrações dos labs GCP (compute + storage)…"
	@$(PY) _instrutor/geradores/generate_illustrations_gcp.py
	@$(PY) _instrutor/geradores/generate_illustrations_gcp_storage.py

.PHONY: illustrations-png
illustrations-png: illustrations
	@echo "🖼  Exportando PNGs 2× (aulas + labs)…"
	@$(PY) _instrutor/geradores/export_illustrations_recursive.py

.PHONY: preview
preview: _check-instrutor
	@mkdir -p _instrutor/material-aulas/previews
	@echo "📊 Gerando PPTX previews dos labs…"
	@$(PY) _instrutor/geradores/gerar_preview_aws.py
	@$(PY) _instrutor/geradores/gerar_preview_aws_storage.py
	@$(PY) _instrutor/geradores/gerar_preview_azure.py
	@$(PY) _instrutor/geradores/gerar_preview_azure_storage.py
	@$(PY) _instrutor/geradores/gerar_preview_gcp.py
	@$(PY) _instrutor/geradores/gerar_preview_gcp_storage.py

.PHONY: present
present: _check-instrutor
	@bash _instrutor/present/whoami.sh

.PHONY: slide-numbers
slide-numbers: _check-instrutor
ifdef N
	@$(PY) _instrutor/geradores/add_slide_numbers.py N=$(N)
else
	@$(PY) _instrutor/geradores/add_slide_numbers.py
endif

# Guard usado pelos targets do INSTRUTOR (slides, briefings, illustrations,
# preview, present, aula/slide/brief): se _instrutor/ não existe (clone público
# do aluno), avisa e sai amigavelmente.
.PHONY: _check-instrutor
_check-instrutor:
	@if [ ! -d _instrutor ]; then \
		echo "Este target depende de _instrutor/ (material do instrutor)."; \
		echo "Alunos usam apenas: make lab, make setup-labs, make localstack-{up,down,logs}."; \
		echo "Veja 'make help' (seção 'Para o aluno')."; \
		exit 1; \
	fi

.PHONY: clean
clean:
	@find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.bak-*" -type f -delete 2>/dev/null || true
	@echo "Limpo."

```
