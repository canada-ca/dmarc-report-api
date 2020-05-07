import graphene

from graphene import relay

from dmarc_report_api.queries.dmarc_summaries import (
    get_dmarc_summary_by_period,
    get_total_dmarc_summaries,
)


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    # Get dmarc summary query object
    get_dmarc_summary_by_period = get_dmarc_summary_by_period

    # Get all dmarc summaries query object
    get_total_dmarc_summaries = get_total_dmarc_summaries


schema = graphene.Schema(query=Query)
