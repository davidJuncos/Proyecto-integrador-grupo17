# usuario.py
from datetime import datetime


class Usuario:
    def __init__(self, user_id, username, password, email, dni):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__email = email
        self.__dni= dni
        self.accesos = []  # Lista para almacenar los accesos del usuario
        
    
    def get_user_id(self):
        return self.__user_id

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_dni(self):
        return self.__dni

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_email(self, email):
        self.__email = email

    def set_dni(self, dni):
        self.__dni = dni


    def __str__(self):
        return f"Usuario(ID: {self.user_id}, Username: {self.username}, Email: {self.email}, dni: {self.dni})"
    
    def __repr__(self):
        return f"Usuario(username='{self.user_id}', nombre='{self.username}', email='{self.email}', dni='{self.dni}')"
    

class Acceso:
    def __init__(self, username):
        self.username = username
        self.fecha_acceso = datetime.now()
    
    def get_username(self):
        return self.__username

    # Setters
    def set_username(self, username):
        self.__username = username

    def __str__(self):
        return f"Usuario: {self.username}, Fecha de acceso: {self.fecha_acceso}"


