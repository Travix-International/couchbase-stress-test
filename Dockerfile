FROM alpine:3.6

MAINTAINER Travix

RUN apk --no-cache add \
      curl \
      python \
      python3.6 \
      py-pip \
    && pip3 install couchbase-stress-test \
    && rm -rf /var/cache/apk/*

# runtime environment variables
ENV COUCHBASE_HOST="127.0.0.1" \
    COUCHBASE_PORT="8091" \
    COUCHBASE_USERNAME="" \
    COUCHBASE_PASSWORD="" \
    MAX_WORKERS="1" \
    RANGE="1000"

CMD prometheus-couchbase-exporter -host ${COUCHBASE_HOST}:${COUCHBASE_PORT} -u ${COUCHBASE_USERNAME} -p ${COUCHBASE_PASSWORD} -m ${MAX_WORKERS} -r ${RANGE}