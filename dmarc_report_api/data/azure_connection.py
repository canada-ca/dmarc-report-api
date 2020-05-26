import os
from azure.cosmos import CosmosClient
import azure.cosmos.exceptions as errors

from graphql import GraphQLError

AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_KEY")
DATABASE = os.getenv("DATABASE")


def create_azure_clients(container):
    try:
        client = CosmosClient(AZURE_ENDPOINT, {"masterKey": AZURE_KEY})
        db_client = client.get_database_client(database=DATABASE)
        return db_client.get_container_client(container=container)
    except errors.HttpResponseError as e:
        raise GraphQLError("Cosmos HTTP Error: " + str(e))
