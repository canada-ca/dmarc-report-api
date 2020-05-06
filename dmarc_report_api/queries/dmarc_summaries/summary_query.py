import graphene

from dmarc_report_api.scalars import URL, EmailAddress
from dmarc_report_api.queries.dmarc_summaries.top_senders import TopSenders
from dmarc_report_api.queries.dmarc_summaries.category_totals import CategoryTotals


class DmarcSummaries(graphene.ObjectType):
    """

    """
    top_senders = graphene.Field(
        lambda: TopSenders,
        description=""
    )
    category_totals = graphene.Field(
        lambda: CategoryTotals,
        description=""
    )
