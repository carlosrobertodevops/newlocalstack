import {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";

export type Lang = "en" | "pt-BR" | "es";

type Dict = Record<string, string>;

const EN: Dict = {
  // app shell
  "app.brand": "New LocalStack Console",
  "app.title": "New LocalStack — Multi-cloud Console",
  "topbar.theme.light": "Light",
  "topbar.theme.dark": "Dark",
  "topbar.theme.toggle": "Toggle theme",
  "topbar.language": "Language",
  "topbar.region": "Region",
  "topbar.endpoint": "Endpoint",
  // sidebar
  "sidebar.services": "{cloud} services",
  "sidebar.loading": "loading…",
  "sidebar.health_offline": "health offline",
  "sidebar.all_clouds_overview": "All Clouds Overview",
  "sidebar.overview": "Overview",
  "sidebar.stack": "Stack (Live)",
  // breadcrumbs
  "breadcrumbs.home": "Home",
  // home / per-cloud
  "home.title": "{cloud} Console",
  "home.subtitle":
    "Pick a service to manage via the UI, Terraform snippet, or Cloud Shell.",
  // service states (badges)
  "state.available": "available",
  "state.running": "running",
  "state.ready": "ready",
  "state.disabled": "disabled",
  "state.unknown": "unknown",
  "state.err": "error",
  "state.error": "error",
  "state.loading": "loading",
  "state.pro": "pro",
  "state.preview": "preview",
  "state.in_action": "Live",
  "state.not_yet_available": "pro / not yet available",
  // badges
  "badge.preview": "preview",
  "badge.pro": "pro",
  // common
  "common.create": "Create",
  "common.delete": "Delete",
  "common.remove": "Remove",
  "common.refresh": "Refresh",
  "common.cancel": "Cancel",
  "common.confirm": "Confirm",
  "common.confirm_reset": "Confirm reset",
  "common.wait": "Please wait…",
  "common.name": "Name",
  "common.actions": "Actions",
  "common.empty": "No items.",
  "common.error": "Error",
  "common.copy": "Copy",
  "common.copied": "Copied to clipboard",
  "common.run": "Run",
  "common.open": "Open",
  "common.more": "more",
  "common.region": "region",
  "common.account": "account",
  "common.project": "project",
  "common.subscription": "subscription",
  // table headers / form labels (generic — service names stay raw)
  "col.name": "Name",
  "col.location": "Location",
  "col.resource_group": "Resource group",
  "col.resource_id": "Resource ID",
  "col.kind": "Kind",
  "col.state": "State",
  "col.cidr": "CIDR",
  "col.sku": "SKU",
  "col.type": "Type",
  "col.description": "Description",
  "col.runtime": "Runtime",
  "col.uri": "URI",
  "col.email": "Email",
  "col.display_name": "Display Name",
  "col.unique_id": "Unique ID",
  "col.class": "Class",
  "col.topic": "Topic",
  "col.bucket": "Bucket",
  "col.dataset": "Dataset",
  "col.dataset_id": "Dataset ID",
  "col.secret_id": "Secret ID",
  "col.account_id": "Account ID",
  "col.key_ring": "Key Ring",
  "col.dns_name": "DNS Name",
  "col.id": "ID",
  "col.arn": "ARN",
  "col.url": "URL",
  "col.az": "AZ",
  "col.created": "Created",
  "col.version": "Version",
  "col.records": "Records",
  "col.retention": "Retention",
  "col.engine": "Engine",
  "col.ami": "AMI",
  "col.status": "Status",
  "col.zone": "Zone",
  "col.schedule": "Schedule",
  "col.display": "Display",
  "col.auto_subnets": "Auto subnets",
  "col.partition_key": "Partition key",
  "col.cluster_name": "Cluster name",
  "col.instance_id": "Instance ID",
  "col.subnet_ids": "Subnet IDs",
  "col.role_arn": "Role ARN",
  "col.vpc_cidr": "VPC CIDR",
  "col.subnet_cidr": "Subnet CIDR",
  "col.shards": "Shards",
  "col.domain_name": "Domain name",
  "col.job_id": "Job ID",
  "col.target_url": "Target URL",
  "col.value": "Value",
  "col.bucket_name": "Bucket name",
  "col.queue_name": "Queue name",
  "col.topic_name": "Topic name",
  "col.group_name": "Group name",
  "col.api_name": "API name",
  "col.bus_name": "Bus name",
  "col.repo_name": "Repository name",
  "col.role_name": "Role name",
  "col.user_name": "User name",
  "col.function": "Function",
  "col.table": "Table",
  "col.role": "Role",
  "col.user": "User",
  "col.kind_or_type": "Kind",
  "common.put": "Put",
  "common.terminate": "Terminate",
  "common.run_instance": "Run instance",
  "common.create_vpc": "Create VPC",
  "common.create_subnet": "Create Subnet",
  "common.schedule_delete": "Schedule delete",
  // stack page
  "stack.title": "{cloud} · Stack Overview",
  "stack.subtitle":
    "{total} resources across {services} services. Created via CLI, Terraform, Serverless Framework or this console.",
  "stack.empty":
    "No {cloud} resources detected yet.\nCreate some via CLI, Terraform, Serverless Framework or the console — they'll appear here.",
  "stack.refresh": "Refresh",
  "stack.clear": "Clear Stack",
  "stack.clear_title": "Clear {cloud} Stack",
  "stack.clear_message":
    "This action removes ALL active resources in {cloud} (full reset).\n\nDoes not affect other providers. Irreversible.",
  "stack.clear_tooltip": "Clear all active services for {cloud}",
  "stack.remove": "Remove",
  "stack.remove_title": "Remove {service}",
  "stack.remove_message":
    "This action removes ALL resources of service {service} in {cloud}. Irreversible — does not affect other providers.",
  "stack.remove_tooltip": "Remove all resources of {service}",
  "stack.remove_error": "Failed to remove {service}: {error}",
  "stack.reset_error": "Failed to clear stack: {error}",
  "stack.open_service": "Open {service} →",
  "stack.region_account": "{region} · {account}",
  "stack.one_region": "1 region",
  "stack.one_account": "1 account",
  // overview
  "overview.title.unified": "Unified Overview · All Clouds",
  "overview.subtitle.unified":
    "Resources created via CLI (aws/az/gcloud), Terraform, Serverless Framework or the New LocalStack Console. {total} resources total.",
  "overview.cloud_badge": "{cloud}: {total} resources · {live} live services",
  "overview.cloud_section_count": "({total} resources)",
  "overview.title.cloud": "{cloud} · Overview",
  "overview.subtitle.cloud":
    "Resources created via CLI, Terraform, Serverless or this console. Live total: {total} across {services} services.",
  "overview.subtitle.aws":
    "Resources created via CLI, Terraform, Serverless or this console. Live total: {total} across {services} services.",
  "overview.subtitle.azure":
    "Resources created via Azure CLI, Terraform azurerm, Serverless or this console. Subscription: {scope}. Live total: {total} across {services} services.",
  "overview.subtitle.gcp":
    "Resources created via gcloud, Terraform google, Serverless or this console. Project: {scope}. Live total: {total} across {services} services.",
  "overview.more_count": "+ {count} more",
  // preview / pro service
  "preview.description": "{service} (preview) — backend wiring in progress.",
  "preview.ui_ready": "UI ready. Provider integration coming soon.",
  "pro.description":
    "Backend not available in this LocalStack distribution. Requires LocalStack Pro or a future community provider.",
  "pro.reason":
    "This service requires a paid provider tier. The UI is wired and ready — once the backend ships, it will work automatically.",
  // resource page / IaC drawer
  "resource.show_as": "Show as {tool}",
  "iac.title": "Infrastructure as Code",
  "iac.tool_label": "Tool",
  "iac.provider_note": "Provider configured to New LocalStack",
  "iac.copy": "Copy",
  "iac.preview": "Preview",
  "iac.plan": "Plan",
  "iac.apply": "Apply",
  "iac.destroy": "Destroy",
  "iac.empty": "(empty)",
  "iac.success": "{action} ok ({duration} ms)",
  "iac.fail": "{action} failed (exit {code})",
  // cloud shell
  "shell.button": "Cloud Shell",
  "shell.title": "Cloud Shell — bridge :4578 or in-container fallback",
  "shell.header_banner": "New LocalStack Cloud Shell — aws | az | gcloud only",
  "shell.placeholder":
    "aws s3 ls   |   az storage account list   |   gcloud projects list",
  "shell.run": "Run",
  "shell.cli_not_allowed": "cli not allowed: {cli}",
};

const PT_BR: Dict = {
  // app shell
  "app.brand": "Console New LocalStack",
  "app.title": "New LocalStack — Console Multi-cloud",
  "topbar.theme.light": "Claro",
  "topbar.theme.dark": "Escuro",
  "topbar.theme.toggle": "Alternar tema",
  "topbar.language": "Idioma",
  "topbar.region": "Região",
  "topbar.endpoint": "Endpoint",
  // sidebar
  "sidebar.services": "Serviços {cloud}",
  "sidebar.loading": "carregando…",
  "sidebar.health_offline": "health offline",
  "sidebar.all_clouds_overview": "Visão geral · todas as clouds",
  "sidebar.overview": "Visão geral",
  "sidebar.stack": "Stack (Em ação)",
  // breadcrumbs
  "breadcrumbs.home": "Início",
  // home / per-cloud
  "home.title": "Console {cloud}",
  "home.subtitle":
    "Escolha um serviço para gerenciar via UI, snippet Terraform ou Cloud Shell.",
  // service states
  "state.available": "disponível",
  "state.running": "ativo",
  "state.ready": "pronto",
  "state.disabled": "desativado",
  "state.unknown": "desconhecido",
  "state.err": "erro",
  "state.error": "erro",
  "state.loading": "carregando",
  "state.pro": "pro",
  "state.preview": "prévia",
  "state.in_action": "Em ação",
  "state.not_yet_available": "pro / ainda indisponível",
  // badges
  "badge.preview": "prévia",
  "badge.pro": "pro",
  // common
  "common.create": "Criar",
  "common.delete": "Excluir",
  "common.remove": "Remover",
  "common.refresh": "Atualizar",
  "common.cancel": "Cancelar",
  "common.confirm": "Confirmar",
  "common.confirm_reset": "Confirmar reset",
  "common.wait": "Aguarde…",
  "common.name": "Nome",
  "common.actions": "Ações",
  "common.empty": "Nenhum item.",
  "common.error": "Erro",
  "common.copy": "Copiar",
  "common.copied": "Copiado",
  "common.run": "Executar",
  "common.open": "Abrir",
  "common.more": "mais",
  "common.region": "região",
  "common.account": "conta",
  "common.project": "projeto",
  "common.subscription": "assinatura",
  // headers de tabela / labels de formulário
  "col.name": "Nome",
  "col.location": "Localização",
  "col.resource_group": "Grupo de recursos",
  "col.resource_id": "ID do recurso",
  "col.kind": "Tipo",
  "col.state": "Estado",
  "col.cidr": "CIDR",
  "col.sku": "SKU",
  "col.type": "Tipo",
  "col.description": "Descrição",
  "col.runtime": "Runtime",
  "col.uri": "URI",
  "col.email": "E-mail",
  "col.display_name": "Nome de exibição",
  "col.unique_id": "ID único",
  "col.class": "Classe",
  "col.topic": "Tópico",
  "col.bucket": "Bucket",
  "col.dataset": "Dataset",
  "col.dataset_id": "ID do dataset",
  "col.secret_id": "ID do segredo",
  "col.account_id": "ID da conta",
  "col.key_ring": "Conjunto de chaves",
  "col.dns_name": "Nome DNS",
  "col.id": "ID",
  "col.arn": "ARN",
  "col.url": "URL",
  "col.az": "AZ",
  "col.created": "Criado",
  "col.version": "Versão",
  "col.records": "Registros",
  "col.retention": "Retenção",
  "col.engine": "Engine",
  "col.ami": "AMI",
  "col.status": "Status",
  "col.zone": "Zona",
  "col.schedule": "Agendamento",
  "col.display": "Exibição",
  "col.auto_subnets": "Subnets automáticas",
  "col.partition_key": "Chave de partição",
  "col.cluster_name": "Nome do cluster",
  "col.instance_id": "ID da instância",
  "col.subnet_ids": "IDs de subnet",
  "col.role_arn": "ARN da role",
  "col.vpc_cidr": "CIDR da VPC",
  "col.subnet_cidr": "CIDR da subnet",
  "col.shards": "Shards",
  "col.domain_name": "Nome do domínio",
  "col.job_id": "ID do job",
  "col.target_url": "URL alvo",
  "col.value": "Valor",
  "col.bucket_name": "Nome do bucket",
  "col.queue_name": "Nome da fila",
  "col.topic_name": "Nome do tópico",
  "col.group_name": "Nome do grupo",
  "col.api_name": "Nome da API",
  "col.bus_name": "Nome do bus",
  "col.repo_name": "Nome do repositório",
  "col.role_name": "Nome da role",
  "col.user_name": "Nome do usuário",
  "col.function": "Função",
  "col.table": "Tabela",
  "col.role": "Role",
  "col.user": "Usuário",
  "col.kind_or_type": "Tipo",
  "common.put": "Salvar",
  "common.terminate": "Encerrar",
  "common.run_instance": "Executar instância",
  "common.create_vpc": "Criar VPC",
  "common.create_subnet": "Criar Subnet",
  "common.schedule_delete": "Agendar exclusão",
  // stack
  "stack.title": "{cloud} · Visão da Stack",
  "stack.subtitle":
    "{total} recursos em {services} serviços. Criados via CLI, Terraform, Serverless Framework ou este console.",
  "stack.empty":
    "Nenhum recurso de {cloud} detectado ainda.\nCrie via CLI, Terraform, Serverless Framework ou pelo console — aparecem aqui.",
  "stack.refresh": "Atualizar",
  "stack.clear": "Limpar Stack",
  "stack.clear_title": "Limpar Stack {cloud}",
  "stack.clear_message":
    "Esta ação remove TODOS os recursos ativos em {cloud} (reset completo).\n\nNão afeta os outros provedores. Ação irreversível.",
  "stack.clear_tooltip": "Limpar todos serviços ativos de {cloud}",
  "stack.remove": "Remover",
  "stack.remove_title": "Remover {service}",
  "stack.remove_message":
    "Esta ação remove TODOS os recursos do serviço {service} em {cloud}. É irreversível e não afeta os outros provedores.",
  "stack.remove_tooltip": "Remover todos os recursos de {service}",
  "stack.remove_error": "Falha ao remover {service}: {error}",
  "stack.reset_error": "Falha ao limpar stack: {error}",
  "stack.open_service": "Abrir {service} →",
  "stack.region_account": "{region} · {account}",
  "stack.one_region": "1 região",
  "stack.one_account": "1 conta",
  // overview
  "overview.title.unified": "Visão Unificada · Todas as Clouds",
  "overview.subtitle.unified":
    "Recursos criados via CLI (aws/az/gcloud), Terraform, Serverless Framework ou pelo Console New LocalStack. {total} recursos no total.",
  "overview.cloud_badge": "{cloud}: {total} recursos · {live} serviços ativos",
  "overview.cloud_section_count": "({total} recursos)",
  "overview.title.cloud": "{cloud} · Visão Geral",
  "overview.subtitle.cloud":
    "Recursos criados via CLI, Terraform, Serverless ou pelo console. Total ativo: {total} em {services} serviços.",
  "overview.subtitle.aws":
    "Recursos criados via CLI, Terraform, Serverless ou pelo console. Total ativo: {total} em {services} serviços.",
  "overview.subtitle.azure":
    "Recursos criados via Azure CLI, Terraform azurerm, Serverless ou pelo console. Assinatura: {scope}. Total ativo: {total} em {services} serviços.",
  "overview.subtitle.gcp":
    "Recursos criados via gcloud, Terraform google, Serverless ou pelo console. Projeto: {scope}. Total ativo: {total} em {services} serviços.",
  "overview.more_count": "+ {count} mais",
  // preview / pro
  "preview.description": "{service} (prévia) — integração de backend em andamento.",
  "preview.ui_ready": "UI pronta. Integração com provider em breve.",
  "pro.description":
    "Backend indisponível nesta distribuição do LocalStack. Requer LocalStack Pro ou provider community futuro.",
  "pro.reason":
    "Este serviço requer tier de provider pago. A UI está pronta — assim que o backend for liberado, funciona automaticamente.",
  // resource page / IaC
  "resource.show_as": "Mostrar como {tool}",
  "iac.title": "Infrastructure as Code",
  "iac.tool_label": "Ferramenta",
  "iac.provider_note": "Provider configurado para o New LocalStack",
  "iac.copy": "Copiar",
  "iac.preview": "Visualizar",
  "iac.plan": "Plan",
  "iac.apply": "Apply",
  "iac.destroy": "Destroy",
  "iac.empty": "(vazio)",
  "iac.success": "{action} ok ({duration} ms)",
  "iac.fail": "{action} falhou (exit {code})",
  // cloud shell
  "shell.button": "Cloud Shell",
  "shell.title": "Cloud Shell — bridge :4578 ou fallback no container",
  "shell.header_banner": "New LocalStack Cloud Shell — aws | az | gcloud apenas",
  "shell.placeholder":
    "aws s3 ls   |   az storage account list   |   gcloud projects list",
  "shell.run": "Executar",
  "shell.cli_not_allowed": "cli não permitido: {cli}",
};

const ES: Dict = {
  // app shell
  "app.brand": "Consola New LocalStack",
  "app.title": "New LocalStack — Consola Multi-cloud",
  "topbar.theme.light": "Claro",
  "topbar.theme.dark": "Oscuro",
  "topbar.theme.toggle": "Cambiar tema",
  "topbar.language": "Idioma",
  "topbar.region": "Región",
  "topbar.endpoint": "Endpoint",
  // sidebar
  "sidebar.services": "Servicios {cloud}",
  "sidebar.loading": "cargando…",
  "sidebar.health_offline": "health desconectado",
  "sidebar.all_clouds_overview": "Vista general · todas las nubes",
  "sidebar.overview": "Vista general",
  "sidebar.stack": "Stack (En acción)",
  // breadcrumbs
  "breadcrumbs.home": "Inicio",
  // home
  "home.title": "Consola {cloud}",
  "home.subtitle":
    "Elige un servicio para gestionar vía UI, snippet Terraform o Cloud Shell.",
  // service states
  "state.available": "disponible",
  "state.running": "activo",
  "state.ready": "listo",
  "state.disabled": "desactivado",
  "state.unknown": "desconocido",
  "state.err": "error",
  "state.error": "error",
  "state.loading": "cargando",
  "state.pro": "pro",
  "state.preview": "vista previa",
  "state.in_action": "En acción",
  "state.not_yet_available": "pro / aún no disponible",
  // badges
  "badge.preview": "vista previa",
  "badge.pro": "pro",
  // common
  "common.create": "Crear",
  "common.delete": "Eliminar",
  "common.remove": "Quitar",
  "common.refresh": "Actualizar",
  "common.cancel": "Cancelar",
  "common.confirm": "Confirmar",
  "common.confirm_reset": "Confirmar reset",
  "common.wait": "Espere…",
  "common.name": "Nombre",
  "common.actions": "Acciones",
  "common.empty": "Sin elementos.",
  "common.error": "Error",
  "common.copy": "Copiar",
  "common.copied": "Copiado al portapapeles",
  "common.run": "Ejecutar",
  "common.open": "Abrir",
  "common.more": "más",
  "common.region": "región",
  "common.account": "cuenta",
  "common.project": "proyecto",
  "common.subscription": "suscripción",
  // encabezados de tabla / etiquetas de formulario
  "col.name": "Nombre",
  "col.location": "Ubicación",
  "col.resource_group": "Grupo de recursos",
  "col.resource_id": "ID del recurso",
  "col.kind": "Tipo",
  "col.state": "Estado",
  "col.cidr": "CIDR",
  "col.sku": "SKU",
  "col.type": "Tipo",
  "col.description": "Descripción",
  "col.runtime": "Runtime",
  "col.uri": "URI",
  "col.email": "Correo",
  "col.display_name": "Nombre de visualización",
  "col.unique_id": "ID único",
  "col.class": "Clase",
  "col.topic": "Tema",
  "col.bucket": "Bucket",
  "col.dataset": "Conjunto de datos",
  "col.dataset_id": "ID del conjunto",
  "col.secret_id": "ID del secreto",
  "col.account_id": "ID de la cuenta",
  "col.key_ring": "Conjunto de claves",
  "col.dns_name": "Nombre DNS",
  "col.id": "ID",
  "col.arn": "ARN",
  "col.url": "URL",
  "col.az": "AZ",
  "col.created": "Creado",
  "col.version": "Versión",
  "col.records": "Registros",
  "col.retention": "Retención",
  "col.engine": "Engine",
  "col.ami": "AMI",
  "col.status": "Estado",
  "col.zone": "Zona",
  "col.schedule": "Programación",
  "col.display": "Visualización",
  "col.auto_subnets": "Subredes automáticas",
  "col.partition_key": "Clave de partición",
  "col.cluster_name": "Nombre del clúster",
  "col.instance_id": "ID de la instancia",
  "col.subnet_ids": "IDs de subred",
  "col.role_arn": "ARN del rol",
  "col.vpc_cidr": "CIDR de VPC",
  "col.subnet_cidr": "CIDR de subred",
  "col.shards": "Shards",
  "col.domain_name": "Nombre del dominio",
  "col.job_id": "ID del job",
  "col.target_url": "URL objetivo",
  "col.value": "Valor",
  "col.bucket_name": "Nombre del bucket",
  "col.queue_name": "Nombre de la cola",
  "col.topic_name": "Nombre del tema",
  "col.group_name": "Nombre del grupo",
  "col.api_name": "Nombre de la API",
  "col.bus_name": "Nombre del bus",
  "col.repo_name": "Nombre del repositorio",
  "col.role_name": "Nombre del rol",
  "col.user_name": "Nombre de usuario",
  "col.function": "Función",
  "col.table": "Tabla",
  "col.role": "Rol",
  "col.user": "Usuario",
  "col.kind_or_type": "Tipo",
  "common.put": "Guardar",
  "common.terminate": "Terminar",
  "common.run_instance": "Ejecutar instancia",
  "common.create_vpc": "Crear VPC",
  "common.create_subnet": "Crear Subred",
  "common.schedule_delete": "Programar eliminación",
  // stack
  "stack.title": "{cloud} · Vista de la Stack",
  "stack.subtitle":
    "{total} recursos en {services} servicios. Creados vía CLI, Terraform, Serverless Framework o esta consola.",
  "stack.empty":
    "Aún no hay recursos de {cloud}.\nCrea algunos vía CLI, Terraform, Serverless Framework o desde la consola — aparecerán aquí.",
  "stack.refresh": "Actualizar",
  "stack.clear": "Limpiar Stack",
  "stack.clear_title": "Limpiar Stack {cloud}",
  "stack.clear_message":
    "Esta acción elimina TODOS los recursos activos en {cloud} (reset completo).\n\nNo afecta a otros proveedores. Irreversible.",
  "stack.clear_tooltip": "Limpiar todos los servicios activos de {cloud}",
  "stack.remove": "Quitar",
  "stack.remove_title": "Quitar {service}",
  "stack.remove_message":
    "Esta acción elimina TODOS los recursos del servicio {service} en {cloud}. Irreversible — no afecta a otros proveedores.",
  "stack.remove_tooltip": "Quitar todos los recursos de {service}",
  "stack.remove_error": "Error al quitar {service}: {error}",
  "stack.reset_error": "Error al limpiar la stack: {error}",
  "stack.open_service": "Abrir {service} →",
  "stack.region_account": "{region} · {account}",
  "stack.one_region": "1 región",
  "stack.one_account": "1 cuenta",
  // overview
  "overview.title.unified": "Vista Unificada · Todas las Nubes",
  "overview.subtitle.unified":
    "Recursos creados vía CLI (aws/az/gcloud), Terraform, Serverless Framework o la Consola New LocalStack. {total} recursos en total.",
  "overview.cloud_badge": "{cloud}: {total} recursos · {live} servicios activos",
  "overview.cloud_section_count": "({total} recursos)",
  "overview.title.cloud": "{cloud} · Vista general",
  "overview.subtitle.cloud":
    "Recursos creados vía CLI, Terraform, Serverless o desde la consola. Total activo: {total} en {services} servicios.",
  "overview.subtitle.aws":
    "Recursos creados vía CLI, Terraform, Serverless o desde la consola. Total activo: {total} en {services} servicios.",
  "overview.subtitle.azure":
    "Recursos creados vía Azure CLI, Terraform azurerm, Serverless o desde la consola. Suscripción: {scope}. Total activo: {total} en {services} servicios.",
  "overview.subtitle.gcp":
    "Recursos creados vía gcloud, Terraform google, Serverless o desde la consola. Proyecto: {scope}. Total activo: {total} en {services} servicios.",
  "overview.more_count": "+ {count} más",
  // preview / pro
  "preview.description":
    "{service} (vista previa) — integración con backend en curso.",
  "preview.ui_ready": "UI lista. Integración con el proveedor próximamente.",
  "pro.description":
    "Backend no disponible en esta distribución de LocalStack. Requiere LocalStack Pro o un proveedor community futuro.",
  "pro.reason":
    "Este servicio requiere un tier de proveedor de pago. La UI está lista — al lanzarse el backend, funcionará automáticamente.",
  // resource page / IaC
  "resource.show_as": "Mostrar como {tool}",
  "iac.title": "Infrastructure as Code",
  "iac.tool_label": "Herramienta",
  "iac.provider_note": "Proveedor configurado al New LocalStack",
  "iac.copy": "Copiar",
  "iac.preview": "Previsualizar",
  "iac.plan": "Plan",
  "iac.apply": "Apply",
  "iac.destroy": "Destroy",
  "iac.empty": "(vacío)",
  "iac.success": "{action} ok ({duration} ms)",
  "iac.fail": "{action} falló (exit {code})",
  // cloud shell
  "shell.button": "Cloud Shell",
  "shell.title": "Cloud Shell — bridge :4578 o fallback en contenedor",
  "shell.header_banner": "New LocalStack Cloud Shell — solo aws | az | gcloud",
  "shell.placeholder":
    "aws s3 ls   |   az storage account list   |   gcloud projects list",
  "shell.run": "Ejecutar",
  "shell.cli_not_allowed": "cli no permitido: {cli}",
};

const DICTS: Record<Lang, Dict> = {
  en: EN,
  "pt-BR": PT_BR,
  es: ES,
};

interface I18nContextValue {
  lang: Lang;
  setLang: (l: Lang) => void;
  t: (key: string, vars?: Record<string, string | number>) => string;
}

const STORAGE_KEY = "localstack-console:lang";

function initialLang(): Lang {
  if (typeof window === "undefined") return "en";
  const stored = window.localStorage.getItem(STORAGE_KEY) as Lang | null;
  if (stored === "en" || stored === "pt-BR" || stored === "es") return stored;
  const nav = window.navigator?.language ?? "en";
  const lower = nav.toLowerCase();
  if (lower.startsWith("pt")) return "pt-BR";
  if (lower.startsWith("es")) return "es";
  return "en";
}

const I18nContext = createContext<I18nContextValue | null>(null);

export function I18nProvider({ children }: { children: ReactNode }) {
  const [lang, setLangState] = useState<Lang>(() => initialLang());

  useEffect(() => {
    document.documentElement.lang = lang;
    try {
      window.localStorage.setItem(STORAGE_KEY, lang);
    } catch {
      /* ignore */
    }
  }, [lang]);

  const value = useMemo<I18nContextValue>(() => {
    const dict = DICTS[lang];
    return {
      lang,
      setLang: setLangState,
      t: (key, vars) => {
        const tpl = dict[key] ?? DICTS.en[key] ?? key;
        if (!vars) return tpl;
        return tpl.replace(/\{(\w+)\}/g, (_m, k) =>
          vars[k] !== undefined ? String(vars[k]) : `{${k}}`,
        );
      },
    };
  }, [lang]);

  return <I18nContext.Provider value={value}>{children}</I18nContext.Provider>;
}

export function useI18n(): I18nContextValue {
  const ctx = useContext(I18nContext);
  if (!ctx) throw new Error("useI18n must be used within I18nProvider");
  return ctx;
}
