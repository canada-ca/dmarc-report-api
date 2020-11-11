const { loadDkimFailConnection } = require('../loaders')
const { cleanseInput } = require('../validators')

const {
  cosmosReturn,
  noCursorTest,
  afterCursor,
  beforeCursor,
  noLimit,
  noLimitReversed,
  firstLimit,
  lastLimit,
} = require('../__mocks__/dkim-fail')

describe('given the loadDkimFailConnection loader', () => {
  let cosmosMockedReturn
  let consoleOutput = []
  const mockedError = (output) => consoleOutput.push(output)
  const mockedWarn = (output) => consoleOutput.push(output)
  beforeEach(() => {
    console.error = mockedError
    console.warn = mockedWarn
    consoleOutput = []
    cosmosMockedReturn = cosmosReturn()
  })

  describe('given a successful load', () => {
    describe('using no cursor', () => {
      it('returns multiple senders', async () => {
        const container = {
          items: {
            query() {
              return {
                fetchAll() {
                  return {
                    resources: cosmosMockedReturn,
                  }
                },
              }
            },
          },
        }
        const loader = loadDkimFailConnection({ container, cleanseInput })

        const dkimFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          before: undefined,
          after: undefined,
        })

        expect(dkimFailSenders).toEqual(noCursorTest)
      })
    })
    describe('using after cursor', () => {
      it('returns multiple senders after a given id', async () => {
        const container = {
          items: {
            query() {
              return {
                fetchAll() {
                  return {
                    resources: cosmosMockedReturn,
                  }
                },
              }
            },
          },
        }

        const loader = loadDkimFailConnection({ container, cleanseInput })

        const dkimFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          after: 'ZmFpbERraW06IDU=',
        })

        expect(dkimFailSenders).toEqual(afterCursor)
      })
    })
    describe('using before cursor', () => {
      it('returns multiple senders before a given id', async () => {
        const container = {
          items: {
            query() {
              return {
                fetchAll() {
                  return {
                    resources: cosmosMockedReturn,
                  }
                },
              }
            },
          },
        }

        const loader = loadDkimFailConnection({ container, cleanseInput })

        const dkimFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          before: 'ZmFpbERraW06MTU=',
        })

        expect(dkimFailSenders).toEqual(beforeCursor)
      })
    })
    describe('using no limit', () => {
      it('returns multiple senders', async () => {
        const container = {
          items: {
            query() {
              return {
                fetchAll() {
                  return {
                    resources: cosmosMockedReturn,
                  }
                },
              }
            },
          },
        }

        const loader = loadDkimFailConnection({ container, cleanseInput })

        const dkimFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: undefined,
          last: undefined,
        })

        expect(dkimFailSenders).toEqual(noLimit)
      })
    })
    describe('using first limit', () => {
      it('returns the first n amount of items', async () => {
        const container = {
          items: {
            query() {
              return {
                fetchAll() {
                  return {
                    resources: cosmosMockedReturn,
                  }
                },
              }
            },
          },
        }

        const loader = loadDkimFailConnection({ container, cleanseInput })

        const dkimFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: 5,
        })

        expect(dkimFailSenders).toEqual(firstLimit)
      })
    })
    describe('using first limit larger than the cosmos return', () => {
      it('returns all the first amount of items', async () => {
        const container = {
          items: {
            query() {
              return {
                fetchAll() {
                  return {
                    resources: cosmosMockedReturn,
                  }
                },
              }
            },
          },
        }

        const loader = loadDkimFailConnection({ container, cleanseInput })

        const dkimFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: 100,
        })

        expect(dkimFailSenders).toEqual(noLimit)
      })
    })
    describe('using last limit', () => {
      it('returns the last n amount of items', async () => {
        const container = {
          items: {
            query() {
              return {
                fetchAll() {
                  return {
                    resources: cosmosMockedReturn,
                  }
                },
              }
            },
          },
        }

        const loader = loadDkimFailConnection({ container, cleanseInput })

        const dkimFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          last: 5,
          first: undefined,
        })

        expect(dkimFailSenders).toEqual(lastLimit)
      })
    })
    describe('using last limit larger then cosmos mocked return', () => {
      it('returns all the last items of items', async () => {
        const container = {
          items: {
            query() {
              return {
                fetchAll() {
                  return {
                    resources: cosmosMockedReturn,
                  }
                },
              }
            },
          },
        }

        const loader = loadDkimFailConnection({ container, cleanseInput })

        const dkimFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          last: 100,
          first: undefined,
        })

        expect(dkimFailSenders).toEqual(noLimitReversed)
      })
    })
    describe('no senders are found', () => {
      it('returns an empty list', async () => {
        const container = {
          items: {
            query() {
              return {
                fetchAll() {
                  return {
                    resources: [],
                  }
                },
              }
            },
          },
        }

        const loader = loadDkimFailConnection({ container, cleanseInput })

        const dkimFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
        })

        expect(dkimFailSenders).toEqual({
          edges: [],
          pageInfo: {
            endCursor: '',
            hasNextPage: false,
            hasPreviousPage: false,
            startCursor: '',
          },
        })
      })
    })
  })
  describe('given an unsuccessful load', () => {
    describe('first and last argument are both set', () => {
      it('throws an error', async () => {
        const container = {
          items: {
            query() {
              return {
                fetchAll() {
                  return {
                    resources: [],
                  }
                },
              }
            },
          },
        }

        const loader = loadDkimFailConnection({ container, cleanseInput })

        try {
          await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: false,
            first: 1,
            last: 1,
          })
        } catch (err) {
          expect(err).toEqual(
            new Error(
              'Unable to have first and last arguments set, when querying for dkim fail senders.',
            ),
          )
        }

        expect(consoleOutput).toEqual([
          'First and last arguments set when trying to retrieve dkim fail senders.',
        ])
      })
    })
  })
  describe('cosmos error occurs', () => {
    it('throws an error message', async () => {
      const container = {
        items: {
          query() {
            return {
              fetchAll() {
                throw new Error('Cosmos Error Occurred.')
              },
            }
          },
        },
      }

      const loader = loadDkimFailConnection({ container, cleanseInput })

      const dkimFailSenders = await loader({
        startDate: '2019-01-01',
        endDate: '2019-01-31',
        domain: 'test.gc.ca',
        thirtyDays: false,
      })

      expect(dkimFailSenders).toEqual({
        edges: [],
        pageInfo: {
          endCursor: '',
          hasNextPage: false,
          hasPreviousPage: false,
          startCursor: '',
        },
      })

      expect(consoleOutput).toEqual([
        'Cosmos error occurred while loading fail dkim senders for test.gc.ca, error: Error: Cosmos Error Occurred.',
      ])
    })
  })
})
