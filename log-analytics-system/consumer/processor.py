import json
from db import insert_log
from redis_client import redis




def process_log(raw_json: str):
data = json.loads(raw_json)
# normalize
insert_log(data)


service = data.get('service')
# update counters
redis.incr(f"logs:{service}:count")
if data.get('level') == 'ERROR':
redis.incr(f"logs:{service}:errors")
# optional: update p99 using sorted sets or HLL (left as exercise)