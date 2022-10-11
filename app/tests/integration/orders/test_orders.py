from http import HTTPStatus
from uuid import uuid1


def test_get_orders(testClient):

    response = testClient.get("/orders")

    assert not len(response.json())


def test_make_order(testClient, database):
    orderId = str(uuid1())
    test_order = {
        "id": orderId,
        "status": "new",
        "items": [
            {
                "title": "avocado",
                "description": "useful description",
                "quantity": 2,
                "price": 27.0,
            }
        ],
        "total_price": 54.0,
    }

    response = testClient.post("/orders", json=test_order)

    assert response.status_code == HTTPStatus.CREATED

    assert database.orders.find_one({"id": orderId})
