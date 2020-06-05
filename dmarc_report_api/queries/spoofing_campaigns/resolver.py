import datetime
from graphql import GraphQLError

from dmarc_report_api.queries.spoofing_campaigns.spoofing_campaigns import (
    Campaigns,
)
from dmarc_report_api.data.fetch_spoofing_campaigns import fetch_campaigns
from dmarc_report_api.shared_functions import cleanse_input
from dmarc_report_api.auth import require_token


@require_token
def resolve_spoofing_campaigns(self, info, **kwargs) -> Campaigns:
    """
    This function is used to create a DmarcSummaryByPeriod object with data
    gathered from an Azure Cosmos Storage DB
    :param self:
    :param info: Request information sent to the sever from a client
    :param kwargs: Field arguments (i.e. url), and user_roles
    :return: DmarcSummaryByPeriod Object with Data
    """
    domain = cleanse_input(kwargs.get("domain", None))

    if domain is None:
        raise GraphQLError("Error, domain was not supplied")

    summary = fetch_campaigns(
        domain=domain
    )

    if not len(summary.get("campaigns")):
        raise GraphQLError(
            "Error, there is no spoofing campaigns for that domain."
        )

    return Campaigns(summary.get("id"), summary["campaigns"])
