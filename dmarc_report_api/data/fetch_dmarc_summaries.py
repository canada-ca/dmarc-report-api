import os
import json
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors

from graphql import GraphQLError

SUMMARIES_CONTAINER = os.getenv('SUMMARIES_CONTAINER')

from dmarc_report_api.data.azure_connection import (
    client,
    DATABASE_NAME
)


def fetch_summaries(domain, start_date, end_date):
    try:
        reports = client.QueryItems(
            "dbs/" + DATABASE_NAME + "/colls/" + SUMMARIES_CONTAINER,
            '''SELECT * FROM c IN dmarc-summaries.periods WHERE c.id = '{domain}' AND c.start > '{start_date}' AND c.end < '{end_date}' '''.format(
                domain=domain,
                start_date=str(start_date),
                end_date=str(end_date)
            ),
            {'enableCrossPartitionQuery': True}
        )
        rtr_list = []
        for item in reports:
            rtr_list.append(item)

    except errors.CosmosError as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    return rtr_list


demo = fetch_summaries("cerb.canada.ca", "2020-04-06", "2020-05-06")
for test in demo:
    print(json.dumps(test, indent=2))

