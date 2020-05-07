import graphene

from dmarc_report_api.scalars import URL, EmailAddress
from dmarc_report_api.queries.dmarc_summaries.top_senders import TopSenders
from dmarc_report_api.queries.dmarc_summaries.category_totals import CategoryTotals


class DmarcSummaries(graphene.ObjectType):
    """
    Summarized DMARC aggregate reports
    """
    start_date = graphene.Date(
        description="Start date of data collection"
    )
    end_date = graphene.Date(
        description="End date of data collection"
    )
    top_senders = graphene.Field(
        lambda: TopSenders, description="Top senders for each category"
    )
    category_totals = graphene.Field(
        lambda: CategoryTotals, description="Category totals for quick viewing"
    )
