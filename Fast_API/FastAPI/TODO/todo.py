# --------------------------------------------------------------------
# IMPORT LIBRARIES
# --------------------------------------------------------------------
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# --------------------------------------------------------------------
# CREATE APP
# --------------------------------------------------------------------
app = FastAPI()

# --------------------------------------------------------------------
# CREATE DATA MODEL(Schema)
# --------------------------------------------------------------------
class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False
# --------------------------------------------------------------------
# TEMPORARY DATABASE
# --------------------------------------------------------------------
todos_lst = []
# --------------------------------------------------------------------
# CRUD OPERATIONS
# --------------------------------------------------------------------
# 1. Create Todo(POST)
@app.post("/todos_lst")
def create_todo(todo: Todo):
    todos_lst.append(todo)
    return {"msg": "Todo created", "data": todo}
# --------------------------------------------------------------------
# Read All Todos(GET)
# --------------------------------------------------------------------
@app.get("/todos_lst")
def get_todos():
    return todos_lst
# --------------------------------------------------------------------
# Read Single Todo(GET by ID)
# --------------------------------------------------------------------
@app.get("/todos_lst/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos_lst:
        if todo.id==todo_id:
            return todo
    raise HTTPException(status_code=404,detail="Todo Not Found")

# --------------------------------------------------------------------
# UPDATE TODO 
# --------------------------------------------------------------------
@app.put("/todos_lst/{todo_id}")
def update_todo(todo_id:int,updated_todo=Todo):
    for index, todo in enumerate(todos_lst):
        if todo.id==todo_id:
            todo[index]=updated_todo
            return {"msg": "Updated Successfully", "data": updated_todo}
    raise HTTPException(status_code=404,detail="Todo not found")
# --------------------------------------------------------------------
# Delete Todo
# --------------------------------------------------------------------
@app.delete("/todos_lst")
def delete_todo():
    deleted=todos_lst.pop()
    return {"msg":"Deleted Successfully","data":deleted}
    return HTTPException(status_code=404,detail="Todo not found")
# --------------------------------------------------------------------
# Delete Todo
# --------------------------------------------------------------------
@app.delete("/todos_lst/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos_lst):
        if todo.id==todo_id:
            deleted=todos_lst.pop(index)
            return {"msg":"Deleted Successfully","data":deleted}
    return HTTPException(status_code=404,detail="Todo not found")