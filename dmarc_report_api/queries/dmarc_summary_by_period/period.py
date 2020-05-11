import graphene
import datetime

from dmarc_report_api.queries.dmarc_summary_by_period.top_senders import TopSenders
from dmarc_report_api.queries.dmarc_summary_by_period.category_totals import CategoryTotals


class Period(graphene.ObjectType):
    """
    Object that contains information for each data collection period
    """
    start_date = graphene.Date(
        description="Start date of data collection"
    )
    end_date = graphene.Date(
        description="End date of data collection"
    )
    top_senders = graphene.Field(
        lambda: TopSenders,
        description="Top senders for each category"
    )
    category_totals = graphene.Field(
        lambda: CategoryTotals,
        description="Category totals for quick viewing"
    )

    def resolve_start_date(self: dict, info):
        return datetime.datetime.strptime(self.get("start_date", "1970-01-01"), "%Y-%m-%d")

    def resolve_end_date(self: dict, info):
        return datetime.datetime.strptime(self.get("end_date", "1970-01-01"), "%Y-%m-%d")
