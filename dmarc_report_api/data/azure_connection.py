import os
import json
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants

import azure.cosmos.database

from graphql import GraphQLError

AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT')
AZURE_KEY = os.getenv('AZURE_KEY')
DATABASE_NAME = os.getenv('DATABASE')
CONTAINER_NAME = os.getenv('CONTAINER')

try:
    client = cosmos_client.CosmosClient(AZURE_ENDPOINT, {'masterKey': AZURE_KEY})
    database = client.ReadDatabase("dbs/" + DATABASE_NAME)
    container = client.ReadContainer("dbs/" + DATABASE_NAME + "/colls/" + CONTAINER_NAME)
except errors.HTTPFailure as e:
    raise GraphQLError("Cosmos HTTP Error: " + str(e))


def fetch_reports(domain, start_date, end_date):
    try:
        reports = client.QueryItems(
            "dbs/" + DATABASE_NAME + "/colls/" + CONTAINER_NAME,
            "SELECT * FROM c WHERE c.header_from='" + domain + "' AND c.report_begin_date > '" + str(start_date) + "' AND c.report_end_date < '" + str(end_date) + "'",
            {'enableCrossPartitionQuery': True}
        )

        rtr_list = []
        for item in reports:
            rtr_list.append(item)

    except errors.CosmosError as e:
        raise GraphQLError("Cosmos Error: " + str(e))

    return rtr_list
