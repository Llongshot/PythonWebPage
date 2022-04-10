from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'webstorageaccount' 
    account_key = 'jx5Kzq5I7Q/W6uvsN+vCIjChtqex9rKP9Dy1aPhNjXFPxITWb7sP5h2X58SIs8weKPa5K82iP7kSx4ARiRYdDA==' # <storage_account_key>
    azure_container = 'media'
    expiration_secs = None