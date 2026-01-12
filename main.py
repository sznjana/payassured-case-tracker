from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import models, database

# This creates the actual database tables (the notebooks) if they don't exist
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Tell the Boss where to find the HTML files
templates = Jinja2Templates(directory="templates")

# --- HOME PAGE ---
@app.get("/")
def home(request: Request, status: str = None, sort: str = None, db: Session = Depends(database.get_db)):
    clients = db.query(models.Client).all()
    
    # Start with all cases
    query = db.query(models.Case)
    
    # 1. Logic for Filtering (e.g., /?status=New)
    if status:
        query = query.filter(models.Case.status == status)
        
    # 2. Logic for Sorting (e.g., /?sort=asc)
    if sort == "asc":
        query = query.order_by(models.Case.due_date.asc())
    elif sort == "desc":
        query = query.order_by(models.Case.due_date.desc())
    
    cases = query.all()
    
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "clients": clients, 
        "cases": cases
    })
# --- CLIENT MANAGEMENT ---

# Show the "Add Client" Form
@app.get("/add-client")
def add_client_form(request: Request):
    return templates.TemplateResponse("add_client.html", {"request": request})

# Save the Client data when the button is clicked
@app.post("/clients")
def create_client(
    client_name: str = Form(...), 
    company_name: str = Form(...), 
    email: str = Form(...), 
    db: Session = Depends(database.get_db)
):
    # 1. Create the new client
    new_client = models.Client(
        client_name=client_name, 
        company_name=company_name, 
        email=email
    )
    
    # 2. Save it to the database
    db.add(new_client)
    db.commit()
    
    # 3. CRUCIAL: You MUST 'return' the redirect, or you get a blank page!
    return RedirectResponse(url="/", status_code=303)
# --- NEXT STEP: CASE MANAGEMENT ---
# We will add Case Creation logic here in the next step!
# --- CASE MANAGEMENT ---

# 1. Show the "Add Case" Form
@app.get("/add-case")
def add_case_form(request: Request, db: Session = Depends(database.get_db)):
    # We need to fetch clients so the user can choose one in the dropdown
    clients = db.query(models.Client).all()
    return templates.TemplateResponse("add_case.html", {"request": request, "clients": clients})

# 2. Save the Case data
@app.post("/cases")
def create_case(
    client_id: int = Form(...),
    invoice_number: str = Form(...),
    invoice_amount: float = Form(...),
    due_date: str = Form(...),
    db: Session = Depends(database.get_db)
):
    new_case = models.Case(
        client_id=client_id,
        invoice_number=invoice_number,
        invoice_amount=invoice_amount,
        due_date=due_date,
        status="New" # Default status
    )
    db.add(new_case)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.get("/cases/{case_id}")
def case_detail(case_id: int, request: Request, db: Session = Depends(database.get_db)):
    case = db.query(models.Case).filter(models.Case.id == case_id).first()
    return templates.TemplateResponse("case_detail.html", {"request": request, "case": case})

@app.post("/cases/{case_id}/update")
def update_case(case_id: int, status: str = Form(...), notes: str = Form(None), db: Session = Depends(database.get_db)):
    case = db.query(models.Case).filter(models.Case.id == case_id).first()
    case.status = status
    # We need to add a 'notes' column to models.py if you want to save notes!
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/cases/{case_id}/update")
def update_case(case_id: int, status: str = Form(...), notes: str = Form(None), db: Session = Depends(database.get_db)):
    case = db.query(models.Case).filter(models.Case.id == case_id).first()
    case.status = status
    case.last_follow_up_notes = notes
    db.commit()
    return RedirectResponse(url="/", status_code=303)