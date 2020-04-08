from re import compile
from graphene.types import Scalar
from graphql.language import ast
from graphql import GraphQLError

URL_REGEX = r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

URL_REGEX_CHECK = compile(URL_REGEX)


class URL(Scalar):
    """
    A field whose value conforms to the standard URL format as specified in RFC3986:
    https://www.ietf.org/rfc/rfc3986.txt.
    """

    @staticmethod
    def serialize(value):
        if not isinstance(value, str):
            raise GraphQLError("Value is not a valid String :" + str(value))

        if not URL_REGEX_CHECK.search(value):
            raise GraphQLError("Value is not a valid URL :" + str(value))

        return value

    @staticmethod
    def parse_value(value):
        if not isinstance(value, str):
            raise GraphQLError("Value is not a valid String :" + str(value))

        if not URL_REGEX_CHECK.search(value):
            raise GraphQLError("Value is not a valid URL :" + str(value))

        return value

    @staticmethod
    def parse_literal(node):
        if not isinstance(node, ast.StringValue):
            raise GraphQLError(
                "Can only validate strings as URL's but got a : " + str(ast.Type)
            )

        if not URL_REGEX_CHECK.search(node.value):
            raise GraphQLError("Value is not a valid URL :" + str(node.value))

        return node.value
