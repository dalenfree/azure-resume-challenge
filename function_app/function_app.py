import logging
import azure.functions as func
import os
import json
from azure.cosmos import CosmosClient, exceptions

# Create the Azure Function App (anonymous access for simplicity)
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Define the HTTP route for GET and POST
@app.route(route="http_trigger", methods=["GET", "POST"])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing HTTP request for visitor counter...")

    # === 1. Initialize Cosmos DB client ===
    cosmos_url = "https://rccdbaccount.documents.azure.com:443/"
    cosmos_key = os.getenv("COSMOS_DB_KEY")  # store your key securely in Azure configuration!

    if not cosmos_key:
        return func.HttpResponse(
            json.dumps({"error": "Missing Cosmos DB key in environment variables."}),
            status_code=500,
            mimetype="application/json"
        )

    client = CosmosClient(cosmos_url, credential=cosmos_key)

    # === 2. Select database and container ===
    database_name = "TablesDB"  
    container_name = "VisitorCount"

    try:
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)
    except exceptions.CosmosResourceNotFoundError:
        return func.HttpResponse(
            json.dumps({"error": "Database or container not found."}),
            status_code=404,
            mimetype="application/json"
        )

    # === 3. Define keys ===
    partition_key = "counter"
    item_id = "visitors"

    # === 4. Handle GET requests ===
    if req.method == "GET":
        try:
            item = container.read_item(item=item_id, partition_key=partition_key)
            count = item.get("count", 0)
            return func.HttpResponse(
                json.dumps({"count": count}),
                mimetype="application/json"
            )
        except exceptions.CosmosResourceNotFoundError:
            return func.HttpResponse(
                json.dumps({"error": "Visitor record not found."}),
                status_code=404,
                mimetype="application/json"
            )

    # === 5. Handle POST requests ===
    elif req.method == "POST":
        try:
            item = container.read_item(item=item_id, partition_key=partition_key)
            item["count"] = item.get("count", 0) + 1
            container.replace_item(item=item_id, body=item)

            return func.HttpResponse(
                json.dumps({"message": "Visitor count incremented", "new_count": item["count"]}),
                mimetype="application/json",
                status_code=200
            )
        except exceptions.CosmosResourceNotFoundError:
            # If the record doesn't exist, create it
            new_item = {
                "id": item_id,
                "counter": partition_key,
                "count": 1
            }
            container.create_item(body=new_item)
            return func.HttpResponse(
                json.dumps({"message": "Visitor record created", "new_count": 1}),
                mimetype="application/json",
                status_code=201
            )

    # === 6. Handle unsupported methods ===
    else:
        return func.HttpResponse(
            json.dumps({"error": "Method not allowed. Use GET or POST."}),
            status_code=405,
            mimetype="application/json"
        )