from flask import *
from models.encryption import Encryption

retrieve_message_bp = Blueprint('retrieve_message', __name__)

@retrieve_message_bp.route('/api/retrieve_message', methods=['GET', 'POST'])
def retrieve_message():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data not found"}), 404
    receiver_id = request.json['receiver_id']

    encryption = Encryption()

    result = encryption.decrypt(receiver_id)
    if result:
        return jsonify({"success": True, "messages": result}), 200
    else:
        return jsonify({"success": False}), 400
