import graphene

from dmarc_report_api.queries.spoofing_campaigns.resolver import resolve_spoofing_campaigns
from dmarc_report_api.queries.spoofing_campaigns.spoofing_campaigns import Campaigns
from dmarc_report_api.scalars import GCURL


get_spoofing_campaigns = graphene.Field(
    lambda: Campaigns,
    domain=graphene.Argument(GCURL, required=True, description=""),
    resolver=resolve_spoofing_campaigns,
    description="",
)
