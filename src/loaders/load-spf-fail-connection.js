const { fromGlobalId, toGlobalId } = require('graphql-relay')

const loadSpfFailConnection = ({ container, cleanseInput }) => async ({
  startDate,
  endDate,
  domain,
  thirtyDays,
  first,
  last,
  before,
  after,
}) => {
  let spfFailData

  if (typeof first !== 'undefined' && typeof last !== 'undefined') {
    // Throw error if both are set
    console.warn(
      'First and last arguments set when trying to retrieve spf fail senders.',
    )
    throw new Error(
      'Unable to have first and last arguments set, when querying for spf fail senders.',
    )
  } else if (typeof first === 'undefined' && typeof last === 'undefined') {
    // Throw error if none are set
    console.warn(
      'First and last arguments were not set when trying to retrieve spf fail senders.',
    )
    throw new Error(
      'Unable to have first and last arguments not set, when querying for spf fail senders.',
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
              f.spf_results AS spfResults,
              f.spf_aligned AS spfAligned,
              f.total_messages AS totalMessages,
              f.cursor AS id,
              f.dns_host AS dnsHost,
              f.guidance
            FROM c JOIN l IN c.periods JOIN f IN l.detail_tables.spf_failure
            WHERE c.id=@domain
            AND l.thirty_days = @thirtyDays) AS sub`,
          parameters: [
            { name: '@domain', value: domain },
            { name: '@thirtyDays', value: thirtyDays },
          ],
        })
        .fetchAll()
      spfFailData = resources
    } catch (err) {
      console.error(
        `Cosmos error occurred while loading spf fail senders for ${domain}, error: ${err}`,
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
              f.spf_results AS spfResults,
              f.spf_aligned AS spfAligned,
              f.total_messages AS totalMessages,
              f.cursor AS id,
              f.dns_host AS dnsHost,
              f.guidance
            FROM c JOIN l IN c.periods JOIN f IN l.detail_tables.spf_failure
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
      spfFailData = resources
    } catch (err) {
      console.error(
        `Cosmos error occurred while loading spf fail senders for ${domain}, error: ${err}`,
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
    spfFailData.reverse()
  }

  let hasPreviousPageArr = []
  // If after is set remove all items before and including the after index
  if (typeof after !== 'undefined') {
    const { id: afterId } = fromGlobalId(cleanseInput(after))
    hasPreviousPageArr = spfFailData.filter((value) => value.id <= afterId)
    spfFailData = spfFailData.filter((value) => value.id > afterId)
  }
  // If before is set remove all items after and including the before index
  if (typeof before !== 'undefined') {
    const { id: beforeId } = fromGlobalId(cleanseInput(before))
    hasPreviousPageArr = spfFailData.filter((value) => value.id >= beforeId)
    spfFailData = spfFailData.filter((value) => value.id < beforeId)
  }

  // Can only have first or last set not both
  let removedItems = []
  if (typeof first !== 'undefined' && typeof last === 'undefined') {
    // If the limit is greater then the actual array size then just ignore
    if (first < spfFailData.length) {
      // Get the items after the limit, and then delete them from the array
      removedItems = spfFailData.slice(first, spfFailData.length - 1)
      spfFailData.length = first
    }
  } else {
    // If the limit is greater then the actual array size then just ignore
    if (last < spfFailData.length) {
      // Get the items after the limit, and then delete them from the array
      removedItems = spfFailData.slice(last, spfFailData.length - 1)
      spfFailData.length = last
    }
  }

  spfFailData = spfFailData.filter((value) => value !== '')

  const edges = spfFailData.map((data) => {
    return {
      cursor: toGlobalId('spfFail', data.id),
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

  const startCursor = toGlobalId('spfFail', spfFailData[0].id)
  const endCursor = toGlobalId(
    'spfFail',
    spfFailData[spfFailData.length - 1].id,
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
  loadSpfFailConnection,
}
