from python:3.8-alpine

# Python, don't write bytecode!
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add -U --no-cache openssl-dev libffi-dev build-base musl-dev python3 python3-dev
RUN python3 -m pip install pipenv
