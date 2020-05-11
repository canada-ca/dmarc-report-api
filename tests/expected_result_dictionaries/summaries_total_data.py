expected_results = {
    "data": {
        "getTotalDmarcSummaries": {
            "id": "test.domain.ca",
            "periods": [
                {
                    "startDate": "2020-04-11",
                    "endDate": "2020-05-11",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2020-05-01",
                    "endDate": "2020-05-31",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
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
                                "total": 1000
                            }
                        ],
                        "dkimFailure": [
                            {
                                "sourceIpAddress": "12.34.567.891",
                                "spfDomains": "test.email.domain.ca",
                                "dkimDomains": "",
                                "dkimSelectors": "",
                                "total": 1000
                            }
                        ],
                        "dkimMisaligned": [],
                        "dmarcFailure": [
                            {
                                "sourceIpAddress": "12.34.567.891",
                                "spfDomains": "test.email.domain.ca",
                                "dkimDomains": "",
                                "dkimSelectors": "",
                                "total": 1000
                            }
                        ]
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 1000,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2020-03-01",
                    "endDate": "2020-03-31",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2020-02-01",
                    "endDate": "2020-02-29",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2020-01-01",
                    "endDate": "2020-01-31",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2019-12-01",
                    "endDate": "2019-12-31",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2019-11-01",
                    "endDate": "2019-11-30",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2019-10-01",
                    "endDate": "2019-10-31",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2019-09-01",
                    "endDate": "2019-09-30",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2019-08-01",
                    "endDate": "2019-08-31",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2019-07-01",
                    "endDate": "2019-07-31",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2019-06-01",
                    "endDate": "2019-06-30",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                },
                {
                    "startDate": "2019-05-01",
                    "endDate": "2019-05-31",
                    "topSenders": {
                        "fullPass": [],
                        "spfFailure": [],
                        "spfMisaligned": [],
                        "dkimFailure": [],
                        "dkimMisaligned": [],
                        "dmarcFailure": []
                    },
                    "categoryTotals": {
                        "dmarcFailNone": 0,
                        "dmarcFailQuarantine": 0,
                        "dmarcFailReject": 0,
                        "spfFailDkimPass": 0,
                        "spfPassDkimFail": 0,
                        "spfPassDkimPass": 0
                    }
                }
            ]
        }
    }
}
