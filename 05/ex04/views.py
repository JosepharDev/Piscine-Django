from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
# Create your views here.
def init(request):
    try:
        conn = psycopg2.connect(dbname="djangotraining", 
                        user="djangouser",
                        password="secret",
                        host="localhost",
                        port="5432")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE if not exists ex04_movies 
            (title varchar(64) unique not null,
            episode_nb serial primary key,
            opening_crawl text,
            director varchar(32) not null,
            producer varchar(128) not null,
            release_date date not null);""")
        conn.commit()
        conn.close()
        cur.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

def populate(request):
    data = [
        (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
        (2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
        (3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
        (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
        (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11")
    ]
    try: 
        conn = psycopg2.connect(dbname="djangotraining", 
                            user="djangouser",
                            password="secret",
                            host="localhost",
                            port="5432")
        cur = conn.cursor()
        cur.executemany("""
                        insert into ex04_movies (episode_nb, title, director, producer, release_date) values (%s,%s,%s,%s,%s)
                        ON CONFLICT (episode_nb)
                        DO UPDATE SET
                            title = EXCLUDED.title,
                            director = EXCLUDED.director,
                            producer = EXCLUDED.producer,
                            release_date = EXCLUDED.release_date""", data)
        conn.commit()
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            
def display(request):
    try: 
        conn = psycopg2.connect(dbname="djangotraining", 
                            user="djangouser",
                            password="secret",
                            host="localhost",
                            port="5432")
        cur = conn.cursor()
        cur.execute("select * from ex04_movies")
        data = cur.fetchall()
        if not data:
            return HttpResponse("No data available")
        return render(request, "ex04_index.html", {"data":data})
    except Exception as e:
        return HttpResponse("No data available")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            
def remove(request):
    try: 
        conn = psycopg2.connect(dbname="djangotraining", 
                            user="djangouser",
                            password="secret",
                            host="localhost",
                            port="5432")
        cur = conn.cursor()
        if request.method == "POST" and "remove" in request.POST:
            title = request.POST.get("title")
            if title:
                cur.execute(
                    "DELETE FROM ex04_movies WHERE title = %s;",
                    (title,)
                )
                conn.commit()
        cur.execute("SELECT title FROM ex04_movies;")
        movies = cur.fetchall()

        if not movies:
            return HttpResponse("No data available")
        return render(request, 'ex04_remove.html', {"movies": movies})

    except Exception as e:
        return HttpResponse( "No data available")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()