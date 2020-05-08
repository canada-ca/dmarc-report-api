expected_summary_period_data = {
    "data": {
        "getDmarcSummaryByPeriod": {
            "startDate": "2020-04-01",
            "endDate": "2020-04-30",
            "topSenders": {
                "fullPass": [],
                "spfFailure": [],
                "spfMisaligned": [
                    {
                        "sourceIpAddress": "12.34.567.891",
                        "spfDomains": "some.spf.domain",
                        "dkimDomains": "",
                        "dkimSelectors": "",
                        "total": 1000
                    }
                ],
                "dkimFailure": [
                    {
                        "sourceIpAddress": "12.34.567.891",
                        "spfDomains": "some.spf.domain",
                        "dkimDomains": "",
                        "dkimSelectors": "",
                        "total": 1000
                    }
                ],
                "dkimMisaligned": [],
                "dmarcFailure": [
                    {
                        "sourceIpAddress": "12.34.567.891",
                        "spfDomains": "some.spf.domain",
                        "dkimDomains": "",
                        "dkimSelectors": "",
                        "total": 1000
                    }
                ]
            },
            "categoryTotals": {
                "spfPassDkimPass": 0,
                "spfFailDkimPass": 0,
                "dmarcFailNone": 1000,
                "forwarded": 0,
                "arcPass": 0,
                "spfPassDkimFail": 0,
                "dmarcFailReject": 0,
                "dmarcFailQuarantine": 0
            }
        }
    }
}
