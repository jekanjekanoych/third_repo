import os.path
import numpy as np
import flask
import sqlite3

from faker import Faker


app = flask.Flask(__name__)


@app.route('/cities/')
def cities():
    if not os.path.exists('cities.db'):
        con = sqlite3.connect("cities.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE cities(cities, areas)")
        con.commit()

    fake = Faker()
    cities = []
    Faker.seed(0)
    for city in range(10):
        city = [fake.city()]
        cities += city
        for city in cities:
            con = sqlite3.connect("cities.db")



    areas = []
    for area in range(10):
        area = [fake.random_int()]
        areas += area
        for area in areas:
            con = sqlite3.connect("cities.db")
            for city in range(10):
                city = [fake.city()]
                cities += city
                for city in cities:
                    con = sqlite3.connect("cities.db")
            con.execute("INSERT INTO cities VALUES(?, ?)", [city, area])
        con.commit()


        con = sqlite3.connect("cities.db")
        cur = con.cursor()
        r = cur.execute("SELECT COUNT(cities) from cities")
        number_of_cities = r.fetchall()
        con.close()


    with app.app_context():
        return flask.render_template('cities.html', number=number_of_cities)

@app.route('/cities_2/')
def areas():
    con = sqlite3.connect("cities.db")
    cur = con.cursor()
    r = cur.execute("SELECT areas FROM cities")
    areas = r.fetchall()
    with app.app_context():
        return flask.render_template('cities.html', areas=areas)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/names/')
def names():
    if not os.path.exists('names.db'):
        con = sqlite3.connect("names.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE names(names)")

    fake = Faker()
    names = []
    for i in range(100):
        i = [[fake.name()]]
        names += i
        for j in names:
            con = sqlite3.connect("names.db")
            con.execute("INSERT INTO names VALUES(?)", j)
        con.commit()
        con.close()

    first_name = []
    for i in names:
        for n in i:
            x = n.split(' ')
        first_name.append(x[0])

    uniq = []
    for n in first_name:
        uniq.append(n)
    res = np.array(uniq)
    unique_res = np.unique(res)

    with app.app_context():
        return flask.render_template('uniq.html', unique=unique_res)


if __name__ == '__main__':
    app.run(debug=True)
    cities()
    names()
