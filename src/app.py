from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection URL
USER = "mike"
PASSWORD = "mike"
DATABASE = "lyrics"
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@localhost/{DATABASE}"
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
