from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from utils import database_utils
from utils import equation_solver

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
    data = database_utils.get_user_by_id(session["user"])["elos"]

    arithmetic_beginner = 1000
    if "arithmetic_beginner" in data:
        arithmetic_beginner = data["arithmetic_beginner"]

    arithmetic_intermediate = 1000
    if "arithmetic_intermediate" in data:
        arithmetic_intermediate = data["arithmetic_intermediate"]

    arithmetic_expert = 1000
    if "arithmetic_expert" in data:
        arithmetic_expert = data["arithmetic_expert"]

    algebra_easy = 1000
    if "algebra_easy" in data:
        algebra_easy = data["algebra_easy"]

    algebra_hard = 1000
    if "algebra_hard" in data:
        algebra_hard = data["algebra_hard"]

    geometry = 1000
    if "geometry" in data:
        geometry = data["geometry"]

    return render_template("home.html", arithmetic_beginner = arithmetic_beginner, arithmetic_intermediate = arithmetic_intermediate, arithmetic_expert = arithmetic_expert,
                          algebra_easy = algebra_easy, algebra_hard = algebra_hard, geometry = geometry)

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
        user = database_utils.authenticate(request.form['user'], request.form['pwd'])
        if user:
            session['user'] = str(user)
            session.permanent = True
            return redirect(url_for('root'))
        else:
            flash('Incorrect username or password')
            return redirect(url_for('login'))
    else:
        success = database_utils.create_user(request.form['user'], request.form['pwd'])
        if (success):
            session['user'] = str(success)
            session.permanent = True
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
    # question = ""
    question = database_utils.get_random_question_by_subject(subject)

    # if subject == 'arithmetic_basic':
    #     question = utils.arith.make_arith_basic(3)[0]
    # elif subject == 'arithmetic_intermediate':
    #     question = utils.arith.make_arith_exp(5)[0]
    # elif subject == 'arithmetic_expert':
    #     question = utils.arith.make_arith()[0]

    # equation = equation_solver.getRes(question)
    # inputPic = equation['input_img']
    # answerPic = equation['answer_img']
    # answers = equation['acceptable_answers']

    return render_template("endless.html", question_img = question['question_img'], question_id = question['_id'])


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/getanswer", methods=["POST"])
def get_question():
    print(request.form)
    if 'questionid' not in request.form or 'useranswer' not in request.form:
        return 'Error!'
    else:
        question = database_utils.get_question_by_id(request.form['questionid'])
        print(request.form['useranswer'], request.form['useranswer'] in question['acceptable_answers'])
        return {"answer_img": question["answer_img"], "acceptable_answers": question["acceptable_answers"]}

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
