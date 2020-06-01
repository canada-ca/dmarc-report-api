import pytest
from graphql.language import ast
from graphql import GraphQLError
from dmarc_report_api.scalars import CustomDate


def test_valid_date_serialize():
    test_date = "2020-01-01"
    assert CustomDate.serialize(test_date)


def test_valid_date_parse_value():
    test_date = "2020-01-01"
    assert CustomDate.parse_value(test_date)


def test_valid_date_parse_literal():
    assert CustomDate.parse_literal(ast.StringValue(value="2020-01-01"))


def test_invalid_date_serialize_not_url():
    test_value = "This Will Fail"
    with pytest.raises(
        GraphQLError, match="Value is not a valid Date : This Will Fail"
    ):
        CustomDate.serialize(test_value)


def test_invalid_date_serialize_wrong_type():
    test_value = 1234
    with pytest.raises(GraphQLError, match="Value is not a valid String : 1234"):
        CustomDate.serialize(test_value)


def test_invalid_date_parse_value_not_url():
    test_value = "This Will Fail"
    with pytest.raises(
        GraphQLError, match="Value is not a valid Date : This Will Fail"
    ):
        CustomDate.parse_value(test_value)


def test_invalid_date_parse_value_wrong_type():
    test_value = 1234
    with pytest.raises(GraphQLError, match="Value is not a valid String : 1234"):
        CustomDate.parse_value(test_value)


def test_invalid_date_parse_literal_not_url():
    test_value = ast.StringValue(value="This Will Fail")
    with pytest.raises(
        GraphQLError, match="Value is not a valid Date : This Will Fail"
    ):
        CustomDate.parse_literal(test_value)


def test_invalid_date_parse_literal_wrong_ast_type():
    test_value = ast.IntValue(value="1234")
    with pytest.raises(
        GraphQLError,
        match=(
            "Can only validate strings as date's but got a : " + str(type(test_value))
        ),
    ):
        CustomDate.parse_literal(test_value)
