from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Product Service")


class Product(BaseModel):
    id: int
    name: str
    price: float


PRODUCTS = {
    1: {"id": 1, "name": "Laptop", "price": 4500.00},
    2: {"id": 2, "name": "Smartphone", "price": 2200.50},
    3: {"id": 3, "name": "Monitor", "price": 750.00},
}


@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    product = PRODUCTS.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
