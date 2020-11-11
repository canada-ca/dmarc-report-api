const { loadCategoryTotals } = require('../loaders')

describe('given the loadCategoryTotals function', () => {
  let consoleOutput = []
  const mockedError = (output) => consoleOutput.push(output)
  beforeEach(() => {
    console.error = mockedError
    consoleOutput = []
  })

  describe('given successful load', () => {
    it('returns category totals', async () => {
      const container = {
        items: {
          query() {
            return {
              fetchAll() {
                const category_totals = {}
                category_totals['pass-spf-only'] = 1
                category_totals['pass-dkim-only'] = 1
                category_totals.pass = 1
                category_totals.fail = 1

                return {
                  resources: [{ category_totals }],
                }
              },
            }
          },
        },
      }

      const loader = loadCategoryTotals({ container })

      const categoryTotals = await loader({
        startDate: '2020-09-01',
        endDate: '2020-09-30',
        domain: 'test.canada.ca',
        thirtyDays: false,
      })

      const expectedReturn = {
        fail: 1,
        pass: 1,
        passDkimOnly: 1,
        passSpfOnly: 1,
      }

      expect(categoryTotals).toEqual(expectedReturn)
    })
  })
  describe('query returns undefined', () => {
    it('returns category totals that are all 0', async () => {
      const container = {
        items: {
          query() {
            return {
              fetchAll() {
                return {
                  resources: [undefined],
                }
              },
            }
          },
        },
      }

      const loader = loadCategoryTotals({ container })

      const categoryTotals = await loader({
        startDate: '2020-09-01',
        endDate: '2020-09-30',
        domain: 'test.canada.ca',
        thirtyDays: false,
      })

      const expectedReturn = {
        fail: 0,
        pass: 0,
        passDkimOnly: 0,
        passSpfOnly: 0,
      }

      expect(categoryTotals).toEqual(expectedReturn)
    })
  })
  describe('cosmos error occurs', () => {
    it('returns category totals that are all 0', async () => {
      const container = {
        items: {
          query() {
            return {
              fetchAll() {
                throw new Error('Cosmos Error')
              },
            }
          },
        },
      }

      const loader = loadCategoryTotals({ container })

      const categoryTotals = await loader({
        startDate: '2020-09-01',
        endDate: '2020-09-30',
        domain: 'test.canada.ca',
        thirtyDays: false,
      })

      const expectedReturn = {
        fail: 0,
        pass: 0,
        passDkimOnly: 0,
        passSpfOnly: 0,
      }

      expect(categoryTotals).toEqual(expectedReturn)
      expect(consoleOutput).toEqual([
        'Cosmos error occurred while loading category totals for test.canada.ca, error: Error: Cosmos Error',
      ])
    })
  })
})
