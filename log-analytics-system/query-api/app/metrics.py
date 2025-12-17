import redis
import os
REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
redis = redis.Redis.from_url(REDIS_URL)