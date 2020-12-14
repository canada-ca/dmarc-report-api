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

  if (typeof first !== 'undefined' && typeof last !== 'undefined') {
    // Throw error if both are set
    console.warn(
      'First and last arguments set when trying to retrieve full pass senders.',
    )
    throw new Error(
      'Unable to have first and last arguments set, when querying for full pass senders.',
    )
  } else if (typeof first === 'undefined' && typeof last === 'undefined') {
    // Throw error if none are set
    console.warn(
      'First and last arguments were not set when trying to retrieve full pass senders.',
    )
    throw new Error(
      'Unable to have first and last arguments not set, when querying for full pass senders.',
    )
  }

  if (thirtyDays) {
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
            AND l.thirty_days = @thirtyDays) AS sub`,
          parameters: [
            { name: '@domain', value: domain },
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
  } else {
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
  }

  if (typeof first === 'undefined' && typeof last !== 'undefined') {
    fullPassData.reverse()
  }

  let hasPreviousPageArr = []
  // If after is set remove all items before and including the after index
  if (typeof after !== 'undefined') {
    const { id: afterId } = fromGlobalId(cleanseInput(after))
    hasPreviousPageArr = fullPassData.filter((value) => value.id <= afterId)
    fullPassData = fullPassData.filter((value) => value.id > afterId)
  }
  // If before is set remove all items after and including the before index
  if (typeof before !== 'undefined') {
    const { id: beforeId } = fromGlobalId(cleanseInput(before))
    hasPreviousPageArr = fullPassData.filter((value) => value.id >= beforeId)
    fullPassData = fullPassData.filter((value) => value.id < beforeId)
  }

  // Can only have first or last set not both
  let removedItems = []
  if (typeof first !== 'undefined' && typeof last === 'undefined') {
    // If the limit is greater then the actual array size then just ignore
    if (first < fullPassData.length) {
      // Get the items after the limit, and then delete them from the array
      removedItems = fullPassData.slice(first, fullPassData.length - 1)
      fullPassData.length = first
    }
  } else {
    // If the limit is greater then the actual array size then just ignore
    if (last < fullPassData.length) {
      // Get the items after the limit, and then delete them from the array
      removedItems = fullPassData.slice(last, fullPassData.length - 1)
      fullPassData.length = last
    }
  }

  fullPassData = fullPassData.filter((value) => value !== '')

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
      hasNextPage: removedItems.length > 0,
      hasPreviousPage: hasPreviousPageArr.length > 0,
      startCursor,
      endCursor,
    },
  }
}

module.exports = {
  loadFullPassConnection,
}
