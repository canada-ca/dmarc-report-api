import graphene

from dmarc_report_api.scalars import URL

from dmarc_report_api.queries.dmarc_summaries.summary_query import DmarcSummaries
from dmarc_report_api.queries.dmarc_summaries.period_resolver import (
    resolve_dmarc_summary_by_period,
)
from dmarc_report_api.queries.dmarc_summaries.total_resolver import (
    resolve_total_dmarc_summaries,
)

get_dmarc_summary_by_period = graphene.Field(
    lambda: DmarcSummaries,
    domain=graphene.Argument(
        URL, description="Domain used to select data", required=True
    ),
    start_date=graphene.Argument(
        graphene.String,
        description="Set the start date in a date range select.",
        required=False,
    ),
    end_date=graphene.Argument(
        graphene.String,
        description="Set the end date in a date range select.",
        required=False,
    ),
    description="Summarized DMARC aggregate reports",
    resolver=resolve_dmarc_summary_by_period,
)

get_total_dmarc_summaries = graphene.List(
    lambda: DmarcSummaries,
    domain=graphene.Argument(
        URL, description="Domain used to select reports", required=True
    ),
    start_date=graphene.Argument(
        graphene.String,
        description="Set the start date in a date range select.",
        required=False,
    ),
    end_date=graphene.Argument(
        graphene.String,
        description="Set the end date in a date range select.",
        required=False,
    ),
    description="Summarized DMARC aggregate reports",
    resolver=resolve_total_dmarc_summaries,
)
