from django.shortcuts import render
import psycopg2
from django.http import HttpResponse

def init(request):
    conn = psycopg2.connect(dbname="djangotraining", 
                        user="djangouser",
                        password="secret",
                        host="localhost",
                        port="5432")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE if not exists ex00_movies 
        (title varchar(64) unique not null,
        episode_nb serial primary key,
        nopening_crawl text not null,
        director varchar(32) not null,
        producer varchar(128) not null,
        release_data date not null);""")
    conn.commit()
    return HttpResponse("OK")