from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models import Base, engine, get_db, Item, ItemSchema

# Initialize FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.get("/items", response_model=List[ItemSchema])
def get_all_items(db: Session = Depends(get_db)):
    """
    Retrieve all items from the database.
    """
    items = db.query(Item).all()
    return items

@app.get("/items/{item_id}", response_model=ItemSchema)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific item by its ID.
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=ItemSchema)
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    """
    Create a new item.
    """
    new_item = Item(name=item.name, description=item.description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
