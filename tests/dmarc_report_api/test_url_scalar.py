import pytest
from graphql.language import ast
from graphql import GraphQLError
from dmarc_report_api.scalars import URL


def test_valid_url_serialize():
    test_email = "test-domain.ca"
    assert URL.serialize(test_email)


def test_valid_url_parse_value():
    test_email = "test-domain.ca"
    assert URL.parse_value(test_email)


def test_valid_url_parse_literal():
    assert URL.parse_literal(ast.StringValue(value="test-domain.ca"))


def test_invalid_url_serialize_not_url():
    test_value = "This Will Fail"
    with pytest.raises(GraphQLError, match="Value is not a valid URL : This Will Fail"):
        URL.serialize(test_value)


def test_invalid_url_serialize_wrong_type():
    test_value = 1234
    with pytest.raises(GraphQLError, match="Value is not a valid String : 1234"):
        URL.serialize(test_value)


def test_invalid_url_parse_value_not_url():
    test_value = "This Will Fail"
    with pytest.raises(GraphQLError, match="Value is not a valid URL : This Will Fail"):
        URL.parse_value(test_value)


def test_invalid_url_parse_value_wrong_type():
    test_value = 1234
    with pytest.raises(GraphQLError, match="Value is not a valid String : 1234"):
        URL.parse_value(test_value)


def test_invalid_url_parse_literal_not_url():
    test_value = ast.StringValue(value="This Will Fail")
    with pytest.raises(GraphQLError, match="Value is not a valid URL : This Will Fail"):
        URL.parse_literal(test_value)


def test_invalid_url_parse_literal_wrong_ast_type():
    test_value = ast.IntValue(value="1234")
    with pytest.raises(
        GraphQLError, match=("Can only validate strings as URL's but got a : " + str(type(test_value)))
    ):
        URL.parse_literal(test_value)
