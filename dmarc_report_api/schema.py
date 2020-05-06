import graphene

from graphene import relay

from dmarc_report_api.scalars.url_scalar import URL
from dmarc_report_api.queries import DmarcSummaries, resolve_dmarc_summaries


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    dmarc_summary = graphene.Field(
        lambda: DmarcSummaries,
        domain=graphene.Argument(
            URL, description="Domain used to select reports", required=True
        ),
        start_date=graphene.Argument(
            graphene.String,
            description="Set the start date in a date range select.",
            required=False,
        ),
        end_date=graphene.Argument(
            graphene.String,
            description="Set the end date in a date range select.",
            required=False,
        ),
        description="Summarized DMARC aggregate reports",
    )

    def resolve_dmarc_summary(self, info, **kwargs):
        return resolve_dmarc_summaries(self, info, **kwargs)


schema = graphene.Schema(query=Query)
