const { nodeDefinitions } = require('graphql-relay')

const { nodeField, nodeInterface } = nodeDefinitions()

module.exports = {
  nodeField,
  nodeInterface,
}
