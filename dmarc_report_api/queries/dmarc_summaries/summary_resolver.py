import datetime

from graphql import GraphQLError

from dmarc_report_api.queries.dmarc_summaries.summary_query import DmarcSummaries
from dmarc_report_api.data.fetch_dmarc_summaries import fetch_summaries
from dmarc_report_api.auth import require_token


# @require_token
def resolve_dmarc_summaries(self, info, **kwargs):
    domain = kwargs.get('domain', None)
    start_date = kwargs.get('start_date', None)
    end_date = kwargs.get('end_date', None)

    if domain is None:
        raise GraphQLError("Error, domain was not supplied")

    if (start_date is not None and end_date is None) or \
        (start_date is None and end_date is not None):
        raise GraphQLError(
            "Error, only one date was supplied need two for date range select"
        )

    if start_date > end_date:
        raise GraphQLError('Error, start date cannot be greater then end date')

    summaries = fetch_summaries(
        domain=domain,
        start_date=start_date,
        end_date=end_date
    )

    for summary in summaries:
        return DmarcSummaries(
            summary['top_senders'],
            summary['category_totals']
        )
