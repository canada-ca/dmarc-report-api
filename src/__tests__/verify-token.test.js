const { DMARC_REPORT_API_SECRET } = process.env

const jwt = require('jsonwebtoken')
const { verifyToken } = require('../auth')

describe('given a encoded token', () => {
  let consoleOutput = []
  const mockedInfo = (output) => consoleOutput.push(output)
  const mockedWarn = (output) => consoleOutput.push(output)
  beforeEach(() => {
    console.info = mockedInfo
    console.warn = mockedWarn
  })

  afterEach(() => {
    consoleOutput = []
  })
  describe('token can be decoded and verified', () => {
    it('returns the parameters', () => {
      const parameters = {
        userId: 1,
      }
      const token = jwt.sign({ parameters }, String(DMARC_REPORT_API_SECRET), {
        algorithm: 'HS256',
      })

      const decoded = verifyToken({ token })
      expect(decoded.userId).toEqual(1)
    })
  })
  describe('if the token has expired', () => {
    it('raises an error', () => {
      const parameters = {
        userId: 1,
      }
      const exp = Math.floor(Date.now() / 1000) - 1000

      const token = jwt.sign(
        {
          parameters,
          exp,
        },
        String(DMARC_REPORT_API_SECRET),
        {
          algorithm: 'HS256',
        },
      )

      expect(() => {
        verifyToken({ token })
      }).toThrow(Error('Token has expired please send a new request.'))
      expect(consoleOutput).toEqual([`JWT has expired when reaching api.`])
    })
  })
  describe('if the secret does not match', () => {
    it('raises an error', () => {
      const parameters = {
        userId: 1,
      }
      const token = jwt.sign({ parameters }, 'superSecretKey', {
        algorithm: 'HS256',
      })

      expect(() => {
        verifyToken({ token })
      }).toThrow(Error('Invalid token, please request a new one.'))
      expect(consoleOutput).toEqual([
        `JWT was attempted to be verified but secret was incorrect.`,
      ])
    })
  })
})
