from flask import Flask, render_template, jsonify, request

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from Route import route
from Driver import driver
#$env:FLASK_APP='app.py'
#$env:DATABASE_URL='postgres://kesybfycsywmcg:0850bcd5d782fff8dc8ef127544875e0aa1d378472c5504380aa6f3cb6aaa890@ec2-52-22-216-69.compute-1.amazonaws.com:5432/daas6ugs49amc0'
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def login():
    global routes
    routes = []
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/newroute", methods = ["POST"])
def newroute():
    title = request.form.get("routetitle")
    startpoint = request.form.get("startpoint")
    endpoint = request.form.get("endpoint")
    webdriver = driver(startpoint, endpoint)
    trip_time, distance, directions, url = webdriver.run_driver()
    new_route = route(title, startpoint, endpoint, trip_time, directions, url)
    routes.append(new_route)
    json_output = {"title": title, "startpoint":startpoint, "endpoint": endpoint,
        "trip_time": trip_time, "distance": distance, "directions": directions, "url": url}
    return jsonify(json_output)

@app.route("/routeview")
def routeview():
    return render_template("routeview.html")

@app.route("/savedroutes")
def savedroutes():
    return render_template("savedroutes.html")

