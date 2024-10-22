import pickle
from datetime import datetime

class Usuario:
    def __init__(self, user_id, username, password, email):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.accesos = []  # Lista para almacenar los accesos del usuario

    def __str__(self):
        return f"Usuario(ID: {self.user_id}, Username: {self.username}, Email: {self.email})"
    
    def __repr__(self):
        return f"Usuario(username='{self.user_id}', nombre='{self.username}', email='{self.email}')"

class Acceso:
    def __init__(self, username):
        self.username = username
        self.fecha_acceso = datetime.now()

    def __str__(self):
        return f"Usuario: {self.username}, Fecha de acceso: {self.fecha_acceso}"


class SistemaUsuarios:
    FILE_NAME_USUARIOS = 'usuarios.ispc'
    FILE_NAME_ACCESOS = 'accesos.ispc'
    FILE_NAME_LOGS = 'logs.txt'

    usuarios_ordenados = False #controlar si los usuarios están ordenados
    
    @staticmethod
    def cargar_usuarios():
        try:
            with open(SistemaUsuarios.FILE_NAME_USUARIOS, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

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
    def buscar_usuario(username):
        usuarios = SistemaUsuarios.cargar_usuarios()

        if SistemaUsuarios.usuarios_ordenados:
            print("Búsqueda realizada por técnica binaria.")
            return SistemaUsuarios.busqueda_binaria(usuarios, username)
        else:
            print("Búsqueda realizada por técnica secuencial.")
            for usuario in usuarios:
                if usuario.username == username:
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
        print(f"Se registró el intento fallido de {username} en 'logs.txt'. ")

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

def crear_usuario():
    user_id = int(input("Ingresa el ID del usuario: "))
    username = input("Ingresa el nombre de usuario: ")
    password = input("Ingresa la contraseña: ")
    email = input("Ingresa el email: ")

    usuario = Usuario(user_id, username, password, email)
    SistemaUsuarios.agregar_usuario(usuario)
    print(f"Usuario {username} creado exitosamente y registrado en 'usuarios.ispc'.")


def modificar_usuario():
    username = input("Ingresa el nombre de usuario a modificar: ")
    new_username = input("Nuevo nombre de usuario (dejar en blanco para no cambiar): ")
    new_password = input("Nueva contraseña (dejar en blanco para no cambiar): ")
    new_email = input("Nuevo email (dejar en blanco para no cambiar): ")

    new_data = {}
    if new_username:
        new_data['username'] = new_username
    if new_password:
        new_data['password'] = new_password
    if new_email:
        new_data['email'] = new_email

    SistemaUsuarios.modificar_usuario(username, new_data)


def eliminar_usuario():
    username_or_email = input("Ingresa el username o email del usuario a eliminar: ")
    SistemaUsuarios.eliminar_usuario(username_or_email)


def buscar_usuario():
    username_or_email = input("Ingresa el username o email del usuario a buscar: ")
    usuario = SistemaUsuarios.buscar_usuario(username_or_email)
    if usuario:
        print(usuario)
    else:
        print("Usuario no encontrado.")


def iniciar_sesion():
    username = input("Ingresa el nombre de usuario: ")
    password = input("Ingresa la contraseña: ")

    usuario = SistemaUsuarios.buscar_usuario(username)
    if usuario and usuario.password == password:
        print(f"Ingreso exitoso para {usuario.username}.")
        SistemaUsuarios.registrar_acceso_exitoso(username)
        while True:
            print("\nMenú de Usuario")
            print("1. Volver al menú principal")
            print("2. Salir de la aplicación")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                break
            elif opcion == '2':
                print("Saliendo...")
                exit()
            else:
                print("Opción no válida.")
    else:
        print("Usuario o contraseña incorrectos.")
        SistemaUsuarios.registrar_acceso_fallido(username, password)

   


def menu_ordenamiento():
    print("\nOpciones de ordenamiento:")
    print("1. Ordenar por Burbuja")
    print("2. Ordenar usando sort() de Python")
    opcion = input("Elige una opción: ")

    usuarios = SistemaUsuarios.cargar_usuarios()

    if opcion == '1':
        SistemaUsuarios.ordenar_por_burbuja(usuarios)
    elif opcion == '2':
        SistemaUsuarios.ordenar_por_python(usuarios)
    else:
        print("Opción no válida.")


def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Agregar un nuevo usuario")
        print("2. Modificar un usuario")
        print("3. Eliminar un usuario")
        print("4. Buscar usuario por username o email")
        print("5. Mostrar todos los usuarios")
        print("6. Ingresar al sistema")
        print("7. Ver accesos desde el archivo binario")
        print("8. Ordenar usuarios")
        print("9. Salir de la aplicación")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            crear_usuario()
        elif opcion == '2':
            modificar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            buscar_usuario()
        elif opcion == '5':
            SistemaUsuarios.mostrar_usuarios()
        elif opcion == '6':
            iniciar_sesion()
        elif opcion == '7':
            SistemaUsuarios.cargar_y_mostrar_accesos()
        elif opcion == '8':
            menu_ordenamiento()  # Llamada al menú de ordenamiento
        elif opcion == '9':
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()
