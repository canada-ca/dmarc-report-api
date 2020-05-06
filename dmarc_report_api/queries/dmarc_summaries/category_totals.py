import graphene


class CategoryTotals(graphene.ObjectType):
    """

    """

    spf_pass_dkim_pass = graphene.Int(description="")
    spf_fail_dkim_pass = graphene.Int(description="")
    dmarc_fail_none = graphene.Int(description="")
    forwarded = graphene.Int(description="")
    arc_pass = graphene.Int(description="")
    spf_pass_dkim_fail = graphene.Int(description="")
    dmarc_fail_reject = graphene.Int(description="")
    dmarc_fail_quarantine = graphene.Int(description="")

    def resolve_spf_pass_dkim_pass(self, info):
        return self["spf-pass/dkim-fail"]

    def resolve_spf_fail_dkim_pass(self, info):
        return self["spf-fail/dkim-pass"]

    def resolve_dmarc_fail_none(self, info):
        return self["dmarc-fail-none"]

    def resolve_forwarded(self, info):
        return self["forwarded"]

    def resolve_arc_pass(self, info):
        return self["arc-pass"]

    def resolve_spf_pass_dkim_fail(self, info):
        return self["spf-pass/dkim-fail"]

    def resolve_dmarc_fail_reject(self, info):
        return self["dmarc-fail-reject"]

    def resolve_dmarc_fail_quarantine(self, info):
        return self["dmarc-fail-quarantine"]
