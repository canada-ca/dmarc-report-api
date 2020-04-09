from graphql import GraphQLError
from graphql.language import ast
from unittest import TestCase

from dmarc_report_api.scalars import EmailAddress


class TestEmailAddressSerialize(TestCase):
    def test_email_address_serialize_valid(self):
        """
        Test to see if a valid email address passes serializer
        """
        test_value = "valid-email@domain.ca"
        assert EmailAddress.serialize(test_value)

    def test_email_address_serialize_not_string(self):
        """
        Test to see if a invalid type passes serializer
        """
        test_value = 1
        with self.assertRaisesRegex(
            GraphQLError,
            'Value is not a valid String : ' + str(test_value)
        ):
            EmailAddress.serialize(test_value)

    def test_email_address_serialize_invalid_email(self):
        """
        Test to see if a invalid email address passes serializer
        """
        test_value = "some string"
        with self.assertRaisesRegex(
            GraphQLError,
            'Value is not a valid email address : ' + str(test_value)
        ):
            EmailAddress.serialize(test_value)


class TestEmailAddressParseValue(TestCase):
    def test_email_address_parse_value_valid(self):
        """
        Test to see if a valid email address passes parse_value
        """
        test_value = "valid-email@domain.ca"
        assert EmailAddress.parse_value(test_value)

    def test_email_address_parse_value_not_string(self):
        """
        Test to see if a invalid type passes parse_value
        """
        test_value = 1
        with self.assertRaisesRegex(
            GraphQLError,
            'Value is not a valid String : ' + str(test_value)
        ):
            EmailAddress.parse_value(test_value)

    def test_email_address_parse_value_invalid_email(self):
        """
        Test to see if a invalid email address passes parse_value
        """
        test_value = "some string"
        with self.assertRaisesRegex(
            GraphQLError,
            'Value is not a valid email address : ' + str(test_value)
        ):
            EmailAddress.parse_value(test_value)


class TestEmailAddressParseLiteral(TestCase):
    def test_email_address_parse_literal_valid(self):
        """
        Test to see if a valid email address passes parse literal
        """
        test_value = ast.StringValue(
            value='test-email@domain.ca'
        )
        assert EmailAddress.parse_literal(test_value)

    def test_email_address_parse_literal_not_string(self):
        """
        Test to see if a invalid type email address fails parse literal
        """
        test_value = '4345'
        test_ast = ast.IntValue(
            value=test_value
        )
        with self.assertRaisesRegex(
            GraphQLError,
            '''Can only validate strings as email address's but got a : {value}'''.format(value=type(test_ast))
        ):
            EmailAddress.parse_literal(test_ast)

    def test_email_address_parse_literal_not_valid_url(self):
        """
        Test to see if a invalid email address fails parse literal
        """
        test_value = 'test string'
        test_ast = ast.StringValue(
            value=test_value
        )
        with self.assertRaisesRegex(
            GraphQLError,
            '''Value is not a valid email address : {test_value}'''.format(test_value=test_value)
        ):
            EmailAddress.parse_literal(test_ast)
