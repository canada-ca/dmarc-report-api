expected_summary_period_data = {
    "data": {
        "getDmarcSummaryByPeriod": {
            "id": "test.domain.ca",
            "period": {
                "startDate": "2020-04-01",
                "endDate": "2020-04-30",
                "topSenders": {
                    "fullPass": [],
                    "spfFailure": [],
                    "spfMisaligned": [
                        {
                            "sourceIpAddress": "12.34.567.891",
                            "spfDomains": "test.email.domain.ca",
                            "dkimDomains": "",
                            "dkimSelectors": "",
                            "total": 1000,
                        }
                    ],
                    "dkimFailure": [
                        {
                            "sourceIpAddress": "12.34.567.891",
                            "spfDomains": "test.email.domain.ca",
                            "dkimDomains": "",
                            "dkimSelectors": "",
                            "total": 1000,
                        }
                    ],
                    "dkimMisaligned": [],
                    "dmarcFailure": [
                        {
                            "sourceIpAddress": "12.34.567.891",
                            "spfDomains": "test.email.domain.ca",
                            "dkimDomains": "",
                            "dkimSelectors": "",
                            "total": 1000,
                        }
                    ],
                },
                "categoryTotals": {
                    "dmarcFailNone": 1000,
                    "dmarcFailQuarantine": 0,
                    "dmarcFailReject": 0,
                    "spfFailDkimPass": 0,
                    "spfPassDkimFail": 0,
                    "spfPassDkimPass": 0,
                },
            },
        }
    }
}
