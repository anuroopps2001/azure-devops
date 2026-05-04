import sys
import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import HttpResponseError

def upload():
    try:
        account_name = os.environ["STORAGE_ACCOUNT"]
        container_name = os.environ.get("CONTAINER_NAME", "appdata")
        blob_name = "from-app.txt"

        credential = DefaultAzureCredential()
        blob_service_client = BlobServiceClient(
            f"https://{account_name}.blob.core.windows.net",
            credential=credential
        )

        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        data = b"Hello from AKS using Workload Identity!"

        print(f"Attempting to upload to container: {container_name}...")
        blob_client.upload_blob(data, overwrite=True)
        print("Upload successful")

    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        # This exit code 1 is what tells K8s the pod failed
        sys.exit(1)

if __name__ == "__main__":
    upload()