# ============================================================
# 📝 FastAPI Movie Ticket Booking System (CRUD) - MySQL Version
# FastAPI TODO App (CRUD) - SQLite Database Version
# ============================================================
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
# ------------------------------------------------------------
# 🚀 App
# ------------------------------------------------------------
app=FastAPI()

# ------------------------------------------------------------
# 🗄️ MySQL Configuration
# ------------------------------------------------------------
url="sqlite:///./app_sqlite.db"
engine=create_engine(
    url, connect_args={"check_same_thread":False}
)
sessionLocal=sessionmaker(bind=engine)
Base=declarative_base()

# ------------------------------------------------------------
# 🧱 Table Model
# ------------------------------------------------------------
class MoviesTable(Base):
    __tablename__="movies_table"
    movie_id = Column(Integer, primary_key=True, index=True)
    movie_name = Column(String(100))
    theater = Column(String(255))
    show_time = Column(String(100))
    available_seats = Column(Integer)

class BookingTable(Base):
    __tablename__ = "booking_table"
    booking_id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer)
    movie_name = Column(String(255))
    status = Column(String(100))

# Create table
Base.metadata.create_all(bind=engine)
# ------------------------------------------------------------
# 🧾 Schema (Pydantic)
# ------------------------------------------------------------
class MovieSchema(BaseModel):
    movie_id: int
    movie_name: str
    theater: str
    show_time: str
    available_seats: int
    model_config = ConfigDict(from_attributes=True)
# ------------------------------------------------------------
# DB Dependency
# ------------------------------------------------------------
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------------------------------------
# Home
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"msg":"FastAPI+SQLite"}

# ------------------------------------------------------------
# ✅ CREATE
# ------------------------------------------------------------
@app.post("/movies")
def createMovie(mve:MovieSchema,db:Session=Depends(get_db)):
    existing=db.query(MoviesTable).filter(MoviesTable.movie_id==mve.movie_id).first()
    if existing:
        raise HTTPException(status_code=400,detail="ID already existing")
    new_mtab=MoviesTable(
        movie_id = mve.movie_id,
        movie_name = mve.movie_name,
        theater=mve.theater,
        show_time=mve.show_time,
        available_seats=mve.available_seats
    )
    db.add(new_mtab)
    db.commit()
    db.refresh(new_mtab)
    return {"msg":"Created","data":new_mtab}
# ------------------------------------------------------------
# ✅ READ ALL
# ------------------------------------------------------------
@app.get("/movies")
def get_all_movies(db:Session=Depends(get_db)):
    movies=db.query(MoviesTable).all()
    return {"count":len(movies),"data":movies}
# ------------------------------------------------------------
# ✅ READ ONE
# ------------------------------------------------------------
@app.get("/movies/{movie_id}")
def get_by_id(movie_id: int, db: Session = Depends(get_db)):
    movie=db.query(MoviesTable).filter(MoviesTable.movie_id==movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Not found")
    return movie
# ------------------------------------------------------------
# ✅ UPDATE
# ------------------------------------------------------------
@app.put("/movies/{movie_id}")
def update(movie_id:int,updated: MovieSchema,db:Session=Depends(get_db)):
    movie=db.query(MoviesTable).filter(MoviesTable.movie_id==movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Not found")
    movie.movie_name = updated.movie_name
    movie.theater = updated.theater
    movie.show_time = updated.show_time
    movie.available_seats = updated.available_seats
    db.commit()
    db.refresh(movie)
    return {"message": "Updated", "data": movie}
# ------------------------------------------------------------
# ✅ DELETE
# ------------------------------------------------------------
@app.delete("/movies/{movie_id}")
def delete(movie_id:int,db: Session=Depends(get_db)):
    movie=db.query(MoviesTable).filter(MoviesTable.movie_id==movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(movie)
    db.commit()
    return {"message": "Deleted"}
# ------------------------------------------------------------
# ✅ POST 
# ------------------------------------------------------------
@app.post("/book-ticket/{id}")
def bookTicket(id:int,db:Session=Depends(get_db)):
    movie=db.query(MoviesTable).filter(id==MoviesTable.movie_id).first()
    if not movie:
        raise HTTPException(status_code=404,detail="Movie not found")
    if movie.available_seats<=0:
        raise HTTPException(status_code=400,detail="No seats available")
    movie.available_seats-=1
    new_booking_tab=BookingTable(
        movie_id=movie.movie_id,
        movie_name=movie.movie_name,
        status="Booked"
    )
    db.add(new_booking_tab)
    db.commit()
    db.refresh(new_booking_tab)
    return {"msg":"Booked Successfully","data":new_booking_tab}
# ------------------------------------------------------------
# ✅ POST 
# ------------------------------------------------------------
@app.post("/cancel-ticket/{id}")
def cancelTicket(id:int,db:Session=Depends(get_db)):
    booking=db.query(BookingTable).filter(BookingTable.booking_id==id).first()
    if not booking:
        raise HTTPException(status_code=404,detail="Booking not found")
    booking.status="Cancelled"
    movie=db.query(MoviesTable).filter(MoviesTable.movie_id==booking.movie_id).first()
    if movie:
        movie.available_seats+=1
    db.commit()
    return {"msg":"Cancelled Successfully","data":booking}
# -------------------------------------------------------------
# Get Available Shows
# -------------------------------------------------------------
@app.get("/available-shows")
def availableShows(db:Session=Depends(get_db)):
    movies=db.query(MoviesTable).filter(MoviesTable.available_seats>0).all()
    return movies
# -------------------------------------------------------------
# Get All Bookings
# -------------------------------------------------------------
@app.get("/bookings")
def getBookings(db:Session=Depends(get_db)):
    bookings=db.query(BookingTable).all()
    return bookings
# -------------------------------------------------------------
# Search Movie
# -------------------------------------------------------------
@app.get("/search-movie/{name}")
def search_movie(name: str, db: Session = Depends(get_db)):
    movies = db.query(MoviesTable).filter(MoviesTable.movie_name.ilike(f"%{name}%")).all()
    if not movies:
        raise HTTPException(status_code=404,detail="Movie not found")
    return movies