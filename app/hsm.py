from flask import Flask, request, jsonify, abort
import os
import base64

app = Flask(__name__)
KEYS = {}

@app.post("/hsm/get_key")
def get_key():
    user_id = request.json.get("user_id")
    if user_id not in KEYS:
        KEYS[user_id] = 'test'
    return jsonify({"key": KEYS[user_id]})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
