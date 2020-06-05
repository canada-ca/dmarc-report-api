import os

from graphql import GraphQLError
from dmarc_report_api.data.azure_connection import create_azure_clients

DATABASE_NAME = os.getenv("DATABASE")
SUMMARIES_CONTAINER = os.getenv("SUMMARIES_CONTAINER")


def fetch_summary(domain, start_date, end_date, thirty_days=False):
    summaries_client = create_azure_clients(container=SUMMARIES_CONTAINER)
    if thirty_days == "True":
        query = """SELECT l.start_date, l.end_date, l.detail_tables, l.category_totals FROM c JOIN l IN c.periods WHERE c.id = '{domain}' AND l.start_date = '{start_date}' AND l.end_date = '{end_date}' AND l.thirty_days = true""".format(
            domain=domain, start_date=str(start_date), end_date=str(end_date)
        )
    else:
        query = """SELECT l.start_date, l.end_date, l.detail_tables, l.category_totals FROM c JOIN l IN c.periods WHERE c.id = '{domain}' AND l.start_date >= '{start_date}' AND l.end_date <= '{end_date}' AND l.thirty_days = false""".format(
            domain=domain, start_date=str(start_date), end_date=str(end_date)
        )

    try:
        reports = summaries_client.query_items(query)
        rtr_list = []
        for item in reports:
            rtr_list.append(item)

    except Exception as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    try:
        reports = summaries_client.query_items(
            """SELECT c.id FROM c JOIN l IN c.periods WHERE c.id = '{domain}'""".format(
                domain=domain, start_date=str(start_date), end_date=str(end_date)
            )
        )
        id_list = []
        for item in reports:
            id_list.append(item)

    except Exception as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    return {"id": id_list[0].get("id", None), "periods": rtr_list}
