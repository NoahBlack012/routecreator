from flask import Flask, render_template, jsonify, request, url_for, redirect, session
import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

from Route import route
from Driver import driver
#$env:FLASK_APP='app.py'
#$env:DATABASE_URL='postgres://kesybfycsywmcg:0850bcd5d782fff8dc8ef127544875e0aa1d378472c5504380aa6f3cb6aaa890@ec2-52-22-216-69.compute-1.amazonaws.com:5432/daas6ugs49amc0'

#Init app
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "xgovctjmgfqdwvxihtkj"#secret key for sessions

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
                    session['userid'] = userid
                    return redirect(url_for('routeview'), code=307)
    #Redirect to login if user got the username or password wrong or didn't go through login
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

    #Saving attributes of the current route in session varibles
    session['title'] = title
    session['startpoint'] = startpoint
    session['endpoint'] = endpoint
    session['trip_time'] = trip_time
    session['distance'] = distance
    session['directions'] = directions
    session['url'] = url
    session['url'] = f"{session['url']}"
    
    json_output = {"title": title, "startpoint":startpoint, "endpoint": endpoint,
        "trip_time": trip_time, "distance": distance, "directions": directions, "url": url}
    return jsonify(json_output)

@app.route("/save", methods = ["POST"])
def save():
    directions_list = []
    #Check if route is in database
    db_titles = db.execute("SELECT title FROM routes WHERE userid = :userid", {"userid": session['userid']}).fetchall()
    if not db_titles == []:
        for db_title in db_titles:
            if session['title'] == db_title:
                db.execute("DELETE FROM routes WHERE title = :title and userid = :userid", {'title': session['title'], 'userid': session['userid']})
    for line in session['directions']:
        if line != '\n':
            directions_list.append(line)
        else: 
            directions_list.append(" ")
    rstrip_directions = ''.join(directions_list)
    #Add route to database
    db.execute("INSERT INTO routes (userid, title, startpoint, endpoint, trip_time, distance, directions, url) VALUES (:userid, :title, :startpoint, :endpoint, :trip_time, :distance, :directions, :url)", 
        {'userid': session['userid'], 'title': session['title'], 'startpoint': session['startpoint'], 'endpoint': session['endpoint'], 'trip_time': session['trip_time'], 'distance':  session['distance'], 
        'directions': rstrip_directions, 'url': session['url']})
    db.commit()
    return redirect(url_for('routeview'), code=307)

@app.route("/routeview", methods = ["POST"])
def routeview():
    return render_template("routeview.html")

@app.route("/savedroutes", methods = ["POST"])
def savedroutes():
    user_route_titles = db.execute("SELECT title FROM routes WHERE userid = :userid", {'userid': session['userid']}).fetchall()[0]
    titles = []
    for title in user_route_titles:
        titles.append(title)
    json_output = {'titles': titles}
    return jsonify(json_output)

@app.route("/logout", methods = ["POST"])
def logout():
    session['login'] = False
    session['user'] = None
    session['userid'] = None
    return redirect(url_for('login'))

