import graphene


class CategoryTotals(graphene.ObjectType):
    """
    This object displays the total amount of messages that fit into each category
    """

    partial_pass = graphene.Int(
        description="Amount of messages that are passing either SPF or DKIM, but failing one."
    )
    full_pass = graphene.Int(
        description="Amount of messages that have are passing SPF and DKIM."
    )
    fail = graphene.Int(description="Amount of messages that fail both SPF and DKIM.")

    def resolve_partial_pass(self: dict, info):
        return self.get("partial-pass", None)

    def resolve_full_pass(self: dict, info):
        return self.get("pass", None)

    def resolve_fail(self: dict, info):
        return self.get("fail", None)
