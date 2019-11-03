from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from utils import database_utils
from utils import equation_solver
import utils

import os
import random


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


@app.route("/auth", methods=["POST"])
def auth():
    if "submit" not in request.form or "user" not in request.form or "pwd" not in request.form:
        flash("At least one form input was incorrect")
        return redirect(url_for('login'))

    if request.form['submit'] == 'Login':
        print(request.form)
        print(database_utils.authenticate(request.form['user'], request.form['pwd']))
        if database_utils.authenticate(request.form['user'], request.form['pwd']):
            session['user'] = True
            return redirect(url_for('root'))
        else:
            flash('Incorrect username or password')
            return redirect(url_for('login'))
    else:
        success = database_utils.create_user(request.form['user'], request.form['pwd'])
        print(success)
        if (success):
            session['user'] = True
            return redirect(url_for('root'))
        else:
            flash('This username already exists!')
            return redirect(url_for('login'))

@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login'))

@app.route("/game", methods=["POST"])
@require_login
def game():
    subject = request.form['subject']
    question = ""
    if subject == 'arithmetic_basic':
        question = utils.arith.make_arith_basic(3)[0]
    elif subject == 'arithmetic_intermediate':
        question = utils.arith.make_arith_exp(5)[0]
    elif subject == 'arithmetic_expert':
        question = utils.arith.make_arith()[0]

    answers = equation_solver.getRes(question)
    inputPic = answers['input_img']


    answerPic = answers['answer_img']

    return render_template("endless.html", questionImg = inputPic)



if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
