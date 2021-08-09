"""
This is the driver file. In this file all routes and flask app creation, db creation is done.

Author Name  : Amit Kumar
Date : 9th Aug 2021

"""
import os
import random
import string
try:
    from flask import Flask, render_template, request, redirect, url_for
    from flask_sqlalchemy import SQLAlchemy
except:
    os.system(
        "pip3 install Flask==1.1.2 psycopg2-binary==2.8.4 "
        "click==7.1.2 Flask-RESTful==0.3.8 Flask-SQLAlchemy==2.4.4 gunicorn==20.0.4"
        "itsdangerous==1.1.0 Jinja2==2.11.2 MarkupSafe==1.1.1 SQLAlchemy==1.3.19 Werkzeug==1.0.1"
    )
    from flask import Flask, render_template, request, redirect, url_for
    from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables(): #Before app run : Creating all required tables.
    db.create_all()

class URL(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))

    def __init__(self, long, short):
        self.long = long
        self.short = short

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        short_url = URL.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url_received = request.form["nm"]
        found_url = URL.query.filter_by(long=url_received).first()

        if found_url:
            return redirect(url_for("display_short_url", url=found_url.short))
        else:
            short_url = shorten_url()
            print(short_url)
            new_url = URL(url_received, short_url)
            db.session.add(new_url)
            db.session.commit()
            return redirect(url_for("display_short_url", url=short_url))
    else:
        return render_template('url_page.html')

@app.route('/<short_url>')
def redirection(short_url):
    long_url = URL.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return "<h1>Url does not exist</h1>"

@app.route('/display/<url>')
def display_short_url(url):
    return render_template('shorturl.html', short_url_display=url)

@app.route('/all_urls')
def display_all():
    return render_template('all_urls.html', vals=URL.query.all())

if __name__ == '__main__':
    app.run(port=5000, debug=False, host="0.0.0.0")
