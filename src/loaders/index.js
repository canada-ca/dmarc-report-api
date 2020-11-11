const { loadCategoryTotals } = require('./load-category-totals')
const { loadDates } = require('./load-dates')
const { loadDkimFailConnection } = require('./load-dkim-fail-connection')
const { loadDmarcFailConnection } = require('./load-dmarc-fail-connection')
const { loadFullPassConnection } = require('./load-full-pass-connection')
const { loadSpfFailConnection } = require('./load-spf-fail-connection')

module.exports = {
  loadCategoryTotals,
  loadDates,
  loadDkimFailConnection,
  loadDmarcFailConnection,
  loadFullPassConnection,
  loadSpfFailConnection,
}
