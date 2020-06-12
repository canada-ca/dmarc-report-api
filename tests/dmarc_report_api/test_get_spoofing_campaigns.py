import os

from flask import Request
from graphene.test import Client
from json import dumps
from pytest import fail
from werkzeug.test import create_environ

from dmarc_report_api.schema import schema
from scripts.jwt_gen import jwt_gen
from tests.test_data.get_spoofing_campaigns import (
    mock_data,
    expected_results,
)


def auth_header():
    env = create_environ()
    env.update(HTTP_AUTHORIZATION=jwt_gen(os.getenv("TOKEN")))
    return Request(env)


def test_valid_query_get_spoofing_campaigns(mocker):
    """
    Test to see if the getSpoofingCampaigns query works
    """
    mocker.patch(
        "dmarc_report_api.queries.spoofing_campaigns.resolver.fetch_campaigns",
        autospec=True,
        return_value=mock_data,
    )

    query = """
    {
        getSpoofingCampaigns(domain: "fake.domain.gc.ca") {
            id
            campaigns {
                reportEndDate
                headerFrom
                envelopeFrom
                sourceIpAddress
                totalMessages
                countryCode
                ispOrg
                prefixOrg
                asName
                asNum
                asOrg
                dnsHost
                dnsDomain
            }
        }
    }
    """

    executed = Client(schema=schema).execute(query, context_value=auth_header())

    if "errors" in executed:
        fail(
            "Tried to execute the getSpoofingCampaigns query, Instead: {}".format(
                dumps(executed, indent=2)
            )
        )

    assert executed == expected_results


def test_invalid_query_get_spoofing_campaigns_incorrect_domain(mocker):
    """
    Test to see error appears when db fetch returns nil because of incorrect
    domain
    """
    mocker.patch(
        "dmarc_report_api.queries.spoofing_campaigns.resolver.fetch_campaigns",
        autospec=True,
        return_value={"id": None, "campaigns": {}},
    )

    query = """
        {
        getSpoofingCampaigns(domain: "test.domain.gc.ca") {
            id
            campaigns {
                reportEndDate
                headerFrom
                envelopeFrom
                sourceIpAddress
                totalMessages
                countryCode
                ispOrg
                prefixOrg
                asName
                asNum
                asOrg
                dnsHost
                dnsDomain
            }
        }
    }
    """

    executed = Client(schema=schema).execute(query, context_value=auth_header())

    if "errors" not in executed:
        fail(
            "Tried to execute the getSpoofingCampaigns query thinking it "
            "would error out, Instead: {}".format(dumps(executed, indent=2))
        )

    errors, data = executed.values()
    [first] = errors
    expected_message = first["message"]
    assert expected_message == "Error, there is no spoofing campaigns for that domain."
