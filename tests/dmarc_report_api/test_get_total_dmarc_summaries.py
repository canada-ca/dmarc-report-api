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
from tests.mock_data.mock_total_dmarc_summaries import mock_data
from tests.expected_result_dictionaries.summaries_total_data import expected_results


def auth_header():
    env = create_environ()
    env.update(HTTP_AUTHORIZATION=jwt_gen(os.getenv("TOKEN")))
    return Request(env)


def test_valid_query_get_dmarc_total(mocker):
    """
    Test to see if the getTotalDmarcSummaries query works
    """
    mocker.patch(
        "dmarc_report_api.queries.dmarc_summary_total.resolver.fetch_all_summaries_by_domain",
        autospec=True,
        return_value=mock_data,
    )

    query = """
    {
        getTotalDmarcSummaries (
            domain: "test.domain.ca"
            startDate: "1970-01-01"
            endDate: "2070-01-01"
        ) {
            id
            periods {
                startDate
                endDate
                topSenders {
                    fullPass {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    spfFailure {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    spfMisaligned {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    dkimFailure {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    dkimMisaligned {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    dmarcFailure {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
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
        "dmarc_report_api.queries.dmarc_summary_total.resolver.fetch_all_summaries_by_domain",
        autospec=True,
        return_value=[],
    )

    query = """
    {
        getTotalDmarcSummaries (
            domain: "test.domain.ca"
            startDate: "1970-01-01"
            endDate: "2000-01-01"
        ) {
            id
            periods {
                startDate
                endDate
                topSenders {
                    fullPass {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    spfFailure {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    spfMisaligned {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    dkimFailure {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    dkimMisaligned {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    dmarcFailure {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
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
        "dmarc_report_api.queries.dmarc_summary_total.resolver.fetch_all_summaries_by_domain",
        autospec=True,
        return_value=[],
    )

    query = """
    {
        getTotalDmarcSummaries (
            domain: "domain.does.not.work"
            startDate: "1970-01-01"
            endDate: "2070-01-01"
        ) {
            id
            periods {
                startDate
                endDate
                topSenders {
                    fullPass {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    spfFailure {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    spfMisaligned {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    dkimFailure {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    dkimMisaligned {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
                    }
                    dmarcFailure {
                        sourceIpAddress
                        spfDomains
                        dkimDomains
                        dkimSelectors
                        total
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
