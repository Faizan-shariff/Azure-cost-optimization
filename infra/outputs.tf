output "storage_account_name" {
  value = azurerm_storage_account.storage.name
}

output "cosmos_db_endpoint" {
  value = azurerm_cosmosdb_account.cosmos.endpoint
}

output "cosmos_db_key" {
  value = azurerm_cosmosdb_account.cosmos.primary_master_key
}
