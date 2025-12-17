from fastapi import FastAPI, HTTPException
from .db import query_logs
from .redis_client import redis
import os
app = FastAPI(title="query-api")
@app.get('/health')
def health():
return {"status": "ok"}
@app.get('/metrics/{service}')
def get_metrics(service: str):
count = int(redis.get(f"logs:{service}:count") or 0)
errors = int(redis.get(f"logs:{service}:errors") or 0)
error_rate = (errors / count) if count else 0
return {"service": service, "count": count, "errors": errors, "error_rate": error_rate}
@app.get('/logs')
def search_logs(service: str = None, level: str = None, limit: int = 50):
rows = query_logs(service=service, level=level, limit=limit)
return {"results": rows}