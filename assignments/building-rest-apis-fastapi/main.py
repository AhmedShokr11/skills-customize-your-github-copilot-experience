from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(title="Building REST APIs with FastAPI - Starter")


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None


# simple in-memory storage
_items: Dict[int, Item] = {}
_next_id = 1


@app.get("/", tags=["root"])
def read_root():
    return {"message": "FastAPI starter is running. See /docs for interactive API."}


@app.get("/items", response_model=list[Item])
def list_items():
    return list(_items.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201, response_model=Item)
def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _items[_next_id] = item
    _next_id += 1
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    existing = _items.get(item_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    _items[item_id] = item
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
    return
