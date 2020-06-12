import graphene

from dmarc_report_api.queries.spoofing_campaigns.campaign_structure import (
    CampaignStructure,
)


class Campaigns(graphene.ObjectType):
    """

    """

    id = graphene.String(description="")
    campaigns = graphene.List(lambda: graphene.List(CampaignStructure), description="")
