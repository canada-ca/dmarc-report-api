const dotenv = require('dotenv-safe')
dotenv.config()

const { CosmosClient } = require('@azure/cosmos')

const PORT = 4001
const { AZURE_CONN_STRING, DATABASE, SUMMARIES_CONTAINER } = process.env

const { Server } = require('./src/server')

;(async () => {
  const client = new CosmosClient(AZURE_CONN_STRING)
  const { database } = await client.databases.createIfNotExists({
    id: DATABASE,
  })

  const {
    container: summariesContainer,
  } = await database.containers.createIfNotExists({
    id: SUMMARIES_CONTAINER,
  })

  Server({
    client,
    database,
    summariesContainer,
  }).listen(PORT, (err) => {
    if (err) throw err
  })
})()
