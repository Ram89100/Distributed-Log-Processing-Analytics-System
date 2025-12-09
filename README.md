# Distributed-Log-Processing-Analytics-System
           +-------------------+
           |   Client Apps     |
           |  (microservices)  |
           +---------+---------+
                     |
                     | 1. Send Logs (HTTP)
                     v
           +-----------------------+
           |  FastAPI Ingest API  |
           +----------+------------+
                      |
                      | 2. Publish
                      v
           +-----------------------+
           | Kafka / Redpanda     |
           | Topic: logs_raw      |
           +----------+------------+
                      |
                      | 3. Consume
                      v
           +-----------------------+
           | Log Consumer Service |
           | (Python worker)      |
           +----------+------------+
                      |
          +-----------+------------+
          |                        |
    4a. Write to DB           4b. Cache Aggregations
     PostgreSQL                 Redis
          |                        |
          v                        v
    +-----------------+     +------------------+
    | logs table      |     | cached metrics   |
    +-----------------+     +------------------+

                     5. Query API
                     FastAPI (service #2)

