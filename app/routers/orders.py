from http import HTTPStatus
from fastapi import APIRouter, Depends
from app.db.db import getDB
from app.models.models import Order
from app.schemas.order import ordersEntity

ordersRouter = APIRouter()


@ordersRouter.get("/orders", status_code=HTTPStatus.OK)
def get_all_orders(db=Depends(getDB)):

    orders = db.orders.find()
    return ordersEntity(orders)


@ordersRouter.post("/orders", status_code=HTTPStatus.CREATED)
def process_order(order: dict, db=Depends(getDB)):
    parsed_order = Order.parse_obj(order)
    db.orders.insert_one(parsed_order.dict())
    return parsed_order
