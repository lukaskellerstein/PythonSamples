from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Sample FastAPI Server", version="1.0.0")

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

items_db = [
    {"id": 1, "name": "Laptop", "description": "Gaming laptop", "price": 1200.0},
    {"id": 2, "name": "Phone", "description": "Smartphone", "price": 800.0}
]

users_db = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Sample Server"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/items", response_model=List[Item])
async def get_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = next((item for item in items_db if item["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    new_id = max([i["id"] for i in items_db], default=0) + 1
    item_dict = item.dict()
    item_dict["id"] = new_id
    items_db.append(item_dict)
    return item_dict

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    item_index = next((i for i, item_data in enumerate(items_db) if item_data["id"] == item_id), None)
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item_dict = item.dict()
    item_dict["id"] = item_id
    items_db[item_index] = item_dict
    return item_dict

@app.patch("/items/{item_id}", response_model=Item)
async def partial_update_item(item_id: int, item: dict):
    item_index = next((i for i, item_data in enumerate(items_db) if item_data["id"] == item_id), None)
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item.items():
        if key in items_db[item_index]:
            items_db[item_index][key] = value
    
    return items_db[item_index]

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    item_index = next((i for i, item_data in enumerate(items_db) if item_data["id"] == item_id), None)
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_item = items_db.pop(item_index)
    return {"message": f"Item {item_id} deleted", "deleted_item": deleted_item}

@app.get("/users", response_model=List[User])
async def get_users():
    return users_db

@app.post("/users", response_model=User)
async def create_user(user: User):
    new_id = max([u["id"] for u in users_db], default=0) + 1
    user_dict = user.dict()
    user_dict["id"] = new_id
    users_db.append(user_dict)
    return user_dict

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
