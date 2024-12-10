import os

from fastapi import FastAPI, Response
from contextlib import asynccontextmanager
from tinydb import TinyDB

import get_form
import repository


@asynccontextmanager
async def lifespan(a: FastAPI):
    repository.dbworker().init_data()
    yield
    print("Server shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(get_form.router)


@app.get("/")
async def api_is_ready():
    return Response(content="API is ready.", status_code=200)


if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", 9000))
    uvicorn.run(app, host=host, port=port)
