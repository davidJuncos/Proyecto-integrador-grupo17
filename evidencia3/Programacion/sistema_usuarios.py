# sistema_usuarios.py
from usuario import Usuario
from usuario import Acceso 
from datetime import datetime
import pickle

class SistemaUsuarios:
    FILE_NAME_USUARIOS = 'usuarios.ispc'
    FILE_NAME_ACCESOS = 'accesos.ispc'
    FILE_NAME_LOGS = 'logs.txt'

    usuarios_ordenados = False

    @staticmethod
    def cargar_usuarios():
        try:
            with open(SistemaUsuarios.FILE_NAME_USUARIOS, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []
        except Exception as e:
            print(f"Error al cargar usuarios: {e}")
            return []
        
    @staticmethod
    def crear_usuario():
        user_id = int(input("Ingresa el ID del usuario: "))
        username = input("Ingresa el nombre de usuario: ")
        password = input("Ingresa la contraseña: ")
        email = input("Ingresa el email: ")

        usuario = Usuario(user_id, username, password, email)
        SistemaUsuarios.agregar_usuario(usuario)
        print(f"Usuario {username} creado y registrado en 'usuarios.ispc'.")

    @staticmethod
    def guardar_usuarios(usuarios):
        with open(SistemaUsuarios.FILE_NAME_USUARIOS, 'wb') as file:
            pickle.dump(usuarios, file)

    @staticmethod
    def agregar_usuario(usuario):
        usuarios = SistemaUsuarios.cargar_usuarios()
        usuarios.append(usuario)
        SistemaUsuarios.guardar_usuarios(usuarios)

    @staticmethod
    def modificar_usuario(username, new_data):
        usuarios = SistemaUsuarios.cargar_usuarios()
        for usuario in usuarios:
            if usuario.username == username:
                usuario.username = new_data.get('username', usuario.username)
                usuario.password = new_data.get('password', usuario.password)
                usuario.email = new_data.get('email', usuario.email)
                SistemaUsuarios.guardar_usuarios(usuarios)
                print(f"Usuario {username} modificado exitosamente.")
                return
        print(f"Usuario {username} no encontrado.")

    @staticmethod
    def eliminar_usuario(username_or_email):
        usuarios = SistemaUsuarios.cargar_usuarios()
        usuarios_filtrados = [usuario for usuario in usuarios if usuario.username != username_or_email and usuario.email != username_or_email]
        if len(usuarios_filtrados) != len(usuarios):
            SistemaUsuarios.guardar_usuarios(usuarios_filtrados)
            print(f"Usuario {username_or_email} eliminado exitosamente.")
        else:
            print(f"Usuario {username_or_email} no encontrado.")

    @staticmethod
    def busqueda_binaria(usuarios, username):
        inicio, fin = 0, len(usuarios) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if usuarios[medio].username == username:
                return usuarios[medio]
            elif usuarios[medio].username < username:
                inicio = medio + 1
            else:
                fin = medio - 1
        return None

    @staticmethod
    def buscar_usuario(username_or_email):
        usuarios = SistemaUsuarios.cargar_usuarios()

        if SistemaUsuarios.usuarios_ordenados:
            print("Búsqueda realizada por técnica binaria.")
            usuario = SistemaUsuarios.busqueda_binaria(usuarios, username_or_email)
            if usuario:
                return usuario
        else:
            print("Búsqueda realizada por técnica secuencial.")
            for usuario in usuarios:
                if usuario.username == username_or_email or usuario.email == username_or_email:
                    return usuario
        return None

    @staticmethod
    def mostrar_usuarios():
        usuarios = SistemaUsuarios.cargar_usuarios()
        if usuarios:
            for usuario in usuarios:
                print(usuario)
        else:
            print("No hay usuarios registrados.")

    @staticmethod
    def registrar_acceso_exitoso(username):
        acceso = Acceso(username)
        with open(SistemaUsuarios.FILE_NAME_ACCESOS, 'ab') as file:
            pickle.dump(acceso, file)
        print(f"Se registró el acceso exitoso de {username} en 'accesos.ispc'.")

    @staticmethod
    def registrar_acceso_fallido(username, password):
        fecha_actual = datetime.now()
        with open(SistemaUsuarios.FILE_NAME_LOGS, 'a') as log_file:
            log_file.write(f"[{fecha_actual}] Intento fallido de acceso - Usuario: {username}, Clave: {password}\n")
        print(f"Se registró el intento fallido de {username} en 'logs.txt'.")

    @staticmethod
    def cargar_y_mostrar_accesos():
        """Función para cargar y mostrar el contenido del archivo accesos.ispc"""
        try:
            with open(SistemaUsuarios.FILE_NAME_ACCESOS, 'rb') as file:
                while True:
                    try:
                        acceso = pickle.load(file)
                        print(acceso)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("El archivo accesos.ispc no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    @staticmethod
    def ordenar_por_python(usuarios):
        usuarios.sort(key=lambda x: x.username)
        SistemaUsuarios.usuarios_ordenados = True
        print("Usuarios ordenados usando sort() de Python.")
        SistemaUsuarios.guardar_usuarios(usuarios)

    @staticmethod
    def ordenar_por_burbuja(usuarios):
        n = len(usuarios)
        for i in range(n):
            for j in range(0, n - i - 1):
                if usuarios[j].username > usuarios[j + 1].username:
                    usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]
        SistemaUsuarios.usuarios_ordenados = True
        print("Usuarios ordenados usando Burbuja.")
        SistemaUsuarios.guardar_usuarios(usuarios)