import os

from graphql import GraphQLError
from dmarc_report_api.data.azure_connection import create_azure_clients

DATABASE_NAME = os.getenv("DATABASE")
IP_ENRICHMENT_CONTAINER = os.getenv("IP_ENRICHMENT_CONTAINER")


def fetch_ip_enrichment(domain):
    ip_client = create_azure_clients(container=IP_ENRICHMENT_CONTAINER)

    try:
        reports = ip_client.query_items(
            """SELECT DISTINCT c.ip_enrichment FROM c WHERE c.id = '{domain}'""".format(
                domain=domain
            ),
        )
        rtr_list = []
        for item in reports:
            rtr_list.append(item)

    except Exception as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    return rtr_list
