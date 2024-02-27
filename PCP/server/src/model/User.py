import secrets
from hashlib import sha512

class User:
    def __init__(self, first_name, last_name, email=None, phone_number=None, username=None, password=None, session_key=None):
        """

        @param id:
        @param first_name:
        @param last_name:
        @param email:
        @param phone_number:
        @param username:
        @param password:
        @param session_key;
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.username = username
        if password is not None:
            self.__password_hash = str(sha512(password.encode()).hexdigest())
        else:
            self.__password_hash = None
        self.__session_key = None

    def match_password(self, password):
        return str(sha512(password.encode()).hexdigest()) == self.__password_hash

    def create_session_key(self):
        self.__session_key = secrets.token_hex(64)
        return self.__session_key

    def match_session_key(self, session_key):
        if self.__session_key is None or self.__session_key == "NA":
            return False
        return self.__session_key == session_key

    def reset_session_key(self):
        self.__session_key = "NA"

    def set_password(self, password):
        if password is not None:
            self.__password_hash = str(sha512(password.encode()).hexdigest())