import graphene

from dmarc_report_api.queries.ip_enrichment.ip_data import IPData


class IPEnrichment(graphene.ObjectType):
    """

    """

    source_ip = graphene.String(description="")
    ip_data = graphene.Field(lambda: IPData, description="")
