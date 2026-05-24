terraform {
  required_version = ">= 1.5"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.110"
    }
  }
}

# The azurerm provider's `metadata_host` lets us route ARM calls at the
# LocalStack TLS sidecar. The provider still calls Entra for tokens; that
# is handled by our entra router on the same gateway.
#
# Required setup (do this BEFORE `terraform plan`):
#   source ./env.sh
#
# `env.sh` exports ARM_* service-principal creds, points SSL_CERT_FILE at
# the sidecar cert, and sets GODEBUG=x509usefallbackroots=1. On macOS the
# fallback flag is sometimes ignored — run `./trust-cert-macos.sh` to add
# the cert to the System keychain instead.
provider "azurerm" {
  features {}

  metadata_host = "localhost:4569"

  skip_provider_registration = true
  storage_use_azuread        = false

  # Use the env vars listed above for credentials.
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
