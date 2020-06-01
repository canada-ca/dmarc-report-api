import datetime

from re import compile
from graphene.types import Scalar
from graphql.language import ast
from graphql import GraphQLError


CUSTOM_DATE_REGEX = r"""\d{4}-\d{2}-\d{2}"""

CUSTOM_DATE_REGEX = compile(CUSTOM_DATE_REGEX)


class CustomDate(Scalar):
    """
    A Field for custom date acceptance
    """

    @staticmethod
    def serialize(value):
        if not isinstance(value, str):
            raise GraphQLError("Value is not a valid String : " + str(value))

        if not CUSTOM_DATE_REGEX.search(value.lower()):
            raise GraphQLError(
                "Value is not a valid Date : " + str(value)
            )

        return value

    @staticmethod
    def parse_value(value):
        if not isinstance(value, str):
            raise GraphQLError("Value is not a valid String : " + str(value))

        if not CUSTOM_DATE_REGEX.search(value.lower()):
            raise GraphQLError(
                "Value is not a valid Date : " + str(value)
            )

        return value

    @staticmethod
    def parse_literal(node):
        if not isinstance(node, ast.StringValue):
            raise GraphQLError(
                "Can only validate strings as date's but got a : "
                + str(type(node))
            )

        if not CUSTOM_DATE_REGEX.search(node.value.lower()):
            raise GraphQLError(
                "Value is not a valid Date : " + str(node.value)
            )

        return node.value
