import graphene


class CategoryTotals(graphene.ObjectType):
    """
    This object displays the total amount of messages that fit into each category
    """

    pass_spf_only = graphene.Int(
        description="Amount of messages that are passing SPF, but failing DKIM."
    )
    pass_dkim_only = graphene.Int(
        description="Amount of messages that are passing DKIM, but failing SPF."
    )
    full_pass = graphene.Int(
        description="Amount of messages that have are passing SPF and DKIM."
    )
    fail = graphene.Int(description="Amount of messages that fail both SPF and DKIM.")

    def resolve_pass_spf_only(self: dict, info):
        return self.get("pass-spf-only", None)

    def resolve_pass_dkim_only(self: dict, info):
        return self.get("pass-dkim-only", None)

    def resolve_full_pass(self: dict, info):
        return self.get("pass", None)

    def resolve_fail(self: dict, info):
        return self.get("fail", None)
