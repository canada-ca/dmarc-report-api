const { GraphQLObjectType } = require('graphql')
const { nodeField } = require('../types')

const { dmarcSummaryByPeriod } = require('./dmarc-summary-by-period')
const { yearlyDmarcSummaries } = require('./yearly-dmarc-summaries')

module.exports.query = new GraphQLObjectType({
  name: 'Query',
  fields: () => ({
    node: nodeField,
    dmarcSummaryByPeriod,
    yearlyDmarcSummaries,
  }),
  description: 'Base query object.',
})
