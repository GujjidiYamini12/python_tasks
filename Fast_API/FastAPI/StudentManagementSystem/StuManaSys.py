# =====================================================================
# IMPORT LIBRARY
# =====================================================================
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from typing import List
# =====================================================================
# Create App
# =====================================================================
app=FastAPI()
# =====================================================================
# Create Data Model(Scheme)
# =====================================================================
class Student(BaseModel):
    id:int
    name:str
    age:int
    course:str
    marks:int
# =====================================================================
# Temperory Database
# =====================================================================
lst=[]
# =====================================================================
# CRUD OPERATIONS
# =====================================================================
# 2. Create API – Add Student
@app.post("/students")
def create_post(stu: Student):
    lst.append(stu)
    return {"msg":"Student added successfully","data":stu}
# 3. Create API – Get All Students
@app.get("/students")
def get_all():
    return lst
# 4. Create API – Get Student By ID
@app.get("/students/{stu_id}")
def get_all(stu_id: int):
    for ide in lst:
        if ide.id==stu_id:
            return ide
    raise HTTPException(status_code=404,detail="Student with {stu_id} not found")
# 5. Create API – Update Student
@app.put("/students/{stu_id}")
def update_by_id(stu_id: int, updated_stu: Student):
    for index, stu in enumerate(lst):
        if stu.id==stu_id:
            lst[index]=updated_stu
            return {"msg":"Updated Successfully","data": updated_stu}
    raise HTTPException(status_code=404,detail="Student not found")
# 6. Create API – Delete Student
@app.delete("/students/{stu_id}")
def delete_by_id(stu_id:int):
    for index,stu in enumerate(lst):
        if stu.id==stu_id:
            delete_stu=lst.pop(index)
            return {"msg":"Student deleted successfully","data":delete_stu}
    raise HTTPException(status_code=404,detail="Student not found")