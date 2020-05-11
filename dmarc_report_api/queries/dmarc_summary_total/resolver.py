import datetime

from graphql import GraphQLError

from dmarc_report_api.queries.dmarc_summary_total.dmarc_summaries import DmarcSummaries
from dmarc_report_api.data.fetch_dmarc_summaries import fetch_all_summaries_by_domain
from dmarc_report_api.shared_functions import cleanse_input
from dmarc_report_api.auth import require_token


@require_token
def resolve_total_dmarc_summaries(self, info, **kwargs) -> DmarcSummaries:
    """
    This function is used to create a DmarcSummaries object with data gathered
    from an Azure Cosmos Storage DB
    :param self:
    :param info: Request information sent to the sever from a client
    :param kwargs: Field arguments (i.e. url), and user_roles
    :return: DmarcSummaries Object with Data
    """
    domain = cleanse_input(kwargs.get("domain", None))
    start_date = cleanse_input(kwargs.get("start_date", None))
    end_date = cleanse_input(kwargs.get("end_date", None))

    if domain is None:
        raise GraphQLError("Error, domain was not supplied")

    if (start_date is not None and end_date is None) or (
        start_date is None and end_date is not None
    ):
        raise GraphQLError(
            "Error, only one date was supplied need two for date range select"
        )

    if start_date > end_date:
        raise GraphQLError("Error, start date cannot be greater then end date")

    summaries = fetch_all_summaries_by_domain(
        domain=domain, start_date=start_date, end_date=end_date
    )

    if not summaries:
        raise GraphQLError(
            "Error, there is no data for that time period, or domain is incorrect"
        )

    return DmarcSummaries(summaries.get("id"), summaries.get("periods"))
