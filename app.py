from flask import Flask, render_template, request
from model import get_recommendations, movies

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", movies=movies["Title"].tolist())

@app.route("/recommend", methods=["POST"])
def recommend():
    movie = request.form["movie"]
    recommendations = get_recommendations(movie)
    return render_template("recommend.html", movie=movie, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)


