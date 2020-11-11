const { cosmosReturn } = require('./spf-fail-test-data')
const { noCursor } = require('./spf-fail-no-cursor-return')
const { afterCursor } = require('./spf-fail-after-cursor-return')
const { beforeCursor } = require('./spf-fail-before-cursor-return')
const { noLimit } = require('./spf-fail-no-limit-return')
const { firstLimit } = require('./spf-fail-first-limit-return')
const { lastLimit } = require('./spf-fail-last-limit-return')
const { noLimitReversed } = require('./spf-fail-reversed-no-limit')

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
