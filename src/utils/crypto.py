from __future__ import annotations

from cryptography.fernet import Fernet

from config.app_config import ENCRYPTION_KEY


class CryptoManager:

    def __init__(self, key=None):
        self.key = ENCRYPTION_KEY
        self.cipher = Fernet(self.key.encode())

    def encrypt(self, plain_text: str) -> str:
        return self.cipher.encrypt(plain_text.encode()).decode()

    def decrypt(self, cipher_text: str) -> str:
        return self.cipher.decrypt(cipher_text.encode()).decode()
