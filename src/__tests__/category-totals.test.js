const { GraphQLSchema, graphql } = require('graphql')
const { query } = require('../queries')

const { cleanseInput } = require('../validators')
const moment = require('moment')
const { loadCategoryTotals } = require('../loaders')

describe('given categoryTotals object', () => {
  let schema, checkToken

  beforeAll(async () => {
    // Create GQL schema
    schema = new GraphQLSchema({
      query,
    })
    checkToken = jest.fn()
  })

  describe('all fields can be queried', () => {
    it('returns category totals', async () => {
      const container = {
        items: {
          query() {
            return {
              fetchAll() {
                const category_totals = {}
                category_totals['pass-spf-only'] = 1
                category_totals['pass-dkim-only'] = 1
                category_totals.pass = 1
                category_totals.fail = 1

                return {
                  resources: [{ category_totals }],
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
              categoryTotals {
                fail
                fullPass
                passDkimOnly
                passSpfOnly
              }
            }
          }
        `,
        null,
        {
          cleanseInput,
          moment,
          checkToken,
          loadCategoryTotals: loadCategoryTotals({ container }),
        },
      )

      const expectedResponse = {
        data: {
          dmarcSummaryByPeriod: {
            categoryTotals: {
              fail: 1,
              fullPass: 1,
              passDkimOnly: 1,
              passSpfOnly: 1,
            },
          },
        },
      }

      expect(response).toEqual(expectedResponse)
    })
  })
})
