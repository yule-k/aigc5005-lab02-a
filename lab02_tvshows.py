# lab02_tvshows.py
import json
from pathlib import Path

import requests

URL = "https://api.tvmaze.com/shows?page=0"
OUTPUT = Path("summary.json")

def tvmaze(URL):
    """Download the TV shows data from TVMaze API and return them as Python objects."""
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()
dfshows = tvmaze(URL)

# Number of shows per genre, 'genres': ['Drama', 'Science-Fiction', 'Thriller']
def number_genres(dfshows):
    """Count the number of shows per genre and return a dictionary with genres as keys and counts as values."""
    genre_counts = {} #{'Drama': count}
    for show in dfshows:
        for genre in show["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


# Average rating by language, 'language': 'English', 'rating': {'average': 6.6}
def average_rating_by_language(dfshows):
    """Calculate the average rating of shows for each language and return a dictionary with languages as keys and average ratings as values."""
    language_basket ={} #{'English': (rating_sum, show_count)}
    for show in dfshows:
        language = show.get("language")
        rating_data = show.get("rating") or {}
        rating = rating_data.get("average")
        if not language or rating is None:
            continue
        rating_sum, show_count = language_basket.get(language, (0, 0))
        language_basket[language] = (rating_sum + rating, show_count + 1)

#{'English': average_rating}
    avg_ratings = {language: round(rating_sum / show_count, 2)
        for language, (rating_sum, show_count) in language_basket.items()
    }
    
    return avg_ratings


#shows premiered per decade, 'premiered': '2013-06-24'
def shows_per_decade(dfshows):
    """Count the number of shows that premiered in each decade and return a dictionary with decades as keys and counts as values."""
    decade_counts = {} #{'2010s': count}
    for show in dfshows:
        premiered = show.get("premiered")
        if not premiered:
            continue
        year = int(premiered[:4])
        decade = (year // 10) * 10
        decade_counts[decade] = decade_counts.get(decade, 0) + 1
    return decade_counts


def main():
    dfshows = tvmaze(URL)
    genre_counts = number_genres(dfshows)
    avg_ratings = average_rating_by_language(dfshows)
    decade_counts = shows_per_decade(dfshows)

    summary = {
         "source URL" : URL,
         "records_processed" : len(dfshows),
         "genres" : genre_counts,  
         "average ratings by language" : avg_ratings,
         "shows premiered per decade" : decade_counts
    }

    OUTPUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Read {len(dfshows)} records across {len(genre_counts)} genres, {len(avg_ratings)} languages, and {len(decade_counts)} decades.")
    print(f"The number of shows per genre is: {genre_counts}")
    print(f"The average rating by language is: {avg_ratings}")
    print(f"The number of shows premiered per decade is: {decade_counts}")
    print(f"Summary written to {OUTPUT}")


if __name__ == "__main__":
    main()