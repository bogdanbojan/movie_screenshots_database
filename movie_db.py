from imdb import IMDb
import os
import psycopg2

'''
- make database with : ID, Movie, Rating, Screeshots(nr of screenshots in the directory)
- make a pie graph with matplotlib that shows how big is each folder compared to the other
- add more features later on, maybe?
'''

con = psycopg2.connect(
        database="IMDb",
        user='postgres',
        password="*******",
        host="localhost",
        port="5432")
print("connected to the database, h4ckerman!")

cur = con.cursor()

# delete_statement = "DELETE from movies_db"
# cur.execute(delete_statement)
# con.commit()
# cur.close()
# con.close()

ia = IMDb()


path = r"x:\Movie Screenshots 2"
dirs = os.listdir(path)




for file in dirs:
    if 'New folder' not in file:
       try:
            movie = ia.search_movie('{}'.format(file))
            movie_path = r"x:\Movie Screenshots 2\{}".format(file)

            ID = movie[0].getID()
            # keys = ['long imdb title', 'title', 'rating', 'directors']
            long_title = ia.get_movie(movie[0].getID())['long imdb title']
            title = ia.get_movie(movie[0].getID())['title']
            rating = ia.get_movie(movie[0].getID())['rating']
            directors_temp = ia.get_movie(movie[0].getID())['directors']
            genre = ia.get_movie(movie[0].getID())['genre']
            year = ia.get_movie(movie[0].getID())['year']
            screenshots_nr = len(movie_path)
            # for key in keys:
            #    movie_attr = ia.get_movie(movie[0].getID())['{}'.format(key)]

            cur.execute("INSERT INTO movies_db (movie_id,movie,director,year,rating,genre,screenshots_nr) VALUES (%s,%s,%s,%s,%s,%s,%s)", (
            ID, title, *[director['name'] for director in directors_temp], year, rating, genre, screenshots_nr))
            con.commit()
            print('commited {} to the db!'.format(file))
       except:
           pass
cur.close()
con.close()

'''
problem with ID and directors - data type is different eg. ID - movie dt and directors - people dt  
'''
# movie = ia.search_movie('{}'.format('The Matrix'))
# ID = movie[0].getID()
# directors_temp = ia.get_movie(movie[0].getID())['directors']
# genre = ia.get_movie(movie[0].getID())['genre']
#
# print(*[genre[i] for i in range(len(genre))])
# #
# print(type(*[director['name'] for director in directors_temp]),type(ID))
