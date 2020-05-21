import os

from graphql import GraphQLError
from dmarc_report_api.data.azure_connection import client

DATABASE_NAME = os.getenv("DATABASE")
SUMMARIES_CONTAINER = os.getenv("SUMMARIES_CONTAINER")


def fetch_ip_enrichment(domain):
    try:
        reports = client.QueryItems(
            "dbs/" + DATABASE_NAME + "/colls/" + SUMMARIES_CONTAINER,
            """SELECT DISTINCT c.ip_enrichment FROM c WHERE c.id = '{domain}'""".format(
                domain=domain
            ),
            {"enableCrossPartitionQuery": True},
        )
        rtr_list = []
        for item in reports:
            rtr_list.append(item)

    except Exception as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    return rtr_list
