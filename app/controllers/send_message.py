from flask import *
from models.encryption import Encryption

send_message_bp = Blueprint('send_message', __name__)

@send_message_bp.route('/api/send_message', methods=['POST'])
def send_message():


    data = request.get_json()
    if not data:
        return jsonify({"error": "Data not found"}), 404

    user_id = request.json['user_id']
    message = request.json['message']
    receiver_id = request.json['receiver_id']
    encryption = Encryption()

    result = encryption.encrypt(user_id,message,receiver_id)
    if result:
        return jsonify({"success": True, "messages": result}), 200
    else:
        return jsonify({"success": False}), 400
