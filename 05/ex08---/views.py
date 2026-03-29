from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from io import StringIO
# Create your views here.
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
        population integer,
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
        cur.close()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"{e}")

def populate(request):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cleaned = []
        with open('/home/yoyahya/Desktop/Piscine-Django/05/d05_data/planets.csv', 'r') as f:
            for line in f:
                parts = line.strip().split()
                row = parts[:8]
                cleaned.append(" ".join(row))
        
        cur.copy_from(StringIO("\n".join(cleaned)), "ex08_planets", sep=' ', columns=("name","climate","diameter","orbital_period","population","rotation_period","surface_water","terrain"))
        cur.commit()
        cur.close()
        conn.close()
        return HttpResponse(f"{s}")
    except Exception as e:
        return HttpResponse(f"{e}")