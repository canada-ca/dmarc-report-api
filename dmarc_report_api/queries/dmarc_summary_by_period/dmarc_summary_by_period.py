import graphene
from dmarc_report_api.queries.shared_structures.period import Period


class DmarcSummaryByPeriod(graphene.ObjectType):
    """
    This object contains the information for dmarc summaries by individual
    periods
    """

    id = graphene.String(description="domain that period data is collected from")
    period = graphene.Field(
        lambda: Period,
        description="Object containing information for data collection period",
    )
