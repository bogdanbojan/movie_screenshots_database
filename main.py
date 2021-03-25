"""
Program that sorts through my screenshots folder and makes a DB with details about all my archived movies.
"""
from config import connection, dirs, ia, cursor




def sort_through_movie_folder():
    for file in dirs:
        if 'New folder' not in file:
            append_movies_to_db(*get_movie_details_from_IMDb_api(file),get_movie_details_from_os(file))




def append_movies_to_db(ID, title, directors, year, rating, genre, screenshots_nr):
    cursor.execute(
        "INSERT INTO movies_db (movie_id,movie,director,year,rating,genre,screenshots_nr) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (
            ID, title, *[director['name'] for director in directors], year, rating, genre, screenshots_nr))

    connection.commit()

def get_movie_details_from_os(file):
    movie_path = r"x:\Movie Screenshots 2\{}".format(file)
    screenshots_nr = len(movie_path)
    return screenshots_nr

def get_movie_details_from_IMDb_api(file):
    movie = ia.search_movie('{}'.format(file))

    long_title = ia.get_movie(movie[0].getID())['long imdb title']
    title = ia.get_movie(movie[0].getID())['title']
    rating = ia.get_movie(movie[0].getID())['rating']
    directors = ia.get_movie(movie[0].getID())['directors']
    genre = ia.get_movie(movie[0].getID())['genre']
    year = ia.get_movie(movie[0].getID())['year']
    ID = movie[0].getID()
    return ID, title, directors, year, rating, genre


sort_through_movie_folder()

cursor.close()
connection.close()



