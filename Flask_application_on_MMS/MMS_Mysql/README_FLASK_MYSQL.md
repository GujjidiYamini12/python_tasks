# Flask + MySQL Movie Booking System

This starter project includes:
- User registration/login/logout
- Modern cinema-style UI (movie cards, posters, stars, premium dark theme)
- Admin dashboard to add theaters, movies, and multiplex shows
- Admin update/delete show controls
- Seat-number based booking and cancellation
- Payment simulation with multiple methods (Card, UPI, NetBanking, Wallet)
- Real-time seat hold (3-minute lock before payment)
- QR ticket endpoint and downloadable PDF ticket
- Admin reports with charts (revenue, booking status, occupancy)
- Seat tracking and booking history
- HTML + CSS + JavaScript frontend templates

## 1) Create MySQL database

```sql
CREATE DATABASE movie_booking_db;
```

## 2) Install dependencies

```bash
pip install -r requirements.txt
```

## 3) Set environment variables

Use `.env.example` as reference:
- `SECRET_KEY`
- `DATABASE_URL` (MySQL URI)

PowerShell example:

```powershell
$env:SECRET_KEY="super-secret"
$env:DATABASE_URL="mysql+pymysql://root:password@localhost:3306/movie_booking_db"
```

## 4) Initialize DB + create default admin

```bash
flask --app flask_app.py init-db
```

If you already ran an older schema, recreate the tables/database once so new fields (`theater_id`, `screen_no`, `show_slot`, `is_ac`, `payment_method`, movie metadata, seat holds table) are applied cleanly.

Default admin:
- Email: `admin@movie.com`
- Password: `admin123`

## 5) Run app

```bash
flask --app flask_app.py run
```

Open:
`http://127.0.0.1:5000`
