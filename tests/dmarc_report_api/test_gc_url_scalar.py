import pytest

import pytest
from graphql.language import ast
from graphql import GraphQLError
from dmarc_report_api.scalars import GCURL


def test_valid_url_serialize_gc():
    test_email = "test-domain.gc.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_gc():
    test_email = "test-domain.gc.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_gc():
    assert GCURL.parse_literal(ast.StringValue(value="test-domain.gc.ca"))


def test_valid_url_serialize_canada():
    test_email = "test-domain.canada.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_canada():
    test_email = "test-domain.canada.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_canada():
    assert GCURL.parse_literal(ast.StringValue(value="test-domain.canada.ca"))


def test_valid_url_serialize_tbs_sct():
    test_email = "tbs-sct.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_tbs_sct():
    test_email = "tbs-sct.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_tbs_sct():
    assert GCURL.parse_literal(ast.StringValue(value="tbs-sct.ca"))


def test_valid_url_serialize_goc_gdc():
    test_email = "goc-gdc.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_goc_gdc():
    test_email = "goc-gdc.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_goc_gdc():
    assert GCURL.parse_literal(ast.StringValue(value="goc-gdc.ca"))


def test_valid_url_serialize_gc_collaboration():
    test_email = "gccollaboration.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_gc_collaboration():
    test_email = "gccollaboration.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_gc_collaboration():
    assert GCURL.parse_literal(ast.StringValue(value="gccollaboration.ca"))


def test_valid_url_serialize_gc_collab():
    test_email = "gccollab.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_gc_collab():
    test_email = "gccollab.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_gc_collab():
    assert GCURL.parse_literal(ast.StringValue(value="gccollab.ca"))


def test_valid_url_serialize_just_canada_ca():
    test_email = "canada.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_just_canada_ca():
    test_email = "canada.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_just_canada_ca():
    assert GCURL.parse_literal(ast.StringValue(value="canada.ca"))


def test_valid_url_serialize_tbs_sct_with_subdomain():
    test_email = "test.tbs-sct.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_tbs_sct_with_subdomain():
    test_email = "test.tbs-sct.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_tbs_sct_with_subdomain():
    assert GCURL.parse_literal(ast.StringValue(value="test.tbs-sct.ca"))


def test_valid_url_serialize_goc_gdc_with_subdomain():
    test_email = "test.goc-gdc.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_goc_gdc_with_subdomain():
    test_email = "test.goc-gdc.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_goc_gdc_with_subdomain():
    assert GCURL.parse_literal(ast.StringValue(value="test.goc-gdc.ca"))


def test_valid_url_serialize_gc_collaboration_with_subdomain():
    test_email = "test.gccollaboration.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_gc_collaboration_with_subdomain():
    test_email = "test.gccollaboration.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_gc_collaboration_with_subdomain():
    assert GCURL.parse_literal(ast.StringValue(value="test.gccollaboration.ca"))


def test_valid_url_serialize_gc_collab_with_subdomain():
    test_email = "test.gccollab.ca"
    assert GCURL.serialize(test_email)


def test_valid_url_parse_value_gc_collab_with_subdomain():
    test_email = "test.gccollab.ca"
    assert GCURL.parse_value(test_email)


def test_valid_url_parse_literal_gc_collab_with_subdomain():
    assert GCURL.parse_literal(ast.StringValue(value="test.gccollab.ca"))\


def test_invalid_url_serialize_not_url():
    test_value = "This Will Fail"
    with pytest.raises(GraphQLError, match="Value is not a valid GC URL : This Will Fail"):
        GCURL.serialize(test_value)


def test_invalid_url_serialize_wrong_type():
    test_value = 1234
    with pytest.raises(GraphQLError, match="Value is not a valid String : 1234"):
        GCURL.serialize(test_value)


def test_invalid_url_parse_value_not_url():
    test_value = "This Will Fail"
    with pytest.raises(GraphQLError, match="Value is not a valid GC URL : This Will Fail"):
        GCURL.parse_value(test_value)


def test_invalid_url_parse_value_wrong_type():
    test_value = 1234
    with pytest.raises(GraphQLError, match="Value is not a valid String : 1234"):
        GCURL.parse_value(test_value)


def test_invalid_url_parse_literal_not_url():
    test_value = ast.StringValue(value="This Will Fail")
    with pytest.raises(GraphQLError, match="Value is not a valid GC URL : This Will Fail"):
        GCURL.parse_literal(test_value)


def test_invalid_url_parse_literal_wrong_ast_type():
    test_value = ast.IntValue(value="1234")
    with pytest.raises(
        GraphQLError, match=("Can only validate strings as GC URL's but got a : " + str(type(test_value)))
    ):
        GCURL.parse_literal(test_value)
