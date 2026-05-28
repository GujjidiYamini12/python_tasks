from flask import *

from bson.objectid import ObjectId

from server import *

app = Flask(__name__)

@app.route("/")

def home():

    movie_count = movies.count_documents({})

    user_count = users.count_documents({})

    theater_count = theaters.count_documents({})

    show_count = shows.count_documents({})

    booking_count = bookings.count_documents({})

    payment_count = payments.count_documents({})

    review_count = reviews.count_documents({})

    return render_template(

        "index.html",

        movie_count=movie_count,

        user_count=user_count,

        theater_count=theater_count,

        show_count=show_count,

        booking_count=booking_count,

        payment_count=payment_count,

        review_count=review_count
    )

@app.route("/movies")

def movie_page():

    data = list(

        movies.find()

    )

    return render_template(

        "view_movies.html",

        movies=data
    )

@app.route(

"/add_movie",

methods=[

"GET",

"POST"

]

)

def add_movie():

    if request.method=="POST":

        movies.insert_one(

            {

                "movie_name":

                request.form[
                "movie_name"
                ],

                "genre":

                request.form[
                "genre"
                ],

                "rating":

                request.form[
                "rating"
                ],

                "duration":

                request.form[
                "duration"
                ]

            }

        )

        return redirect(
            "/movies"
        )

    return render_template(
        "add_movie.html"
    )

@app.route(

"/delete_movie/<id>"

)

def delete_movie(id):

    movies.delete_one(

        {

            "_id":

            ObjectId(id)

        }

    )

    return redirect(
        "/movies"
    )

if __name__=="__main__":

    app.run(
        debug=True
    )