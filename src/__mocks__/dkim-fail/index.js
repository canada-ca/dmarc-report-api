const { afterCursor } = require('./dkim-fail-after-cursor-return')
const { beforeCursor } = require('./dkim-fail-before-cursor-return')
const { firstLimit } = require('./dkim-fail-first-limit-return')
const { lastLimit } = require('./dkim-fail-last-limit-return')
const { noCursorTest } = require('./dkim-fail-no-cursor-return')
const { noLimit } = require('./dkim-fail-no-limit-return')
const { cosmosReturn } = require('./dkim-fail-test-data')
const { noLimitReversed } = require('./dkim-fail-reversed-no-limit')

module.exports = {
  afterCursor,
  beforeCursor,
  firstLimit,
  lastLimit,
  noCursorTest,
  noLimit,
  noLimitReversed,
  cosmosReturn,
}
