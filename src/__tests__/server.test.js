const {
  DEPTH_LIMIT: maxDepth,
  COST_LIMIT: complexityCost,
  SCALAR_COST: scalarCost,
  OBJECT_COST: objectCost,
  LIST_FACTOR: listFactor,
} = process.env

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
    describe('endpoint is alive', () => {
      it('returns 200', async () => {
        const response = await request(
          Server(
            maxDepth,
            complexityCost,
            scalarCost,
            objectCost,
            listFactor,
            {
              query: jest.fn(),
              collections: jest.fn(),
              transaction: jest.fn(),
            },
          ),
        )
          .post('/graphql')
          .set('Accept', 'application/json')
          .send({ query: '{__schema {types {kind}}}' })

        expect(response.status).toEqual(200)
      })
    })
    describe('validation rule is broken', () => {
      describe('query cost is too high', () => {
        it('returns an error message', async () => {
          const response = await request(
            Server(maxDepth, 1, 100, 100, 100, {
              query: jest.fn(),
              collections: jest.fn(),
              transaction: jest.fn(),
            }),
          )
            .post('/graphql')
            .set('Accept', 'application/json')
            .send({ query: '{__schema {types {kind}}}' })

          expect(response.status).toEqual(400)
          expect(response.text).toEqual(
            expect.stringContaining('Query error, query is too complex.'),
          )
        })
      })
    })
  })
})
