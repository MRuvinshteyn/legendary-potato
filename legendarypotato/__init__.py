from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from utils import database_utils
import os
import random

# authentication wrapper
def require_login(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if 'user' not in session:
            flash("Please log in to use Legendary Potato")
            return redirect(url_for("login"))
        else:
            return f(*args, **kwargs)
    return inner

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/")
@require_login
def root():
    return render_template("home.html")

@app.route("/single")
@require_login
def single():
    return render_template("single.html")

@app.route("/multi")
@require_login
def multi():
    return render_template("multi.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
