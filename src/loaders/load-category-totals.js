const loadCategoryTotals = ({ container }) => async ({
  startDate,
  endDate,
  domain,
  thirtyDays,
}) => {
  let dataReturned

  if (thirtyDays) {
    try {
      const { resources } = await container.items
        .query({
          query: `SELECT l.category_totals 
              FROM c JOIN l IN c.periods 
              WHERE c.id=@domain 
              AND l.thirty_days = @thirtyDay`,
          parameters: [
            { name: '@domain', value: domain },
            { name: '@thirtyDay', value: thirtyDays },
          ],
        })
        .fetchAll()

      dataReturned = resources
    } catch (err) {
      console.error(
        `Cosmos error occurred while loading category totals for ${domain}, error: ${err}`,
      )

      // If there is an error return 0's
      return {
        passSpfOnly: 0,
        passDkimOnly: 0,
        pass: 0,
        fail: 0,
      }
    }
  } else {
    try {
      const { resources } = await container.items
        .query({
          query: `SELECT l.category_totals 
              FROM c JOIN l IN c.periods 
              WHERE c.id=@domain 
              AND l.start_date >= @startDate
              AND l.end_date <= @endDate
              AND l.thirty_days = @thirtyDay`,
          parameters: [
            { name: '@domain', value: domain },
            { name: '@startDate', value: startDate },
            { name: '@endDate', value: endDate },
            { name: '@thirtyDay', value: thirtyDays },
          ],
        })
        .fetchAll()

      dataReturned = resources
    } catch (err) {
      console.error(
        `Cosmos error occurred while loading category totals for ${domain}, error: ${err}`,
      )

      // If there is an error return 0's
      return {
        passSpfOnly: 0,
        passDkimOnly: 0,
        pass: 0,
        fail: 0,
      }
    }
  }

  // Destruct returned array
  const [categoryTotals] = dataReturned

  // If period cannot be found return 0's
  if (typeof categoryTotals === 'undefined') {
    return {
      passSpfOnly: 0,
      passDkimOnly: 0,
      pass: 0,
      fail: 0,
    }
  }

  // Return actual totals if period is found
  return {
    passSpfOnly: categoryTotals.category_totals['pass-spf-only'],
    passDkimOnly: categoryTotals.category_totals['pass-dkim-only'],
    pass: categoryTotals.category_totals.pass,
    fail: categoryTotals.category_totals.fail,
  }
}

module.exports = {
  loadCategoryTotals,
}
