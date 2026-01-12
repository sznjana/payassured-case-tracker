from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This creates a simple database file in your folder named recovery.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./recovery.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# This is a helper tool to open and close the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()