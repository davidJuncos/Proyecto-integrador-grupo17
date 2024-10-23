import pickle
from datetime import datetime
import os
import random
import csv
from graficos_registros import Graficos
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

    usuarios_ordenados = False  # Controlar si los usuarios están ordenados

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

# Clase para la gestión de registros pluviales
class RegistrosPluviales:
    @staticmethod
    def obtener_ruta_archivo_csv(anio):
        directorio = os.path.dirname(__file__)  # Ruta actual del archivo .py
        ruta_completa = os.path.join(directorio, f"registroPluvial{anio}.csv")
        return ruta_completa
    
    @staticmethod
    def cargar_o_generar_registros(anio):
        nombre_archivo = RegistrosPluviales.obtener_ruta_archivo_csv(anio)
        # Verificar si el archivo existe
        if os.path.exists(nombre_archivo):
            try:
                print(f"Archivo {nombre_archivo} encontrado. Cargando datos...")
                return RegistrosPluviales.cargar_registros_csv(nombre_archivo)
            except Exception as e:
                print(f"Error al cargar el archivo CSV: {e}. Generando datos aleatorios...")
                registros = RegistrosPluviales.generar_registros_aleatorios()
                RegistrosPluviales.guardar_registros_csv(nombre_archivo, registros)
                return registros
        else:
            print(f"Archivo {nombre_archivo} no encontrado. Generando datos aleatorios...")
            registros = RegistrosPluviales.generar_registros_aleatorios()
            RegistrosPluviales.guardar_registros_csv(nombre_archivo, registros)
            return registros

    @staticmethod
    def cargar_registros_csv(nombre_archivo):
        registros = []
        with open(nombre_archivo, mode='r') as file:
            csv_reader = csv.reader(file)
            for fila in csv_reader:
                registros.append([int(dia) for dia in fila])
        return registros

    @staticmethod
    def guardar_registros_csv(nombre_archivo, registros):
        with open(nombre_archivo, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(registros)
        print(f"Registros guardados en {nombre_archivo}.")

    @staticmethod
    def generar_registros_aleatorios():
        registros = []
        # 12 meses: 31 días (excepto febrero que tiene 28, pero simplificamos aquí)
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for dias in dias_por_mes:
            mes = [random.randint(0, 100) for _ in range(dias)]  # Generar lluvias aleatorias (0 a 100 mm)
            registros.append(mes)
        return registros

    @staticmethod
    def mostrar_registros_por_mes(registros, mes):
        # Mes: Enero=1, Febrero=2, etc.
        if 1 <= mes <= 12:
            print(f"Registros de lluvia para el mes {mes}:")
            for dia, lluvia in enumerate(registros[mes - 1], start=1):
                print(f"Día {dia}: {lluvia} mm")
        else:
            print("Mes inválido. Debes ingresar un número entre 1 y 12.")

def crear_usuario():
    user_id = int(input("Ingresa el ID del usuario: "))
    username = input("Ingresa el nombre de usuario: ")
    password = input("Ingresa la contraseña: ")
    email = input("Ingresa el email: ")

    usuario = Usuario(user_id, username, password, email)
    SistemaUsuarios.agregar_usuario(usuario)
    print(f"Usuario {username} creado exitosamente y registrado en 'usuarios.ispc'.")

def menu_graficos(registros):
    while True: 
        print("\n--- Menú de Gráficos ---") 
        print("1. Grafico de Lluvias Anual por Mes")
        print("2. Grafico de Lluvias Diarias por Mes")
        print("3. Gráfico de Proporción de Lluvias por Mes")
        print("4. Salir")
        opcion = input("Selecciona una opción:")
        
        if opcion == "1":
            Graficos.graficar_lluvias_anuales_barra(registros)
        elif opcion == "2":
            Graficos.graficar_dispersión_lluvias_dia_mes(registros)
        elif opcion == "3":
            Graficos.graficar_proporcion_lluvia_mes(registros)
        elif opcion == "4":
            break
        else: 
            print("Opción no váliada")    

def menu_usuarios():
    while True:
        print("\n--- Menú de Usuarios ---")
        print("1. Crear Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Mostrar Usuarios")
        print("6. Ordenar Usuarios")
        print("7. Cargar Accesos")
        print("8. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            crear_usuario()
        elif opcion == '2':
            username = input("Ingresa el username del usuario a modificar: ")
            new_data = {}
            new_username = input("Nuevo username (dejar vacío para no modificar): ")
            if new_username:
                new_data['username'] = new_username
            new_password = input("Nueva contraseña (dejar vacío para no modificar): ")
            if new_password:
                new_data['password'] = new_password
            new_email = input("Nuevo email (dejar vacío para no modificar): ")
            if new_email:
                new_data['email'] = new_email
            SistemaUsuarios.modificar_usuario(username, new_data)
        elif opcion == '3':
            username_or_email = input("Ingresa el username o email del usuario a eliminar: ")
            SistemaUsuarios.eliminar_usuario(username_or_email)
        elif opcion == '4':
            username_or_email = input("Ingresa el username o email del usuario a buscar: ")
            usuario = SistemaUsuarios.buscar_usuario(username_or_email)
            if usuario:
                print(usuario)
            else:
                print("Usuario no encontrado.")
        elif opcion == '5':
            SistemaUsuarios.mostrar_usuarios()
        elif opcion == '6':
            usuarios = SistemaUsuarios.cargar_usuarios()
            if usuarios:
                metodo = input("Selecciona el método de ordenación (burbuja o python): ").strip().lower()
                if metodo == 'burbuja':
                    SistemaUsuarios.ordenar_por_burbuja(usuarios)
                elif metodo == 'python':
                    SistemaUsuarios.ordenar_por_python(usuarios)
                else:
                    print("Método no reconocido.")
            else:
                print("No hay usuarios para ordenar.")
        elif opcion == '7':
            SistemaUsuarios.cargar_y_mostrar_accesos()
        elif opcion == '8':
            print("Saliendo del menú de usuarios.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

def menu_principal():
    registros = None 
    while True:
        print("\n--- Menú Principal ---")
        print("1. Menú de Usuarios")
        print("2. Cargar Registros Pluviales")
        print("3. Menú de Gráficos")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            menu_usuarios()
        elif opcion == '2':
            anio = int(input("Ingresa el año para cargar registros pluviales: "))
            registros = RegistrosPluviales.cargar_o_generar_registros(anio)
            mes = int(input("Ingresa el mes para mostrar los registros (1-12): "))
            RegistrosPluviales.mostrar_registros_por_mes(registros, mes)
        elif opcion == "3":
            if registros:
                menu_graficos(registros)
                print("Primero debes cargar los registros pluviales antes de generar gráficos.")
        elif opcion == '4':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu_principal()
