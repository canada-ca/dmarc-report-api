const { fromGlobalId, toGlobalId } = require('graphql-relay')

const loadFullPassConnection = ({ container, cleanseInput }) => async ({
  startDate,
  endDate,
  domain,
  thirtyDays,
  first,
  last,
  before,
  after,
}) => {
  let fullPassData

  try {
    const { resources } = await container.items
      .query({
        query: `SELECT * FROM (
          SELECT 
            f.cursor AS id, 
            f.source_ip_address AS sourceIpAddress,
            f.envelope_from AS envelopeFrom,
            f.header_from AS headerFrom,
            f.spf_domains AS spfDomains,
            f.dkim_domains AS dkimDomains,
            f.dkim_selectors AS dkimSelectors,
            f.total_messages AS totalMessages,
            f.dns_host AS dnsHost
          FROM c JOIN l IN c.periods JOIN f IN l.detail_tables.full_pass
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
    fullPassData = resources
  } catch (err) {
    console.error(
      `Cosmos error occurred while loading full pass senders for ${domain}, error: ${err}`,
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

  // If after is set remove all items before and including the after index
  if (typeof after !== 'undefined') {
    const { id: afterId } = fromGlobalId(cleanseInput(after))
    fullPassData = fullPassData.filter((value) => {
      return value.id > afterId
    })
  }

  // If before is set remove all items after and including the before index
  if (typeof before !== 'undefined') {
    const { id: beforeId } = fromGlobalId(cleanseInput(before))
    fullPassData = fullPassData.filter((value) => {
      return value.id < beforeId
    })
  }

  // Can only have first or last set not both
  let removedItems = []
  if (typeof first !== 'undefined' && typeof last === 'undefined') {
    // If the limit is greater then the actual array size then just ignore
    if (first < fullPassData.length) {
      // Get the items after the limit, and then delete them from the array
      removedItems = fullPassData.slice(0, first)
      fullPassData.length = first
    }
  } else if (typeof first === 'undefined' && typeof last !== 'undefined') {
    // Invert the array
    fullPassData.reverse()

    // If the limit is greater then the actual array size then just ignore
    if (last < fullPassData.length) {
      // Get the items after the limit, and then delete them from the array
      removedItems = fullPassData.slice(0, last)
      fullPassData.length = last
    }
  } else if (typeof first !== 'undefined' && typeof last !== 'undefined') {
    // Throw error if both are set
    console.warn(
      'First and last arguments set when trying to retrieve full pass senders.',
    )
    throw new Error(
      'Unable to have first and last arguments set, when querying for full pass senders.',
    )
  }

  const hasNextPage = typeof first !== 'undefined' && removedItems.length > 0
  const hasPreviousPage = typeof last !== 'undefined' && removedItems.length > 0

  fullPassData = fullPassData.filter((value) => {
    return value !== ''
  })

  const edges = fullPassData.map((data) => {
    return {
      cursor: toGlobalId('fullPass', data.id),
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

  const startCursor = toGlobalId('fullPass', fullPassData[0].id)
  const endCursor = toGlobalId(
    'fullPass',
    fullPassData[fullPassData.length - 1].id,
  )

  return {
    edges,
    pageInfo: {
      hasNextPage,
      hasPreviousPage,
      startCursor,
      endCursor,
    },
  }
}

module.exports = {
  loadFullPassConnection,
}
