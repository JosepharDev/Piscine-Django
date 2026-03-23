from django.shortcuts import render
import psycopg2
from django.http import HttpResponse

def init(request):
    try:
        conn = psycopg2.connect(dbname="djangotraining", 
                        user="djangouser",
                        password="secret",
                        host="localhost",
                        port="5432")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE if not exists ex00_movies 
            (title varchar(64) unique not null,
            episode_nb serial primary key,
            nopening_crawl text,
            director varchar(32) not null,
            producer varchar(128) not null,
            release_date date not null);""")
        conn.commit()
        conn.close()
        cur.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
    