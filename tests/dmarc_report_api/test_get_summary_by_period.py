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
from tests.mock_data.mock_dmarc_summary_by_period import mock_data
from tests.expected_result_dictionaries.summary_data_by_period import \
    expected_summary_period_data


def auth_header():
    env = create_environ()
    env.update(HTTP_AUTHORIZATION=jwt_gen(os.getenv("TOKEN")))
    return Request(env)


def test_valid_query_get_dmarc_summary_by_period(mocker):
    """
    Test to see if the getDmarcSummaryByPeriod query works
    """
    mocker.patch(
        "dmarc_report_api.queries.dmarc_summaries.period_resolver.fetch_summary_by_period",
        autospec=True,
        return_value=mock_data
    )

    query = '''
    {
        getDmarcSummaryByPeriod (
            domain: "test.domain.ca"
            startDate: "2020-04-01"
            endDate: "2020-04-30"
        ) {
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
                spfPassDkimPass
                spfFailDkimPass
                dmarcFailNone
                forwarded
                arcPass
                spfPassDkimFail
                dmarcFailReject
                dmarcFailQuarantine
            }
        }
    }
    '''

    executed = Client(schema=schema).execute(query, context_value=auth_header())

    if "errors" in executed:
        fail(
            "Tried to execute the getDmarcSummaryByPeriod query, Instead: {}"
            .format(dumps(executed, indent=2))
        )

    assert executed == expected_summary_period_data


def test_invalid_query_get_dmarc_summary_by_period_incorrect_start_date(mocker):
    """
    Test to see if correct error appears when start date does not match any
    periods in the db
    """
    mocker.patch(
        "dmarc_report_api.queries.dmarc_summaries.period_resolver.fetch_summary_by_period",
        autospec=True,
        return_value=[]
    )

    query = '''
        {
            getDmarcSummaryByPeriod (
                domain: "test.domain.ca"
                startDate: "2020-04-05"
                endDate: "2020-04-30"
            ) {
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
                    spfPassDkimPass
                    spfFailDkimPass
                    dmarcFailNone
                    forwarded
                    arcPass
                    spfPassDkimFail
                    dmarcFailReject
                    dmarcFailQuarantine
                }
            }
        }
        '''

    executed = Client(schema=schema).execute(query, context_value=auth_header())

    if "errors" not in executed:
        fail(
            "Tried to execute the getDmarcSummaryByPeriod query thinking it "
            "would error out, Instead: {}".format(dumps(executed, indent=2))
        )

    errors, data = executed.values()
    [first] = errors
    expected_message = first["message"]
    assert expected_message == "Error, there is no data for that time " \
                               "period, or domain is incorrect"


def test_invalid_query_get_dmarc_summary_by_period_incorrect_end_date(mocker):
    """
    Test to see if correct error appears when end date does not match any
    periods in the db
    """
    mocker.patch(
        "dmarc_report_api.queries.dmarc_summaries.period_resolver.fetch_summary_by_period",
        autospec=True,
        return_value=[]
    )

    query = '''
        {
            getDmarcSummaryByPeriod (
                domain: "test.domain.ca"
                startDate: "2020-04-01"
                endDate: "2020-04-25"
            ) {
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
                    spfPassDkimPass
                    spfFailDkimPass
                    dmarcFailNone
                    forwarded
                    arcPass
                    spfPassDkimFail
                    dmarcFailReject
                    dmarcFailQuarantine
                }
            }
        }
        '''

    executed = Client(schema=schema).execute(query, context_value=auth_header())

    if "errors" not in executed:
        fail(
            "Tried to execute the getDmarcSummaryByPeriod query thinking it "
            "would error out, Instead: {}".format(dumps(executed, indent=2))
        )

    errors, data = executed.values()
    [first] = errors
    expected_message = first["message"]
    assert expected_message == "Error, there is no data for that time " \
                               "period, or domain is incorrect"
