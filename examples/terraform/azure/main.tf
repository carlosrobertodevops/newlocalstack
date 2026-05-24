terraform {
  required_version = ">= 1.5"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.110"
    }
  }
}

# LocalStack Azure emulator — fully self-contained.
#
# `metadata_host` routes ARM calls at the TLS sidecar (https://localhost:4569).
# Token exchange goes to login.microsoftonline.com, which the sidecar cert
# (mkcert-signed) also covers. Run `make setup-azure-tls` once per machine
# to install the mkcert root CA into the OS trust store.
#
# Credentials below are LocalStack dummy values — no `az login`, no env vars,
# no `source env.sh` needed. `use_cli = false` disables AzureCLI fallback.
variable "arm_client_id"       { default = "00000000-0000-0000-0000-000000000001" }
variable "arm_client_secret"   { default = "test-secret" }
variable "arm_tenant_id"       { default = "00000000-0000-0000-0000-000000000002" }
variable "arm_subscription_id" { default = "00000000-0000-0000-0000-000000000000" }

provider "azurerm" {
  features {}

  metadata_host = "localhost:4569"

  client_id       = var.arm_client_id
  client_secret   = var.arm_client_secret
  tenant_id       = var.arm_tenant_id
  subscription_id = var.arm_subscription_id

  use_cli  = false
  use_msi  = false
  use_oidc = false

  skip_provider_registration = true
  storage_use_azuread        = false
}

resource "azurerm_resource_group" "demo" {
  name     = "tf-localstack-rg"
  location = "eastus"
}

resource "azurerm_storage_account" "demo" {
  name                     = "tflocalstackstor"
  resource_group_name      = azurerm_resource_group.demo.name
  location                 = azurerm_resource_group.demo.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "demo" {
  name                  = "demo"
  storage_account_name  = azurerm_storage_account.demo.name
  container_access_type = "private"
}

output "rg"               { value = azurerm_resource_group.demo.name }
output "storage_account"  { value = azurerm_storage_account.demo.name }
output "container"        { value = azurerm_storage_container.demo.name }
