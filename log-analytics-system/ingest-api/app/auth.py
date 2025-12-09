from fastapi import Depends, HTTPException


# Simple placeholder auth dependency using header token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


security = HTTPBearer()


async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
token = credentials.credentials
# In prod: validate JWT, check issuer/audience
if token != "dev-token":
raise HTTPException(status_code=401, detail="Invalid token")
return {"sub": "dev-user"}