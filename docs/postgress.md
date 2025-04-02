# Setting Up a Python Application with PostgreSQL on macOS (Using VS Code)

## 1. Install and Set Up Required Software

### 1.1 Install Homebrew (if not already installed)
Homebrew is a package manager for macOS that simplifies software installation.
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 1.2 Install PostgreSQL
```sh
brew install postgresql
```
Start the PostgreSQL service:
```sh
brew services start postgresql
```
Verify installation:
```sh
psql --version
```

### 1.3 Create a PostgreSQL User and Database
Open the PostgreSQL shell:
```sh
psql postgres
```
Create a new database user with a password:
```sql
CREATE USER myuser WITH PASSWORD 'mypassword';
```
Create a new database:
```sql
CREATE DATABASE mydatabase;
```
Grant privileges to the user:
```sql
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
```
Exit PostgreSQL:
```sh
\q
```

### 1.4 Install Python and Virtual Environment
Ensure Python is installed:
```sh
python3 --version
```
Install `venv` if not installed:
```sh
python3 -m ensurepip --default-pip
```
Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```

### 1.5 Install Required Python Packages
```sh
pip install psycopg2-binary sqlalchemy
```

---

## 2. Configure VS Code for PostgreSQL

### 2.1 Install VS Code (if not installed)
Download and install from [VS Code official website](https://code.visualstudio.com/).

### 2.2 Install VS Code Extensions
- Open VS Code.
- Install the following extensions:
  - **Python** (Microsoft)
  - **SQLTools** (Matheus Teixeira)
  - **SQLTools PostgreSQL Driver**

### 2.3 Configure SQLTools to Connect to PostgreSQL
- Open VS Code.
- Open Command Palette (`Cmd + Shift + P`), search for `SQLTools: Manage Connections`.
- Click `Add New Connection` and choose **PostgreSQL**.
- Fill in the following details:
  - **Server**: `localhost`
  - **Port**: `5432`
  - **Database**: `mydatabase`
  - **Username**: `myuser`
  - **Password**: `mypassword`
- Click `Save`.
- Test the connection by clicking `Connect`.

---

## 3. Create a Sample Python App

### 3.1 Create `app.py`
Create a new file `app.py` inside your VS Code workspace and add the following code:

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL
DATABASE_URL = "postgresql://myuser:mypassword@localhost/mydatabase"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Define a sample table
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Create database schema
Base.metadata.create_all(engine)

# Insert a user
def insert_user():
    session = SessionLocal()
    new_user = User(name="Alice", email="alice@example.com")
    session.add(new_user)
    session.commit()
    session.close()
    print("User added!")

# Update a user
def update_user():
    session = SessionLocal()
    user = session.query(User).filter_by(name="Alice").first()
    if user:
        user.email = "alice@newdomain.com"
        session.commit()
        print("User updated!")
    session.close()

# Delete a user
def delete_user():
    session = SessionLocal()
    user = session.query(User).filter_by(name="Alice").first()
    if user:
        session.delete(user)
        session.commit()
        print("User deleted!")
    session.close()

if __name__ == "__main__":
    insert_user()
    update_user()
    delete_user()
```

### 3.2 Run the Python Script
```sh
python app.py
```
Expected output:
```
User added!
User updated!
User deleted!
```

---

## 4. Verify the Data in PostgreSQL
Open `psql` and run:
```sh
psql -U myuser -d mydatabase
```
Check if the table exists:
```sql
SELECT * FROM users;
```
Since the script inserts and deletes the user, the table should be empty.

---

## 5. Conclusion
You have successfully:
✅ Installed PostgreSQL and Python.
✅ Configured VS Code to connect to PostgreSQL.
✅ Created a sample Python app using SQLAlchemy.
✅ Executed database operations (insert, update, delete).

This setup allows you to build scalable Python applications with PostgreSQL easily! 🚀

