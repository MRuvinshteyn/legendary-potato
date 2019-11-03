from pymongo import MongoClient
from hashlib import sha256
from bson.objectid import ObjectId
import datetime
from random import randint

client = MongoClient()
db = client.legendarypotato
users = db.users
games = db.games
questions = db.questions

def hash_password(username, password):
    return sha256(str(username+password).encode('utf-8')).hexdigest()

def create_user(username, password):
    if get_user_by_name(username) == None:
        user = users.insert_one({
            "username": username,
            "password": hash_password(username, password),
            "games": [],
            "games_played": {},
            "elos": {}
        })
        return user.inserted_id
    return None

def get_user_by_name(username):
    return users.find_one({"username": username})

def get_user_by_id(userid):
    return users.find_one({"_id": ObjectId(userid)})

def addELO(userid, questionType):
    user = get_user_by_id(userid)
    assert user
    if user['elos'].keys().contains()[questionType]:
        user['elos'][questionType] += 50 * (1/int(user['games_played'][questionType]))
    else:
        user['elos'][questionType] = 1050

def subELO(userid, questionType):
    user = get_user_by_id(userid)
    assert user
    if user['elos'].keys().contains(questionType):
        user['elos'][questionType] -= 50 * (1/int(user['games_played'][questionType]))
    else:
        user['elos'][questionType] = 950

def playGame(userid, questionType):
    user = get_user_by_id(userid)
    assert user
    if user['games_played'].keys().contains(questionType):
        user['games_played'][questionType] += 1
    else:
        user['games_played'][questionType] = 1


def authenticate(username, password):
    user = get_user_by_name(username)
    if user == None:
        return None
    return user["_id"]

def create_game(player1, player2, endless, subject):
    game = games.insert_one({
            "players": (ObjectId(player1), ObjectId(player2)),
            "endless": bool(endless),
            "subject": subject,
            "timestamp": str(datetime.datetime.now())
        })
    return game.inserted_id

def get_game_by_id(game_id):
    return games.find_one({"_id": ObjectId(game_id)})

def get_games_by_player_id(player_id):
    return list(games.find({"players": ObjectId(player_id)}))

def create_question(question_img, acceptable_answers, answer_img, subject):
    question = questions.insert_one({
        "question_img": question_img,
        "acceptable_answers": acceptable_answers,
        "answer_img": answer_img,
        "subject": subject
    })
    return question.inserted_id

def get_questions_by_subject(subject):
    return list(questions.find({"subject": subject}))

def get_random_question_by_subject(subject):
    all_questions = get_questions_by_subject(subject)
    return all_questions[randint(0, len(all_questions)-1)]

def get_question_by_id(id_num):
    return questions.find_one({"_id": ObjectId(id_num)})
