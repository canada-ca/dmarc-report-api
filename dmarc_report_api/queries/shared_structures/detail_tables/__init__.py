import graphene

from dmarc_report_api.queries.shared_structures.detail_tables.detail_tables import (
    TopSenderStructure,
)


class DetailTables(graphene.ObjectType):
    """
    Object that contains the top senders for each category
    """

    full_pass = graphene.List(
        lambda: TopSenderStructure,
        description="List of top senders that have full pass",
    )
    spf_failure = graphene.List(
        lambda: TopSenderStructure,
        description="List of top senders that have an spf failure",
    )
    spf_misaligned = graphene.List(
        lambda: TopSenderStructure,
        description="List of top senders that have spf misaligned",
    )
    dkim_failure = graphene.List(
        lambda: TopSenderStructure,
        description="List of top senders that have an dkim failure",
    )
    dkim_misaligned = graphene.List(
        lambda: TopSenderStructure,
        description="List of top senders that have dkim misaligned",
    )
    dmarc_failure = graphene.List(
        lambda: TopSenderStructure,
        description="List of top senders that have an dmarc failure",
    )
