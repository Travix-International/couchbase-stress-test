=============================
Couchbase STRESS TEST
=============================

This COUCHBASE STESS TEST by inseting data

----------

Installation instructions:
--------------------------

Install via ``pip3``:

.. code-block::

   $ pip3 install couchbase-stress-test

Usage example:
--------------

By default, it will bind to port 9420, query Couchbase on 127.0.0.1:8091 and run queries configured in an external module `StatsMetrics <https://github.com/brunopsoares/statsmetrics>`_.
You can change these defaults as required by passing in options:

.. code-block::

   $ couchbase-stress-test -c <couchbase host:port> -u <couchbase username> -p <couchbase password> -m <number of thread to execute the calls asynchronously> - r <how many inserts to couchbase>

Docker instructions:
--------------------

Environment variables
In order to configure the Couchbase stress test for use with other than default settings you can pass in the
following environment variables:

.. csv-table:: Environment variables
   :header: "Name", "Description", "Default value"
   :widths: 18, 26, 10

   "COUCHBASE_HOST", "Couchbase host address", "127.0.0.1"
   "COUCHBASE_PORT", "Couchbase port address", "8091"
   "COUCHBASE_USERNAME", "Couchbase username",
   "COUCHBASE_PASSWORD", "Couchbase password",
   "PROMETHEUS_PORT", "Prometheus port to listen", "9420"
   "MAX_WORKERS", "Number of thread to execute the calls asynchronously", "1"
   "RANGE", "How many inserts to couchbase", "1000"

Running the container

.. code-block::

   docker run -t -i -p 9420:9420 -e COUCHBASE_HOST=127.0.0.1 -e COUCHBASE_PORT=8091 billmoritz/couchbase-exporter
