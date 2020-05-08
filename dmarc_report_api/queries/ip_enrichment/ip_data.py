import graphene


class IPData(graphene.ObjectType):
    """

    """
    country = graphene.String(
        description=""
    )
    country_code = graphene.String(
        description=""
    )
    isp = graphene.String(
        description=""
    )
    org = graphene.String(
        description=""
    )
    as_name = graphene.String(
        description=""
    )
    as_num = graphene.String(
        description=""
    )
    as_org = graphene.String(
        description=""
    )
    dns_host = graphene.String(
        description=""
    )
    dns_domain = graphene.String(
        description=""
    )

    def resolve_country_code(self, info):
        return self.get('countryCode', None)
