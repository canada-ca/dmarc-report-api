from re import compile
from graphene.types import Scalar
from graphql.language import ast
from graphql import GraphQLError

GC_URL_REGEX = r"([-a-zA-Z0-9@:%._\+~#=]{1,256}\.\b((canada|gc|tbs-sct|goc-gdc|gccollaboration|gccollab)\.\b(ca)|(cdssandbox)\.(xyz))|(canada|tbs-sct|goc-gdc|gccollaboration|gccollab)\.(ca))"

GC_URL_REGEX_CHECK = compile(GC_URL_REGEX)


class GCURL(Scalar):
    """
    A field whose value conforms to the standard URL format as specified in RFC3986:
    https://www.ietf.org/rfc/rfc3986.txt.
    """

    @staticmethod
    def serialize(value):
        if not isinstance(value, str):
            raise GraphQLError("Value is not a valid String : " + str(value))

        if not GC_URL_REGEX_CHECK.search(value):
            raise GraphQLError("Value is not a valid GC URL : " + str(value))

        return value

    @staticmethod
    def parse_value(value):
        if not isinstance(value, str):
            raise GraphQLError("Value is not a valid String : " + str(value))

        if not GC_URL_REGEX_CHECK.search(value):
            raise GraphQLError("Value is not a valid GC URL : " + str(value))

        return value

    @staticmethod
    def parse_literal(node):
        if not isinstance(node, ast.StringValue):
            raise GraphQLError(
                "Can only validate strings as GC URL's but got a : " + str(type(node))
            )

        if not GC_URL_REGEX_CHECK.search(node.value):
            raise GraphQLError("Value is not a valid GC URL : " + str(node.value))

        return node.value
