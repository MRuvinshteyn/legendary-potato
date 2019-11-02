from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os
import random

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/single")
def single():
    return render_template("single.html")

@app.route("/multi")
def multi():
    return render_template("multi.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
