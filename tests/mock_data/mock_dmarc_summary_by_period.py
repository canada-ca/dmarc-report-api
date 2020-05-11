mock_data = {
    "id": "test.domain.ca",
    "periods": [
        {
            "start_date": "2020-04-01",
            "end_date": "2020-04-30",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [
                    {
                        "source_ip_address": "12.34.567.891",
                        "spf_domains": "test.email.domain.ca",
                        "dkim_domains": "",
                        "dkim_selectors": "",
                        "total": 1000,
                    }
                ],
                "dkim_failure": [
                    {
                        "source_ip_address": "12.34.567.891",
                        "spf_domains": "test.email.domain.ca",
                        "dkim_domains": "",
                        "dkim_selectors": "",
                        "total": 1000,
                    }
                ],
                "dkim_misaligned": [],
                "dmarc_failure": [
                    {
                        "source_ip_address": "12.34.567.891",
                        "spf_domains": "test.email.domain.ca",
                        "dkim_domains": "",
                        "dkim_selectors": "",
                        "total": 1000,
                    }
                ],
            },
            "category_totals": {
                "dmarc-fail-none": 1000,
                "arc-pass": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0,
            },
        }
    ],
}
