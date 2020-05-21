import os
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as errors

from graphql import GraphQLError

AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_KEY")

try:
    client = cosmos_client.CosmosClient(AZURE_ENDPOINT, {"masterKey": AZURE_KEY})
except errors.HttpResponseError as e:
    raise GraphQLError("Cosmos HTTP Error: " + str(e))
