const jwt = require('jsonwebtoken')

const { DMARC_REPORT_API_SECRET } = process.env

const verifyToken = ({ token, secret = String(DMARC_REPORT_API_SECRET) }) => {
  let decoded
  try {
    decoded = jwt.verify(token, secret)
  } catch (err) {
    if (err.name === 'TokenExpiredError') {
      console.warn('JWT has expired when reaching api.')
      throw new Error('Token has expired please send a new request.')
    } else {
      console.warn('JWT was attempted to be verified but secret was incorrect.')
      throw new Error('Invalid token, please request a new one.')
    }
  }
  return decoded.parameters
}

module.exports = {
  verifyToken,
}
