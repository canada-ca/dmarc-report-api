from flask import Flask
from flask_graphql import GraphQLView
from waitress import serve

from dmarc_report_api.backend.security_check import SecurityAnalysisBackend
from dmarc_report_api.schema import schema

app = Flask(__name__)


backend = SecurityAnalysisBackend(max_depth=20, max_cost=1000)


app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, backend=backend, graphiql=True
    ),
)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
