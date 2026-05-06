import os
from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

@app.route("/")
def health():
    return "AKS App Running!"

@app.route("/upload")
def upload():

    account_name = os.environ["STORAGE_ACCOUNT"]
    container_name = os.environ.get("CONTAINER_NAME", "appdata")
    blob_name = "from-app.txt"

    credential = DefaultAzureCredential()

    blob_service_client = BlobServiceClient(
        f"https://{account_name}.blob.core.windows.net",
        credential=credential
    )

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    data = b"Hello from AKS using Workload Identity!"
    blob_client.upload_blob(data, overwrite=True)

    return "Upload successful"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)