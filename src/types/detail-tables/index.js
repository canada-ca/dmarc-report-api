const { GraphQLObjectType } = require('graphql')
const { connectionArgs } = require('graphql-relay')

const { dkimFailureConnection } = require('./dkim-failure-table')
const { dmarcFailureConnection } = require('./dmarc-failure-table')
const { fullPassConnection } = require('./full-pass-table')
const { spfFailureConnection } = require('./spf-failure-table')

const detailTablesType = new GraphQLObjectType({
  name: 'DetailTables',
  description:
    'Object that contains the various senders and details for each category.',
  fields: () => ({
    dkimFailure: {
      description: 'List of senders that are failing DKIM checks.',
      args: connectionArgs,
      type: dkimFailureConnection.connectionType,
      resolve: async (
        { startDate, endDate, domain, thirtyDays },
        { first, last, before, after },
        { loadDkimFailConnection },
      ) => {
        const dkimFailData = await loadDkimFailConnection({
          startDate,
          endDate,
          domain,
          thirtyDays,
          first,
          last,
          before,
          after,
        })
        return dkimFailData
      },
    },
    dmarcFailure: {
      description: 'List of senders that are failing DMARC checks.',
      args: connectionArgs,
      type: dmarcFailureConnection.connectionType,
      resolve: async (
        { startDate, endDate, domain, thirtyDays },
        { first, last, before, after },
        { loadDmarcFailConnection },
      ) => {
        const dmarcFailData = await loadDmarcFailConnection({
          startDate,
          endDate,
          domain,
          thirtyDays,
          first,
          last,
          before,
          after,
        })
        return dmarcFailData
      },
    },
    fullPass: {
      description: 'List of senders that are passing all checks.',
      args: connectionArgs,
      type: fullPassConnection.connectionType,
      resolve: async (
        { startDate, endDate, domain, thirtyDays },
        { first, last, before, after },
        { loadFullPassConnection },
      ) => {
        const fullPassData = await loadFullPassConnection({
          startDate,
          endDate,
          domain,
          thirtyDays,
          first,
          last,
          before,
          after,
        })
        return fullPassData
      },
    },
    spfFailure: {
      description: 'List of senders that are failing SPF checks.',
      args: connectionArgs,
      type: spfFailureConnection.connectionType,
      resolve: async (
        { startDate, endDate, domain, thirtyDays },
        { first, last, before, after },
        { loadSpfFailConnection },
      ) => {
        const spfFailData = await loadSpfFailConnection({
          startDate,
          endDate,
          domain,
          thirtyDays,
          first,
          last,
          before,
          after,
        })
        return spfFailData
      },
    },
  }),
})

module.exports = {
  detailTablesType,
}
