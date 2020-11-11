const { loadFullPassConnection } = require('../loaders')
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
} = require('../__mocks__/full-pass')

describe('given the loadFullPassConnection loader', () => {
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
        const loader = loadFullPassConnection({ container, cleanseInput })

        const fullPassSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          before: undefined,
          after: undefined,
        })

        expect(fullPassSenders).toEqual(noCursor)
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
        const loader = loadFullPassConnection({ container, cleanseInput })

        const fullPassSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          before: undefined,
          after: 'ZnVsbFBhc3M6MTU=',
        })

        expect(fullPassSenders).toEqual(afterCursor)
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
        const loader = loadFullPassConnection({ container, cleanseInput })

        const fullPassSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          before: 'ZnVsbFBhc3M6Ng==',
          after: undefined,
        })

        expect(fullPassSenders).toEqual(beforeCursor)
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
        const loader = loadFullPassConnection({ container, cleanseInput })

        const fullPassSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: undefined,
          last: undefined,
        })

        expect(fullPassSenders).toEqual(noLimit)
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
        const loader = loadFullPassConnection({ container, cleanseInput })

        const fullPassSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: 5,
          last: undefined,
        })

        expect(fullPassSenders).toEqual(firstLimit)
      })
    })
    describe('using first limit greater than cosmos return', () => {
      it('returns all full pass senders', async () => {
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
        const loader = loadFullPassConnection({ container, cleanseInput })

        const fullPassSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: 100,
          last: undefined,
        })

        expect(fullPassSenders).toEqual(noLimit)
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
        const loader = loadFullPassConnection({ container, cleanseInput })

        const fullPassSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: undefined,
          last: 5,
        })

        expect(fullPassSenders).toEqual(lastLimit)
      })
    })
    describe('using last limit greater than cosmos return', () => {
      it('returns all full pass senders', async () => {
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
        const loader = loadFullPassConnection({ container, cleanseInput })

        const fullPassSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: undefined,
          last: 100,
        })

        expect(fullPassSenders).toEqual(noLimitReversed)
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
        const loader = loadFullPassConnection({ container, cleanseInput })

        const fullPassSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
        })

        expect(fullPassSenders).toEqual({
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

        const loader = loadFullPassConnection({ container, cleanseInput })

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
              'Unable to have first and last arguments set, when querying for full pass senders.',
            ),
          )
        }

        expect(consoleOutput).toEqual([
          'First and last arguments set when trying to retrieve full pass senders.',
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

      const loader = loadFullPassConnection({ container, cleanseInput })

      const fullPassSenders = await loader({
        startDate: '2019-01-01',
        endDate: '2019-01-31',
        domain: 'test.gc.ca',
        thirtyDays: false,
      })

      expect(fullPassSenders).toEqual({
        edges: [],
        pageInfo: {
          endCursor: '',
          hasNextPage: false,
          hasPreviousPage: false,
          startCursor: '',
        },
      })

      expect(consoleOutput).toEqual([
        'Cosmos error occurred while loading full pass senders for test.gc.ca, error: Error: Cosmos Error Occurred.',
      ])
    })
  })
})
