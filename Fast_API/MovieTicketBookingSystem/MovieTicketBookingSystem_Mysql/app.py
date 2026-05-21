# ============================================================
# 🎬 Movie Ticket Booking System (Normalized DB Design)
# ============================================================

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from datetime import datetime

# ------------------------------------------------------------
# 🚀 App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🗄️ DB CONNECTION
# ------------------------------------------------------------
url = "mysql+pymysql://root:root@localhost:3306/movie_booking_db"

engine = create_engine(url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ============================================================
# 🧱 TABLES
# ============================================================

# 👤 USERS
class UserTable(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(100))


# 🎬 MOVIES
class MovieTable(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True, index=True)
    movie_name = Column(String(100))
    genre = Column(String(100))
    rating = Column(String(10))
    duration = Column(String(50))


# 🏢 THEATERS
class TheaterTable(Base):
    __tablename__ = "theaters"

    theater_id = Column(Integer, primary_key=True, index=True)
    theater_name = Column(String(100))
    location = Column(String(100))


# 🎥 SHOWS
class ShowTable(Base):
    __tablename__ = "shows"

    show_id = Column(Integer, primary_key=True, index=True)

    movie_id = Column(Integer, ForeignKey("movies.movie_id"))

    theater_id = Column(Integer, ForeignKey("theaters.theater_id"))

    show_time = Column(String(50))

    show_type = Column(String(50))   # Morning / Afternoon / Evening

    ticket_price = Column(Integer)

    available_seats = Column(Integer)


# 🎟️ BOOKINGS
class BookingTable(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.user_id"))

    show_id = Column(Integer, ForeignKey("shows.show_id"))

    status = Column(String(50))  # Booked / Cancelled

    booking_date = Column(String(50))


# 💳 PAYMENTS
class PaymentTable(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(Integer, ForeignKey("bookings.booking_id"))

    amount = Column(Integer)

    method = Column(String(50))  # UPI / Card / Cash

    status = Column(String(50))  # Paid / Failed

    payment_date = Column(String(50))


# ⭐ REVIEWS
class ReviewTable(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.user_id"))

    movie_id = Column(Integer, ForeignKey("movies.movie_id"))

    rating = Column(String(10))

    review = Column(String(255))


# ------------------------------------------------------------
# CREATE TABLES
# ------------------------------------------------------------
Base.metadata.create_all(bind=engine)

# ============================================================
# 🧾 SCHEMAS
# ============================================================

class UserSchema(BaseModel):
    user_id: int
    username: str
    email: str


class MovieSchema(BaseModel):
    movie_id: int
    movie_name: str
    genre: str
    rating: str
    duration: str


class TheaterSchema(BaseModel):
    theater_id: int
    theater_name: str
    location: str


class ShowSchema(BaseModel):
    movie_id: int
    theater_id: int
    show_time: str
    show_type: str
    ticket_price: int
    available_seats: int


class BookingSchema(BaseModel):
    user_id: int
    show_id: int


class PaymentSchema(BaseModel):
    booking_id: int
    amount: int
    method: str


class ReviewSchema(BaseModel):
    user_id: int
    movie_id: int
    rating: str
    review: str


# ============================================================
# DB DEPENDENCY
# ============================================================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============================================================
# 🏠 HOME
# ============================================================

@app.get("/")
def home():
    return {"msg": "Movie Ticket Booking System - Normalized DB"}

# ============================================================
# 👤 USERS
# ============================================================

@app.post("/users")
def add_user(user: UserSchema, db: Session = Depends(get_db)):

    db.add(UserTable(**user.dict()))
    db.commit()
    return {"msg": "User created"}


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(UserTable).all()

# ============================================================
# 🎬 MOVIES
# ============================================================

@app.post("/movies")
def add_movie(movie: MovieSchema, db: Session = Depends(get_db)):

    db.add(MovieTable(**movie.dict()))
    db.commit()
    return {"msg": "Movie added"}


@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(MovieTable).all()

# ============================================================
# 🏢 THEATERS
# ============================================================

@app.post("/theaters")
def add_theater(th: TheaterSchema, db: Session = Depends(get_db)):

    db.add(TheaterTable(**th.dict()))
    db.commit()
    return {"msg": "Theater added"}


@app.get("/theaters")
def get_theaters(db: Session = Depends(get_db)):
    return db.query(TheaterTable).all()

# ============================================================
# 🎥 SHOWS
# ============================================================

@app.post("/shows")
def add_show(show: ShowSchema, db: Session = Depends(get_db)):

    db.add(ShowTable(**show.dict()))
    db.commit()
    return {"msg": "Show created"}


@app.get("/shows")
def get_shows(db: Session = Depends(get_db)):
    return db.query(ShowTable).all()

# ============================================================
# 🎟️ BOOKINGS
# ============================================================

@app.post("/bookings")
def book_ticket(book: BookingSchema, db: Session = Depends(get_db)):

    booking = BookingTable(
        user_id=book.user_id,
        show_id=book.show_id,
        status="Booked",
        booking_date=str(datetime.now())
    )

    db.add(booking)
    db.commit()
    return {"msg": "Ticket booked"}


@app.get("/bookings")
def get_bookings(db: Session = Depends(get_db)):
    return db.query(BookingTable).all()

# ============================================================
# 💳 PAYMENTS
# ============================================================

@app.post("/payments")
def make_payment(pay: PaymentSchema, db: Session = Depends(get_db)):

    payment = PaymentTable(
        booking_id=pay.booking_id,
        amount=pay.amount,
        method=pay.method,
        status="Paid",
        payment_date=str(datetime.now())
    )

    db.add(payment)
    db.commit()
    return {"msg": "Payment successful"}


@app.get("/payments")
def get_payments(db: Session = Depends(get_db)):
    return db.query(PaymentTable).all()

# ============================================================
# ⭐ REVIEWS
# ============================================================

@app.post("/reviews")
def add_review(rv: ReviewSchema, db: Session = Depends(get_db)):

    db.add(ReviewTable(**rv.dict()))
    db.commit()
    return {"msg": "Review added"}


@app.get("/reviews")
def get_reviews(db: Session = Depends(get_db)):
    return db.query(ReviewTable).all()