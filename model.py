import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load and merge both datasets
usecols = ["movieId", "Title", "genres"]
movies1 = pd.read_csv("data/movies.csv", usecols=usecols)
# For All_Movies2.csv, handle extra columns and unify genre separator
movies2 = pd.read_csv("data/All_Movies2.csv", usecols=usecols)
movies2["genres"] = movies2["genres"].fillna("").str.replace(",", "|")
movies1["genres"] = movies1["genres"].fillna("").str.replace(",", "|")
movies = pd.concat([movies1, movies2], ignore_index=True).drop_duplicates(subset=["Title"]).reset_index(drop=True)

# Use description/genres for similarity
tfidf = TfidfVectorizer(stop_words="english")
movies["genres"] = movies["genres"].fillna("")
tfidf_matrix = tfidf.fit_transform(movies["genres"])


# Helper function to get recommendations
def get_recommendations(title, num=10):
    if title not in movies["Title"].values:
        return ["Movie not found in database!"]

    idx = movies[movies["Title"] == title].index[0]
    # Compute cosine similarity only for the selected movie
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    # Get indices of top similar movies (excluding itself)
    sim_indices = sim_scores.argsort()[::-1]
    sim_indices = sim_indices[sim_indices != idx][:num]
    return movies["Title"].iloc[sim_indices].tolist()
