from re import compile
from graphene.types import Scalar
from graphql.language import ast
from graphql import GraphQLError


EMAIL_ADDRESS_REGEX = r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][
0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

EMAIL_ADDRESS_REGEX = compile(EMAIL_ADDRESS_REGEX)


class EmailAddress(Scalar):
    """
    A field whose value conforms to the standard internet email address format as specified in RFC822:
    https://www.w3.org/Protocols/rfc822/.
    """

    @staticmethod
    def serialize(value):
        if not isinstance(value, str):
            raise GraphQLError("Value is not a valid String :" + str(value))

        if not EMAIL_ADDRESS_REGEX.search(value.lower()):
            raise GraphQLError("Value is not a valid email address :" + str(value.lower()))

        return value.lower()

    @staticmethod
    def parse_value(value):
        if not isinstance(value, str):
            raise GraphQLError("Value is not a valid String :" + str(value))

        if not EMAIL_ADDRESS_REGEX.search(value.lower()):
            raise GraphQLError("Value is not a valid email address :" + str(value.lower()))

        return value.lower()

    @staticmethod
    def parse_literal(node):
        if not isinstance(node, ast.StringValue):
            raise GraphQLError(
                "Can only validate strings as email address's but got a : " + str(type(node))
            )

        if not EMAIL_ADDRESS_REGEX.search(node.value.lower()):
            raise GraphQLError("Value is not a valid email address :" + str(node.value.lower()))

        return node.value.lower()
