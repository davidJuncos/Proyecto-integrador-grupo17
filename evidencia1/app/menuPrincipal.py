# from datetime import datetime
# import re
# import captcha  


# usuarios = {}

# # Función para validar el nombre de usuario
# def es_nombre_usuario_valido(nombre_usuario):
#     if not (6 <= len(nombre_usuario) <= 12):
#         raise ValueError("El nombre de usuario debe tener entre 6 y 12 caracteres.")
#     return True

# # Función para validar la clave
# def es_clave_valida(clave):
#     if len(clave) < 8:
#         raise ValueError("La clave debe tener al menos 8 caracteres.")
    
#     tiene_minuscula = re.search(r'[a-z]', clave)
#     tiene_mayuscula = re.search(r'[A-Z]', clave)
#     tiene_numero = re.search(r'[0-9]', clave)
#     tiene_caracter_especial = re.search(r'[\W_]', clave)
    
#     condiciones_cumplidas = sum([bool(tiene_minuscula), bool(tiene_mayuscula), bool(tiene_numero), bool(tiene_caracter_especial)])
#     if condiciones_cumplidas < 2:
#         raise ValueError("La clave debe cumplir al menos dos de las siguientes condiciones: minúscula, mayúscula, número, carácter especial.")
    
#     return True

# # Función para registrar un ingreso
# def registrar_ingreso(nombre_usuario):
#     fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open("ingresos.txt", "a") as file:
#         file.write(f"Usuario: {nombre_usuario}, Fecha de ingreso: {fecha_ingreso}\n")
#     print(f"Ingreso exitoso. Registro guardado en 'ingresos.txt'.")

# # Función para iniciar sesión
# def iniciar_sesion():
#     nombre_usuario = input("Ingresa tu nombre de usuario: ")
    
#     if nombre_usuario not in usuarios:
#         print("Usuario no encontrado. Regístrese primero.")
#         return
    
#     captcha.main()  # Valida el captcha antes de permitir el ingreso

#     intentos_fallidos = 0
#     while intentos_fallidos < 4:
#         clave_ingresada = input("Ingresa tu clave: ")
        
#         if clave_ingresada == usuarios[nombre_usuario]['clave']:
#             print("Ingreso exitoso.")
#             registrar_ingreso(nombre_usuario)
#             # Registrar el acceso exitoso
#             with open("ingresos.txt", "a") as file:
#                 file.write(f"Usuario: {nombre_usuario}, Fecha de acceso exitoso: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
#             break
#         else:
#             intentos_fallidos += 1
#             print(f"Clave incorrecta. Intentos fallidos: {intentos_fallidos}/4.")
            
#             if intentos_fallidos == 4:
#                 print("Usuario bloqueado por demasiados intentos fallidos.")
#                 # Registrar el bloqueo
#                 with open("log.txt", "a") as file:
#                     file.write(f"Usuario: {nombre_usuario}, Bloqueado por 4 intentos fallidos el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
#                 break

# # Función de recuperación de contraseña (aún no implementada)
# def olvido_contraseña():
#     print("La funcionalidad de recuperación de contraseña aún no está implementada.")

# # Función para crear un nuevo usuario
# def crear_usuario():
#     while True:
#         try:
#             nombre_usuario = input("Ingresa un nombre de usuario: ")

#             # Validar el nombre de usuario
#             es_nombre_usuario_valido(nombre_usuario)
#             if nombre_usuario in usuarios:
#                 raise ValueError("El nombre de usuario ya está registrado.")

#             # Validar la clave
#             clave = input("Ingresa una contraseña: ")
#             es_clave_valida(clave)
            
#             captcha.main()  # Validar captcha antes de registrar el usuario

#             # Agregar el usuario al diccionario
#             usuarios[nombre_usuario] = {
#                 'clave': clave,
#                 'creado_el': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             }

#             # Registrar la creación del usuario
#             with open("usuariosCreados.txt", "a") as file:
#                 file.write(f"Usuario: {nombre_usuario}, Clave: {clave}, Creado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
#             print("Usuario creado exitosamente.")
#             break

#         except ValueError as e:
#             print(f"Error: {e}. Intenta de nuevo.")
#         except Exception as e:
#             print(f"Error inesperado: {e}. Intenta de nuevo.")

# # Menú principal
# def menu_principal():
#     while True:
#         print("\n--- Menú Principal ---")
#         print("1. Iniciar sesión")
#         print("2. Olvidé la contraseña")
#         print("3. Crear un nuevo usuario")
#         print("4. Salir")
        
#         opcion = input("Selecciona una opción: ")
        
#         if opcion == '1':
#             iniciar_sesion()
#         elif opcion == '2':
#             olvido_contraseña()
#         elif opcion == '3':
#             crear_usuario()
#         elif opcion == '4':
#             print("Saliendo del sistema...")
#             break
#         else:
#             print("Opción no válida. Intenta nuevamente.")

# # Ejecutar el menú principal
# if __name__ == "__main__":
#     menu_principal()

import pickle
from datetime import datetime

# Clase Usuario que tiene un ID, username, password y email
class Usuario:
    def __init__(self, user_id, username, password, email):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.accesos = []  # Lista para almacenar los accesos del usuario

    def __str__(self):
        return f"Usuario(ID: {self.user_id}, Username: {self.username}, Email: {self.email})"

# Clase Acceso que registra la fecha de ingreso y salida del usuario logueado
class Acceso:
    def __init__(self, acceso_id, fecha_ingreso, fecha_salida, usuario_logueado):
        self.acceso_id = acceso_id
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.usuario_logueado = usuario_logueado  # Este es un objeto de tipo Usuario

    def __str__(self):
        return (f"Acceso(ID: {self.acceso_id}, Ingreso: {self.fecha_ingreso}, "
                f"Salida: {self.fecha_salida}, Usuario: {self.usuario_logueado.username})")

# Clase para manejar el CRUD de usuarios y accesos
class SistemaUsuarios:
    FILE_NAME_USUARIOS = 'usuarios.ispc'
    FILE_NAME_ACCESOS = 'accesos.ispc'
    LOG_FILE = 'logs.txt'

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
    def obtener_usuario(username):
        usuarios = SistemaUsuarios.cargar_usuarios()
        for usuario in usuarios:
            if usuario.username == username:
                return usuario
        return None

    @staticmethod
    def cargar_accesos():
        try:
            with open(SistemaUsuarios.FILE_NAME_ACCESOS, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    @staticmethod
    def guardar_acceso(acceso):
        accesos = SistemaUsuarios.cargar_accesos()
        accesos.append(acceso)
        with open(SistemaUsuarios.FILE_NAME_ACCESOS, 'wb') as file:
            pickle.dump(accesos, file)

    @staticmethod
    def registrar_intento_fallido(username, password):
        with open(SistemaUsuarios.LOG_FILE, 'a') as file:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Intento fallido el {fecha}. Usuario: {username}, Clave: {password}\n")
        print(f"Intento fallido registrado en logs.txt.")

    @staticmethod
    def mostrar_usuarios():
        usuarios = SistemaUsuarios.cargar_usuarios()
        for usuario in usuarios:
            print(usuario)
            for acceso in usuario.accesos:
                print(f"  {acceso}")

# Función para crear un nuevo usuario
def crear_usuario():
    user_id = int(input("Ingresa el ID del usuario: "))
    username = input("Ingresa el nombre de usuario: ")
    password = input("Ingresa la contraseña: ")
    email = input("Ingresa el email: ")
    
    usuario = Usuario(user_id, username, password, email)
    SistemaUsuarios.agregar_usuario(usuario)
    print(f"Usuario {username} creado exitosamente.")

# Función para registrar un acceso exitoso
def registrar_acceso(usuario):
    acceso_id = len(usuario.accesos) + 1
    fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fecha_salida = 'Pendiente'  # Fecha de salida se completa más tarde
    acceso = Acceso(acceso_id, fecha_ingreso, fecha_salida, usuario)

    # Guardar el acceso en la lista del usuario
    usuario.accesos.append(acceso)
    SistemaUsuarios.guardar_usuarios(SistemaUsuarios.cargar_usuarios())

    # Guardar el acceso en el archivo binario
    SistemaUsuarios.guardar_acceso(acceso)

    print(f"Acceso registrado para el usuario {usuario.username}.")

# Función para iniciar sesión
def iniciar_sesion():
    username = input("Ingresa el nombre de usuario: ")
    password = input("Ingresa la contraseña: ")

    usuario = SistemaUsuarios.obtener_usuario(username)
    
    if usuario and usuario.password == password:
        print(f"Ingreso exitoso para {username}.")
        registrar_acceso(usuario)
        
        while True:
            print("Menú de Usuario")
            print("1. Volver al menú principal")
            print("2. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                break
            elif opcion == '2':
                # Registrar la salida del usuario antes de salir
                marcar_salida(usuario)
                print("Saliendo...")
                exit()
            else:
                print("Opción no válida.")
    else:
        print("Usuario o contraseña incorrectos.")
        SistemaUsuarios.registrar_intento_fallido(username, password)

# Función para marcar salida de un acceso
def marcar_salida(usuario):
    if usuario and usuario.accesos:
        acceso_actual = usuario.accesos[-1]  # Obtener el último acceso
        if acceso_actual.fecha_salida == 'Pendiente':
            acceso_actual.fecha_salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Guardar los accesos actualizados del usuario en el archivo binario
            SistemaUsuarios.guardar_usuarios(SistemaUsuarios.cargar_usuarios())

            # Guardar también el acceso actualizado en el archivo de accesos
            accesos = SistemaUsuarios.cargar_accesos()
            for acc in accesos:
                if acc.acceso_id == acceso_actual.acceso_id and acc.usuario_logueado.username == usuario.username:
                    acc.fecha_salida = acceso_actual.fecha_salida
                    break
            with open(SistemaUsuarios.FILE_NAME_ACCESOS, 'wb') as file:
                pickle.dump(accesos, file)
            
            print(f"Salida registrada para el usuario {usuario.username}.")
        else:
            print(f"El último acceso ya tiene registrada una salida: {acceso_actual.fecha_salida}")
    else:
        print("Usuario no encontrado o sin accesos.")

# Menú principal
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear un nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Mostrar todos los usuarios y accesos")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            crear_usuario()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            SistemaUsuarios.mostrar_usuarios()
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()
