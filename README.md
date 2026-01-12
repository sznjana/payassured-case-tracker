PayAssured: Invoice Recovery Case Tracker 🚀
This is a full-stack internal CRM module designed for PayAssured to manage client data and track the recovery process of unpaid invoices. It allows internal teams to monitor active cases, record recovery notes, and organize follow-up actions efficiently.

🛠️ Tech Stack
Backend: Python (FastAPI)
Database: SQLite with SQLAlchemy ORM (Relational structure)
Frontend: HTML5 with Jinja2 Templates
Server: Uvicorn (ASGI)

📂 Project Structure
Plaintext

/PayAssured_Project
├── main.py              # Application logic & API routes
├── models.py            # Relational database tables (Clients & Cases)
├── database.py          # Database connection & session setup
├── /templates           # HTML UI components
│   ├── index.html       # Main Dashboard (Case List & Client List)
│   ├── add_client.html  # Client registration form
│   ├── add_case.html    # Case creation form
│   └── case_detail.html # Case detail & update page
├── /screenshots         # Visual proof of functionality
└── README.md            # Project documentation
⚙️ Setup & Installation
1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

2. Install Dependencies
Run the following command to install the required libraries:
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart

3. Database Creation
The application uses SQLite. On the first run, the system will automatically generate a file named recovery.db and create the required clients and cases tables.

4. Running the Application
   
Start the server using Uvicorn:
python -m uvicorn main:app --reload
Once the server is running, visit http://127.0.0.1:8000 in your browser.

💡 How to Use
Add a Client: Go to the "Add New Client" page to register a business.

Create a Case: Use the "Add New Case" page to link an unpaid invoice to an existing client.

Filter & Sort: On the Dashboard, use the filter links to view cases by status (New, Closed) or sort them by their Due Date.

✅ Assignment Requirements Met
Relational Database: Proper Foreign Key linkage between Clients and Cases.

Clean APIs: Structured GET and POST endpoints for data management.

UI/UX: A functional, scannable dashboard for day-to-day operations.

Filtering/Sorting: Functional logic to organize recovery priorities.
