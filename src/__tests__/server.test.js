require('dotenv-safe').config({
  allowEmptyValues: true,
})

const { DMARC_REPORT_API_SECRET, DMARC_REPORT_API_TOKEN } = process.env

const jwt = require('jsonwebtoken')
const request = require('supertest')
const { Server } = require('../server')

describe('parse server', () => {
  const consoleInfoOutput = []
  const consoleWarnOutput = []
  const mockedInfo = (output) => consoleInfoOutput.push(output)
  const mockedWarn = (output) => consoleWarnOutput.push(output)

  beforeEach(() => {
    console.info = mockedInfo
    console.warn = mockedWarn
    consoleInfoOutput.length = 0
    consoleWarnOutput.length = 0
  })

  describe('/alive', () => {
    it('responds with a 200', async () => {
      const response = await request(Server({})).get('/alive')
      expect(response.status).toEqual(200)
      expect(consoleInfoOutput).toEqual([
        `🚀 Server ready at http://localhost:4001/graphql`,
      ])
    })
  })
  describe('/ready', () => {
    it('responds with a 200', async () => {
      const response = await request(Server({})).get('/ready')
      expect(response.status).toEqual(200)
      expect(consoleInfoOutput).toEqual([
        `🚀 Server ready at http://localhost:4001/graphql`,
      ])
    })
  })
  describe('/graphql', () => {
    describe('successful server creation', () => {
      it('returns 500', async () => {
        const token = jwt.sign(
          {
            parameters: {
              apiKey: DMARC_REPORT_API_TOKEN,
            },
          },
          DMARC_REPORT_API_SECRET,
          { algorithm: 'HS256' },
        )

        const response = await request(Server({}))
          .post('/graphql')
          .set('Authorization', token)

        expect(response.status).toEqual(500)
        expect(consoleInfoOutput).toEqual([
          `🚀 Server ready at http://localhost:4001/graphql`,
        ])
      })
    })
    describe('token was not included in request', () => {
      it('throws an error', async () => {
        const response = await request(Server({})).post('/graphql')
        const [error] = JSON.parse(response.error.text).errors

        expect(error.message).toEqual(
          'Context creation failed: Unable to access dmarc-report-api',
        )
        expect(consoleWarnOutput).toEqual([
          'User attempted to access dmarc-report-api without auth token.',
        ])
      })
    })
    describe('token parameters is incorrect', () => {
      it('throws an error', async () => {
        const token = jwt.sign(
          {
            parameters: {
              apiKey: 'someSecretToken',
            },
          },
          DMARC_REPORT_API_SECRET,
          { algorithm: 'HS256' },
        )

        const response = await request(Server({}))
          .post('/graphql')
          .set('Authorization', token)

        const [error] = JSON.parse(response.error.text).errors

        expect(error.message).toEqual(
          'Context creation failed: Unable to access dmarc-report-api',
        )
        expect(consoleWarnOutput).toEqual([
          'User attempted to access dmarc-report-api with an incorrect auth token.',
        ])
      })
    })
  })
})
