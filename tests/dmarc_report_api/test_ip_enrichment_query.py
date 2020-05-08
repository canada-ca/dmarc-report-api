import os
import pytest
import pytest_mock

from flask import Request
from graphene.test import Client
from json import dumps
from pytest import fail
from werkzeug.test import create_environ

from dmarc_report_api.schema import schema
from scripts.jwt_gen import jwt_gen
from tests.mock_data.mock_ip_enrichment import mock_data


def auth_header():
    env = create_environ()
    env.update(HTTP_AUTHORIZATION=jwt_gen(os.getenv("TOKEN")))
    return Request(env)


def test_valid_query_get_ip_enrichment(mocker):
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
            "{}".format(dumps(executed, indent=2))
        )

    assert executed == expected_result


def test_query_get_ip_enrichment_invalid_domain(mocker):
    """
    Test to see if error appears if domain is left blank
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
            domain: "notAUrl"
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

    if "errors" not in executed:
        fail(
            "Expecting query to error out, Instead "
            "{}".format(
                dumps(executed, indent=2)
            )
        )

    errors = executed.values()
    [first] = errors
    expected_message = first[0]["message"]
    assert expected_message == "Value is not a valid URL : notAUrl"


def test_query_get_ip_enrichment_empty_data_return(mocker):
    """
    Test to see if error appears if no data is found for that domain
    """
    mocker.patch(
        "dmarc_report_api.queries.ip_enrichment.ip_enrichment_resolver"
        ".fetch_ip_enrichment",
        autospec=True,
        return_value=[],
    )

    query = """
    {
        getIpEnrichmentData(
            domain: "empty.test.ca"
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

    if "errors" not in executed:
        fail(
            "Expecting query to error out, Instead "
            "{}".format(
                dumps(executed, indent=2)
            )
        )

    errors, data = executed.values()
    [first] = errors
    message, _, _ = first.values()

    assert message == "Error, there is no data for that domain"
