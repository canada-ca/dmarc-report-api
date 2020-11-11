const moment = require('moment')
const { stringify } = require('jest-matcher-utils')
const { loadDates } = require('../loaders')

describe('given the date range function', () => {
  let consoleOutput = []
  const mockedWarn = (output) => consoleOutput.push(output)
  beforeEach(() => {
    console.warn = mockedWarn
    consoleOutput = []
  })

  describe('given a successful return', () => {
    describe('given two date strings', () => {
      describe('date strings range is one month', () => {
        it('returns the single month', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-01-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is two months', () => {
        it('returns the two months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-02-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is three months', () => {
        it('returns the three months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-03-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
            {
              startDate: '2020-03-01',
              endDate: '2020-03-31',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is four months', () => {
        it('returns the four months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-04-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
            {
              startDate: '2020-03-01',
              endDate: '2020-03-31',
            },
            {
              startDate: '2020-04-01',
              endDate: '2020-04-30',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is five months', () => {
        it('returns the five months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-05-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
            {
              startDate: '2020-03-01',
              endDate: '2020-03-31',
            },
            {
              startDate: '2020-04-01',
              endDate: '2020-04-30',
            },
            {
              startDate: '2020-05-01',
              endDate: '2020-05-31',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is six months', () => {
        it('returns the six months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-06-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
            {
              startDate: '2020-03-01',
              endDate: '2020-03-31',
            },
            {
              startDate: '2020-04-01',
              endDate: '2020-04-30',
            },
            {
              startDate: '2020-05-01',
              endDate: '2020-05-31',
            },
            {
              startDate: '2020-06-01',
              endDate: '2020-06-30',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is seven months', () => {
        it('returns the seven months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-07-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
            {
              startDate: '2020-03-01',
              endDate: '2020-03-31',
            },
            {
              startDate: '2020-04-01',
              endDate: '2020-04-30',
            },
            {
              startDate: '2020-05-01',
              endDate: '2020-05-31',
            },
            {
              startDate: '2020-06-01',
              endDate: '2020-06-30',
            },
            {
              startDate: '2020-07-01',
              endDate: '2020-07-31',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is eight months', () => {
        it('returns the eight months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-08-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
            {
              startDate: '2020-03-01',
              endDate: '2020-03-31',
            },
            {
              startDate: '2020-04-01',
              endDate: '2020-04-30',
            },
            {
              startDate: '2020-05-01',
              endDate: '2020-05-31',
            },
            {
              startDate: '2020-06-01',
              endDate: '2020-06-30',
            },
            {
              startDate: '2020-07-01',
              endDate: '2020-07-31',
            },
            {
              startDate: '2020-08-01',
              endDate: '2020-08-31',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is nine months', () => {
        it('returns the nine months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-09-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
            {
              startDate: '2020-03-01',
              endDate: '2020-03-31',
            },
            {
              startDate: '2020-04-01',
              endDate: '2020-04-30',
            },
            {
              startDate: '2020-05-01',
              endDate: '2020-05-31',
            },
            {
              startDate: '2020-06-01',
              endDate: '2020-06-30',
            },
            {
              startDate: '2020-07-01',
              endDate: '2020-07-31',
            },
            {
              startDate: '2020-08-01',
              endDate: '2020-08-31',
            },
            {
              startDate: '2020-09-01',
              endDate: '2020-09-30',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is ten months', () => {
        it('returns the ten months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-10-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
            {
              startDate: '2020-03-01',
              endDate: '2020-03-31',
            },
            {
              startDate: '2020-04-01',
              endDate: '2020-04-30',
            },
            {
              startDate: '2020-05-01',
              endDate: '2020-05-31',
            },
            {
              startDate: '2020-06-01',
              endDate: '2020-06-30',
            },
            {
              startDate: '2020-07-01',
              endDate: '2020-07-31',
            },
            {
              startDate: '2020-08-01',
              endDate: '2020-08-31',
            },
            {
              startDate: '2020-09-01',
              endDate: '2020-09-30',
            },
            {
              startDate: '2020-10-01',
              endDate: '2020-10-31',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is eleven months', () => {
        it('returns the eleven months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-11-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
            {
              startDate: '2020-03-01',
              endDate: '2020-03-31',
            },
            {
              startDate: '2020-04-01',
              endDate: '2020-04-30',
            },
            {
              startDate: '2020-05-01',
              endDate: '2020-05-31',
            },
            {
              startDate: '2020-06-01',
              endDate: '2020-06-30',
            },
            {
              startDate: '2020-07-01',
              endDate: '2020-07-31',
            },
            {
              startDate: '2020-08-01',
              endDate: '2020-08-31',
            },
            {
              startDate: '2020-09-01',
              endDate: '2020-09-30',
            },
            {
              startDate: '2020-10-01',
              endDate: '2020-10-31',
            },
            {
              startDate: '2020-11-01',
              endDate: '2020-11-30',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
      describe('date strings range is twelve months', () => {
        it('returns the twelve months', () => {
          const dateLoader = loadDates({ moment })
          const dates = dateLoader({
            startDate: '2020-01-01',
            endDate: '2020-12-01',
          })
          const expectedDates = [
            {
              startDate: '2020-01-01',
              endDate: '2020-01-31',
            },
            {
              startDate: '2020-02-01',
              endDate: '2020-02-29',
            },
            {
              startDate: '2020-03-01',
              endDate: '2020-03-31',
            },
            {
              startDate: '2020-04-01',
              endDate: '2020-04-30',
            },
            {
              startDate: '2020-05-01',
              endDate: '2020-05-31',
            },
            {
              startDate: '2020-06-01',
              endDate: '2020-06-30',
            },
            {
              startDate: '2020-07-01',
              endDate: '2020-07-31',
            },
            {
              startDate: '2020-08-01',
              endDate: '2020-08-31',
            },
            {
              startDate: '2020-09-01',
              endDate: '2020-09-30',
            },
            {
              startDate: '2020-10-01',
              endDate: '2020-10-31',
            },
            {
              startDate: '2020-11-01',
              endDate: '2020-11-30',
            },
            {
              startDate: '2020-12-01',
              endDate: '2020-12-31',
            },
          ]
          expect(dates).toEqual(expectedDates)
        })
      })
    })
  })
  describe('given an unsuccessful return', () => {
    describe('startDate is not a string', () => {
      const dateLoader = loadDates({ moment })
      ;[123, {}, [], null, undefined, true].forEach((invalidInput) => {
        it(`throws an error when generating dates ${stringify(
          invalidInput,
        )}`, () => {
          expect(() =>
            dateLoader({ startDate: invalidInput, endDate: '' }),
          ).toThrow(
            new Error('Start date is not a valid string. Please try again.'),
          )
          expect(consoleOutput).toEqual([
            `Error: startDate for dateRange must be of type string, instead: startDate: ${typeof invalidInput}`,
          ])
        })
      })
    })
    describe('endDate is not a string', () => {
      const dateLoader = loadDates({ moment })
      ;[123, {}, [], null, undefined, true].forEach((invalidInput) => {
        it(`throws an error when generating dates ${stringify(
          invalidInput,
        )}`, () => {
          expect(() =>
            dateLoader({ startDate: '', endDate: invalidInput }),
          ).toThrow(
            new Error('End date is not a valid string. Please try again.'),
          )
          expect(consoleOutput).toEqual([
            `Error: endDate for dateRange must be of type string, instead: endDate: ${typeof invalidInput}`,
          ])
        })
      })
    })
    describe('startDate does not match format of YYYY-MM-DD', () => {
      it('throws an error', () => {
        const dateLoader = loadDates({ moment })
        expect(() =>
          dateLoader({ startDate: 'string', endDate: '1970-12-01' }),
        ).toThrow(
          new Error(
            'Start date is not a valid format, please conform to YYYY-MM-DD. Please try again.',
          ),
        )
        expect(consoleOutput).toEqual([
          `Error: startDate for dateRange must conform to format: YYYY-MM-DD, instead: startDate: string`,
        ])
      })
    })
    describe('endDate does not match format of YYYY-MM-DD', () => {
      it('throws an error', () => {
        const dateLoader = loadDates({ moment })
        expect(() =>
          dateLoader({ startDate: '1970-01-01', endDate: 'string' }),
        ).toThrow(
          new Error(
            'End date is not a valid format, please conform to YYYY-MM-DD. Please try again.',
          ),
        )
        expect(consoleOutput).toEqual([
          `Error: endDate for dateRange must conform to format: YYYY-MM-DD, instead: endDate: string`,
        ])
      })
    })
    describe('startDate is greater than endDate', () => {
      it('throws an error', () => {
        const dateLoader = loadDates({ moment })
        expect(() =>
          dateLoader({ startDate: '2020-01-01', endDate: '1970-01-01' }),
        ).toThrow(
          new Error(
            'End date must be greater than start date. Please try again.',
          ),
        )
        expect(consoleOutput).toEqual([
          `Error: end date is before start date, end date is required to be greater than start date, startDate: 2020-01-01, endDate: 1970-01-01`,
        ])
      })
    })
  })
})
