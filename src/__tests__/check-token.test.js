const { DMARC_REPORT_API_TOKEN, DMARC_REPORT_API_SECRET } = process.env


const bcrypt = require('bcrypt')
const jwt = require('jsonwebtoken')
const { checkToken, verifyToken } = require('../auth')

describe('given the checkToken function', () => {
  const consoleOutput = []
  const mockedWarn = (output) => consoleOutput.push(output)

  beforeAll(() => {
    console.warn = mockedWarn
  })

  beforeEach(() => {
    consoleOutput.length = 0
  })

  describe('given a valid token', () => {
    it('does not throw an error', () => {
      const mockedBcrypt = {
        compareSync() { return jest.fn().mockReturnValue(true) },
      }
      const token = jwt.sign(
        {
          parameters: {
            apiKey: DMARC_REPORT_API_TOKEN,
          },
        },
        DMARC_REPORT_API_SECRET,
        { algorithm: 'HS256' },
      )

      const testCheckToken = checkToken(verifyToken, mockedBcrypt, token)

      expect(() => testCheckToken()).not.toThrow(Error)
    })
  })
  describe('given an invalid token payload', () => {
    it('throws an error', () => {
      const token = jwt.sign(
        {
          parameters: {
            apiKey: 'not a token',
          },
        },
        DMARC_REPORT_API_SECRET,
        { algorithm: 'HS256' },
      )

      const testCheckToken = checkToken(verifyToken, bcrypt, token)

      expect(() => testCheckToken()).toThrow(
        Error('Unable to access dmarc-report-api'),
      )
      expect(consoleOutput).toEqual([
        'User attempted to access dmarc-report-api with an incorrect auth token.',
      ])
    })
  })
  describe('given an invalid token secret', () => {
    it('throws an error', () => {
      const token = jwt.sign(
        {
          parameters: {
            apiKey: DMARC_REPORT_API_TOKEN,
          },
        },
        'some secret',
        { algorithm: 'HS256' },
      )

      const testCheckToken = checkToken(verifyToken, bcrypt, token)

      expect(() => testCheckToken()).toThrow(
        Error('Invalid token, please request a new one.'),
      )
      expect(consoleOutput).toEqual([
        'JWT was attempted to be verified but secret was incorrect.',
      ])
    })
  })
  describe('given no token', () => {
    it('throws an error', () => {
      const token = ''

      const testCheckToken = checkToken(verifyToken, bcrypt, token)

      expect(() => testCheckToken()).toThrow(
        Error('Unable to access dmarc-report-api'),
      )
      expect(consoleOutput).toEqual([
        'User attempted to access dmarc-report-api without auth token.',
      ])
    })
  })
})
