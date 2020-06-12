import graphene


class CampaignStructure(graphene.ObjectType):
    """

    """

    report_end_date = graphene.String(description="")
    header_from = graphene.String(description="")
    envelope_from = graphene.String(description="")
    source_ip_address = graphene.String(description="")
    total_messages = graphene.Int(description="")
    country_code = graphene.String(description="")
    isp_org = graphene.String(description="")
    prefix_org = graphene.String(description="")
    as_name = graphene.String(description="")
    as_num = graphene.Int(description="")
    as_org = graphene.String(description="")
    dns_host = graphene.String(description="")
    dns_domain = graphene.String(description="")
