import graphene
import datetime

from dmarc_report_api.queries.shared_structures.detail_tables import DetailTables
from dmarc_report_api.queries.shared_structures.category_totals import CategoryTotals


class Period(graphene.ObjectType):
    """
    Object that contains information for each data collection period
    """

    start_date = graphene.Date(description="Start date of data collection")
    end_date = graphene.Date(description="End date of data collection")
    detail_tables = graphene.Field(
        lambda: DetailTables, description="Top senders for each category"
    )
    category_totals = graphene.Field(
        lambda: CategoryTotals, description="Category totals for quick viewing"
    )

    def resolve_start_date(self: dict, info):
        return datetime.datetime.strptime(
            self.get("start_date", "1970-01-01"), "%Y-%m-%d"
        )

    def resolve_end_date(self: dict, info):
        return datetime.datetime.strptime(
            self.get("end_date", "1970-01-01"), "%Y-%m-%d"
        )
