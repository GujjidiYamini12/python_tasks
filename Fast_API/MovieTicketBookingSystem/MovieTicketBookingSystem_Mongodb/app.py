# ============================================================
# 📝 FastAPI Movie Ticket Booking System (CRUD) - MongoDB Atlas + MongoEngine
# pip install fastapi uvicorn mongoengine pymongo
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import connect, Document, IntField, StringField, BooleanField

# ------------------------------------------------------------
# 🚀 App
# ------------------------------------------------------------
app=FastAPI()

# ------------------------------------------------------------
# 🗄️ MySQL Configuration
# ------------------------------------------------------------
url="mongodb+srv://yaminigujjidi_db_user:.5w_8ZbPY58kW9j@cluster0.5dfjgav.mongodb.net/movie_db?appName=Cluster0&retryWrites=true&w=majority"
connect(host=url)

# ------------------------------------------------------------
# 🧱 Table Model
# ------------------------------------------------------------
class MoviesTable(Document):
    movie_id = IntField(primary_key=True, index=True)
    movie_name = StringField(required=True)
    theater = StringField(required=True)
    show_time = StringField(required=True)
    available_seats = IntField(required=True)
    meta = {
        "collection": "Movies"
    }

class BookingTable(Document):
    booking_id = IntField(primary_key=True, index=True)
    movie_id = IntField(required=True)
    movie_name = StringField(required=True)
    status = StringField(required=True)
    meta = {
        "collection": "Booking"
    }

# ------------------------------------------------------------
# 🧾 Schema (Pydantic)
# ------------------------------------------------------------
class MovieSchema(BaseModel):
    movie_id: int
    movie_name: str
    theater: str
    show_time: str
    available_seats: int
# ------------------------------------------------------------
# Home
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"msg":"FastAPI + MongoDB Atlas 🚀"}

# ------------------------------------------------------------
# ✅ CREATE
# ------------------------------------------------------------
@app.post("/movies")
def createMovie(mve:MovieSchema):
    existing=MoviesTable.objects(movie_id=mve.movie_id).first()
    if existing:
        raise HTTPException(status_code=400,detail="ID already existing")
    new_mtab=MoviesTable(
        movie_id = mve.movie_id,
        movie_name = mve.movie_name,
        theater=mve.theater,
        show_time=mve.show_time,
        available_seats=mve.available_seats
    )
    new_mtab.save()
    return {"msg":"Created",
            "data":{
                "movie_id": new_mtab.movie_id,
                "movie_name": new_mtab.movie_name,
                "theater": new_mtab.theater,
                "show_time": new_mtab.show_time,
                "available_seats": new_mtab.available_seats
            }
            
        }
# ------------------------------------------------------------
# ✅ READ ALL
# ------------------------------------------------------------
@app.get("/movies")
def get_all_movies():
    movies=MoviesTable.objects()
    data=[]
    for movie in movies:
        data.append({
            "movie_id" : movie.movie_id,
            "movie_name" : movie.movie_name,
            "theater" : movie.theater,
            "show_time" : movie.show_time,
            "available_seats" : movie.available_seats
        })
    return {"count":len(movies),"data":data}
# ------------------------------------------------------------
# ✅ READ ONE
# ------------------------------------------------------------
@app.get("/movies/{movie_id}")
def get_by_id(movie_id: int):
    movie=MoviesTable.objects(movie_id=movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Not found")
    return {"msg":"Created",
            "data":{
                "movie_id": movie.movie_id,
                "movie_name": movie.movie_name,
                "theater": movie.theater,
                "show_time": movie.show_time,
                "available_seats": movie.available_seats
            }
        }
# ------------------------------------------------------------
# ✅ UPDATE
# ------------------------------------------------------------
@app.put("/movies/{movie_id}")
def update(movie_id:int,updated: MovieSchema):
    movie=MoviesTable.objects(movie_id=movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Not found")
    movie.movie_name = updated.movie_name
    movie.theater = updated.theater
    movie.show_time = updated.show_time
    movie.available_seats = updated.available_seats
    movie.save()
    return {"message": "Updated", 
            "data": {
                "movie_id": movie.movie_id,
                "movie_name": movie.movie_name,
                "theater": movie.theater,
                "show_time": movie.show_time,
                "available_seats": movie.available_seats
            }
            }
# ------------------------------------------------------------
# ✅ DELETE
# ------------------------------------------------------------
@app.delete("/movies/{movie_id}")
def delete(movie_id:int):
    movie=MoviesTable.objects(movie_id=movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Not found")
    movie.delete()
    return {"message": "Deleted"}
# ------------------------------------------------------------
# ✅ POST 
# ------------------------------------------------------------
@app.post("/book-ticket/{id}")
def bookTicket(id:int):
    movie=MoviesTable.objects(movie_id=id).first()
    if not movie:
        raise HTTPException(status_code=404,detail="Movie not found")
    if movie.available_seats<=0:
        raise HTTPException(status_code=400,detail="No seats available")
    movie.available_seats-=1
    movie.save()
    new_booking_tab=BookingTable(
        booking_id=id,
        movie_id=movie.movie_id,
        movie_name=movie.movie_name,
        status="Booked"
    )
    new_booking_tab.save()
    return {"msg":"Booked Successfully",
            "data":{
                "booking_id": new_booking_tab.booking_id,
                "movie_id": new_booking_tab.movie_id,
                "movie_name": new_booking_tab.movie_name,
                "status": new_booking_tab.status
            }}
# ------------------------------------------------------------
# ✅ POST 
# ------------------------------------------------------------
@app.post("/cancel-ticket/{id}")
def cancelTicket(id:int):
    booking=BookingTable.objects(booking_id=id).first()
    if not booking:
        raise HTTPException(status_code=404,detail="Booking not found")
    booking.status="Cancelled"
    movie=MoviesTable.objects(movie_id=booking.movie_id).first()
    if movie:
        movie.available_seats+=1
    booking.save()
    movie.save()
    return {"msg":"Cancelled Successfully",
            "data":{
                "booking_id": booking.booking_id,
                "movie_id": booking.movie_id,
                "movie_name": booking.movie_name,
                "status": booking.status
            }}
# -------------------------------------------------------------
# Get Available Shows
# -------------------------------------------------------------
@app.get("/available-shows")
def availableShows():
    movies=MoviesTable.objects(
        available_seats__gt=0
        ).all()
    data=[]
    for movie in movies:
        data.append({
            "movie_id" : movie.movie_id,
            "movie_name" : movie.movie_name,
            "theater" : movie.theater,
            "show_time" : movie.show_time,
            "available_seats" : movie.available_seats
        })
    return {"count": len(data), 
            "data": data
            }
# -------------------------------------------------------------
# Get All Bookings
# -------------------------------------------------------------
@app.get("/bookings")
def getBookings():
    bookings=BookingTable.objects()
    data=[]
    for booking in bookings:
        data.append({
            "booking_id": booking.booking_id,
            "movie_id": booking.movie_id,
            "movie_name": booking.movie_name,
            "status": booking.status
        })
    return {"count":len(data),
            "data":data}
# -------------------------------------------------------------
# Search Movie
# -------------------------------------------------------------
@app.get("/search-movie/{name}")
def search_movie(name: str):
    movies = MoviesTable.objects(movie_name__icontains=name)
    if not movies:
        raise HTTPException(status_code=404,detail="Movie not found")
    data=[]
    for movie in movies:
        data.append({
            "movie_id" : movie.movie_id,
            "movie_name" : movie.movie_name,
            "theater" : movie.theater,
            "show_time" : movie.show_time,
            "available_seats" : movie.available_seats
        })
    return {"count": len(data), 
            "data": data
            }