from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="Stock Service")


class Stock(BaseModel):
    productId: int
    quantity: int


# "Na sztywno" zdefiniowane stany magazynowe
STOCKS = {
    1: {"productId": 1, "quantity": 15},
    2: {"productId": 2, "quantity": 0},
    3: {"productId": 3, "quantity": 7},
}


PRODUCT_SERVICE_BASE = "http://127.0.0.1:8001"


@app.get("/stock/{product_id}", response_model=Stock)
async def get_stock(product_id: int):
    try:
        resp = requests.get(f"{PRODUCT_SERVICE_BASE}/products/{product_id}", timeout=2)
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Failed to contact Product Service: {e}")

    if resp.status_code == 404:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} does not exist")
    if resp.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Product Service returned status {resp.status_code}")

    stock = STOCKS.get(product_id)
    if not stock:
        return {"productId": product_id, "quantity": 0}

    return stock
