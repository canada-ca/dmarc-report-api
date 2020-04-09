import graphene

from graphene import relay

from dmarc_report_api.queries import ReportQuery, resolve_report_query
from dmarc_report_api.scalars.url_scalar import URL


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    dmarc_report = graphene.List(
        lambda: ReportQuery,
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

    def resolve_dmarc_report(self, info, **kwargs):
        return resolve_report_query(self, info, **kwargs)


schema = graphene.Schema(query=Query)
