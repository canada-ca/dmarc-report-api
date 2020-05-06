import graphene

from dmarc_report_api.queries.dmarc_summaries.top_senders.full_pass import FullPass
from dmarc_report_api.queries.dmarc_summaries.top_senders.dkim_misaligned import (
    DKIMMisaligned,
)
from dmarc_report_api.queries.dmarc_summaries.top_senders.dkim_failure import (
    DKIMFailure,
)
from dmarc_report_api.queries.dmarc_summaries.top_senders.dmarc_failure import (
    DMARCFailure,
)
from dmarc_report_api.queries.dmarc_summaries.top_senders.spf_failure import SPFFailure
from dmarc_report_api.queries.dmarc_summaries.top_senders.spf_misaligned import (
    SPFMisaligned,
)


class TopSenders(graphene.ObjectType):
    """
    Object that contains the top senders for each category
    """

    full_pass = graphene.List(
        lambda: FullPass, description="List of top senders that have full pass"
    )
    spf_failure = graphene.List(
        lambda: SPFFailure, description="List of top senders that have an spf failure"
    )
    spf_misaligned = graphene.List(
        lambda: SPFMisaligned,
        description="List of top senders that have spf misaligned",
    )
    dkim_failure = graphene.List(
        lambda: DKIMFailure, description="List of top senders that have an dkim failure"
    )
    dkim_misaligned = graphene.List(
        lambda: DKIMMisaligned,
        description="List of top senders that have dkim misaligned",
    )
    dmarc_failure = graphene.List(
        lambda: DMARCFailure,
        description="List of top senders that have an dmarc failure",
    )
