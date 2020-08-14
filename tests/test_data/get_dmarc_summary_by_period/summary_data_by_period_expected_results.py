expected_summary_period_data = {
    "data": {
        "getDmarcSummaryByPeriod": {
            "id": "test.domain.gc.ca",
            "period": {
                "startDate": "2020-04-01",
                "endDate": "2020-04-30",
                "detailTables": {
                    "fullPass": [],
                    "spfFailure": [],
                    "spfMisaligned": [
                        {
                            "sourceIpAddress": "12.34.567.891",
                            "envelopeFrom": "test.email.domain.ca",
                            "spfDomains": "test.email.domain.ca",
                            "dkimDomains": "",
                            "dkimSelectors": "",
                            "totalMessages": 1000,
                            "countryCode": "CA",
                            "ispOrg": "Test ISP",
                            "prefixOrg": "Test ISP",
                            "asName": "TISP",
                            "asNum": 5342,
                            "asOrg": "Some Org",
                            "dnsHost": "dns.host.ca",
                            "dnsDomain": "dns.domain.ca",
                        }
                    ],
                    "dkimFailure": [
                        {
                            "sourceIpAddress": "12.34.567.891",
                            "envelopeFrom": "test.email.domain.ca",
                            "spfDomains": "test.email.domain.ca",
                            "dkimDomains": "",
                            "dkimSelectors": "",
                            "totalMessages": 1000,
                            "countryCode": "CA",
                            "ispOrg": "Test ISP",
                            "prefixOrg": "Test ISP",
                            "asName": "TISP",
                            "asNum": 5342,
                            "asOrg": "Some Org",
                            "dnsHost": "dns.host.ca",
                            "dnsDomain": "dns.domain.ca",
                        }
                    ],
                    "dkimMisaligned": [],
                    "dmarcFailure": [
                        {
                            "sourceIpAddress": "12.34.567.891",
                            "envelopeFrom": "test.email.domain.ca",
                            "spfDomains": "test.email.domain.ca",
                            "dkimDomains": "",
                            "dkimSelectors": "",
                            "totalMessages": 1000,
                            "countryCode": "CA",
                            "ispOrg": "Test ISP",
                            "prefixOrg": "Test ISP",
                            "asName": "TISP",
                            "asNum": 5342,
                            "asOrg": "Some Org",
                            "dnsHost": "dns.host.ca",
                            "dnsDomain": "dns.domain.ca",
                        }
                    ],
                },
                "categoryTotals": {
                    "passDkimOnly": 2000,
                    "passSpfOnly": 1000,
                    "fullPass": 0,
                    "fail": 1000,
                },
            },
        }
    }
}
