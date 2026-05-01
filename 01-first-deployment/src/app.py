from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import os

account_name = os.environ["STORAGE_ACCOUNT"]

credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(
    f"https://{account_name}.blob.core.windows.net",
    credential=credential
)

container_name = "appdata"
blob_name = "from-app.txt"

blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

data = b"Hello from AKS using Workload Identity!"

blob_client.upload_blob(data, overwrite=True)

print("Upload successful")