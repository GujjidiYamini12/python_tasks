import os
from io import BytesIO
from datetime import datetime
from functools import wraps
from datetime import timedelta
from uuid import uuid4

import qrcode
from flask import Flask, abort, flash, redirect, render_template, request, send_file, session, url_for
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DataError
from sqlalchemy import func
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-this-in-production")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:root@localhost:3306/movie_booking_db",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

APP_NAME = "CineOrbit"
SUPPORTED_CITIES = ["Hyderabad", "Bengaluru", "Chennai"]
FIXED_TIME_OPTIONS = [
    ("10:00", "10:00 AM"),
    ("13:00", "1:00 PM"),
    ("16:00", "4:00 PM"),
    ("19:00", "7:00 PM"),
    ("22:00", "10:00 PM"),
    ("01:00", "1:00 AM"),
]
FIXED_TIME_VALUES = {item[0] for item in FIXED_TIME_OPTIONS}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    bookings = db.relationship("Booking", backref="user", lazy=True)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    genre = db.Column(db.String(120), nullable=False)
    duration_mins = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(80), nullable=False)
    actors = db.Column(db.String(255), nullable=False, default="")
    poster_url = db.Column(db.Text, nullable=False, default="")
    rating = db.Column(db.Float, nullable=False, default=0.0)
    shows = db.relationship("Show", backref="movie", lazy=True, cascade="all, delete")


class Theater(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    shows = db.relationship("Show", backref="theater", lazy=True)


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    theater_id = db.Column(db.Integer, db.ForeignKey("theater.id"), nullable=False)
    screen_no = db.Column(db.Integer, nullable=False, default=1)
    show_slot = db.Column(db.String(30), nullable=False, default="Morning")
    is_ac = db.Column(db.Boolean, default=True)
    show_time = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    bookings = db.relationship("Booking", backref="show", lazy=True)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey("show.id"), nullable=False)
    seats_booked = db.Column(db.Integer, nullable=False)
    seat_numbers = db.Column(db.String(255), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False, default="Card")
    payment_ref = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Booked")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class SeatHold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey("show.id"), nullable=False)
    seat_numbers = db.Column(db.String(255), nullable=False)
    hold_token = db.Column(db.String(64), unique=True, nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def current_user():
    user_id = session.get("user_id")
    if not user_id:
        return None
    return db.session.get(User, user_id)


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login first.", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        user = current_user()
        if not user or not user.is_admin:
            flash("Admin access required.", "danger")
            return redirect(url_for("index"))
        return view(*args, **kwargs)

    return wrapped


@app.context_processor
def inject_user():
    return {
        "logged_user": current_user(),
        "app_name": APP_NAME,
        "fixed_time_options": FIXED_TIME_OPTIONS,
    }


@app.template_filter("duration_hm")
def duration_hm(minutes):
    hours = int(minutes) // 60
    mins = int(minutes) % 60
    return f"{hours}h {mins}m"


def generate_all_seat_labels(total_seats, per_row=10):
    labels = []
    for index in range(total_seats):
        row = chr(65 + (index // per_row))
        seat_no = (index % per_row) + 1
        labels.append(f"{row}{seat_no}")
    return labels


def get_booked_seat_set(show):
    booked = set()
    active_bookings = Booking.query.filter_by(show_id=show.id, status="Booked").all()
    for booking in active_bookings:
        booked.update([seat.strip() for seat in booking.seat_numbers.split(",") if seat.strip()])
    return booked


def cleanup_expired_holds():
    now = datetime.utcnow()
    expired_holds = SeatHold.query.filter(
        SeatHold.is_active == True, SeatHold.expires_at < now
    ).all()
    changed = False
    for hold in expired_holds:
        hold.is_active = False
        changed = True
    if changed:
        db.session.commit()


def get_active_held_seats(show_id, ignore_token=None):
    now = datetime.utcnow()
    held = set()
    holds_query = SeatHold.query.filter(
        SeatHold.show_id == show_id,
        SeatHold.is_active == True,
        SeatHold.expires_at >= now,
    )
    if ignore_token:
        holds_query = holds_query.filter(SeatHold.hold_token != ignore_token)

    for hold in holds_query.all():
        held.update([seat.strip() for seat in hold.seat_numbers.split(",") if seat.strip()])
    return held


def parse_fixed_show_datetime(show_date_str, show_time_str):
    if show_time_str not in FIXED_TIME_VALUES:
        return None
    return datetime.strptime(f"{show_date_str} {show_time_str}", "%Y-%m-%d %H:%M")


@app.route("/")
def index():
    city_cards = []
    for city in SUPPORTED_CITIES:
        theater_count = Theater.query.filter(func.lower(Theater.city) == city.lower()).count()
        city_cards.append({"name": city, "theater_count": theater_count})
    return render_template("index.html", city_cards=city_cards)


@app.route("/cities/<string:city_name>/theaters")
def city_theaters(city_name):
    search = request.args.get("q", "").strip()
    city_title = city_name.title()
    theater_query = Theater.query.filter(func.lower(Theater.city) == city_name.lower())
    if search:
        theater_query = theater_query.filter(Theater.name.ilike(f"%{search}%"))
    theaters = theater_query.order_by(Theater.name.asc()).all()
    return render_template(
        "city_theaters.html", city_name=city_title, theaters=theaters, search=search
    )


@app.route("/theaters/<int:theater_id>/movies")
def theater_movies(theater_id):
    cleanup_expired_holds()
    theater = db.session.get(Theater, theater_id)
    if not theater:
        flash("Theater not found.", "danger")
        return redirect(url_for("index"))
    shows = (
        Show.query.filter_by(theater_id=theater.id)
        .order_by(Show.movie_id.asc(), Show.show_time.asc())
        .all()
    )
    effective_availability = {}
    for show in shows:
        active_holds = len(get_active_held_seats(show.id))
        effective_availability[show.id] = max(show.available_seats - active_holds, 0)
    return render_template(
        "theater_movies.html",
        theater=theater,
        shows=shows,
        effective_availability=effective_availability,
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        if not name or not email or not password:
            flash("All fields are required.", "danger")
            return redirect(url_for("register"))

        if User.query.filter_by(email=email).first():
            flash("Email already exists.", "danger")
            return redirect(url_for("register"))

        user = User(name=name, email=email, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Login now.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash("Invalid credentials.", "danger")
            return redirect(url_for("login"))

        session["user_id"] = user.id
        flash("Logged in successfully.", "success")
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("index"))


@app.route("/select-seats/<int:show_id>")
@login_required
def select_seats(show_id):
    cleanup_expired_holds()
    show = db.session.get(Show, show_id)
    if not show:
        flash("Show not found.", "danger")
        return redirect(url_for("index"))

    all_seats = generate_all_seat_labels(show.total_seats)
    booked_seats = get_booked_seat_set(show)
    held_seats = get_active_held_seats(show.id)
    unavailable = booked_seats.union(held_seats)
    available_seats = [seat for seat in all_seats if seat not in unavailable]
    return render_template(
        "select_seats.html",
        show=show,
        available_seats=available_seats,
        booked_seats=unavailable,
    )


@app.route("/hold-seats/<int:show_id>", methods=["POST"])
@login_required
def hold_seats(show_id):
    cleanup_expired_holds()
    show = db.session.get(Show, show_id)
    if not show:
        flash("Show not found.", "danger")
        return redirect(url_for("index"))

    selected_seats = request.form.getlist("selected_seats")
    if not selected_seats:
        flash("Please select seats first.", "danger")
        return redirect(url_for("select_seats", show_id=show_id))

    selected_seats = sorted(set([seat.strip() for seat in selected_seats if seat.strip()]))
    if not selected_seats:
        flash("Invalid seat selection.", "danger")
        return redirect(url_for("select_seats", show_id=show_id))

    all_valid = set(generate_all_seat_labels(show.total_seats))
    if any(seat not in all_valid for seat in selected_seats):
        flash("Invalid seat number selected.", "danger")
        return redirect(url_for("select_seats", show_id=show_id))

    booked_seats = get_booked_seat_set(show)
    held_seats = get_active_held_seats(show.id)
    unavailable = booked_seats.union(held_seats)
    if any(seat in unavailable for seat in selected_seats):
        flash("Some selected seats were just booked by someone else. Please try again.", "warning")
        return redirect(url_for("select_seats", show_id=show_id))

    seats_booked = len(selected_seats)
    if show.available_seats < seats_booked or (show.available_seats - len(held_seats)) < seats_booked:
        flash("Not enough seats available.", "danger")
        return redirect(url_for("select_seats", show_id=show_id))

    # Keep one active hold per user per show.
    previous_holds = SeatHold.query.filter(
        SeatHold.user_id == session["user_id"],
        SeatHold.show_id == show.id,
        SeatHold.is_active == True,
    ).all()
    for hold in previous_holds:
        hold.is_active = False

    hold_token = uuid4().hex
    hold = SeatHold(
        user_id=session["user_id"],
        show_id=show.id,
        seat_numbers=",".join(selected_seats),
        hold_token=hold_token,
        expires_at=datetime.utcnow() + timedelta(minutes=3),
        is_active=True,
    )
    db.session.add(hold)
    db.session.commit()
    return redirect(url_for("payment_page", hold_token=hold_token))


@app.route("/payment/<string:hold_token>")
@login_required
def payment_page(hold_token):
    cleanup_expired_holds()
    hold = SeatHold.query.filter_by(
        hold_token=hold_token, user_id=session["user_id"], is_active=True
    ).first()
    if not hold:
        flash("Seat hold not found. Please reselect seats.", "warning")
        return redirect(url_for("index"))

    if hold.expires_at < datetime.utcnow():
        flash("Seat hold expired. Please reselect seats.", "warning")
        return redirect(url_for("select_seats", show_id=hold.show_id))

    show = db.session.get(Show, hold.show_id)
    remaining_seconds = int((hold.expires_at - datetime.utcnow()).total_seconds())
    if remaining_seconds < 1:
        hold.is_active = False
        db.session.commit()
        flash("Seat hold expired. Please reselect seats.", "warning")
        return redirect(url_for("select_seats", show_id=show.id))

    seat_numbers = [seat for seat in hold.seat_numbers.split(",") if seat]
    return render_template(
        "payment.html",
        show=show,
        hold=hold,
        seat_numbers=seat_numbers,
        seat_count=len(seat_numbers),
        total_amount=len(seat_numbers) * show.price,
        remaining_seconds=remaining_seconds,
    )


@app.route("/payment/<string:hold_token>/confirm", methods=["POST"])
@login_required
def confirm_payment(hold_token):
    cleanup_expired_holds()
    hold = SeatHold.query.filter_by(
        hold_token=hold_token, user_id=session["user_id"], is_active=True
    ).first()
    if not hold or hold.expires_at < datetime.utcnow():
        flash("Seat hold expired. Please reselect seats.", "warning")
        return redirect(url_for("index"))

    show = db.session.get(Show, hold.show_id)
    selected_seats = [seat for seat in hold.seat_numbers.split(",") if seat]
    held_others = get_active_held_seats(show.id, ignore_token=hold_token)
    booked_seats = get_booked_seat_set(show)
    if any(seat in booked_seats or seat in held_others for seat in selected_seats):
        hold.is_active = False
        db.session.commit()
        flash("Seat conflict occurred. Please select seats again.", "danger")
        return redirect(url_for("select_seats", show_id=show.id))

    payment_method = request.form.get("payment_method", "Card").strip()
    card_name = request.form.get("card_name", "").strip()
    card_number = request.form.get("card_number", "").replace(" ", "")
    expiry = request.form.get("expiry", "").strip()
    cvv = request.form.get("cvv", "").strip()
    upi_id = request.form.get("upi_id", "").strip()
    bank_name = request.form.get("bank_name", "").strip()
    wallet_provider = request.form.get("wallet_provider", "").strip()

    valid_methods = {"Card", "UPI", "NetBanking", "Wallet"}
    if payment_method not in valid_methods:
        flash("Invalid payment method.", "danger")
        return redirect(url_for("payment_page", hold_token=hold_token))

    if payment_method == "Card":
        if not card_name or not card_number or not expiry or not cvv:
            flash("Card details are required.", "danger")
            return redirect(url_for("payment_page", hold_token=hold_token))
        if not card_number.isdigit() or len(card_number) < 12:
            flash("Payment failed: invalid card number.", "danger")
            return redirect(url_for("payment_page", hold_token=hold_token))
        if not cvv.isdigit() or len(cvv) not in [3, 4]:
            flash("Payment failed: invalid CVV.", "danger")
            return redirect(url_for("payment_page", hold_token=hold_token))
    elif payment_method == "UPI":
        if "@" not in upi_id or len(upi_id) < 5:
            flash("Payment failed: invalid UPI ID.", "danger")
            return redirect(url_for("payment_page", hold_token=hold_token))
    elif payment_method == "NetBanking":
        if not bank_name:
            flash("Please choose a bank for net banking.", "danger")
            return redirect(url_for("payment_page", hold_token=hold_token))
    elif payment_method == "Wallet":
        if not wallet_provider:
            flash("Please choose a wallet provider.", "danger")
            return redirect(url_for("payment_page", hold_token=hold_token))

    seats_booked = len(selected_seats)
    if show.available_seats < seats_booked:
        hold.is_active = False
        db.session.commit()
        flash("Seats are no longer available.", "danger")
        return redirect(url_for("select_seats", show_id=show.id))

    total_amount = seats_booked * show.price
    payment_ref = f"PAY-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{uuid4().hex[:6].upper()}"
    booking = Booking(
        user_id=session["user_id"],
        show_id=show.id,
        seats_booked=seats_booked,
        seat_numbers=",".join(selected_seats),
        total_amount=total_amount,
        payment_method=payment_method,
        payment_ref=payment_ref,
        status="Booked",
    )

    show.available_seats -= seats_booked
    hold.is_active = False
    db.session.add(booking)
    db.session.commit()
    flash(f"Payment successful. Booking confirmed ({payment_ref}).", "success")
    return redirect(url_for("my_bookings"))


@app.route("/my-bookings")
@login_required
def my_bookings():
    bookings = (
        Booking.query.filter_by(user_id=session["user_id"])
        .order_by(Booking.created_at.desc())
        .all()
    )
    return render_template("my_bookings.html", bookings=bookings)


@app.route("/cancel-booking/<int:booking_id>", methods=["POST"])
@login_required
def cancel_booking(booking_id):
    booking = Booking.query.filter_by(id=booking_id, user_id=session["user_id"]).first()
    if not booking:
        flash("Booking not found.", "danger")
        return redirect(url_for("my_bookings"))

    if booking.status == "Cancelled":
        flash("Booking already cancelled.", "warning")
        return redirect(url_for("my_bookings"))

    booking.status = "Cancelled"
    booking.show.available_seats += booking.seats_booked
    db.session.commit()
    flash("Booking cancelled.", "success")
    return redirect(url_for("my_bookings"))


@app.route("/ticket/<int:booking_id>/qr")
@login_required
def ticket_qr(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    user = current_user()
    if not user.is_admin and booking.user_id != user.id:
        abort(403)

    payload = (
        f"BookingID:{booking.id}|Movie:{booking.show.movie.title}|"
        f"Seats:{booking.seat_numbers}|Payment:{booking.payment_ref}|Status:{booking.status}"
    )
    qr = qrcode.QRCode(box_size=8, border=2)
    qr.add_data(payload)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    image.save(img_io, format="PNG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png")


@app.route("/ticket/<int:booking_id>/pdf")
@login_required
def ticket_pdf(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    user = current_user()
    if not user.is_admin and booking.user_id != user.id:
        abort(403)

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 70

    pdf.setTitle(f"MovieTicket-{booking.id}")
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(60, y, "Movie Ticket")
    y -= 30

    pdf.setFont("Helvetica", 12)
    lines = [
        f"Booking ID: {booking.id}",
        f"Movie: {booking.show.movie.title}",
        f"Theater: {booking.show.theater.name} ({booking.show.theater.city})",
        f"Screen: Screen {booking.show.screen_no} | {booking.show.show_slot} | {'AC' if booking.show.is_ac else 'Non-AC'}",
        f"Show Time: {booking.show.show_time.strftime('%d %b %Y, %I:%M %p')}",
        f"Seat Numbers: {booking.seat_numbers}",
        f"Seats Booked: {booking.seats_booked}",
        f"Total Amount: INR {booking.total_amount:.2f}",
        f"Payment Method: {booking.payment_method}",
        f"Payment Ref: {booking.payment_ref}",
        f"Status: {booking.status}",
        f"Booked On: {booking.created_at.strftime('%d %b %Y, %I:%M %p')}",
    ]
    for line in lines:
        pdf.drawString(60, y, line)
        y -= 22

    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(60, y - 10, "Show this ticket QR/PDF at theater entry.")
    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name=f"ticket_{booking.id}.pdf",
    )


@app.route("/admin")
@admin_required
def admin_dashboard():
    movies = Movie.query.order_by(Movie.title.asc()).all()
    shows = Show.query.order_by(Show.show_time.asc()).all()
    theaters = Theater.query.order_by(Theater.name.asc()).all()
    return render_template(
        "admin_dashboard.html", movies=movies, shows=shows, theaters=theaters
    )


@app.route("/admin/reports")
@admin_required
def admin_reports():
    total_movies = Movie.query.count()
    total_shows = Show.query.count()
    total_active_bookings = Booking.query.filter_by(status="Booked").count()
    total_cancelled = Booking.query.filter_by(status="Cancelled").count()
    total_revenue = (
        db.session.query(func.coalesce(func.sum(Booking.total_amount), 0.0))
        .filter(Booking.status == "Booked")
        .scalar()
    )

    revenue_by_movie_rows = (
        db.session.query(
            Movie.title,
            func.coalesce(func.sum(Booking.total_amount), 0.0).label("revenue"),
        )
        .join(Show, Show.movie_id == Movie.id)
        .join(Booking, Booking.show_id == Show.id)
        .filter(Booking.status == "Booked")
        .group_by(Movie.id, Movie.title)
        .order_by(func.sum(Booking.total_amount).desc())
        .all()
    )
    booking_status_rows = (
        db.session.query(Booking.status, func.count(Booking.id))
        .group_by(Booking.status)
        .all()
    )
    occupancy_rows = (
        db.session.query(
            Show.id,
            Movie.title,
            Theater.name,
            Show.total_seats,
            Show.available_seats,
        )
        .join(Movie, Movie.id == Show.movie_id)
        .join(Theater, Theater.id == Show.theater_id)
        .order_by(Show.show_time.asc())
        .all()
    )

    revenue_labels = [row[0] for row in revenue_by_movie_rows]
    revenue_values = [float(row[1]) for row in revenue_by_movie_rows]
    status_labels = [row[0] for row in booking_status_rows]
    status_values = [row[1] for row in booking_status_rows]
    occupancy_labels = [f"{row[1]} ({row[2]})" for row in occupancy_rows]
    occupancy_values = [
        (row[3] - row[4]) / row[3] * 100 if row[3] > 0 else 0 for row in occupancy_rows
    ]

    return render_template(
        "admin_reports.html",
        total_movies=total_movies,
        total_shows=total_shows,
        total_active_bookings=total_active_bookings,
        total_cancelled=total_cancelled,
        total_revenue=total_revenue,
        revenue_labels=revenue_labels,
        revenue_values=revenue_values,
        status_labels=status_labels,
        status_values=status_values,
        occupancy_labels=occupancy_labels,
        occupancy_values=occupancy_values,
    )


@app.route("/admin/movies/add", methods=["GET", "POST"])
@admin_required
def add_movie():
    if request.method == "GET":
        return redirect(url_for("admin_dashboard"))

    title = request.form.get("title", "").strip()
    genre = request.form.get("genre", "").strip()
    duration = request.form.get("duration_mins", "").strip()
    language = request.form.get("language", "").strip()
    actors = request.form.get("actors", "").strip()
    poster_url = request.form.get("poster_url", "").strip()
    rating = request.form.get("rating", "").strip()

    if not title or not genre or not duration or not language or not actors:
        flash("All movie fields are required.", "danger")
        return redirect(url_for("admin_dashboard"))

    movie = Movie(
        title=title,
        genre=genre,
        duration_mins=int(duration),
        language=language,
        actors=actors,
        poster_url=poster_url,
        rating=float(rating) if rating else 0.0,
    )
    db.session.add(movie)
    try:
        db.session.commit()
    except DataError:
        db.session.rollback()
        flash(
            "Poster data is too large for current DB schema. Run ALTER TABLE for poster_url or use a shorter image URL.",
            "danger",
        )
        return redirect(url_for("admin_dashboard"))
    flash("Movie added.", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/shows/add", methods=["GET", "POST"])
@admin_required
def add_show():
    if request.method == "GET":
        return redirect(url_for("admin_dashboard"))

    movie_id = request.form.get("movie_id", "").strip()
    theater_id = request.form.get("theater_id", "").strip()
    screen_no = request.form.get("screen_no", "").strip()
    show_slot = request.form.get("show_slot", "").strip()
    is_ac = request.form.get("is_ac", "").strip() == "yes"
    show_date = request.form.get("show_date", "").strip()
    show_time_value = request.form.get("show_time_value", "").strip()
    price = request.form.get("price", "").strip()
    total_seats = request.form.get("total_seats", "").strip()

    if (
        not movie_id
        or not theater_id
        or not screen_no
        or not show_slot
        or not show_date
        or not show_time_value
        or not price
        or not total_seats
    ):
        flash("All show fields are required.", "danger")
        return redirect(url_for("admin_dashboard"))

    if int(screen_no) not in [1, 2]:
        flash("Only Screen 1 and Screen 2 are supported.", "danger")
        return redirect(url_for("admin_dashboard"))

    if not db.session.get(Movie, int(movie_id)) or not db.session.get(Theater, int(theater_id)):
        flash("Invalid movie or theater selected.", "danger")
        return redirect(url_for("admin_dashboard"))
    show_time_obj = parse_fixed_show_datetime(show_date, show_time_value)
    if not show_time_obj:
        flash("Invalid show time. Use one of the fixed slots.", "danger")
        return redirect(url_for("admin_dashboard"))

    show = Show(
        movie_id=int(movie_id),
        theater_id=int(theater_id),
        screen_no=int(screen_no),
        show_slot=show_slot,
        is_ac=is_ac,
        show_time=show_time_obj,
        price=float(price),
        total_seats=int(total_seats),
        available_seats=int(total_seats),
    )
    db.session.add(show)
    db.session.commit()
    flash("Show added.", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/shows/<int:show_id>/update", methods=["POST"])
@admin_required
def update_show(show_id):
    show = db.session.get(Show, show_id)
    if not show:
        flash("Show not found.", "danger")
        return redirect(url_for("admin_dashboard"))

    theater_id = request.form.get("theater_id", "").strip()
    screen_no = request.form.get("screen_no", "").strip()
    show_slot = request.form.get("show_slot", "").strip()
    is_ac = request.form.get("is_ac", "").strip() == "yes"
    show_date = request.form.get("show_date", "").strip()
    show_time_value = request.form.get("show_time_value", "").strip()
    price = request.form.get("price", "").strip()

    if not theater_id or not screen_no or not show_slot or not show_date or not show_time_value or not price:
        flash("All update fields are required.", "danger")
        return redirect(url_for("admin_dashboard"))

    if int(screen_no) not in [1, 2]:
        flash("Only Screen 1 and Screen 2 are supported.", "danger")
        return redirect(url_for("admin_dashboard"))
    if not db.session.get(Theater, int(theater_id)):
        flash("Invalid theater selected.", "danger")
        return redirect(url_for("admin_dashboard"))
    show_time_obj = parse_fixed_show_datetime(show_date, show_time_value)
    if not show_time_obj:
        flash("Invalid show time. Use one of the fixed slots.", "danger")
        return redirect(url_for("admin_dashboard"))

    show.theater_id = int(theater_id)
    show.screen_no = int(screen_no)
    show.show_slot = show_slot
    show.is_ac = is_ac
    show.show_time = show_time_obj
    show.price = float(price)
    db.session.commit()
    flash("Show updated.", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/shows/<int:show_id>/delete", methods=["POST"])
@admin_required
def delete_show(show_id):
    show = db.session.get(Show, show_id)
    if not show:
        flash("Show not found.", "danger")
        return redirect(url_for("admin_dashboard"))

    active_bookings = Booking.query.filter_by(show_id=show.id, status="Booked").count()
    if active_bookings > 0:
        flash("Cannot delete show with active bookings.", "warning")
        return redirect(url_for("admin_dashboard"))

    SeatHold.query.filter_by(show_id=show.id).delete()
    db.session.delete(show)
    db.session.commit()
    flash("Show deleted.", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/theaters/add", methods=["POST"])
@admin_required
def add_theater():
    name = request.form.get("name", "").strip()
    city = request.form.get("city", "").strip()
    if not name or not city:
        flash("Theater name and city are required.", "danger")
        return redirect(url_for("admin_dashboard"))

    existing = Theater.query.filter(func.lower(Theater.name) == name.lower()).first()
    if existing:
        flash("Theater already exists.", "warning")
        return redirect(url_for("admin_dashboard"))

    theater = Theater(name=name, city=city)
    db.session.add(theater)
    db.session.commit()
    flash("Theater added.", "success")
    return redirect(url_for("admin_dashboard"))


@app.cli.command("init-db")
def init_db():
    db.create_all()
    changed = False
    if Theater.query.count() == 0:
        db.session.add_all(
            [
                Theater(name="PVR Nexus", city="Hyderabad"),
                Theater(name="INOX Forum", city="Bengaluru"),
                Theater(name="AGS Cinemas", city="Chennai"),
            ]
        )
        changed = True
    if not User.query.filter_by(email="admin@movie.com").first():
        admin = User(
            name="Admin",
            email="admin@movie.com",
            password_hash=generate_password_hash("admin123"),
            is_admin=True,
        )
        db.session.add(admin)
        changed = True
    if changed:
        db.session.commit()
    print("Database initialized. Admin login: admin@movie.com / admin123")


if __name__ == "__main__":
    app.run(debug=True)
