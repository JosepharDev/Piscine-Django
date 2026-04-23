from django.shortcuts import render
import psycopg2
from django.http import HttpResponse
from .forms import Update_crawl

def init(request):
    try:
        conn = psycopg2.connect(dbname="djangotraining", 
                        user="djangouser",
                        password="secret",
                        host="localhost",
                        port="5432")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE if not exists ex06_movies 
            (title varchar(64) unique not null,
            episode_nb serial primary key,
            opening_crawl text,
            director varchar(32) not null,
            producer varchar(128) not null,
            release_date date not null,
            created timestamptz default current_timestamp,
            updated timestamptz default current_timestamp);""")
            
        cur.execute("""CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();""")

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
        (6, "Return of the Jedi", " Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11")
    ]
    try: 
        conn = psycopg2.connect(dbname="djangotraining", 
                            user="djangouser",
                            password="secret",
                            host="localhost",
                            port="5432")
        cur = conn.cursor()
        cur.executemany("insert into ex06_movies (episode_nb, title, director, producer, release_date) values (%s,%s,%s,%s,%s)", data)
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
        cur.execute("select * from ex06_movies")
        data = cur.fetchall()
        if not data:
            return HttpResponse("No data available")
        return render(request, "ex06_display.html", {"data":data})
    except Exception as e:
        return HttpResponse("No data available")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def get_db_connection():
    return psycopg2.connect(
        dbname="djangotraining", user="djangouser", 
        password="secret", host="localhost"
    )
def update(request):
    movie_choices = []
    message = ""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT title FROM ex06_movies")
    movie_choices = [(row[0], row[0]) for row in cur.fetchall()]
    
    if not movie_choices:
        return render(request, 'update_crawl.html', {'no_data': True})
    # 2. Handle Form Submission
    if request.method == 'POST':
        form = Update_crawl(movie_choices, request.POST)
        if form.is_valid():
            m_title = form.cleaned_data['item_to_update']
            new_text = form.cleaned_data['new_crawl']
            
            try:
                cur.execute(
                    "UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s",
                    (new_text, m_title)
                )
                conn.commit()
                message = "Successfully updated!"
            except Exception as e:
                message = f"Error: {e}"
    else:
        form = Update_crawl(movie_choices)

    cur.close()
    conn.close()
    
    return render(request, 'update_crawl.html', {'form': form, 'message': message})