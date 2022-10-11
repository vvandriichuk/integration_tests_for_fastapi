from fastapi import FastAPI

from app.routers.orders import ordersRouter

app = FastAPI()

app.include_router(ordersRouter)


@app.get("/")
def read_root():
    return {"hello": "world"}
