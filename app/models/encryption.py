from flask import g
import sqlite3
import os
import base64

from cryptography.fernet import Fernet
import requests

class Encryption:
    def __init__(self):
        self.hsm_get_key = "http://localhost:5000/hsm/get_key"

    def get_db(self):
        if "db" not in g:
            g.db = sqlite3.connect("./databases/database.db")
        return g.db

    def fetch_key(self, user_id:int, receiver_id:int,salt:str):
        response = requests.post(self.hsm_get_key, json={"user_id": user_id, "receiver_id":receiver_id, "salt":salt})
        data = response.json()
        return data['key'].encode()

    def encrypt(self, user_id, message, receiver_id):
        salt = os.urandom(16)
        saltdecoded = base64.urlsafe_b64encode(salt).decode()
        key = self.fetch_key(user_id,receiver_id,saltdecoded)
        fernet = Fernet(key)
        message = fernet.encrypt(message.encode())
        db = self.get_db()
        query = "INSERT INTO messages (user_id, message, receiver_id,salt) VALUES (?, ?, ?, ?)"
        result = db.execute(query, (user_id, message, receiver_id, saltdecoded))
        db.commit()
        print("key to encrypt", key, "message",message)
        if result:
            return {'message': message.decode()}
        else:
            return {'error': 'Failed to encrypt message'}


    def decrypt(self, receiver_id):
        db = self.get_db()
        query = "SELECT * FROM messages WHERE receiver_id=? ORDER BY id DESC LIMIT 1"
        result = db.execute(query, (receiver_id,)).fetchone()

        key = self.fetch_key(result[1], result[2], result[4])
        fernet = Fernet(key)

        message = fernet.decrypt(result[3])
        print("key to decrypt", key, "message", result[3])
        return {'message': message.decode()}