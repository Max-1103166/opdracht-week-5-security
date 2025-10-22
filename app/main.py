from flask import Flask, render_template
app = Flask(__name__, static_folder='static/', template_folder='templates/')
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
    app.run(debug=True)