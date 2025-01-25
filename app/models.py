from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel


# Database configuration
# DATABASE_USERNAME = "myuser"
# DATABASE_PASSWORD = "mypassword"
# DATABASE_HOST = "localhost"  # Replace with your MySQL server's host
# DATABASE_PORT = 3306         # Default MySQL port
# DATABASE_NAME = "fastapidb"

# Create the database URL for SQLAlchemy
# DATABASE_URL = (
#     f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
# )

# Database configuration
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://myuser:mypassword@localhost/fastapidb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SQLAlchemy model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema for response
class ItemSchema(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True







