const { GraphQLSchema, graphql } = require('graphql')
const { query } = require('../queries')

const { cosmosReturn } = require('../__mocks__/full-pass')

const moment = require('moment')
const { cleanseInput } = require('../validators')
const { loadFullPassConnection } = require('../loaders')

describe('given fullPassTableObject', () => {
  let schema, cosmosMockedReturn, checkToken

  beforeAll(async () => {
    // Create GQL schema
    schema = new GraphQLSchema({
      query,
    })
    checkToken = jest.fn()
  })

  beforeEach(async () => {
    cosmosMockedReturn = cosmosReturn()
  })

  describe('all fields can be queried', () => {
    it('returns top senders that are passing all checks', async () => {
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
                fullPass(first: 1) {
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
          loadFullPassConnection: loadFullPassConnection({
            container,
            cleanseInput,
          }),
          checkToken,
        },
      )

      const expectedReturn = {
        data: {
          dmarcSummaryByPeriod: {
            detailTables: {
              fullPass: {
                edges: [
                  {
                    node: {
                      id: 'ZnVsbFBhc3M6MQ==',
                      dkimDomains: 'test.gc.ca',
                      dkimSelectors: 'selector1',
                      dnsHost: 'test.canada.ca',
                      envelopeFrom: 'test.gc.ca',
                      headerFrom: 'test.gc.ca',
                      sourceIpAddress: '123.456.78.91',
                      spfDomains: 'test.gc.ca',
                      totalMessages: 50,
                    },
                  },
                ],
                pageInfo: {
                  startCursor: 'ZnVsbFBhc3M6MQ==',
                  endCursor: 'ZnVsbFBhc3M6MQ==',
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
