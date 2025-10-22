from cryptography.fernet import Fernet

class Encryption:
    def __init__(self):
        pass

    def encrypt(self, user_id, message, receiver_id):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        message = fernet.encrypt(message.encode())
        return [user_id,message.decode(),receiver_id]
