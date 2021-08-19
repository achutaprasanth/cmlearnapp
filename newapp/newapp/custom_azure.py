from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    # Must be replaced by your <storage_account_name>
    account_name = 'cmlearn'
    # Must be replaced by your <storage_account_key>
    account_key = 'T+Bqsmo4mYTU6EaZSTEBy2Xb2yKt2Yj6qFZXpf0+HfkGyXWEGJnlXuXl5sSY3nTj/rMDKZ7frNrVtZdEKFpUmA=='
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    # Must be replaced by your storage_account_name
    account_name = 'cmlearn'
    account_key = 'T+Bqsmo4mYTU6EaZSTEBy2Xb2yKt2Yj6qFZXpf0+HfkGyXWEGJnlXuXl5sSY3nTj/rMDKZ7frNrVtZdEKFpUmA=='  # Must be replaced by your <storage_account_key>
    
    azure_container = 'static'
    expiration_secs = None
