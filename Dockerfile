FROM ubuntu:20.04

ENV PYTHONUNBUFFERED=TRUE
ENV PIPENV_NOSPIN=TRUE
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/api

RUN set -ex \
	\
	&& savedAptMark="$(apt-mark showmanual)" \
	&& apt-get update && apt-get install -y --no-install-recommends \
    openssl \
    libffi-dev \
    musl-dev \
    python3.8 \
    python3-dev \
    python3-pip

RUN addgroup -gid 1000 -system dmarcapi && \
      adduser -u 1000 -system dmarcapi -gecos dmarcapi

RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install wheel
RUN python3 -m pip install pipenv --no-cache-dir

COPY /dmarc_report_api /api/dmarc_report_api
COPY Pipfile /api
COPY Pipfile.lock /api

WORKDIR /api

USER dmarcapi
RUN pipenv sync --bare

EXPOSE 5000
CMD pipenv run server
