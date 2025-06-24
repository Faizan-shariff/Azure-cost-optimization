import datetime
import json
import logging
import os

import azure.functions as func
from azure.cosmos import CosmosClient
from azure.storage.blob import BlobServiceClient

COSMOS_URL = os.getenv("COSMOS_DB_URI")
COSMOS_KEY = os.getenv("COSMOS_DB_KEY")
DB_NAME = os.getenv("COSMOS_DB_NAME")
CONTAINER_NAME = os.getenv("COSMOS_DB_CONTAINER")

BLOB_CONN_STRING = os.getenv("BLOB_STORAGE_CONN")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

    logging.info("Python timer trigger function started at %s", utc_timestamp)

    # Cosmos DB setup
    cosmos_client = CosmosClient(COSMOS_URL, COSMOS_KEY)
    db = cosmos_client.get_database_client(DB_NAME)
    container = db.get_container_client(CONTAINER_NAME)

    # Blob Storage setup
    blob_service = BlobServiceClient.from_connection_string(BLOB_CONN_STRING)
    blob_container = blob_service.get_container_client(BLOB_CONTAINER_NAME)

    cutoff_date = (datetime.datetime.utcnow() - datetime.timedelta(days=90)).isoformat()

    query = f"SELECT * FROM c WHERE c.timestamp < '{cutoff_date}'"
    items = container.query_items(query, enable_cross_partition_query=True)

    for item in items:
        billing_id = item.get("billingId")
        blob_name = f"{billing_id}.json"
        blob_data = json.dumps(item).encode("utf-8")
        blob_container.upload_blob(blob_name, blob_data, overwrite=True)
        container.delete_item(item=item, partition_key=item["partitionKey"])

    logging.info("Archival function completed at %s", datetime.datetime.utcnow())
