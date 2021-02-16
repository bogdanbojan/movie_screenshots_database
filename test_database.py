import psycopg2

con = psycopg2.connect(
        database="IMDb",
        user='postgres',
        password="abc123tampon",
        host="localhost",
        port="5432")
# print("succes")

cur = con.cursor()

'''
maybe make a separate table with actors and their roles
'''

cur.execute("INSERT INTO movies_db (movie_id,movie,director,year,rating,genre) VALUES (%s,%s,%s,%s,%s,%s)",(15234,'The Assassination of Jesse James by the Coward Robert Ford','Alexander Somehow',2007,7.5,'crime, drama'))
con.commit()
cur.close()
con.close()