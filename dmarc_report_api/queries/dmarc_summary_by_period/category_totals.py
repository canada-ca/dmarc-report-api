import graphene


class CategoryTotals(graphene.ObjectType):
    """
    This object displays the total amount of messages that fit into each category
    """
    dmarc_fail_none = graphene.Int(
        description="Amount of messages that"
    )
    dmarc_fail_quarantine = graphene.Int(
        description="Amount of messages that failed DMARC and were quarantined"
    )
    dmarc_fail_reject = graphene.Int(
        description="Amount of messages that failed DMARC and were rejected"
    )
    spf_fail_dkim_pass = graphene.Int(
        description="Amount of messages that failed SPF, but passed DKIM"
    )
    spf_pass_dkim_fail = graphene.Int(
        description="Amount of messages that passed SPF, but failed DKIM"
    )
    spf_pass_dkim_pass = graphene.Int(
        description="Amount of messages that passed SPF and DKIM"
    )

    def resolve_dmarc_fail_none(self: dict, info):
        return self.get("dmarc-fail-none", None)

    def resolve_dmarc_fail_quarantine(self: dict, info):
        return self.get("dmarc-fail-quarantine", None)

    def resolve_dmarc_fail_reject(self: dict, info):
        return self.get("dmarc-fail-reject", None)

    def resolve_spf_fail_dkim_pass(self: dict, info):
        return self.get("spf-fail/dkim-pass", None)

    def resolve_spf_pass_dkim_fail(self: dict, info):
        return self.get("spf-pass/dkim-fail", None)

    def resolve_spf_pass_dkim_pass(self: dict, info):
        return self.get("spf-pass/dkim-pass", None)
