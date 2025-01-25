# FastAPI Project

A FastAPI application designed to demonstrate features like WSGI middleware integration, database operations, and more.

## Getting Started

Follow these instructions to set up the project on your local machine.

---

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.8 or higher
- MySQL Server
- Git

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Create a virtual environment (optional but recommended):
```bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create database and user
```sql
sudo mysql -u root -p
CREATE DATABASE your_database_name;
CREATE USER 'your_username'@'%' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'%';
FLUSH PRIVILEGES;
```

5. Update DB credentials in the main.py file on the line
```bash
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://myuser:mypassword@localhost/fastapidb"
#where myuser is the db user, mypassword is the userpassword and fastapidb is the database name
```

6. Populate the DB with dummy data
```bash
mysql -u myuser -p fastapidb < data.sql
#details used here are based on the db, and user created in the previous step
```

7. Run the application Locally
```bash
uvicorn wsgi:app --host 0.0.0.0 --port 8000
```
8. Access it on a browser
```bash
http://127.0.0.1:8000
```