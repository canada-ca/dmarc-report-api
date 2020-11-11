require('dotenv-safe').config({
  allowEmptyValues: true,
})

const { GraphQLSchema, graphql } = require('graphql')
const { query } = require('../queries')

const { cosmosReturn } = require('../__mocks__/dkim-fail')

const moment = require('moment')
const { cleanseInput } = require('../validators')
const { loadDkimFailConnection } = require('../loaders')

describe('given dkimFailureTableObject', () => {
  let schema, cosmosMockedReturn

  beforeAll(async () => {
    // Create GQL schema
    schema = new GraphQLSchema({
      query,
    })
  })

  beforeEach(async () => {
    cosmosMockedReturn = cosmosReturn()
  })

  describe('all fields can be queried', () => {
    it('returns top senders failing dkim', async () => {
      const container = {
        items: {
          query() {
            return {
              fetchAll() {
                return {
                  resources: cosmosMockedReturn,
                }
              },
            }
          },
        },
      }

      const response = await graphql(
        schema,
        `
          query {
            dmarcSummaryByPeriod(
              month: SEPTEMBER
              year: "2020"
              domain: "cyber.gc.ca"
            ) {
              detailTables {
                dkimFailure(first: 1) {
                  pageInfo {
                    startCursor
                    endCursor
                    hasNextPage
                    hasPreviousPage
                  }
                  edges {
                    node {
                      id
                      dkimAligned
                      dkimDomains
                      dkimResults
                      dkimSelectors
                      dnsHost
                      envelopeFrom
                      guidance
                      headerFrom
                      sourceIpAddress
                      totalMessages
                    }
                  }
                }
              }
            }
          }
        `,
        null,
        {
          cleanseInput,
          moment,
          loadDkimFailConnection: loadDkimFailConnection({
            container,
            cleanseInput,
          }),
        },
      )

      const expectedResponse = {
        data: {
          dmarcSummaryByPeriod: {
            detailTables: {
              dkimFailure: {
                edges: [
                  {
                    node: {
                      id: 'ZGtpbUZhaWw6MQ==',
                      dkimAligned: false,
                      dkimDomains: '',
                      dkimResults: '',
                      dkimSelectors: '',
                      dnsHost: 'test.dns.gc.ca',
                      envelopeFrom: 'test.domain.canada.ca',
                      guidance: '',
                      headerFrom: 'test.gc.ca',
                      sourceIpAddress: '123.456.78.99',
                      totalMessages: 30,
                    },
                  },
                ],
                pageInfo: {
                  startCursor: 'ZmFpbERraW06MQ==',
                  endCursor: 'ZmFpbERraW06MQ==',
                  hasNextPage: true,
                  hasPreviousPage: false,
                },
              },
            },
          },
        },
      }

      expect(response).toEqual(expectedResponse)
    })
  })
})
