# ============================================================
# 🔐 FastAPI TODO App + JWT Authentication (RAW JSON LOGIN)
# ============================================================

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import List

# ============================================================
# 🚀 CREATE FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🔐 JWT CONFIGURATION
# ============================================================

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(minutes=5)

# ============================================================
# 🧾 PYDANTIC MODELS
# ============================================================

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

# ------------------------------------------------------------

class Login(BaseModel):
    username: str
    password: str

# ============================================================
# 🗃️ TEMP DATABASE
# ============================================================

todos: List[Todo] = []

# ============================================================
# 🔐 OAUTH2 SCHEME
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ============================================================
# 🔐 CREATE ACCESS TOKEN
# ============================================================

def create_access_token(data: dict):

    # Copy data
    to_encode = data.copy()

    # Add expiry
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE

    to_encode.update({"exp": expire})

    # Generate token
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# ============================================================
# 🔐 VERIFY TOKEN
# ============================================================

def verify_token(token: str = Depends(oauth2_scheme)):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )

# ============================================================
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "FastAPI JWT CRUD API 🚀"
    }

# ============================================================
# 🔐 LOGIN API (RAW JSON)
# ============================================================

@app.post("/login")
def login(user: Login):

    # Dummy authentication
    if user.username != "admin" or user.password != "admin123":

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Create token
    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": "5 minutes"
    }

# ============================================================
# ✅ CREATE TODO
# ============================================================

@app.post("/todos")
def create_todo(
    todo: Todo,
    user: str = Depends(verify_token)
):

    # Check duplicate ID
    for existing in todos:

        if existing.id == todo.id:

            raise HTTPException(
                status_code=400,
                detail="ID already exists"
            )

    # Add todo
    todos.append(todo)

    return {
        "message": "Todo created successfully",
        "data": todo
    }

# ============================================================
# ✅ GET ALL TODOS
# ============================================================

@app.get("/todos")
def get_all_todos(
    user: str = Depends(verify_token)
):

    return {
        "count": len(todos),
        "data": todos
    }

# ============================================================
# ✅ GET SINGLE TODO
# ============================================================

@app.get("/todos/{todo_id}")
def get_todo(
    todo_id: int,
    user: str = Depends(verify_token)
):

    for todo in todos:

        if todo.id == todo_id:

            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

# ============================================================
# ✅ UPDATE TODO
# ============================================================

@app.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    updated: Todo,
    user: str = Depends(verify_token)
):

    for index, todo in enumerate(todos):

        if todo.id == todo_id:

            todos[index] = updated

            return {
                "message": "Todo updated successfully",
                "data": updated
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

# ============================================================
# ✅ DELETE TODO
# ============================================================

@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    user: str = Depends(verify_token)
):

    for index, todo in enumerate(todos):

        if todo.id == todo_id:

            deleted = todos.pop(index)

            return {
                "message": "Todo deleted successfully",
                "data": deleted
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

# ============================================================
# 🌐 RUN SERVER
# ============================================================

'''
uvicorn Todo_Token:app --reload
'''

# ============================================================
# 🌐 SWAGGER UI
# ============================================================

'''
http://127.0.0.1:8000/docs
'''
