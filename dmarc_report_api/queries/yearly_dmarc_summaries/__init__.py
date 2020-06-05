import graphene

from dmarc_report_api.queries.yearly_dmarc_summaries.resolver import (
    resolve_total_dmarc_summaries,
)
from dmarc_report_api.scalars import CustomDate, GCURL
from dmarc_report_api.queries.yearly_dmarc_summaries.yearly_dmarc_summaries import (
    DmarcSummaries,
)


get_yearly_dmarc_summaries = graphene.Field(
    lambda: DmarcSummaries,
    domain=graphene.Argument(
        GCURL, description="Domain used to select reports", required=True
    ),
    start_date=graphene.Argument(
        CustomDate,
        description="Set the start date in a date range select.",
        required=False,
    ),
    end_date=graphene.Argument(
        CustomDate,
        description="Set the end date in a date range select.",
        required=False,
    ),
    description="Summarized DMARC aggregate reports",
    resolver=resolve_total_dmarc_summaries,
)
