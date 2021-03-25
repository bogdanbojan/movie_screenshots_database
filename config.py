import psycopg2
import os
from imdb import IMDb


connection = psycopg2.connect(
        database="IMDb",
        user='postgres',
        password="passsword",
        host="localhost",
        port="5432")


path = r"x:\Movie Screenshots 2"
dirs = os.listdir(path)


cursor = connection.cursor()
ia = IMDb()
