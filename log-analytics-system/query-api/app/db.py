import os
import psycopg2
import json


DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@postgres:5432/postgres')


_conn = None


def get_conn():
global _conn
if _conn is None:
_conn = psycopg2.connect(DATABASE_URL)
return _conn




def query_logs(service: str = None, level: str = None, limit: int = 50):
c = get_conn()
with c.cursor() as cur:
sql = "SELECT service, level, message, timestamp, latency_ms, metadata FROM logs"
where = []
params = []
if service:
where.append('service = %s')
params.append(service)
if level:
where.append('level = %s')
params.append(level)
if where:
sql += ' WHERE ' + ' AND '.join(where)
sql += ' ORDER BY timestamp DESC LIMIT %s'
params.append(limit)
cur.execute(sql, tuple(params))
rows = cur.fetchall()
results = []
for r in rows:
results.append({
'service': r[0],
'level': r[1],
'message': r[2],
'timestamp': r[3].isoformat(),
'latency_ms': r[4],
'metadata': json.loads(r[5]) if r[5] else {}
})
return results