import logging
import azure.functions as func
from azure.data.tables import TableClient, UpdateMode
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing visitor counter request...')

    account_name = os.environ["ACCOUNT_NAME"]
    account_key = os.environ["ACCOUNT_KEY"]
    table_name = os.environ["TABLE_NAME"]

    # Connect to Table API endpoint (Cosmos DB with Table API)
    endpoint = f"https://{account_name}.table.cosmos.azure.com:443"
    table_client = TableClient(
        endpoint=endpoint,
        table_name=table_name,
        credential={"account_name": account_name, "account_key": account_key}
    )

    partition_key = "counter"
    row_key = "visitors"

    try:
        try:
            entity = table_client.get_entity(partition_key, row_key)
        except Exception as e:
            if "ResourceNotFound" in str(e):
                entity = {"PartitionKey": partition_key, "RowKey": row_key, "Count": 0}
                table_client.create_entity(entity)
            else:
                raise e

        new_count = int(entity.get("Count", 0)) + 1
        entity["Count"] = new_count

        table_client.update_entity(entity=entity, mode=UpdateMode.REPLACE)

        headers = {
            "Access-Control-Allow-Origin": "*",  # allow CORS for your static site
            "Content-Type": "application/json"
        }

        return func.HttpResponse(f'{{"count": {new_count}}}', headers=headers, mimetype="application/json")

    except Exception as e:
        logging.error(f"Error updating visitor count: {e}")
        return func.HttpResponse(
            f'{{"error": "{str(e)}"}}',
            status_code=500,
            mimetype="application/json"
        )
