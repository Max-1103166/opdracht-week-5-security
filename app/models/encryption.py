import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class Encryption:
    def __init__(self):
        pass

    def encrypt(self, user_id, message, receiver_id):
        receiver_password = "dit is een geheim wachtwoord"

        salt = os.urandom(16)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1_200_000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(receiver_password.encode()))
        fernet = Fernet(key)
        message = fernet.encrypt(message.encode())
        salt = base64.urlsafe_b64encode(salt)
        return {'message': message.decode(), 'salt': salt.decode()}

    def decrypt(self, receiver_id):
        print("test", receiver_id)
        return {'message': receiver_id}