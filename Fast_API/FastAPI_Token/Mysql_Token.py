# ============================================================
# 🔐 FastAPI TODO App + JWT + MySQL (FIXED LOGIN)
# ============================================================
 
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import List
 
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session
 
# ============================================================
# 🚀 APP
# ============================================================
 
app = FastAPI()
 
# ============================================================
# 🔐 JWT CONFIG
# ============================================================
 
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(minutes=5)
 
# ============================================================
# 🗄️ MYSQL
# ============================================================
 
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/jwt_db"
 
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
 
Base = declarative_base()
 
# ============================================================
# 🧾 TODOS TABLE
# ============================================================
 
class TodoDB(Base):
    __tablename__ = "todos"
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    completed = Column(Boolean, default=False)
 
# ============================================================
# 👤 USERS TABLE (NEW)
# ============================================================
 
class UserDB(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True)
    password = Column(String(100))
 
# Create tables
Base.metadata.create_all(bind=engine)
 
# ============================================================
# 📌 MODELS
# ============================================================
 
class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False
 
class Login(BaseModel):
    username: str
    password: str
 
# ============================================================
# 🔐 AUTH
# ============================================================
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
# ============================================================
# 🔐 TOKEN
# ============================================================
 
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE
    to_encode.update({"exp": expire})
 
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
 
# ============================================================
# 🔐 VERIFY TOKEN
# ============================================================
 
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
 
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
 
        return username
 
    except JWTError:
        raise HTTPException(status_code=401, detail="Token expired or invalid")
 
# ============================================================
# 🏠 HOME
# ============================================================
 
@app.get("/")
def home():
    return {"message": "FastAPI JWT + MySQL CRUD API 🚀"}
 
# ============================================================
# 🔐 LOGIN (NOW FROM MYSQL ✅)
# ============================================================
 
@app.post("/login")
def login(user: Login, db: Session = Depends(get_db)):
 
    db_user = db.query(UserDB).filter(UserDB.username == user.username).first()
 
    if not db_user:
        raise HTTPException(status_code=401, detail="User not found")
 
    if db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")
 
    token = create_access_token({"sub": db_user.username})
 
    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_in": "5 minutes"
    }
 
# ============================================================
# ✅ CREATE TODO
# ============================================================
 
@app.post("/todos")
def create_todo(todo: Todo, user: str = Depends(verify_token), db: Session = Depends(get_db)):
 
    if db.query(TodoDB).filter(TodoDB.id == todo.id).first():
        raise HTTPException(status_code=400, detail="ID already exists")
 
    new_todo = TodoDB(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
 
    return {"message": "Todo created"}
 
# ============================================================
# ✅ GET ALL
# ============================================================
 
@app.get("/todos")
def get_all_todos(user: str = Depends(verify_token), db: Session = Depends(get_db)):
 
    todos = db.query(TodoDB).all()
 
    return {
        "count": len(todos),
        "data": todos
    }
 
# ============================================================
# ✅ GET ONE
# ============================================================
 
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, user: str = Depends(verify_token), db: Session = Depends(get_db)):
 
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
 
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
 
    return todo
 
# ============================================================
# ✅ UPDATE
# ============================================================
 
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: Todo, user: str = Depends(verify_token), db: Session = Depends(get_db)):
 
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
 
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
 
    todo.title = updated.title
    todo.completed = updated.completed
 
    db.commit()
 
    return {"message": "Updated"}
 
# ============================================================
# ✅ DELETE
# ============================================================
 
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, user: str = Depends(verify_token), db: Session = Depends(get_db)):
 
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
 
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
 
    db.delete(todo)
    db.commit()
 
    return {"message": "Deleted"}