from graphql import GraphQLError
from graphql.language import ast
from unittest import TestCase

from dmarc_report_api.scalars import URL


class TestURLSerialize(TestCase):
    def test_url_serialize_valid(self):
        """
        Test to see if a valid URL passes serializer
        """
        test_value = 'www.domain.ca'
        assert URL.serialize(test_value)

    def test_url_serialize_not_string(self):
        """
        Test to see if a invalid type URL fails serializer
        """
        test_value = 1
        with self.assertRaisesRegex(
            GraphQLError,
            'Value is not a valid String : ' + str(test_value)
        ):
            URL.serialize(test_value)

    def test_url_serialize_not_valid_url(self):
        """
        Test to see if a invalid URL fails serializer
        """
        test_value = 'test string'
        with self.assertRaisesRegex(
            GraphQLError,
            'Value is not a valid URL : ' + str(test_value)
        ):
            URL.serialize(test_value)


class TestURLParseValue(TestCase):
    def test_url_parse_value_valid(self):
        """
        Test to see if a valid URL passes parse value
        """
        test_value = 'www.domain.ca'
        assert URL.parse_value(test_value)

    def test_url_parse_value_not_string(self):
        """
        Test to see if a invalid type URL fails parse value
        """
        test_value = 1
        with self.assertRaisesRegex(
            GraphQLError,
            'Value is not a valid String : ' + str(test_value)
        ):
            URL.parse_value(test_value)

    def test_url_parse_value_not_valid_url(self):
        """
        Test to see if a invalid URL fails parse value
        """
        test_value = 'test string'
        with self.assertRaisesRegex(
            GraphQLError,
            'Value is not a valid URL : ' + str(test_value)
        ):
            URL.parse_value(test_value)


class TestURLParseLiteral(TestCase):
    def test_url_parse_literal_valid(self):
        """
        Test to see if a valid URL passes parse literal
        """
        test_value = ast.StringValue(
            value='www.domain.ca'
        )
        assert URL.parse_literal(test_value)

    def test_url_parse_literal_not_string(self):
        """
        Test to see if a invalid type URL fails parse literal
        """
        test_value = '4345'
        test_ast = ast.IntValue(
            value=test_value
        )
        with self.assertRaisesRegex(
            GraphQLError,
            '''Can only validate strings as URL's but got a : {value}'''.format(value=type(test_ast))
        ):
            URL.parse_literal(test_ast)

    def test_url_parse_literal_not_valid_url(self):
        """
        Test to see if a invalid URL fails parse literal
        """
        test_value = 'test string'
        test_ast = ast.StringValue(
            value=test_value
        )
        with self.assertRaisesRegex(
            GraphQLError,
            '''Value is not a valid URL : {test_value}'''.format(test_value=test_value)
        ):
            URL.parse_literal(test_ast)
