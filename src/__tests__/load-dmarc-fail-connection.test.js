const { loadDmarcFailConnection } = require('../loaders')
const { cleanseInput } = require('../validators')

const {
  cosmosReturn,
  noCursor,
  afterCursor,
  beforeCursor,
  noLimit,
  firstLimit,
  lastLimit,
  noLimitReversed,
} = require('../__mocks__/dmarc-fail')

describe('given the loadDmarcFailConnection loader', () => {
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
        const loader = loadDmarcFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          before: undefined,
          after: undefined,
        })

        expect(dmarcFailSenders).toEqual(noCursor)
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
        const loader = loadDmarcFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          after: 'ZmFpbERtYXJjOjE1',
        })

        expect(dmarcFailSenders).toEqual(afterCursor)
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
        const loader = loadDmarcFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          before: 'ZmFpbERtYXJjOjY=',
        })

        expect(dmarcFailSenders).toEqual(beforeCursor)
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
        const loader = loadDmarcFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: undefined,
          last: undefined,
        })

        expect(dmarcFailSenders).toEqual(noLimit)
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
        const loader = loadDmarcFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: 5,
          last: undefined,
        })

        expect(dmarcFailSenders).toEqual(firstLimit)
      })
    })
    describe('using first limit greater than cosmos return', () => {
      it('returns all dmarc fail senders', async () => {
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
        const loader = loadDmarcFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: 100,
          last: undefined,
        })

        expect(dmarcFailSenders).toEqual(noLimit)
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
        const loader = loadDmarcFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: undefined,
          last: 5,
        })

        expect(dmarcFailSenders).toEqual(lastLimit)
      })
    })
    describe('using last limit greater than cosmos return', () => {
      it('returns all dmarc fail senders', async () => {
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
        const loader = loadDmarcFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: undefined,
          last: 100,
        })

        expect(dmarcFailSenders).toEqual(noLimitReversed)
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

        const loader = loadDmarcFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
        })

        expect(dmarcFailSenders).toEqual({
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

        const loader = loadDmarcFailConnection({ container, cleanseInput })

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
              'Unable to have first and last arguments set, when querying for dmarc fail senders.',
            ),
          )
        }

        expect(consoleOutput).toEqual([
          'First and last arguments set when trying to retrieve dmarc fail senders.',
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

      const loader = loadDmarcFailConnection({ container, cleanseInput })

      const dmarcFailSenders = await loader({
        startDate: '2019-01-01',
        endDate: '2019-01-31',
        domain: 'test.gc.ca',
        thirtyDays: false,
      })

      expect(dmarcFailSenders).toEqual({
        edges: [],
        pageInfo: {
          endCursor: '',
          hasNextPage: false,
          hasPreviousPage: false,
          startCursor: '',
        },
      })

      expect(consoleOutput).toEqual([
        'Cosmos error occurred while loading fail dmarc senders for test.gc.ca, error: Error: Cosmos Error Occurred.',
      ])
    })
  })
})
