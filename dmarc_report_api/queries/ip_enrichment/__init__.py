import graphene

from dmarc_report_api.queries.ip_enrichment.ip_enrichment import IPEnrichment
from dmarc_report_api.scalars import URL
from dmarc_report_api.queries.ip_enrichment.ip_enrichment_resolver import (
    resolve_ip_enrichment,
)

get_ip_enrichment_data = graphene.List(
    lambda: IPEnrichment,
    domain=graphene.Argument(
        URL, description="Domain used to select data", required=True
    ),
    description="",
    resolver=resolve_ip_enrichment,
)
