from pymongo import MongoClient
from hashlib import sha256
from bson.objectid import ObjectId
import datetime

client = MongoClient()
db = client.legendarypotato
users = db.users
games = db.games


def hash_password(username, password):
    return sha256(str(username+password).encode('utf-8')).hexdigest()

def create_user(username, password):
    if get_user_by_name(username) == None:
        users.insert_one({
            "username": username,
            "password": hash_password(username, password),
            "games": [],
            "games_played": {}
        })
        return True
    return False

def get_user_by_name(username):
    return users.find_one({"username": username})

def get_user_by_id(userid):
    return users.find_one({"_id": ObjectId(userid)})

def authenticate(username, password):
    user = get_user_by_name(username)
    if user == None:
        return False
    return user["password"] == hashPass(username, password)

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
