import graphene


class CategoryTotals(graphene.ObjectType):
    """
    This object displays the total amount of messages that fit into each category
    """

    spf_pass_dkim_pass = graphene.Int(
        description="Amount of messages that passed SPF and DKIM"
    )
    spf_fail_dkim_pass = graphene.Int(
        description="Amount of messages that failed SPF, but passed DKIM"
    )
    dmarc_fail_none = graphene.Int(description="Amount of messages that ")
    forwarded = graphene.Int(description="Amount of messages forwarded")
    arc_pass = graphene.Int(description="Amount of messages that passed ARC")
    spf_pass_dkim_fail = graphene.Int(
        description="Amount of messages that passed SPF, but failed DKIM"
    )
    dmarc_fail_reject = graphene.Int(
        description="Amount of messages that failed DMARC and were rejected"
    )
    dmarc_fail_quarantine = graphene.Int(
        description="Amount of messages that failed DMARC and were quarantined"
    )

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
