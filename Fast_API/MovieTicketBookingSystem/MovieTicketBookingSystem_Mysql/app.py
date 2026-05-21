# ============================================================
# 📝 FastAPI Movie Ticket Booking System (MySQL)
# ============================================================

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import Session, sessionmaker, declarative_base

# ------------------------------------------------------------
# 🚀 App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🗄️ MySQL Configuration
# ------------------------------------------------------------
url = "mysql+pymysql://root:root@localhost:3306/movie_booking_db"

engine = create_engine(url)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ------------------------------------------------------------
# 🧱 TABLE MODELS
# ------------------------------------------------------------

# 🎬 Movies Table
class MoviesTable(Base):
    __tablename__ = "movies_table"

    movie_id = Column(Integer, primary_key=True, index=True)
    movie_name = Column(String(100))
    theater_name = Column(String(100))
    show_time = Column(String(100))
    available_seats = Column(Integer)


# 👤 Users Table
class UserTable(Base):
    __tablename__ = "users_table"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(100))


# 🏢 Theater Table
class TheaterTable(Base):
    __tablename__ = "theater_table"

    theater_id = Column(Integer, primary_key=True, index=True)
    theater_name = Column(String(100))
    location = Column(String(100))


# 🎟️ Booking Table
class BookingTable(Base):
    __tablename__ = "booking_table"

    booking_id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users_table.user_id"))

    movie_id = Column(Integer, ForeignKey("movies_table.movie_id"))

    movie_name = Column(String(100))

    username = Column(String(100))

    status = Column(String(100))


# ------------------------------------------------------------
# CREATE TABLES
# ------------------------------------------------------------
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 SCHEMAS
# ------------------------------------------------------------

# Movie Schema
class MovieSchema(BaseModel):
    movie_id: int
    movie_name: str
    theater_name: str
    show_time: str
    available_seats: int

    model_config = ConfigDict(from_attributes=True)


# User Schema
class UserSchema(BaseModel):
    user_id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


# Theater Schema
class TheaterSchema(BaseModel):
    theater_id: int
    theater_name: str
    location: str

    model_config = ConfigDict(from_attributes=True)


# Booking Schema
class BookingSchema(BaseModel):
    user_id: int
    movie_id: int

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
# 🏠 HOME
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"msg": "FastAPI Movie Booking System"}

# ============================================================
# 👤 USER APIs
# ============================================================

# ------------------------------------------------------------
# ADD USER
# ------------------------------------------------------------
@app.post("/users")
def add_user(user: UserSchema, db: Session = Depends(get_db)):

    existing = db.query(UserTable).filter(
        UserTable.user_id == user.user_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = UserTable(
        user_id=user.user_id,
        username=user.username,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "User Created", "data": new_user}

# ------------------------------------------------------------
# GET USERS
# ------------------------------------------------------------
@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(UserTable).all()

    return users

# ============================================================
# 🏢 THEATER APIs
# ============================================================

# ------------------------------------------------------------
# ADD THEATER
# ------------------------------------------------------------
@app.post("/theaters")
def add_theater(th: TheaterSchema, db: Session = Depends(get_db)):

    theater = TheaterTable(
        theater_id=th.theater_id,
        theater_name=th.theater_name,
        location=th.location
    )

    db.add(theater)
    db.commit()
    db.refresh(theater)

    return {"msg": "Theater Added", "data": theater}

# ------------------------------------------------------------
# GET THEATERS
# ------------------------------------------------------------
@app.get("/theaters")
def get_theaters(db: Session = Depends(get_db)):

    theaters = db.query(TheaterTable).all()

    return theaters

# ============================================================
# 🎬 MOVIE APIs
# ============================================================

# ------------------------------------------------------------
# ADD MOVIE
# ------------------------------------------------------------
@app.post("/movies")
def create_movie(movie: MovieSchema, db: Session = Depends(get_db)):

    existing = db.query(MoviesTable).filter(
        MoviesTable.movie_id == movie.movie_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Movie ID already exists")

    new_movie = MoviesTable(
        movie_id=movie.movie_id,
        movie_name=movie.movie_name,
        theater_name=movie.theater_name,
        show_time=movie.show_time,
        available_seats=movie.available_seats
    )

    db.add(new_movie)

    db.commit()

    db.refresh(new_movie)

    return {"msg": "Movie Added", "data": new_movie}

# ------------------------------------------------------------
# GET ALL MOVIES
# ------------------------------------------------------------
@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):

    movies = db.query(MoviesTable).all()

    return {
        "count": len(movies),
        "data": movies
    }

# ------------------------------------------------------------
# GET MOVIE BY ID
# ------------------------------------------------------------
@app.get("/movies/{id}")
def get_movie(id: int, db: Session = Depends(get_db)):

    movie = db.query(MoviesTable).filter(
        MoviesTable.movie_id == id
    ).first()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    return movie

# ------------------------------------------------------------
# SEARCH MOVIE
# ------------------------------------------------------------
@app.get("/search-movie/{name}")
def search_movie(name: str, db: Session = Depends(get_db)):

    movies = db.query(MoviesTable).filter(
        MoviesTable.movie_name.ilike(f"%{name}%")
    ).all()

    if not movies:
        raise HTTPException(status_code=404, detail="Movie not found")

    return movies

# ------------------------------------------------------------
# AVAILABLE SHOWS
# ------------------------------------------------------------
@app.get("/available-shows")
def available_shows(db: Session = Depends(get_db)):

    movies = db.query(MoviesTable).filter(
        MoviesTable.available_seats > 0
    ).all()

    return movies

# ============================================================
# 🎟️ BOOKING APIs
# ============================================================

# ------------------------------------------------------------
# BOOK TICKET
# ------------------------------------------------------------
@app.post("/book-ticket")
def book_ticket(book: BookingSchema, db: Session = Depends(get_db)):

    user = db.query(UserTable).filter(
        UserTable.user_id == book.user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    movie = db.query(MoviesTable).filter(
        MoviesTable.movie_id == book.movie_id
    ).first()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    if movie.available_seats <= 0:
        raise HTTPException(status_code=400, detail="No seats available")

    # Reduce Seat
    movie.available_seats -= 1

    # Create Booking
    booking = BookingTable(
        user_id=user.user_id,
        movie_id=movie.movie_id,
        movie_name=movie.movie_name,
        username=user.username,
        status="Booked"
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return {
        "msg": "Ticket Booked",
        "data": booking
    }

# ------------------------------------------------------------
# CANCEL TICKET
# ------------------------------------------------------------
@app.post("/cancel-ticket/{id}")
def cancel_ticket(id: int, db: Session = Depends(get_db)):

    booking = db.query(BookingTable).filter(
        BookingTable.booking_id == id
    ).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    booking.status = "Cancelled"

    movie = db.query(MoviesTable).filter(
        MoviesTable.movie_id == booking.movie_id
    ).first()

    if movie:
        movie.available_seats += 1

    db.commit()

    return {
        "msg": "Ticket Cancelled",
        "data": booking
    }

# ------------------------------------------------------------
# GET BOOKINGS
# ------------------------------------------------------------
@app.get("/bookings")
def get_bookings(db: Session = Depends(get_db)):

    bookings = db.query(BookingTable).all()

    return bookings