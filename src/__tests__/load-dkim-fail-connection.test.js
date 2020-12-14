const { loadDkimFailConnection } = require('../loaders')
const { cleanseInput } = require('../validators')

const {
  cosmosReturn,
  noCursorTest,
  afterCursor,
  beforeCursor,
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

  describe('thirty days is true', () => {
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
            thirtyDays: true,
            before: undefined,
            after: undefined,
            first: 50,
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
            thirtyDays: true,
            after: 'ZmFpbERraW06IDU=',
            first: 50,
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
            thirtyDays: true,
            before: 'ZmFpbERraW06MTU=',
            last: 50,
          })

          expect(dkimFailSenders).toEqual(beforeCursor)
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
            thirtyDays: true,
            first: 5,
          })

          expect(dkimFailSenders).toEqual(firstLimit)
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
            thirtyDays: true,
            last: 5,
            first: undefined,
          })

          expect(dkimFailSenders).toEqual(lastLimit)
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
            first: 50,
            thirtyDays: true,
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
              thirtyDays: true,
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
      describe('first and last argument are both not set', () => {
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
              thirtyDays: true,
              first: undefined,
              last: undefined,
            })
          } catch (err) {
            expect(err).toEqual(
              new Error(
                'Unable to have first and last arguments not set, when querying for dkim fail senders.',
              ),
            )
          }

          expect(consoleOutput).toEqual([
            'First and last arguments were not set when trying to retrieve dkim fail senders.',
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
          thirtyDays: true,
          first: 50,
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
  describe('thirty days is false', () => {
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
            first: 50,
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
            first: 50,
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
            last: 50,
          })

          expect(dkimFailSenders).toEqual(beforeCursor)
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
            first: 50,
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
      describe('first and last argument are both not set', () => {
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
              first: undefined,
              last: undefined,
            })
          } catch (err) {
            expect(err).toEqual(
              new Error(
                'Unable to have first and last arguments not set, when querying for dkim fail senders.',
              ),
            )
          }

          expect(consoleOutput).toEqual([
            'First and last arguments were not set when trying to retrieve dkim fail senders.',
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
          first: 50,
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
})
