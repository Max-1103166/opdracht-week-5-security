from flask import *
from models.encryption import Encryption

send_message_bp = Blueprint('send_message', __name__)

@send_message_bp.route('/api/send_message', methods=['POST'])
def send_message():

    user_id = request.json['user_id']
    message = request.json['message']
    receiver_id = request.json['receiver_id']
    encryption = Encryption()

    encrypted_message = encryption.encrypt(user_id,message,receiver_id)
    return jsonify({'message': encrypted_message})
