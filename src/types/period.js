const { GraphQLObjectType, GraphQLString } = require('graphql')

const { categoryTotalsType } = require('./category-totals')
const { detailTablesType } = require('./detail-tables')

const periodType = new GraphQLObjectType({
  name: 'Period',
  description:
    'Object that contains information for each data collection period.',
  fields: () => ({
    startDate: {
      type: GraphQLString,
      description: 'Start date of data collection.',
      resolve: async ({ startDate }) => startDate,
    },
    endDate: {
      type: GraphQLString,
      description: 'End date of data collection.',
      resolve: async ({ endDate }) => endDate,
    },
    categoryTotals: {
      type: categoryTotalsType,
      description: 'Category totals for quick viewing.',
      resolve: async (
        { startDate, endDate, domain, thirtyDays },
        _,
        { loadCategoryTotals },
      ) => {
        const categoryTotals = await loadCategoryTotals({
          startDate,
          endDate,
          domain,
          thirtyDays,
        })
        return categoryTotals
      },
    },
    detailTables: {
      type: detailTablesType,
      description: 'Various senders for each category.',
      resolve: async (source) => {
        return source
      },
    },
  }),
})

module.exports = {
  periodType,
}
