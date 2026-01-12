from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String)
    company_name = Column(String)
    city = Column(String)  # Added to meet assignment requirements
    contact_person = Column(String)  # Added to meet assignment requirements
    phone = Column(String)  # Added to meet assignment requirements
    email = Column(String, unique=True)
    
    # This allows a client to "own" multiple cases
    cases = relationship("Case", back_populates="owner")

class Case(Base):
    __tablename__ = "cases"
    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True)
    invoice_amount = Column(Float)
    
    # --- NEW COLUMNS ADDED BELOW ---
    due_date = Column(String)  # This was the cause of your 'Internal Server Error'
    status = Column(String, default="New") # (New, In Follow-up, Partially Paid, Closed)
    last_follow_up_notes = Column(String, nullable=True) 
    # -------------------------------

    client_id = Column(Integer, ForeignKey("clients.id"))
    
    # This links the case back to the client
    owner = relationship("Client", back_populates="cases")