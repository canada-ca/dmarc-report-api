require('dotenv-safe').config({
  allowEmptyValues: true,
})

const { GraphQLSchema, graphql } = require('graphql')
const { query } = require('../queries')

const { cosmosReturn } = require('../__mocks__/dmarc-fail')

const moment = require('moment')
const { cleanseInput } = require('../validators')
const { loadDmarcFailConnection } = require('../loaders')

describe('given dmarcFailureTableObject', () => {
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
    it('returns top senders failing dmarc', async () => {
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
                dmarcFailure(first: 1) {
                  pageInfo {
                    startCursor
                    endCursor
                    hasNextPage
                    hasPreviousPage
                  }
                  edges {
                    node {
                      id
                      dkimDomains
                      dkimSelectors
                      disposition
                      dnsHost
                      envelopeFrom
                      headerFrom
                      sourceIpAddress
                      spfDomains
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
          loadDmarcFailConnection: loadDmarcFailConnection({
            container,
            cleanseInput,
          }),
        },
      )

      const expectedResponse = {
        data: {
          dmarcSummaryByPeriod: {
            detailTables: {
              dmarcFailure: {
                edges: [
                  {
                    node: {
                      id: 'ZG1hcmNGYWlsOjE=',
                      dkimDomains: '',
                      dkimSelectors: '',
                      disposition: 'none',
                      dnsHost: 'test.dns.gc.ca',
                      envelopeFrom: 'test.domain.canada.ca',
                      headerFrom: 'test.domain.canada.ca',
                      sourceIpAddress: '123.456.78.91',
                      spfDomains: 'test.domain.gc.ca',
                      totalMessages: 30,
                    },
                  },
                ],
                pageInfo: {
                  startCursor: 'ZmFpbERtYXJjOjE=',
                  endCursor: 'ZmFpbERtYXJjOjE=',
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
