# usuario.py
from datetime import datetime


class Usuario:
    def __init__(self, user_id, username, password, email, dni):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
<<<<<<< HEAD:Proyecto_Final/Programacion/usuario.py
        self._dni = dni 
=======
        self.dni= dni
>>>>>>> 3551e7d98f076b24f0eaa1b5a644a1c527676160:Proyecto Final/Programacion/usuario.py
        self.accesos = []  # Lista para almacenar los accesos del usuario
        
    def get_dni(self):
        return self._dni
        

    def __str__(self):
        return f"Usuario(ID: {self.user_id}, Username: {self.username}, Email: {self.email}, dni: {self.dni})"
    
    def __repr__(self):
        return f"Usuario(username='{self.user_id}', nombre='{self.username}', email='{self.email}', dni='{self.dni}')"
    

class Acceso:
    def __init__(self, username):
        self.username = username
        self.fecha_acceso = datetime.now()

    def __str__(self):
        return f"Usuario: {self.username}, Fecha de acceso: {self.fecha_acceso}"


