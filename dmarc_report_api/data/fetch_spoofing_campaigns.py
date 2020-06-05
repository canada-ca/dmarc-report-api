import os

from graphql import GraphQLError
from dmarc_report_api.data.azure_connection import create_azure_clients

DATABASE_NAME = os.getenv("DATABASE")
SUMMARIES_CONTAINER = os.getenv("SUMMARIES_CONTAINER")


def fetch_campaigns(domain):
    summaries_client = create_azure_clients(container=SUMMARIES_CONTAINER)

    try:
        reports = summaries_client.query_items(
            """SELECT c.id, c.campaigns FROM c WHERE c.id = '{domain}'""".format(
                domain=domain
            )
        )
        id_list = []
        for item in reports:
            id_list.append(item)

    except Exception as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    return {
        "id": id_list[0].get("id", None),
        "campaigns": id_list[0].get("campaigns")
    }
