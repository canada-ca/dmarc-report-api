import os

from flask import Request
from graphene.test import Client
from json import dumps
from pytest import fail
from werkzeug.test import create_environ

from dmarc_report_api.schema import schema
from scripts.jwt_gen import jwt_gen
from tests.test_data.get_yearly_dmarc_summaries import (
    mock_data,
    expected_results,
)


def auth_header():
    env = create_environ()
    env.update(HTTP_AUTHORIZATION=jwt_gen(os.getenv("TOKEN")))
    return Request(env)


def test_valid_query_get_dmarc_total(mocker):
    """
    Test to see if the getTotalDmarcSummaries query works
    """
    mocker.patch(
        "dmarc_report_api.queries.yearly_dmarc_summaries.resolver.fetch_summary",
        autospec=True,
        return_value=mock_data,
    )

    query = """
    {
        getYearlyDmarcSummaries (
            domain: "test.domain.gc.ca"
            startDate: "1970-01-01"
            endDate: "2070-01-01"
        ) {
            id
            periods {
                startDate
                endDate
                detailTables {
                    fullPass {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    spfFailure {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    spfMisaligned {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    dkimFailure {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    dkimMisaligned {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    dmarcFailure {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                categoryTotals {
                    dmarcFailNone
                    dmarcFailQuarantine
                    dmarcFailReject
                    spfFailDkimPass
                    spfPassDkimFail
                    spfPassDkimPass
                }
            }
        }
    }
    """

    executed = Client(schema=schema).execute(query, context_value=auth_header())

    if "errors" in executed:
        fail(
            "Tried to execute the getDmarcSummaryByPeriod query, Instead: {}".format(
                dumps(executed, indent=2)
            )
        )

    assert executed == expected_results


def test_invalid_query_get_total_dmarc_summaries_no_data_in_range(mocker):
    """
    Test to see if error appears for query in date range that does not exist
    """
    mocker.patch(
        "dmarc_report_api.queries.yearly_dmarc_summaries.resolver.fetch_summary",
        autospec=True,
        return_value={"id": None, "periods": {}},
    )

    query = """
    {
        getYearlyDmarcSummaries (
            domain: "test.domain.gc.ca"
            startDate: "1970-01-01"
            endDate: "2000-01-01"
        ) {
            id
            periods {
                startDate
                endDate
                detailTables {
                    fullPass {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    spfFailure {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    spfMisaligned {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    dkimFailure {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    dkimMisaligned {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    dmarcFailure {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                categoryTotals {
                    dmarcFailNone
                    dmarcFailQuarantine
                    dmarcFailReject
                    spfFailDkimPass
                    spfPassDkimFail
                    spfPassDkimPass
                }
            }
        }
    }
    """

    executed = Client(schema=schema).execute(query, context_value=auth_header())

    if "errors" not in executed:
        fail(
            "Tried to execute the getTotalDmarcSummaries query thinking it "
            "would error out, Instead: {}".format(dumps(executed, indent=2))
        )

    errors, data = executed.values()
    [first] = errors
    expected_message = first["message"]
    assert (
        expected_message == "Error, there is no data for that time "
        "period, or domain is incorrect"
    )


def test_invalid_query_get_total_dmarc_summaries_incorrect_domain(mocker):
    """
    Test to see error appears when db fetch returns nil because of incorrect
    domain
    """
    mocker.patch(
        "dmarc_report_api.queries.yearly_dmarc_summaries.resolver.fetch_summary",
        autospec=True,
        return_value={"id": None, "periods": {}},
    )

    query = """
    {
        getYearlyDmarcSummaries (
            domain: "domain.does.not.work.gc.ca"
            startDate: "1970-01-01"
            endDate: "2070-01-01"
        ) {
            id
            periods {
                startDate
                endDate
                detailTables {
                    fullPass {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    spfFailure {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    spfMisaligned {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    dkimFailure {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    dkimMisaligned {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                    dmarcFailure {
                        sourceIpAddress
                        envelopeFrom
                        spfDomains
                        dkimDomains
                        dkimSelectors
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
                categoryTotals {
                    dmarcFailNone
                    dmarcFailQuarantine
                    dmarcFailReject
                    spfFailDkimPass
                    spfPassDkimFail
                    spfPassDkimPass
                }
            }
        }
    }
    """

    executed = Client(schema=schema).execute(query, context_value=auth_header())

    if "errors" not in executed:
        fail(
            "Tried to execute the getTotalDmarcSummaries query thinking it "
            "would error out, Instead: {}".format(dumps(executed, indent=2))
        )

    errors, data = executed.values()
    [first] = errors
    expected_message = first["message"]
    assert (
        expected_message == "Error, there is no data for that time "
        "period, or domain is incorrect"
    )
