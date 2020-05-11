from graphql import GraphQLError

from dmarc_report_api.queries.ip_enrichment import IPEnrichment
from dmarc_report_api.shared_functions import cleanse_input
from dmarc_report_api.data.fetch_ip_enrichment import fetch_ip_enrichment
from dmarc_report_api.auth import require_token


@require_token
def resolve_ip_enrichment(self, info, **kwargs):
    domain = cleanse_input(kwargs.get("domain", None))

    if domain is None or domain == "":
        raise GraphQLError("Error, domain was not supplied")

    ip_data_set = fetch_ip_enrichment(domain=domain)

    if not ip_data_set:
        raise GraphQLError("Error, there is no data for that domain")

    rtr_list = []
    for data in ip_data_set:
        for k, v in data["ip_enrichment"].items():
            rtr_list.append(IPEnrichment(k, v))

    return rtr_list
