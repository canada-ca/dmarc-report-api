const { TOKEN_HASH } = process.env

const checkToken = (verifyToken, bcrypt, token) => () => {
  if (token !== '') {
    const apiKey = verifyToken({ token }).apiKey
    if (!bcrypt.compareSync(apiKey, TOKEN_HASH)) {
      console.warn(
        'User attempted to access dmarc-report-api with an incorrect auth token.',
      )
      throw new Error('Unable to access dmarc-report-api')
    }
  } else {
    console.warn(
      'User attempted to access dmarc-report-api without auth token.',
    )
    throw new Error('Unable to access dmarc-report-api')
  }
}

module.exports = {
  checkToken,
}
