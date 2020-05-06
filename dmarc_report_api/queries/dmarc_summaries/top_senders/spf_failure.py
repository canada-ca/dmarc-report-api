import graphene

from dmarc_report_api.scalars import URL


class SPFFailure(graphene.ObjectType):
    """

    """

    source_ip_address = graphene.String(description="")
    spf_domains = graphene.String(description="")
    dkim_domains = graphene.String(description="")
    dkim_selectors = graphene.String(description="")
    total = graphene.Int(description="")
