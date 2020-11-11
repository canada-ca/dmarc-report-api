const { cosmosReturn } = require('./dmarc-fail-test-data')
const { noCursor } = require('./dmarc-fail-no-cursor-return')
const { afterCursor } = require('./dmarc-fail-after-cursor-return')
const { beforeCursor } = require('./dmarc-fail-before-cursor-return')
const { noLimit } = require('./dmarc-fail-no-limit-return')
const { firstLimit } = require('./dmarc-fail-first-limit-return')
const { lastLimit } = require('./dmarc-fail-last-limit-return')
const { noLimitReversed } = require('./dmarc-fail-reversed-no-limit')

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
