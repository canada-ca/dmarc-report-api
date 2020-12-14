const { fromGlobalId, toGlobalId } = require('graphql-relay')

const loadDmarcFailConnection = ({ container, cleanseInput }) => async ({
  startDate,
  endDate,
  domain,
  thirtyDays,
  first,
  last,
  before,
  after,
}) => {
  let failDmarcData

  if (typeof first !== 'undefined' && typeof last !== 'undefined') {
    // Throw error if both are set
    console.warn(
      'First and last arguments set when trying to retrieve dmarc fail senders.',
    )
    throw new Error(
      'Unable to have first and last arguments set, when querying for dmarc fail senders.',
    )
  } else if (typeof first === 'undefined' && typeof last === 'undefined') {
    // Throw error if none are set
    console.warn(
      'First and last arguments were not set when trying to retrieve dmarc fail senders.',
    )
    throw new Error(
      'Unable to have first and last arguments not set, when querying for dmarc fail senders.',
    )
  }

  if (thirtyDays) {
    try {
      const { resources } = await container.items
        .query({
          query: `SELECT * FROM (
            SELECT 
              f.source_ip_address AS sourceIpAddress,
              f.envelope_from AS envelopeFrom,
              f.header_from AS headerFrom,
              f.spf_domains AS spfDomains,
              f.dkim_domains AS dkimDomains,
              f.dkim_selectors AS dkimSelectors,
              f.disposition,
              f.total_messages AS totalMessages,
              f.cursor AS id,
              f.dns_host AS dnsHost
            FROM c JOIN l IN c.periods JOIN f IN l.detail_tables.dmarc_failure
            WHERE c.id=@domain
            AND l.thirty_days = @thirtyDays) AS sub`,
          parameters: [
            { name: '@domain', value: domain },
            { name: '@thirtyDays', value: thirtyDays },
          ],
        })
        .fetchAll()
      failDmarcData = resources
    } catch (err) {
      console.error(
        `Cosmos error occurred while loading fail dmarc senders for ${domain}, error: ${err}`,
      )

      return {
        edges: [],
        pageInfo: {
          hasNextPage: false,
          hasPreviousPage: false,
          startCursor: '',
          endCursor: '',
        },
      }
    }
  } else {
    try {
      const { resources } = await container.items
        .query({
          query: `SELECT * FROM (
            SELECT 
              f.source_ip_address AS sourceIpAddress,
              f.envelope_from AS envelopeFrom,
              f.header_from AS headerFrom,
              f.spf_domains AS spfDomains,
              f.dkim_domains AS dkimDomains,
              f.dkim_selectors AS dkimSelectors,
              f.disposition,
              f.total_messages AS totalMessages,
              f.cursor AS id,
              f.dns_host AS dnsHost
            FROM c JOIN l IN c.periods JOIN f IN l.detail_tables.dmarc_failure
            WHERE c.id=@domain
            AND l.start_date >= @startDate
            AND l.end_date <= @endDate
            AND l.thirty_days = @thirtyDays) AS sub`,
          parameters: [
            { name: '@domain', value: domain },
            { name: '@startDate', value: startDate },
            { name: '@endDate', value: endDate },
            { name: '@thirtyDays', value: thirtyDays },
          ],
        })
        .fetchAll()
      failDmarcData = resources
    } catch (err) {
      console.error(
        `Cosmos error occurred while loading fail dmarc senders for ${domain}, error: ${err}`,
      )

      return {
        edges: [],
        pageInfo: {
          hasNextPage: false,
          hasPreviousPage: false,
          startCursor: '',
          endCursor: '',
        },
      }
    }
  }

  if (typeof first === 'undefined' && typeof last !== 'undefined') {
    failDmarcData.reverse()
  }

  let hasPreviousPageArr = []
  // If after is set remove all items before and including the after index
  if (typeof after !== 'undefined') {
    const { id: afterId } = fromGlobalId(cleanseInput(after))
    hasPreviousPageArr = failDmarcData.filter((value) => value.id <= afterId)
    failDmarcData = failDmarcData.filter((value) => value.id > afterId)
  }
  // If before is set remove all items after and including the before index
  if (typeof before !== 'undefined') {
    const { id: beforeId } = fromGlobalId(cleanseInput(before))
    hasPreviousPageArr = failDmarcData.filter((value) => value.id >= beforeId)
    failDmarcData = failDmarcData.filter((value) => value.id < beforeId)
  }

  // Can only have first or last set not both
  let removedItems = []
  if (typeof first !== 'undefined' && typeof last === 'undefined') {
    // If the limit is greater then the actual array size then just ignore
    if (first < failDmarcData.length) {
      // Get the items after the limit, and then delete them from the array
      removedItems = failDmarcData.slice(first, failDmarcData.length - 1)
      failDmarcData.length = first
    }
  } else {
    // If the limit is greater then the actual array size then just ignore
    if (last < failDmarcData.length) {
      // Get the items after the limit, and then delete them from the array
      removedItems = failDmarcData.slice(last, failDmarcData.length - 1)
      failDmarcData.length = last
    }
  }

  failDmarcData = failDmarcData.filter((value) => value !== '')

  const edges = failDmarcData.map((data) => {
    return {
      cursor: toGlobalId('failDmarc', data.id),
      node: data,
    }
  })

  if (edges.length === 0) {
    return {
      edges: [],
      pageInfo: {
        hasNextPage: false,
        hasPreviousPage: false,
        startCursor: '',
        endCursor: '',
      },
    }
  }

  const startCursor = toGlobalId('failDmarc', failDmarcData[0].id)
  const endCursor = toGlobalId(
    'failDmarc',
    failDmarcData[failDmarcData.length - 1].id,
  )

  return {
    edges,
    pageInfo: {
      hasNextPage: removedItems.length > 0,
      hasPreviousPage: hasPreviousPageArr.length > 0,
      startCursor,
      endCursor,
    },
  }
}

module.exports = {
  loadDmarcFailConnection,
}
