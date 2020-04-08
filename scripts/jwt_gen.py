import jwt
import datetime
import os

from graphql import GraphQLError

try:
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0,seconds=1),
        'iat': datetime.datetime.utcnow(),
        'api_token': os.getenv('TOKEN')
    }
    token = jwt.encode(
        payload,
        str(os.getenv('JWT_SECRET')),
        algorithm='HS256'
    ).decode('utf-8')
except Exception as e:
    raise GraphQLError('Token Generation Error: ' + str(e))

print(token)
