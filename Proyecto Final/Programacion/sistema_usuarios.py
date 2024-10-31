from usuario import Usuario
from usuario import Acceso 
from datetime import datetime
import pickle
import os

class SistemaUsuarios:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROGRAMACION_DIR = os.path.join(SCRIPT_DIR, '..', 'Programacion')
    BUSQUEDA_BINARIA_DNI_DIR = os.path.join(SCRIPT_DIR, '..', 'búsquedasYordenamientos')

    FILE_NAME_USUARIOS = os.path.join(PROGRAMACION_DIR, 'usuarios.ispc')
    FILE_NAME_ACCESOS = os.path.join(PROGRAMACION_DIR, 'accesos.ispc')
    FILE_NAME_LOGS = os.path.join(PROGRAMACION_DIR, 'logs.txt')

    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    FILE_NAME_LOGS_BUSQUEDA_BINARIA_DNI = os.path.join(BUSQUEDA_BINARIA_DNI_DIR, f'buscandoUsuarioPorDNI-{fecha_actual}.txt')
    FILE_NAME_LOGS_BUSQUEDA_BINARIA_USERNAME = os.path.join(BUSQUEDA_BINARIA_DNI_DIR, f'buscandoUsuarioPorUsername-{fecha_actual}.txt')

    usuarios_ordenados = False

    @staticmethod
    def mostrar_usuarios():
        usuarios_principal = SistemaUsuarios.cargar_usuarios()
        usuarios_ordenados = SistemaUsuarios.cargar_usuarios_ordenados()

        print("\n--- Usuarios del archivo 'usuarios.ispc' ---")
        if usuarios_principal:
            for usuario in usuarios_principal:
                print(usuario)
        else:
            print("No hay usuarios registrados en 'usuarios.ispc'.")

        print("\n--- Usuarios del archivo 'usuariosOrdenadosPorUsername.ispc' ---")
        if usuarios_ordenados:
            for usuario in usuarios_ordenados:
                print(usuario)
        else:
            print("No se encontraron usuarios en 'usuariosOrdenadosPorUsername.ispc'.")

    @staticmethod
    def cargar_usuarios_ordenados():
        file_path = os.path.join(SistemaUsuarios.PROGRAMACION_DIR, 'usuariosOrdenadosPorUsername.ispc')
        try:
            with open(file_path, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    @staticmethod
    def cargar_usuarios():
        try:
            with open(SistemaUsuarios.FILE_NAME_USUARIOS, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    @staticmethod
    def crear_usuario():
        user_id = int(input("Ingresa el ID del usuario: "))
        username = input("Ingresa el nombre de usuario: ")
        password = input("Ingresa la contraseña: ")
        email = input("Ingresa el email: ")
        dni = input("Ingrese el D.N.I.:")
        usuario = Usuario(user_id, username, password, email, dni)
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
        usuarios.sort(key=lambda u: int(u.dni))
        SistemaUsuarios.guardar_usuarios(usuarios)
        print(f"Usuario {usuario.username} agregado y usuarios ordenados por DNI.")

    @staticmethod
    def modificar_usuario(username, new_data):
        usuarios = SistemaUsuarios.cargar_usuarios()
        for usuario in usuarios:
            if usuario.username == username:
                usuario.username = new_data.get('username', usuario.username)
                usuario.password = new_data.get('password', usuario.password)
                usuario.email = new_data.get('email', usuario.email)
                usuario.dni = new_data.get('dni', usuario.dni)
                SistemaUsuarios.guardar_usuarios(usuarios)
                print(f"Usuario {username} modificado exitosamente.")
                return
        print(f"Usuario {username} no encontrado.")

    @staticmethod
    def eliminar_usuario(username_or_email):
        usuarios = SistemaUsuarios.cargar_usuarios()
        usuarios = [usuario for usuario in usuarios if usuario.username != username_or_email and usuario.email != username_or_email]
        SistemaUsuarios.guardar_usuarios(usuarios)
        print(f"Usuario {username_or_email} eliminado exitosamente." if len(usuarios) else "Usuario no encontrado.")

    @staticmethod
    def iniciar_sesion():
        username = input("Ingresa tu nombre de usuario: ")
        password = input("Ingresa tu contraseña: ")
        usuario = SistemaUsuarios.buscar_usuario(username)

        if usuario:
            if usuario.password == password:
                print("Inicio de sesión exitoso.")
                SistemaUsuarios.registrar_acceso_exitoso(username)
            else:
                print("Contraseña incorrecta.")
                SistemaUsuarios.registrar_acceso_fallido(username, password)
        else:
            print("Usuario no encontrado.")
            SistemaUsuarios.registrar_acceso_fallido(username, password)

    @staticmethod
    def buscar_usuario(username_or_email_or_DNI):
        usuarios = SistemaUsuarios.cargar_usuarios()
        if SistemaUsuarios.usuarios_ordenados:
            print("Búsqueda realizada por técnica binaria.")
            return SistemaUsuarios.busqueda_binaria(usuarios, username_or_email_or_DNI)
        else:
            print("Búsqueda realizada por técnica secuencial.")
            return next((u for u in usuarios if u.username == username_or_email_or_DNI or u.email == username_or_email_or_DNI or u.dni == username_or_email_or_DNI), None)

    @staticmethod
    def registrar_acceso_exitoso(username):
        acceso = Acceso(username)
        with open(SistemaUsuarios.FILE_NAME_ACCESOS, 'ab') as file:
            pickle.dump(acceso, file)
        print(f"Se registró el acceso exitoso de {username} en 'accesos.ispc'.")

    @staticmethod
    def registrar_acceso_fallido(username, password):
        with open(SistemaUsuarios.FILE_NAME_LOGS, 'a') as log_file:
            log_file.write(f"[{datetime.now()}] Intento fallido de acceso - Usuario: {username}, Clave: {password}\n")
        print(f"Se registró el intento fallido de {username} en 'logs.txt'.")

    @staticmethod
    def busqueda_binaria(usuarios, clave_busqueda, clave="username"):
        inicio, fin = 0, len(usuarios) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            valor_medio = getattr(usuarios[medio], clave)
            if valor_medio == clave_busqueda:
                return usuarios[medio]
            elif valor_medio < clave_busqueda:
                inicio = medio + 1
            else:
                fin = medio - 1
        return None

    @staticmethod
    def crear_directorio_logs():
        os.makedirs("búsquedasYordenamientos", exist_ok=True)
