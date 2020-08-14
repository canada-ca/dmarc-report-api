mock_data = {
    "id": "test.domain.gc.ca",
    "periods": [
        {
            "start_date": "2020-04-01",
            "end_date": "2020-04-30",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [
                    {
                        "source_ip_address": "12.34.567.891",
                        "envelope_from": "test.email.domain.ca",
                        "spf_domains": "test.email.domain.ca",
                        "dkim_domains": "",
                        "dkim_selectors": "",
                        "total_messages": 1000,
                        "country_code": "CA",
                        "isp_org": "Test ISP",
                        "prefix_org": "Test ISP",
                        "as_name": "TISP",
                        "as_num": 5342,
                        "as_org": "Some Org",
                        "dns_host": "dns.host.ca",
                        "dns_domain": "dns.domain.ca",
                    }
                ],
                "dkim_failure": [
                    {
                        "source_ip_address": "12.34.567.891",
                        "envelope_from": "test.email.domain.ca",
                        "spf_domains": "test.email.domain.ca",
                        "dkim_domains": "",
                        "dkim_selectors": "",
                        "total_messages": 1000,
                        "country_code": "CA",
                        "isp_org": "Test ISP",
                        "prefix_org": "Test ISP",
                        "as_name": "TISP",
                        "as_num": 5342,
                        "as_org": "Some Org",
                        "dns_host": "dns.host.ca",
                        "dns_domain": "dns.domain.ca",
                    }
                ],
                "dkim_misaligned": [],
                "dmarc_failure": [
                    {
                        "source_ip_address": "12.34.567.891",
                        "envelope_from": "test.email.domain.ca",
                        "spf_domains": "test.email.domain.ca",
                        "dkim_domains": "",
                        "dkim_selectors": "",
                        "total_messages": 1000,
                        "country_code": "CA",
                        "isp_org": "Test ISP",
                        "prefix_org": "Test ISP",
                        "as_name": "TISP",
                        "as_num": 5342,
                        "as_org": "Some Org",
                        "dns_host": "dns.host.ca",
                        "dns_domain": "dns.domain.ca",
                    }
                ],
            },
            "category_totals": {
                "pass-dkim-only": 2000,
                "pass-spf-only": 1000,
                "pass": 0,
                "fail": 1000,
            },
        }
    ],
}
