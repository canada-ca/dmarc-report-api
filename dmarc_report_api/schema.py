import graphene

from graphene import relay

from dmarc_report_api.scalars.url_scalar import URL
from dmarc_report_api.queries.dmarc_summaries.summary_query import DmarcSummaries
from dmarc_report_api.queries.dmarc_summaries.summary_resolver import resolve_report_query


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    dmarc_summary = graphene.Field(
        lambda: DmarcSummaries,
        domain=graphene.Argument(
            URL,
            description="Domain used to select reports",
            required=True
        ),
        start_date=graphene.Argument(
            graphene.String,
            description="Set the start date in a date range select.",
            required=False
        ),
        end_date=graphene.Argument(
            graphene.String,
            description="Set the end date in a date range select.",
            required=False
        )
    )

    def resolve_dmarc_summary(self, info, **kwargs):
        return resolve_report_query(self, info, **kwargs)

schema = graphene.Schema(query=Query)
