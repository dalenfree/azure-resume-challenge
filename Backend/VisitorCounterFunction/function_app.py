import os
import logging
import azure.functions as func
from azure.data.tables import TableClient, UpdateMode

# Define the Function App (Programming Model v2)
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="VisitorCounterFunction", methods=["GET"])
def visitor_counter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing visitor counter request...")

    # Environment variables from Function App configuration
    account_name = os.environ.get("ACCOUNT_NAME")
    account_key = os.environ.get("ACCOUNT_KEY")
    table_name = os.environ.get("TABLE_NAME")

    # Cosmos DB Table API endpoint
    endpoint = f"https://{account_name}.table.cosmos.azure.com:443"

    # Create TableClient connection
    table_client = TableClient(
        endpoint=endpoint,
        table_name=table_name,
        credential={"account_name": account_name, "account_key": account_key}
    )

    partition_key = "counter"
    row_key = "visitors"

    try:
        # Try to get entity, or create one if it doesn’t exist
        try:
            entity = table_client.get_entity(partition_key, row_key)
        except Exception as e:
            if "ResourceNotFound" in str(e):
                entity = {"PartitionKey": partition_key, "RowKey": row_key, "Count": 0}
                table_client.create_entity(entity)
            else:
                raise e

        # Increment the visitor count
        new_count = int(entity.get("Count", 0)) + 1
        entity["Count"] = new_count

        # Update the entity in the table
        table_client.update_entity(entity=entity, mode=UpdateMode.REPLACE)

        headers = {
            "Access-Control-Allow-Origin": "*",  # CORS for static website
            "Content-Type": "application/json"
        }

        return func.HttpResponse(
            body=f'{{"count": {new_count}}}',
            status_code=200,
            headers=headers,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error updating visitor count: {e}")
        return func.HttpResponse(
            body=f'{{"error": "{str(e)}"}}',
            status_code=500,
            mimetype="application/json"
        )
