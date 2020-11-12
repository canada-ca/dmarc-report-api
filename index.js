const dotenv = require('dotenv-safe')
dotenv.config()

const { CosmosClient } = require('@azure/cosmos')

const PORT = 4001
const {
  AZURE_CONN_STRING,
  DATABASE,
  SUMMARIES_CONTAINER,
  DEPTH_LIMIT: maxDepth,
  COST_LIMIT: complexityCost,
  SCALAR_COST: scalarCost,
  OBJECT_COST: objectCost,
  LIST_FACTOR: listFactor,
} = process.env

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

  Server(maxDepth, complexityCost, scalarCost, objectCost, listFactor, {
    client,
    database,
    summariesContainer,
  }).listen(PORT, (err) => {
    if (err) throw err
  })
})()
