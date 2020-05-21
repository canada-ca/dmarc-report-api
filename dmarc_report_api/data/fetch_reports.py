import os

from graphql import GraphQLError

from dmarc_report_api.data.azure_connection import client

DATABASE_NAME = os.getenv("DATABASE")
RECORD_CONTAINER = os.getenv("RECORD_CONTAINER")

def fetch_reports(domain, start_date, end_date):
    try:
        reports = client.QueryItems(
            "dbs/" + DATABASE_NAME + "/colls/" + RECORD_CONTAINER,
            """SELECT * FROM c WHERE c.header_from='{domain}' AND c.report_end_date > '{start_date}' AND c.report_end_date < '{end_date}' ORDER BY c.report_end_date ASC""".format(
                domain=domain, start_date=str(start_date), end_date=str(end_date)
            ),
            {"enableCrossPartitionQuery": True},
        )
        rtr_list = []
        for item in reports:
            rtr_list.append(item)

    except Exception as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    return rtr_list
