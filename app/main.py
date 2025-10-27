from flask import Flask, render_template, blueprints
from controllers.send_message import send_message_bp
from controllers.retrieve_message import retrieve_message_bp
app = Flask(__name__, static_folder='static/', template_folder='templates/')

app.register_blueprint(send_message_bp)
app.register_blueprint(retrieve_message_bp)
@app.route('/')
def main():
    users = [
        {
            "id" : 1,
            "name": "max",
        },
        {
            "id" : 2,
            "name": "sophia",
        },
        {
            "id" : 3,
            "name" : "sam"
        }
    ]
    return render_template('encrypt_decrypt_message.html', users=users)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)