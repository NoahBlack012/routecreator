from flask import Flask, render_template, jsonify, request, url_for, redirect, session
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from Route import route
from Driver import driver
#$env:FLASK_APP='app.py'
#$env:DATABASE_URL='postgres://kesybfycsywmcg:0850bcd5d782fff8dc8ef127544875e0aa1d378472c5504380aa6f3cb6aaa890@ec2-52-22-216-69.compute-1.amazonaws.com:5432/daas6ugs49amc0'

#Init app
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "nb12"#secret key for sessions


#Init database engine
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def login():
    session['login'] = False
    global routes
    routes = []
    return render_template("login.html")

@app.route("/home", methods = ["POST", 'GET'])
def home():
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")
        db_users = db.execute("SELECT username FROM users").fetchall()[0]
        for db_user in db_users:
            if db_user == user:
                userid = db.execute("SELECT userid FROM users WHERE username=:user", {"user": user}).fetchall()[0][0]
                db_password = db.execute("SELECT password FROM users WHERE userid=:userid", {"userid": userid}).fetchall()[0][0]
                if password == db_password:
                    #Login the user when the username and password are correct
                    session['login'] = True
                    session['user'] = user
                    session['password'] = password
                    session['userid'] = userid
                    return render_template("home.html")
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route("/newroute", methods = ["POST"])
def newroute():
    global current_route
    title = request.form.get("routetitle")
    startpoint = request.form.get("startpoint")
    endpoint = request.form.get("endpoint")
    webdriver = driver(startpoint, endpoint)
    trip_time, distance, directions, url = webdriver.run_driver()
    current_route = route(title, startpoint, endpoint, trip_time, directions, url)
    routes.append(current_route)
    json_output = {"title": title, "startpoint":startpoint, "endpoint": endpoint,
        "trip_time": trip_time, "distance": distance, "directions": directions, "url": url}
    return jsonify(json_output)

@app.route("/save", methods = ["POST"])
def save():
    return redirect(url_for('routeview'))

@app.route("/routeview", methods = ["POST"])
def routeview():
    return render_template("routeview.html")

@app.route("/savedroutes")
def savedroutes():
    return render_template("savedroutes.html")

