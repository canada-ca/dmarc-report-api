import os
import json
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants

import azure.cosmos.database

AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT')
AZURE_KEY = os.getenv('AZURE_KEY')
DATABASE_NAME = os.getenv('DATABASE')
CONTAINER_NAME = os.getenv('CONTAINER')

client = cosmos_client.CosmosClient(AZURE_ENDPOINT, {'masterKey': AZURE_KEY})

database = client.ReadDatabase("dbs/" + DATABASE_NAME)
container = client.ReadContainer("dbs/" + DATABASE_NAME + "/colls/" + CONTAINER_NAME)


def fetch_reports(domain):
    reports = client.QueryItems(
        "dbs/" + DATABASE_NAME + "/colls/" + CONTAINER_NAME,
        'SELECT * FROM c WHERE c.header_from="' + domain + '"',
        {'enableCrossPartitionQuery': True}
    )

    rtr_list = []
    for item in reports:
        rtr_list.append(item)

    return rtr_list
