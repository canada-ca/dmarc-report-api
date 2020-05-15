import graphene


class TopSenderStructure(graphene.ObjectType):
    """
    Object that contains the fields of each top sender
    """

    source_ip_address = graphene.String(description="Source IP address")
    spf_domains = graphene.String(description="Domains that are used for SPF")
    dkim_domains = graphene.String(description="Domains that are used for DKIM")
    dkim_selectors = graphene.String(
        description="A string used to to point to a specific DKIM public key "
        "record in the DNS"
    )
    total = graphene.Int(description="Total messages sent by this domain")
