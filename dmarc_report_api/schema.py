import graphene

from dmarc_report_api.queries.ip_enrichment import get_ip_enrichment_data
from dmarc_report_api.queries.dmarc_summary_total import get_total_dmarc_summaries
from dmarc_report_api.queries.dmarc_summary_by_period import get_dmarc_summary_by_period


class Query(graphene.ObjectType):
    # Get dmarc summary query object
    get_dmarc_summary_by_period = get_dmarc_summary_by_period

    # Get all dmarc summaries query object
    get_total_dmarc_summaries = get_total_dmarc_summaries

    get_ip_enrichment_data = get_ip_enrichment_data


schema = graphene.Schema(query=Query)
