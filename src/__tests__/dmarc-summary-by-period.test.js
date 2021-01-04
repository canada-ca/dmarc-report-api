const { GraphQLSchema, graphql, GraphQLError } = require('graphql')
const { query } = require('../queries')

const { cleanseInput } = require('../validators')

describe('given dmarcSummaryByPeriod', () => {
  let schema, checkToken
  const consoleOutput = []
  const mockedWarn = (output) => consoleOutput.push(output)

  beforeAll(async () => {
    // Create GQL schema
    schema = new GraphQLSchema({
      query,
    })
    console.warn = mockedWarn
    checkToken = jest.fn()
  })

  beforeEach(() => {
    consoleOutput.length = 0
  })

  describe('if month is not set to thirty days', () => {
    it('returns dmarc report data for a given period', async () => {
      const moment = jest
        .fn()
        .mockReturnValueOnce({
          startOf() {
            return {
              isBetween() {
                return true
              },
              format() {
                return '2020-01-01'
              },
            }
          },
        })
        .mockReturnValueOnce({
          endOf() {
            return {
              format() {
                return '2020-01-31'
              },
              isBetween() {
                return true
              },
            }
          },
        })
        .mockReturnValueOnce({
          startOf() {
            return '2020-01-01'
          },
        })
        .mockReturnValueOnce({
          subtract() {
            return {
              startOf() {
                return '2019-01-01'
              },
            }
          },
        })
        .mockReturnValueOnce({
          endOf() {
            return '2020-01-31'
          },
        })
        .mockReturnValueOnce({
          subtract() {
            return {
              endOf() {
                return '2019-01-31'
              },
            }
          },
        })

      const response = await graphql(
        schema,
        `
          query {
            dmarcSummaryByPeriod(
              month: SEPTEMBER
              year: "2020"
              domain: "test.domain.ca"
            ) {
              startDate
              endDate
            }
          }
        `,
        null,
        {
          cleanseInput,
          moment,
          checkToken,
        },
      )

      const expectedResponse = {
        data: {
          dmarcSummaryByPeriod: {
            startDate: '2020-01-01',
            endDate: '2020-01-31',
          },
        },
      }
      expect(response).toEqual(expectedResponse)
    })
  })
  describe('if month is set to thirty days', () => {
    it('returns the last thirty days period information', async () => {
      const moment = jest
        .fn()
        .mockReturnValueOnce({
          subtract() {
            return {
              format() {
                return '2020-01-01'
              },
              year() {
                return '2020'
              },
            }
          },
        })
        .mockReturnValueOnce({
          format() {
            return '2020-01-30'
          },
        })

      const response = await graphql(
        schema,
        `
          query {
            dmarcSummaryByPeriod(
              month: LAST30DAYS
              year: "2020"
              domain: "test.domain.ca"
            ) {
              startDate
              endDate
            }
          }
        `,
        null,
        {
          cleanseInput,
          moment,
          checkToken,
        },
      )
      const expectedResponse = {
        data: {
          dmarcSummaryByPeriod: {
            startDate: '2020-01-01',
            endDate: '2020-01-30',
          },
        },
      }
      expect(response).toEqual(expectedResponse)
    })
  })
  describe('date range is not currently within one year period', () => {
    describe('thirty days is not set', () => {
      it('throws an error', async () => {
        const moment = jest
          .fn()
          .mockReturnValueOnce({
            startOf() {
              return {
                isBetween() {
                  return false
                },
                format() {
                  return '2018-01-01'
                },
              }
            },
          })
          .mockReturnValueOnce({
            endOf() {
              return {
                format() {
                  return '2018-01-31'
                },
                isBetween() {
                  return false
                },
              }
            },
          })
          .mockReturnValueOnce({
            startOf() {
              return '2018-01-01'
            },
          })
          .mockReturnValueOnce({
            subtract() {
              return {
                startOf() {
                  return '2017-01-01'
                },
              }
            },
          })
          .mockReturnValueOnce({
            endOf() {
              return '2018-01-31'
            },
          })
          .mockReturnValueOnce({
            subtract() {
              return {
                endOf() {
                  return '2017-01-31'
                },
              }
            },
          })

        const response = await graphql(
          schema,
          `
            query {
              dmarcSummaryByPeriod(
                month: SEPTEMBER
                year: "2018"
                domain: "test.domain.ca"
              ) {
                startDate
                endDate
              }
            }
          `,
          null,
          {
            cleanseInput,
            moment,
            checkToken,
          },
        )

        const error = [
          new GraphQLError(
            'Unable to have dates not within a one year period with this time last year.',
          ),
        ]
        expect(response.errors).toEqual(error)
        expect(consoleOutput).toEqual([
          'Date range is not valid, must be within one year of current date, startDate: 2018-01-01 endDate: 2018-01-31',
        ])
      })
    })
    describe('thirty days is set', () => {
      it('throws an error', async () => {
        const moment = jest
          .fn()
          .mockReturnValueOnce({
            subtract() {
              return {
                format() {
                  return '2020-01-01'
                },
                year() {
                  return '2020'
                },
              }
            },
          })
          .mockReturnValueOnce({
            format() {
              return '2020-01-30'
            },
            year() {
              return '2020'
            },
          })

        const response = await graphql(
          schema,
          `
            query {
              dmarcSummaryByPeriod(
                month: LAST30DAYS
                year: "2018"
                domain: "test.domain.ca"
              ) {
                startDate
                endDate
              }
            }
          `,
          null,
          {
            cleanseInput,
            moment,
            checkToken,
          },
        )

        const error = [
          new GraphQLError(
            'Unable to have year set to any other, other than current year.',
          ),
        ]
        expect(response.errors).toEqual(error)
        expect(consoleOutput).toEqual([
          'Can only have current year set with last 30 days, current year startDate year: 2020 or endDate year: 2020, submitted year: 2018',
        ])
      })
    })
  })
})
