const bcrypt = require('bcrypt')
const cors = require('cors')
const express = require('express')
const moment = require('moment')
const { GraphQLSchema } = require('graphql')
const { createServer } = require('http')
const { ApolloServer } = require('apollo-server-express')
const depthLimit = require('graphql-depth-limit')
const { createComplexityLimitRule } = require('graphql-validation-complexity')

const { query } = require('./queries')

const { checkToken, verifyToken } = require('./auth')
const { cleanseInput } = require('./validators')
const {
  loadCategoryTotals,
  loadDates,
  loadFullPassConnection,
  loadDkimFailConnection,
  loadDmarcFailConnection,
  loadSpfFailConnection,
} = require('./loaders')

const createValidationRules = (
  maxDepth,
  complexityCost,
  scalarCost,
  objectCost,
  listFactor,
) => {
  return [
    depthLimit(maxDepth),
    createComplexityLimitRule(complexityCost, {
      scalarCost,
      objectCost,
      listFactor,
      formatErrorMessage: (cost) => {
        console.warn(`User attempted a costly request: ${cost}`)
        return `Query error, query is too complex.`
      },
    }),
  ]
}

const Server = (
  maxDepth,
  complexityCost,
  scalarCost,
  objectCost,
  listFactor,
  context = {},
) => {
  const app = express()

  app.use('*', cors())

  app.get('/alive', (_req, res) => {
    res.json({ ok: 'yes' })
  })

  app.get('/ready', (_req, res) => {
    res.json({ ok: 'yes' })
  })

  const server = new ApolloServer({
    schema: new GraphQLSchema({
      query: query,
    }),
    validationRules: createValidationRules(
      maxDepth,
      complexityCost,
      scalarCost,
      objectCost,
      listFactor,
    ),
    context: async ({ req, res }) => {
      const { summariesContainer } = context
      const token = req.headers.authorization || ''

      return {
        checkToken: checkToken(verifyToken, bcrypt, token),
        cleanseInput,
        loadCategoryTotals: loadCategoryTotals({
          container: summariesContainer,
          cleanseInput,
        }),
        loadDates: loadDates({ moment }),
        loadDkimFailConnection: loadDkimFailConnection({
          container: summariesContainer,
          cleanseInput,
        }),
        loadDmarcFailConnection: loadDmarcFailConnection({
          container: summariesContainer,
          cleanseInput,
        }),
        loadFullPassConnection: loadFullPassConnection({
          container: summariesContainer,
          cleanseInput,
        }),
        loadSpfFailConnection: loadSpfFailConnection({
          container: summariesContainer,
          cleanseInput,
        }),
        moment,
        req,
        res,
        ...context,
      }
    },
    introspection: true,
  })

  server.applyMiddleware({ app })
  const httpServer = createServer(app)

  console.info(`🚀 Server ready at http://localhost:4001${server.graphqlPath}`)
  return httpServer
}

module.exports = {
  Server,
}
