import graphene

from dmarc_report_api.queries.yearly_dmarc_summaries import get_yearly_dmarc_summaries
from dmarc_report_api.queries.dmarc_summary_by_period import get_dmarc_summary_by_period


class Query(graphene.ObjectType):
    # Get dmarc summary query object
    get_dmarc_summary_by_period = get_dmarc_summary_by_period

    # Get all dmarc summaries query object
    get_yearly_dmarc_summaries = get_yearly_dmarc_summaries


schema = graphene.Schema(query=Query)
