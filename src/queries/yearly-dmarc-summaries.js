const { GraphQLNonNull, GraphQLList } = require('graphql')
const { Domain } = require('../scalars')
const { periodType } = require('../types')

const yearlyDmarcSummaries = {
  description: 'Yearly summarized DMARC aggregate reports.',
  args: {
    domain: {
      type: GraphQLNonNull(Domain),
      description: 'Gather yearly reports related to this domain.',
    },
  },
  type: new GraphQLList(periodType),
  resolve: async (_, args, { cleanseInput, loadDates, moment }) => {
    const domain = cleanseInput(args.domain)
    const startDateStr = moment()
      .startOf('month')
      .subtract(1, 'year')
      .format('YYYY-MM-DD')
    const endDateStr = moment().startOf('month').format('YYYY-MM-DD')

    const dates = loadDates({
      startDate: startDateStr,
      endDate: endDateStr,
    })

    const queryData = dates.map((range) => {
      return {
        domain,
        thirtyDays: false,
        ...range,
      }
    })

    return queryData
  },
}

module.exports = {
  yearlyDmarcSummaries,
}
