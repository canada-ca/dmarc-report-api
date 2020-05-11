mock_data = {
    "id": "test.domain.ca",
    "periods": [
        {
            "start_date": "2020-04-11",
            "end_date": "2020-05-11",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2020-05-01",
            "end_date": "2020-05-31",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
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
                        "total": 1000
                    }
                ],
                "dkim_failure": [
                    {
                        "source_ip_address": "12.34.567.891",
                        "spf_domains": "test.email.domain.ca",
                        "dkim_domains": "",
                        "dkim_selectors": "",
                        "total": 1000
                    }
                ],
                "dkim_misaligned": [],
                "dmarc_failure": [
                    {
                        "source_ip_address": "12.34.567.891",
                        "spf_domains": "test.email.domain.ca",
                        "dkim_domains": "",
                        "dkim_selectors": "",
                        "total": 1000
                    }
                ]
            },
            "category_totals": {
                "dmarc-fail-none": 1000,
                "arc-pass": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2020-03-01",
            "end_date": "2020-03-31",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2020-02-01",
            "end_date": "2020-02-29",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2020-01-01",
            "end_date": "2020-01-31",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2019-12-01",
            "end_date": "2019-12-31",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2019-11-01",
            "end_date": "2019-11-30",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2019-10-01",
            "end_date": "2019-10-31",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2019-09-01",
            "end_date": "2019-09-30",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2019-08-01",
            "end_date": "2019-08-31",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2019-07-01",
            "end_date": "2019-07-31",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2019-06-01",
            "end_date": "2019-06-30",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        },
        {
            "start_date": "2019-05-01",
            "end_date": "2019-05-31",
            "top_senders": {
                "full_pass": [],
                "spf_failure": [],
                "spf_misaligned": [],
                "dkim_failure": [],
                "dkim_misaligned": [],
                "dmarc_failure": []
            },
            "category_totals": {
                "arc-pass": 0,
                "dmarc-fail-none": 0,
                "dmarc-fail-quarantine": 0,
                "spf-pass/dkim-fail": 0,
                "forwarded": 0,
                "dmarc-fail-reject": 0,
                "spf-fail/dkim-pass": 0,
                "spf-pass/dkim-pass": 0
            }
        }
    ]
}

