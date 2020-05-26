import graphene

from dmarc_report_api.queries.dmarc_summary_by_period.resolver import (
    resolve_dmarc_summary_by_period,
)
from dmarc_report_api.scalars import GCURL
from dmarc_report_api.queries.dmarc_summary_by_period.dmarc_summary_by_period import (
    DmarcSummaryByPeriod,
)


get_dmarc_summary_by_period = graphene.Field(
    lambda: DmarcSummaryByPeriod,
    domain=graphene.Argument(
        GCURL, description="Domain used to select data", required=True
    ),
    start_date=graphene.Argument(
        graphene.Date,
        description="Set the start date in a date range select.",
        required=False,
    ),
    end_date=graphene.Argument(
        graphene.Date,
        description="Set the end date in a date range select.",
        required=False,
    ),
    description="Summarized DMARC aggregate reports",
    resolver=resolve_dmarc_summary_by_period,
)
