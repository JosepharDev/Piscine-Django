from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from io import StringIO
# Create your views here.

CSV_PATH_PEOPLE = "/home/yoyahya/Desktop/Piscine-Django/05/data/people.csv"
CSV_PATH_PLANETS = "/home/yoyahya/Desktop/Piscine-Django/05/data/planets.csv"
def connect_db():
    conn = psycopg2.connect(
            dbname="djangotraining",
            user="djangouser",
            password="secret",
            host="localhost",
            port="5432"
        )
    return conn

def init(request):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""create table if not exists ex08_planets
        (id serial primary key,
        name varchar(64) unique not null,
        climate varchar,
        diameter integer,
        orbital_period integer,
        population bigint,
        rotation_period integer,
        surface_water real,
        terrain varchar(128));""")
        conn.commit()
        cur.execute("""create table if not exists ex08_people
        (id serial primary key,
        name varchar(64) unique not null,
        birth_year varchar(32),
        gender varchar(32),
        eye_color varchar(32),
        hair_color varchar(32),
        height integer,
        mass real,
        homeworld varchar(64) references ex08_planets(name));""")
        conn.commit()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def populate(request):
    conn = None
    cur = None

    try:
        conn = connect_db()
        cur = conn.cursor()

        results = []

        # -------------------
        # POPULATE PLANETS
        # -------------------
        try:
            with open(CSV_PATH_PLANETS, 'r') as f: 
                cur.copy_from(
                    f,
                    "ex08_planets",
                    sep="\t",
                    columns=(
                        "name",
                        "climate",
                        "diameter",
                        "orbital_period",
                        "population",
                        "rotation_period",
                        "surface_water",
                        "terrain",
                    ),
                    null="NULL",
                )
            results.append("planets: OK")

        except Exception as e:
            results.append(f"planets: ERROR ({e})")
        
        # -------------------
        # POPULATE PEOPLE
        # -------------------
        try:
           with open(CSV_PATH_PEOPLE, "r") as f:
               cur.copy_from(
                   f,
                   "ex08_people",
                   sep="\t",
                   columns=("name", "birth_year", "gender","eye_color", "hair_color", "height", "mass", "homeworld"),null="NULL",
                )
           results.append("people: OK")

        except Exception as e:
            results.append(f"people: ERROR ({e})")

        conn.commit()

        return HttpResponse("<br>".join(results))

    except Exception as e:
        if conn:
            conn.rollback()
        return HttpResponse(f"Fatal error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def display(request):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
                    select p.name, p.homeworld, pl.climate
                    from ex08_people p
                    join ex08_planets pl on p.homeworld = pl.name
                    where pl.climate like '%%windy%%'
                    order by p.name ASC
                    """)
        result = cur.fetchall()
        return render(request, "display_08.html", {"result": result})
    except Exception as e:
        return HttpResponse("No data available")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()