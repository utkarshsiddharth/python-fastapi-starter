from enum import Enum 
from api.app import app
from pydantic import BaseModel
from fastapi import Query

class CoinSymbols(str, Enum):
    BTC='BTC',
    BNB='BNB',
    TBNB='TBNB',
    AAVE='AAVE',
    DOT='DOT',
    SHIB='SHIB',

class Course(BaseModel):
    id: int 
    name: str 
    pricing: float 
    is_early_bird: bool | None

@app.get("/",)
async def health_check() -> dict:
    return {
        "status": "OK"
    }

# Path using Enum only parameter
@app.get("/coin/{coin_symbol}")
async def get_coin_data_by_symbol(coin_symbol: CoinSymbols) -> dict:
    return {
        "status": "OK",
        "data": {
            coin_symbol: coin_symbol
        }
    }

# Path using typesafe parameters
@app.get("/item/{item_id}")
async def get_item_by_id(item_id: int) -> dict:
    return {
        "status": "OK",
        "item": item_id
    }

# Path with any parameters - :path
@app.get("/file/{file_path:path}")
async def get_file_by_path(file_path: str):
    return {
        "path": file_path
    }

# Path using query parameters
@app.get("/products/{product_id}")
async def get_products_by_id(product_id: int, needs: str, skip: int = Query(default=0,  description="Provide a number from which the items will be skipped"), limit: int = 10, q: str | None = None) -> dict:
    return {
        "status": "OK",
        "product_id": product_id,
        "query": q,
        "limit": limit,
        "skip": skip,
        "requiredQueryParam": f"needs {needs}",
    }
