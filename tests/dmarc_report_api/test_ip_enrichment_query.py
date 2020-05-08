import graphene
import unittest

from graphene.test import Client

from tests.mock_data.mock_ip_enrichment import mock_data
from unittest.mock import patch
from dmarc_report_api.schema import schema


class TestIPEnrichmentQuery(unittest.TestCase):
    @patch('dmarc_report_api.queries.ip_enrichment.ip_enrichment_resolver.fetch_ip_enrichment')
    def test(self, mock_resolver):
        mock_resolver.return_value = mock_data

        client = Client(schema=schema)

        query = '''
        {
            getIpEnrichmentData(
                domain: "test.ca"
            ) {
                sourceIp
                ipData {
                    country
                    countryCode
                    isp
                    org
                    asName
                    asNum
                    asOrg
                    dnsHost
                    dnsDomain
                }
            }
        }
        '''

        executed = client.execute(query)

        expected_result = {
            'data': {
                'getIpEnrichmentData': [
                    {
                        'sourceIp': "12.34.567.891",
                        'ipData': {
                            'country': "Canada",
                            'countryCode': "CA",
                            'isp': "Some Cool ISP",
                            'org': "SCI DATA (canada-east-1)",
                            'asName': "SCI-DATA",
                            'asNum': "123456",
                            'asOrg': "Some Cool, Inc.",
                            'dnsHost': "dns.test.ca",
                            'dnsDomain': "test.ca",
                        }
                    }
                ]
            }
        }

        assert executed == expected_result
