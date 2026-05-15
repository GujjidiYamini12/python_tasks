# ============================================================
# 📝 FastAPI TODO App - MongoDB Atlas + MongoEngine
# pip install fastapi uvicorn mongoengine pymongo
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import connect, Document, IntField, StringField, BooleanField

# ------------------------------------------------------------
# Create FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------
MONGO_URL = "mongodb+srv://yaminigujjidi_db_user:.5w_8ZbPY58kW9j@cluster0.5dfjgav.mongodb.net/student_db?appName=Cluster0&retryWrites=true&w=majority"
'''
mongodb+srv://username:password@clustername.xxxxx.mongodb.net/todo_db?retryWrites=true&w=majority
│              │        │        │                              │
│              │        │        │                              └── Database name
│              │        │        └──────────────────────────────── Cluster URL
│              │        └───────────────────────────────────────── Password
│              └────────────────────────────────────────────────── Username
└───────────────────────────────────────────────────────────────── MongoDB protocol
'''
connect(
    host=MONGO_URL,
    tls=True,
    tlsAllowInvalidCertificates=True
)

# ------------------------------------------------------------
# MongoDB Model (Like SQLAlchemy Model)
# ------------------------------------------------------------
class studentDB(Document):
    __tablename__="Student"
    stud_id = IntField(required=True, unique=True)
    name = StringField(required=True)
    age = IntField(required=True)
    course = StringField(required=True)
    marks = IntField(required=True)
    

    # Create table
    meta = {
            "collection": "students"
        }

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Student(BaseModel):
    stud_id:int
    name:str
    age:int
    course:str
    marks:int

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "FastAPI + MongoDB Atlas 🚀"}
# ------------------------------------------------------------
# ✅ 1. CREATE TODO
# ------------------------------------------------------------
@app.post("/student")
def create_student(stu: Student):

     # Check duplicate ID
    existing = studentDB.objects(stud_id=stu.stud_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="ID already exists")

    new_stu = studentDB(
        stud_id=stu.stud_id,
        name=stu.name,
        age=stu.age,
        course=stu.course,
        marks=stu.marks
    )

    new_stu.save()

    return {"message": "Student created", "data": new_stu}

# ------------------------------------------------------------
# ✅ 2. READ ALL TODOS
# ------------------------------------------------------------
@app.get("/student")
def get_all_studs():
    stud = studentDB.objects()
    data = []

    for stu in stud:
        data.append({
            "id": stu.stud_id,
            "name":stu.name,
            "age":stu.age,
            "course":stu.course,
            "marks":stu.marks
        })
    return {"count": len(stud), "data": stud}

# ------------------------------------------------------------
# ✅ 3. READ SINGLE TODO
# ------------------------------------------------------------
@app.get("/student/{stu_id}")
def get_todo(stu_id: int):
    stud = studentDB.objects(stud_id=stu_id.stud_id).first()

    if not stud:
        raise HTTPException(status_code=404, detail="Student not found")

    return stud

# ------------------------------------------------------------
# ✅ 4. UPDATE TODO
# ------------------------------------------------------------
@app.put("/student/{stu_id}")
def update_todo(stu_id: int, updated: Student):
    stud = studentDB.objects(stud_id=stu_id.stud_id).first()

    if not stud:
        raise HTTPException(status_code=404, detail="Student not found")

    stud.name = updated.name
    stud.age = updated.age
    stud.course = updated.course
    stud.marks = updated.marks

    stud.save()

    return {"message": "Updated successfully", "data": stud}

# ------------------------------------------------------------
# ✅ 5. DELETE TODO
# ------------------------------------------------------------
@app.delete("/student/{stu_id}")
def delete_todo(stu_id: int):
    stud = studentDB.objects(stud_id=stu_id.stud_id).first()

    if not stud:
        raise HTTPException(status_code=404, detail="Student not found")

    stud.delete()

    return {"message": "Deleted successfully"}