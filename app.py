from flask import Flask, render_template, jsonify, request

from Route import route
from Driver import driver
#$env:FLASK_APP=app
#$env:DATABASE_URL='postgres://kesybfycsywmcg:0850bcd5d782fff8dc8ef127544875e0aa1d378472c5504380aa6f3cb6aaa890@ec2-52-22-216-69.compute-1.amazonaws.com:5432/daas6ugs49amc0'
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello"

@app.route("/newroute")
def newroute():
    return "New route"

@app.route("/routeview")
def routeview():
    return "Route view"

@app.route("/savedroutes")
def savedroutes():
    return "Saved routes"