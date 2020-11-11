require('dotenv-safe').config({
  allowEmptyValues: true,
})

const { GraphQLSchema, graphql } = require('graphql')
const { query } = require('../queries')

const { cleanseInput } = require('../validators')
const moment = require('moment')
const { loadDates } = require('../loaders')

describe('given dmarcSummaryByPeriod', () => {
  let schema
  const consoleOutput = []
  const mockedWarn = (output) => consoleOutput.push(output)

  beforeAll(async () => {
    // Create GQL schema
    schema = new GraphQLSchema({
      query,
    })
    console.warn = mockedWarn
  })

  beforeEach(() => {
    consoleOutput.length = 0
  })

  describe('if month is not set to thirty days', () => {
    it('returns dmarc report data for a given period', async () => {
      const mockedMoment = jest
        .fn()
        .mockReturnValueOnce({
          startOf() {
            return {
              subtract() {
                return {
                  format() {
                    return '2019-01-01'
                  },
                }
              },
            }
          },
        })
        .mockReturnValueOnce({
          startOf() {
            return {
              format() {
                return '2020-01-01'
              },
            }
          },
        })

      const response = await graphql(
        schema,
        `
          query {
            yearlyDmarcSummaries(domain: "test.domain.ca") {
              startDate
              endDate
            }
          }
        `,
        null,
        {
          cleanseInput,
          moment: mockedMoment,
          loadDates: loadDates({ moment }),
        },
      )

      const expectedResponse = {
        data: {
          yearlyDmarcSummaries: [
            {
              startDate: '2019-01-01',
              endDate: '2019-01-31',
            },
            {
              startDate: '2019-02-01',
              endDate: '2019-02-28',
            },
            {
              startDate: '2019-03-01',
              endDate: '2019-03-31',
            },
            {
              startDate: '2019-04-01',
              endDate: '2019-04-30',
            },
            {
              startDate: '2019-05-01',
              endDate: '2019-05-31',
            },
            {
              startDate: '2019-06-01',
              endDate: '2019-06-30',
            },
            {
              startDate: '2019-07-01',
              endDate: '2019-07-31',
            },
            {
              startDate: '2019-08-01',
              endDate: '2019-08-31',
            },
            {
              startDate: '2019-09-01',
              endDate: '2019-09-30',
            },
            {
              startDate: '2019-10-01',
              endDate: '2019-10-31',
            },
            {
              startDate: '2019-11-01',
              endDate: '2019-11-30',
            },
            {
              startDate: '2019-12-01',
              endDate: '2019-12-31',
            },
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
          ],
        },
      }
      expect(response).toEqual(expectedResponse)
    })
  })
})
