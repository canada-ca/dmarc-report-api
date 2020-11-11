const { GraphQLNonNull } = require('graphql')

const { MonthEnums } = require('../enums')
const { Domain, Year } = require('../scalars')
const { periodType } = require('../types')

const dmarcSummaryByPeriod = {
  description: 'Summarized DMARC aggregate reports.',
  args: {
    month: {
      type: GraphQLNonNull(MonthEnums),
      description: 'The month in which the returned data is relevant to.',
    },
    year: {
      type: GraphQLNonNull(Year),
      description: 'The year in which the returned data is relevant to.',
    },
    domain: {
      type: GraphQLNonNull(Domain),
      description: 'Gather reports related to this domain.',
    },
  },
  type: periodType,
  resolve: async (_, args, { checkToken, cleanseInput, moment }) => {
    checkToken()

    const month = cleanseInput(args.month)
    const year = cleanseInput(args.year)
    const domain = cleanseInput(args.domain)

    if (month !== 'last30days') {
      const convertMonthNameToNumber = {
        january: '01',
        february: '02',
        march: '03',
        april: '04',
        may: '05',
        june: '06',
        july: '07',
        august: '08',
        september: '09',
        october: '10',
        november: '11',
        december: '12',
      }

      const startDate = moment(
        `${year}-${convertMonthNameToNumber[month]}-01`,
      ).startOf('month')
      const endDate = moment(
        `${year}-${convertMonthNameToNumber[month]}-01`,
      ).endOf('month')

      // Get last current years dates and last years to make sure they are in range
      const currentStartOfMonth = moment().startOf('month')
      const lastYearStartOfMonth = moment().subtract(1, 'year').startOf('month')
      const currentEndOfMonth = moment().endOf('month')
      const lastYearEndOfMonth = moment().subtract(1, 'year').endOf('month')

      if (
        !startDate.isBetween(
          lastYearStartOfMonth,
          currentStartOfMonth,
          undefined,
          '[]',
        ) &&
        !endDate.isBetween(
          lastYearEndOfMonth,
          currentEndOfMonth,
          undefined,
          '[]',
        )
      ) {
        console.warn(
          `Date range is not valid, must be within one year of current date, startDate: ${startDate.format(
            'YYYY-MM-DD',
          )} endDate: ${endDate.format('YYYY-MM-DD')}`,
        )
        throw new Error(
          'Unable to have dates not within a one year period with this time last year.',
        )
      }

      return {
        startDate: startDate.format('YYYY-MM-DD'),
        endDate: endDate.format('YYYY-MM-DD'),
        domain,
        thirtyDays: false,
      }
    } else {
      const startDate = moment().subtract(30, 'days')
      const endDate = moment()

      if (year !== String(startDate.year())) {
        console.warn(
          `Can only have current year set with last 30 days, current year: ${startDate.year()}, submitted year: ${year}`,
        )
        throw new Error(
          'Unable to have year set to any other, other than current year.',
        )
      }

      return {
        startDate: startDate.format('YYYY-MM-DD'),
        endDate: endDate.format('YYYY-MM-DD'),
        domain,
        thirtyDays: true,
      }
    }
  },
}

module.exports = {
  dmarcSummaryByPeriod,
}
