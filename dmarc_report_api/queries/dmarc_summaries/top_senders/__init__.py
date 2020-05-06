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

    """

    full_pass = graphene.List(lambda: FullPass, description="")
    spf_failure = graphene.List(lambda: SPFFailure, description="")
    spf_misaligned = graphene.List(lambda: SPFMisaligned, description="")
    dkim_failure = graphene.List(lambda: DKIMFailure, description="")
    dkim_misaligned = graphene.List(lambda: DKIMMisaligned, description="")
    dmarc_failure = graphene.List(lambda: DMARCFailure, description="")
