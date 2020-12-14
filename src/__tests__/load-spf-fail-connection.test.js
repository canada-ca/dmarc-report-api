const { loadSpfFailConnection } = require('../loaders')
const { cleanseInput } = require('../validators')

const {
  cosmosReturn,
  noCursor,
  afterCursor,
  beforeCursor,
  firstLimit,
  lastLimit,
} = require('../__mocks__/spf-fail')

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

  describe('thirty days is set to true', () => {
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
          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: true,
            before: undefined,
            after: undefined,
            first: 50,
          })

          expect(spfFailSenders).toEqual(noCursor)
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
          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: true,
            before: undefined,
            after: 'c3BmRmFpbDoxNA==',
            first: 50,
          })

          expect(spfFailSenders).toEqual(afterCursor)
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
          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: true,
            before: 'c3BmRmFpbDo2',
            after: undefined,
            last: 50,
          })

          expect(spfFailSenders).toEqual(beforeCursor)
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
          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: true,
            first: 5,
            last: undefined,
          })

          expect(spfFailSenders).toEqual(firstLimit)
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
          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: true,
            first: undefined,
            last: 5,
          })

          expect(spfFailSenders).toEqual(lastLimit)
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

          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: true,
            first: 50,
          })

          expect(spfFailSenders).toEqual({
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

          const loader = loadSpfFailConnection({ container, cleanseInput })

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
                'Unable to have first and last arguments set, when querying for spf fail senders.',
              ),
            )
          }

          expect(consoleOutput).toEqual([
            'First and last arguments set when trying to retrieve spf fail senders.',
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

          const loader = loadSpfFailConnection({ container, cleanseInput })

          try {
            await loader({
              startDate: '2019-01-01',
              endDate: '2019-01-31',
              domain: 'test.gc.ca',
              thirtyDays: true,
            })
          } catch (err) {
            expect(err).toEqual(
              new Error(
                'Unable to have first and last arguments not set, when querying for spf fail senders.',
              ),
            )
          }

          expect(consoleOutput).toEqual([
            'First and last arguments were not set when trying to retrieve spf fail senders.',
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

        const loader = loadSpfFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: true,
          first: 50,
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
          'Cosmos error occurred while loading spf fail senders for test.gc.ca, error: Error: Cosmos Error Occurred.',
        ])
      })
    })
  })
  describe('thirty days is set to false', () => {
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
          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: false,
            before: undefined,
            after: undefined,
            first: 50,
          })

          expect(spfFailSenders).toEqual(noCursor)
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
          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: false,
            before: undefined,
            after: 'c3BmRmFpbDoxNA==',
            first: 50,
          })

          expect(spfFailSenders).toEqual(afterCursor)
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
          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: false,
            before: 'c3BmRmFpbDo2',
            after: undefined,
            last: 50,
          })

          expect(spfFailSenders).toEqual(beforeCursor)
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
          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: false,
            first: 5,
            last: undefined,
          })

          expect(spfFailSenders).toEqual(firstLimit)
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
          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: false,
            last: 5,
          })

          expect(spfFailSenders).toEqual(lastLimit)
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

          const loader = loadSpfFailConnection({ container, cleanseInput })

          const spfFailSenders = await loader({
            startDate: '2019-01-01',
            endDate: '2019-01-31',
            domain: 'test.gc.ca',
            thirtyDays: false,
            first: 50,
          })

          expect(spfFailSenders).toEqual({
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

          const loader = loadSpfFailConnection({ container, cleanseInput })

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
                'Unable to have first and last arguments set, when querying for spf fail senders.',
              ),
            )
          }

          expect(consoleOutput).toEqual([
            'First and last arguments set when trying to retrieve spf fail senders.',
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

          const loader = loadSpfFailConnection({ container, cleanseInput })

          try {
            await loader({
              startDate: '2019-01-01',
              endDate: '2019-01-31',
              domain: 'test.gc.ca',
              thirtyDays: false,
            })
          } catch (err) {
            expect(err).toEqual(
              new Error(
                'Unable to have first and last arguments not set, when querying for spf fail senders.',
              ),
            )
          }

          expect(consoleOutput).toEqual([
            'First and last arguments were not set when trying to retrieve spf fail senders.',
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

        const loader = loadSpfFailConnection({ container, cleanseInput })

        const dmarcFailSenders = await loader({
          startDate: '2019-01-01',
          endDate: '2019-01-31',
          domain: 'test.gc.ca',
          thirtyDays: false,
          first: 50,
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
          'Cosmos error occurred while loading spf fail senders for test.gc.ca, error: Error: Cosmos Error Occurred.',
        ])
      })
    })
  })
})
