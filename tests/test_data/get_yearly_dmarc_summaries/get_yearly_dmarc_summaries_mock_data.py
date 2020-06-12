mock_data = {
    "id": "test.domain.canada.ca",
    "periods": [
        {
            "start_date": "2020-04-11",
            "end_date": "2020-05-11",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2020-05-01",
            "end_date": "2020-05-31",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
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
            "category_totals": {"partial-pass": 2000, "pass": 0, "fail": 1000},
        },
        {
            "start_date": "2020-03-01",
            "end_date": "2020-03-31",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2020-02-01",
            "end_date": "2020-02-29",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2020-01-01",
            "end_date": "2020-01-31",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2019-12-01",
            "end_date": "2019-12-31",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2019-11-01",
            "end_date": "2019-11-30",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2019-10-01",
            "end_date": "2019-10-31",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2019-09-01",
            "end_date": "2019-09-30",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2019-08-01",
            "end_date": "2019-08-31",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2019-07-01",
            "end_date": "2019-07-31",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2019-06-01",
            "end_date": "2019-06-30",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
        {
            "start_date": "2019-05-01",
            "end_date": "2019-05-31",
            "detail_tables": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": [],
            },
            "category_totals": {"partial-pass": 0, "pass": 0, "fail": 0},
        },
    ],
}
