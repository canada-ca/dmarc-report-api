const { TOKEN_HASH } = process.env

const bcrypt = require('bcrypt')
const cors = require('cors')
const express = require('express')
const moment = require('moment')
const { GraphQLSchema } = require('graphql')
const { createServer } = require('http')
const { ApolloServer } = require('apollo-server-express')

const { query } = require('./queries')

const { verifyToken } = require('./auth')
const { cleanseInput } = require('./validators')
const {
  loadCategoryTotals,
  loadDates,
  loadFullPassConnection,
  loadDkimFailConnection,
  loadDmarcFailConnection,
  loadSpfFailConnection,
} = require('./loaders')

const Server = (context = {}) => {
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
    context: async ({ req, res }) => {
      const { summariesContainer } = context
      const token = req.headers.authorization || ''
      if (token !== '') {
        const apiKey = verifyToken({ token }).apiKey
        if (!bcrypt.compareSync(apiKey, TOKEN_HASH)) {
          console.warn(
            'User attempted to access dmarc-report-api with an incorrect auth token.',
          )
          throw new Error('Unable to access dmarc-report-api')
        }
      } else {
        console.warn(
          'User attempted to access dmarc-report-api without auth token.',
        )
        throw new Error('Unable to access dmarc-report-api')
      }

      return {
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
  })

  server.applyMiddleware({ app })
  const httpServer = createServer(app)

  console.info(`🚀 Server ready at http://localhost:4001${server.graphqlPath}`)
  return httpServer
}

module.exports = {
  Server,
}
