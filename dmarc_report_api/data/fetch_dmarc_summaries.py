import os
import azure.cosmos.errors as errors
from graphql import GraphQLError
from dmarc_report_api.data.azure_connection import client, DATABASE_NAME

SUMMARIES_CONTAINER = os.getenv("SUMMARIES_CONTAINER")


def fetch_summary_by_period(domain, start_date, end_date):
    try:
        reports = client.QueryItems(
            "dbs/" + DATABASE_NAME + "/colls/" + SUMMARIES_CONTAINER,
            """SELECT l.start_date, l.end_date, l.top_senders, l.category_totals FROM c JOIN l IN c.periods WHERE c.id = '{domain}' AND l.start_date = '{start_date}' AND l.end_date = '{end_date}'""".format(
                domain=domain, start_date=str(start_date), end_date=str(end_date)
            ),
            {"enableCrossPartitionQuery": True},
        )
        rtr_list = []
        for item in reports:
            rtr_list.append(item)

    except errors.CosmosError as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    try:
        reports = client.QueryItems(
            "dbs/" + DATABASE_NAME + "/colls/" + SUMMARIES_CONTAINER,
            """SELECT c.id FROM c JOIN l IN c.periods WHERE c.id = '{domain}'""".format(
                domain=domain, start_date=str(start_date), end_date=str(end_date)
            ),
            {"enableCrossPartitionQuery": True},
        )
        id_list = []
        for item in reports:
            id_list.append(item)

    except errors.CosmosError as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    return {
        "id": id_list[0].get("id", None),
        "periods": rtr_list
    }


def fetch_all_summaries_by_domain(domain, start_date, end_date):
    try:
        reports = client.QueryItems(
            "dbs/" + DATABASE_NAME + "/colls/" + SUMMARIES_CONTAINER,
            """SELECT l.start_date, l.end_date, l.top_senders, l.category_totals FROM c JOIN l IN c.periods WHERE c.id = '{domain}' AND l.start_date >= '{start_date}' AND l.end_date <= '{end_date}' """.format(
                domain=domain, start_date=str(start_date), end_date=str(end_date)
            ),
            {"enableCrossPartitionQuery": True},
        )
        rtr_list = []
        for item in reports:
            rtr_list.append(item)

    except errors.CosmosError as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    try:
        reports = client.QueryItems(
            "dbs/" + DATABASE_NAME + "/colls/" + SUMMARIES_CONTAINER,
            """SELECT c.id FROM c JOIN l IN c.periods WHERE c.id = '{domain}'""".format(
                domain=domain, start_date=str(start_date), end_date=str(end_date)
            ),
            {"enableCrossPartitionQuery": True},
        )
        id_list = []
        for item in reports:
            id_list.append(item)

    except errors.CosmosError as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    return {
        "id": id_list[0].get("id", None),
        "periods": rtr_list
    }
