import os
import pytest
import pytest_mock

from flask import Request
from graphene.test import Client
from pytest import fail
from werkzeug.test import create_environ

from dmarc_report_api.schema import schema
from scripts.jwt_gen import jwt_gen
from tests.mock_data.mock_ip_enrichment import mock_data


def auth_header():
    env = create_environ()
    env.update(HTTP_AUTHORIZATION=jwt_gen(os.getenv("TOKEN")))
    return Request(env)


def test_query_get_ip_enrichment(mocker):
    """
    Test to see if the getIpEnrichment query works
    """
    mocker.patch(
        "dmarc_report_api.queries.ip_enrichment.ip_enrichment_resolver"
        ".fetch_ip_enrichment",
        autospec=True,
        return_value=mock_data,
    )

    query = """
    {
        getIpEnrichmentData(
            domain: "test.ca"
        ) {
            sourceIp
            ipData {
                country
                countryCode
                isp
                org
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

    expected_result = {
        "data": {
            "getIpEnrichmentData": [
                {
                    "sourceIp": "12.34.567.891",
                    "ipData": {
                        "country": "Canada",
                        "countryCode": "CA",
                        "isp": "Some Cool ISP",
                        "org": "SCI DATA (canada-east-1)",
                        "asName": "SCI-DATA",
                        "asNum": "123456",
                        "asOrg": "Some Cool, Inc.",
                        "dnsHost": "dns.test.ca",
                        "dnsDomain": "test.ca",
                    },
                }
            ]
        }
    }

    if "errors" in executed:
        fail(
            "Tried to execute the getIpEnrichment query, this error occurred: "
            "{}".format(executed)
        )

    assert executed == expected_result
