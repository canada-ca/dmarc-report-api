from unittest import TestCase

from dmarc_report_api.shared_functions import cleanse_input


class TestInputValidation(TestCase):
    def test_valid_input(self):
        """
        Test to see if regular text stays the same
        """
        input = "Some Text"
        assert input == cleanse_input(input)

    def test_string_stripping(self):
        """
        Test to see if spaces on either end of the string are removed
        """
        input = "   Some Spaces    "
        assert "Some Spaces" == cleanse_input(input)

    def test_html_escaping(self):
        """
        Test to ensure that special characters are escaped
        """
        input = "<script>This Should Be Escaped</script>"
        assert "&lt;script&gt;This Should Be Escaped&lt;/script&gt;" == cleanse_input(input)
