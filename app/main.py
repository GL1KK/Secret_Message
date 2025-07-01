from fastapi import FastAPI
from routers.myrouter import Router

app = FastAPI()

router = Router()

app.include_router(router.router)