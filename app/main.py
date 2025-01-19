from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dummy data: A list of items (simulating a database)
items = [
    {"id": 1, "name": "Laptop", "price": 1000.00, "description": "A high-performance laptop."},
    {"id": 2, "name": "Smartphone", "price": 500.00, "description": "A feature-packed smartphone."},
    {"id": 3, "name": "Headphones", "price": 100.00, "description": "Noise-cancelling headphones."},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items")
def get_all_items():
    """Return all items."""
    return {"items": items}

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    """Return a specific item by ID."""
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
