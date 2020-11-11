const loadDates = ({ moment }) => ({ startDate, endDate }) => {
  // Check to see if startDate is a string
  if (typeof startDate !== 'string') {
    console.warn(
      `Error: startDate for dateRange must be of type string, instead: startDate: ${typeof startDate}`,
    )
    throw new Error('Start date is not a valid string. Please try again.')
  }

  // Check to see if endDate is a string
  if (typeof endDate !== 'string') {
    console.warn(
      `Error: endDate for dateRange must be of type string, instead: endDate: ${typeof endDate}`,
    )
    throw new Error('End date is not a valid string. Please try again.')
  }

  // Check to see if startDate matches the following regex
  const DATE_REGEX = /\d\d\d\d-\d\d-\d\d/
  if (!DATE_REGEX.test(startDate)) {
    console.warn(
      `Error: startDate for dateRange must conform to format: YYYY-MM-DD, instead: startDate: ${startDate}`,
    )
    throw new Error(
      'Start date is not a valid format, please conform to YYYY-MM-DD. Please try again.',
    )
  }

  if (!DATE_REGEX.test(endDate)) {
    console.warn(
      `Error: endDate for dateRange must conform to format: YYYY-MM-DD, instead: endDate: ${endDate}`,
    )
    throw new Error(
      'End date is not a valid format, please conform to YYYY-MM-DD. Please try again.',
    )
  }

  let start = moment(startDate)
  const end = moment(endDate)

  if (end.isBefore(start)) {
    console.warn(
      `Error: end date is before start date, end date is required to be greater than start date, startDate: ${startDate}, endDate: ${endDate}`,
    )
    throw new Error(
      'End date must be greater than start date. Please try again.',
    )
  }

  const dates = []

  while (end > start || start.format('M') === end.format('M')) {
    dates.push({
      startDate: start.startOf('month').format('YYYY-MM-DD'),
      endDate: start.endOf('month').format('YYYY-MM-DD'),
    })
    start = start.add(1, 'month')
  }

  return dates
}

module.exports = {
  loadDates,
}
