from contextlib import asynccontextmanager

import httpx
import uvicorn
from fastapi import FastAPI
from routers import include_routers

from infra.httpx_client import client


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = httpx.AsyncClient()
    app.state.httpx_client = client
    yield
    await client.aclose()

app = FastAPI(lifespan=lifespan)


include_routers(app)



if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)