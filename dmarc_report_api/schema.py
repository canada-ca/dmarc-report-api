import graphene

from graphene import relay

from queries.report_query import ReportQuery
from queries.report_resolver import resolve_report_query
from scalars.url_scalar import URL


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    dmarc_report = graphene.List(
        lambda: ReportQuery,
        domain=graphene.Argument(URL),
        start_date=graphene.Argument(graphene.String),
        end_date=graphene.Argument(graphene.String)
    )

    def resolve_dmarc_report(self, info, **kwargs):
        return resolve_report_query(self, info, **kwargs)


schema = graphene.Schema(query=Query)
