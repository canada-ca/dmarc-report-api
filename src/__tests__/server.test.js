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
})
