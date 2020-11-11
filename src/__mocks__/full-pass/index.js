const { cosmosReturn } = require('./full-pass-test-data')
const { noCursor } = require('./full-pass-no-cursor-return')
const { afterCursor } = require('./full-pass-after-cursor-return')
const { beforeCursor } = require('./full-pass-before-cursor-return')
const { noLimit } = require('./full-pass-no-limit-return')
const { firstLimit } = require('./full-pass-first-limit-return')
const { lastLimit } = require('./full-pass-last-limit-return')
const { noLimitReversed } = require('./full-pass-reversed-no-limit')

module.exports = {
  cosmosReturn,
  noCursor,
  afterCursor,
  beforeCursor,
  noLimit,
  firstLimit,
  lastLimit,
  noLimitReversed,
}
