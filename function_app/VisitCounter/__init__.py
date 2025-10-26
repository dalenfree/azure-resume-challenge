import json, logging, time
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.data.tables import TableClient, UpdateMode
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError
from azure.core import MatchConditions

TABLE_ENDPOINT = "https://rccdbaccount.table.cosmos.azure.com:443/"
TABLE_NAME = "VisitorCounter"
PARTITION_KEY = "counter"
ROW_KEY = "visitors"

credential = DefaultAzureCredential()

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        table = TableClient(endpoint=TABLE_ENDPOINT, table_name=TABLE_NAME, credential=credential)
        for _ in range(5):
            try:
                entity = table.get_entity(PARTITION_KEY, ROW_KEY)
            except ResourceNotFoundError:
                try:
                    table.create_entity({"PartitionKey": PARTITION_KEY, "RowKey": ROW_KEY, "count": 0})
                except HttpResponseError:
                    time.sleep(0.1)
                continue
            etag = getattr(entity, "_metadata", {}).get("etag") or entity.get("etag")
            count = int(entity.get("count", 0)) + 1
            entity["count"] = count
            try:
                table.update_entity(entity, mode=UpdateMode.REPLACE, etag=etag, match_condition=MatchConditions.IfNotModified)
                return func.HttpResponse(json.dumps({"count": count}), mimetype="application/json")
            except HttpResponseError:
                time.sleep(0.1)
        final = table.get_entity(PARTITION_KEY, ROW_KEY)
        return func.HttpResponse(json.dumps({"count": int(final.get("count", 0))}), mimetype="application/json")
    except Exception as e:
        logging.exception("Unhandled")
        return func.HttpResponse(json.dumps({"error": str(e)}), status_code=500, mimetype="application/json")
