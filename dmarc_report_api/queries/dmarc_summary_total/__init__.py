import graphene

from dmarc_report_api.queries.dmarc_summary_total.resolver import (
    resolve_total_dmarc_summaries,
)
from dmarc_report_api.scalars import URL
from dmarc_report_api.queries.dmarc_summary_total.dmarc_summaries import DmarcSummaries


get_total_dmarc_summaries = graphene.Field(
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
