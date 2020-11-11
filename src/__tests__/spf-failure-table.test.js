require('dotenv-safe').config({
  allowEmptyValues: true,
})

const { GraphQLSchema, graphql } = require('graphql')
const { query } = require('../queries')

const { cosmosReturn } = require('../__mocks__/spf-fail')

const moment = require('moment')
const { cleanseInput } = require('../validators')
const { loadSpfFailConnection } = require('../loaders')

describe('given spfFailTableObject', () => {
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
    it('returns top senders that are failing spf', async () => {
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
                spfFailure(first: 1) {
                  pageInfo {
                    startCursor
                    endCursor
                    hasNextPage
                    hasPreviousPage
                  }
                  edges {
                    node {
                      id
                      dnsHost
                      envelopeFrom
                      guidance
                      headerFrom
                      sourceIpAddress
                      spfAligned
                      spfDomains
                      spfResults
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
          loadSpfFailConnection: loadSpfFailConnection({
            container,
            cleanseInput,
          }),
        },
      )

      const dnsHost = 'test.dns.canada.ca'
      const envelopeFrom = 'test.gc.ca'
      const guidance = ''
      const headerFrom = 'test.gc.ca'
      const sourceIpAddress = '123.456.78.91'
      const spfAligned = false
      const spfDomains = 'test.gc.ca'
      const spfResults = ''
      const totalMessages = 30

      const expectedReturn = {
        data: {
          dmarcSummaryByPeriod: {
            detailTables: {
              spfFailure: {
                edges: [
                  {
                    node: {
                      id: 'c3BmRmFpbDox',
                      dnsHost,
                      envelopeFrom,
                      guidance,
                      headerFrom,
                      sourceIpAddress,
                      spfAligned,
                      spfDomains,
                      spfResults,
                      totalMessages,
                    },
                  },
                ],
                pageInfo: {
                  startCursor: 'c3BmRmFpbDox',
                  endCursor: 'c3BmRmFpbDox',
                  hasNextPage: true,
                  hasPreviousPage: false,
                },
              },
            },
          },
        },
      }

      expect(response).toEqual(expectedReturn)
    })
  })
})
