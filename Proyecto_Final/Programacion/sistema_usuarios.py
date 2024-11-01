from usuario import Usuario
from usuario import Acceso 
from datetime import datetime
import pickle
import os

class SistemaUsuarios:
    # Obtén el directorio del script actual
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

    # Especifica la ruta de la carpeta "Programación" dentro de "Evidencia3"
    PROGRAMACION_DIR = os.path.join(SCRIPT_DIR, '..', 'Programacion')
    BUSQUEDA_BINARIA_DNI_DIR = os.path.join(SCRIPT_DIR, '..', 'búsquedasYordenamientos')
    # Define las rutas para los archivos dentro de la carpeta "Programación"
    FILE_NAME_USUARIOS = os.path.join(PROGRAMACION_DIR, 'usuarios.ispc')
    FILE_NAME_USUARIOS_Username = os.path.join(PROGRAMACION_DIR, 'usuariosOrdenadosPorUsername.ispc')
    FILE_NAME_ACCESOS = os.path.join(PROGRAMACION_DIR, 'accesos.ispc')
    FILE_NAME_LOGS = os.path.join(PROGRAMACION_DIR, 'logs.txt')
   
    fecha_actual = datetime.now()
    FILE_NAME_LOGS_BUSQUEDA_BINARIA_DNI = os.path.join(BUSQUEDA_BINARIA_DNI_DIR, 'buscandoUsuarioPorDNI-[{fecha_actual}].txt')
    FILE_NAME_LOGS_BUSQUEDA_BINARIA_USERNAME = os.path.join(BUSQUEDA_BINARIA_DNI_DIR, 'buscandoUsuarioPorUsername-[{fecha_actual}].txt')
    
    usuarios_ordenados = False
    
    @staticmethod
    # def mostrar_todos_los_usuarios():
    def mostrar_usuarios():
        usuarios_archivo_principal = SistemaUsuarios.cargar_usuarios()
        usuarios_ordenados = SistemaUsuarios.cargar_usuarios_ordenados()

        print("\n--- Usuarios del archivo 'usuarios.ispc' ---")
        if usuarios_archivo_principal:
            for usuario in usuarios_archivo_principal:
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
        """Carga los usuarios desde 'usuariosOrdenadosPorUsername.ispc' si existe."""
        # file_path = os.path.join(SistemaUsuarios.PROGRAMACION_DIR, 'usuariosOrdenadosPorUsername.ispc')
        file_path = os.path.join(SistemaUsuarios.FILE_NAME_USUARIOS_Username)
        try:
            with open(file_path, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []
        except Exception as e:
            print(f"Error al cargar usuarios ordenados: {e}")
            return []
        
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
        dni = input("Ingrese el D.N.I.:")
        usuario = Usuario(user_id, username, password, email, dni)
        SistemaUsuarios.agregar_usuario(usuario)
        print(f"Usuario {username} creado y registrado en 'usuarios.ispc'.")

    @staticmethod
    def guardar_usuarios(usuarios):
        with open(SistemaUsuarios.FILE_NAME_USUARIOS, 'wb') as file:
            pickle.dump(usuarios, file)

    def guardar_usuarios_metodo_propio(usuarios):
        with open(SistemaUsuarios.FILE_NAME_USUARIOS_Username, 'wb') as file:
            pickle.dump(usuarios, file)
    @staticmethod
    def agregar_usuario(usuario):
        """Agrega un nuevo usuario y los ordena por DNI antes de guardar."""
        usuarios = SistemaUsuarios.cargar_usuarios()
        usuarios.append(usuario)

        # Ordenar los usuarios por DNI
        usuarios.sort(key=lambda u: int(u.dni))

        # Guardar los usuarios ordenados
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
        usuarios_filtrados = [usuario for usuario in usuarios if usuario.username != username_or_email and usuario.email != username_or_email]
        if len(usuarios_filtrados) != len(usuarios):
            SistemaUsuarios.guardar_usuarios(usuarios_filtrados)
            print(f"Usuario {username_or_email} eliminado exitosamente.")
        else:
            print(f"Usuario {username_or_email} no encontrado.")
    
    @staticmethod
    def iniciar_sesion():
        username = input("Ingresa tu nombre de usuario: ")
        password = input("Ingresa tu contraseña: ")

        # Buscar usuario
        usuario = SistemaUsuarios.buscar_usuario(username)
        
        if usuario:
            if usuario.password == password:
                print("Inicio de sesión exitoso.")
                SistemaUsuarios.registrar_acceso_exitoso(username)  # Registrar acceso exitoso
            else:
                print("Contraseña incorrecta.")
                SistemaUsuarios.registrar_acceso_fallido(username, password)  # Registrar acceso fallido
        else:
            print("Usuario no encontrado.")
            SistemaUsuarios.registrar_acceso_fallido(username, password)  # Registrar acceso fallido

    
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
    def buscar_usuario(username_or_email_or_DNI):
        usuarios = SistemaUsuarios.cargar_usuarios()

        if SistemaUsuarios.usuarios_ordenados:
            print("Búsqueda realizada por técnica binaria.")
            usuario = SistemaUsuarios.busqueda_binaria(usuarios, username_or_email_or_DNI)
            if usuario:
                return usuario
        else:
            print("Búsqueda realizada por técnica secuencial.")
            for usuario in usuarios:
                if usuario.username == username_or_email_or_DNI or usuario.email == username_or_email_or_DNI or usuario.dni == username_or_email_or_DNI :
                    return usuario
        return None

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
            # Crea el archivo si no existe
            with open(SistemaUsuarios.FILE_NAME_ACCESOS, 'wb') as file:
                print("El archivo accesos.ispc no existía, se creó uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
    
    @staticmethod
    def ordenar_por_python(usuarios):
        usuarios.sort(key=lambda x: x.username)
        SistemaUsuarios.usuarios_ordenados = True
        print("Usuarios ordenados usando sort() de Python.")
        SistemaUsuarios.guardar_usuarios_metodo_propio(usuarios)

    @staticmethod
    def ordenar_por_burbuja(usuarios):
        n = len(usuarios)
        for i in range(n):
            for j in range(0, n - i - 1):
                if usuarios[j].username > usuarios[j + 1].username:
                    usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]
        SistemaUsuarios.usuarios_ordenados = True
        print("Usuarios ordenados usando Burbuja.")
        SistemaUsuarios.guardar_usuarios_metodo_propio(usuarios)
    
    @staticmethod
    def buscar_por_username():
        """Buscar usuario por username usando búsqueda secuencial o binaria."""
        username = input("Ingrese el Username a buscar: ")

        # Verificar si está ordenado por username (existe el archivo usuariosOrdenadosPorUsername.ispc)
        usuarios_ordenados = SistemaUsuarios.cargar_usuarios_ordenados()

        if usuarios_ordenados:
            print("Búsqueda realizada por técnica binaria.")
            usuario = SistemaUsuarios.busqueda_binaria(usuarios_ordenados, username)
        else:
            print("Búsqueda realizada por técnica secuencial.")
            usuarios = SistemaUsuarios.cargar_usuarios()
            usuario = next((u for u in usuarios if u.username == username), None)

        if usuario:
            print(f"Usuario encontrado: {usuario}")
        else:
            print("Usuario no encontrado.")
    print("Método de búsqueda binaria.")
    @staticmethod
    def buscar_por_dni():
        """Buscar usuario por DNI usando búsqueda binaria."""
        dni = input("Ingrese el DNI a buscar: ")
        usuarios = SistemaUsuarios.cargar_usuarios()  # El CRUD garantiza que está ordenado por DNI

        # Realizar búsqueda binaria por DNI
        usuario = SistemaUsuarios.busqueda_binaria(usuarios, dni, clave="dni")

        if usuario:
            print(f"Usuario encontrado: {usuario}")
        else:
            print("Usuario no encontrado.")
    print("Método de búsqueda binaria.")
    @staticmethod
    def buscar_por_email():
        """Buscar usuario por email usando búsqueda secuencial."""
        email = input("Ingrese el Email a buscar: ")
        usuarios = SistemaUsuarios.cargar_usuarios()

        # Búsqueda secuencial por email
        usuario = next((u for u in usuarios if u.email == email), None)

        if usuario:
            print(f"Usuario encontrado: {usuario}")
        else:
            print("Usuario no encontrado.")
    print("Método de búsqueda secuencial.")
    @staticmethod
    def busqueda_binaria(usuarios, clave_busqueda, clave="username"):
        """Realiza una búsqueda binaria en función de la clave dada."""
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

   
    # Crear la carpeta de logs si no existe
    @staticmethod
    def crear_directorio_logs():
        # Crea el directorio si no existe
        os.makedirs("búsquedasYordenamientos", exist_ok=True)

    @staticmethod
    def busqueda_binaria_por_dni(usuarios, dni_buscar):
        # Asegúrate de que el dni_buscar es un entero
         
        dni_buscar_int = int(dni_buscar)
        print("Se utilizó la búsqueda por DNI y la técnica de búsqueda fue método binario.")
        
        SistemaUsuarios.crear_directorio_logs()
        
        total_usuarios = len(usuarios)
        intentos = 0

        try:
            # Abrimos el archivo de log
            # with open(log_filename, 'a') as log:
            with open(SistemaUsuarios.FILE_NAME_LOGS_BUSQUEDA_BINARIA_DNI, 'a') as log:
                fecha_actual = datetime.now()
                log.write(f"[{fecha_actual}] Búsqueda Binaria por DNI: buscando el DNI {dni_buscar} en {total_usuarios} usuarios.\n")

                # Verificación de límites
                if total_usuarios == 0:
                    log.write("No hay usuarios registrados.\n")
                    return None

                primer_dni = int(usuarios[0].dni)
                ultimo_dni = int(usuarios[-1].dni)

                if dni_buscar_int < primer_dni:
                    log.write(f"No se encuentra registrado el usuario con ese DNI debido a que el DNI a buscar es más chico que el más chico de los registrados ({primer_dni}).\n")
                    return None
                elif dni_buscar_int > ultimo_dni:
                    log.write(f"No se encuentra registrado el usuario con ese DNI debido a que el DNI a buscar es más grande que el más grande de los registrados ({ultimo_dni}).\n")
                    return None

                # Lógica de búsqueda binaria
                inicio, fin = 0, total_usuarios - 1
                while inicio <= fin:
                    intentos += 1
                    medio = (inicio + fin) // 2
                    dni_medio = int(usuarios[medio].dni)

                    log.write(f"Intento {intentos}: DNI en la posición {medio} es {dni_medio}. ")

                    if dni_medio == dni_buscar_int:
                        log.write(f"Se encontró en {intentos} intentos.\n")
                        return usuarios[medio]
                    elif dni_medio < dni_buscar_int:
                        log.write(f"Buscar en la derecha (posición {medio + 1} a {fin}).\n")
                        inicio = medio + 1
                    else:
                        log.write(f"Buscar en la izquierda (posición {inicio} a {medio - 1}).\n")
                        fin = medio - 1

                # Mensaje si no se encuentra el DNI
                log.write(f"Se realizaron {intentos} intentos y no se encontró el DNI buscado, no está registrado.\n")
        except IOError as e:
            print(f"Error al escribir en el archivo de log: {e}")

        return None

    @staticmethod
    def busqueda_binaria_por_username(usuarios, username_buscar):
        print("Se utilizó la búsqueda por Username y la técnica de búsqueda fue método binario.")
        SistemaUsuarios.crear_directorio_logs()
      
        total_usuarios = len(usuarios)

        inicio, fin = 0, total_usuarios - 1
        intentos = 0

        with open(SistemaUsuarios.FILE_NAME_LOGS_BUSQUEDA_BINARIA_USERNAME, 'a') as log:
            log.write(f"Búsqueda Binaria por Username: buscando '{username_buscar}' en {total_usuarios} usuarios.\n")

            while inicio <= fin:
                intentos += 1
                medio = (inicio + fin) // 2
                username_medio = usuarios[medio].username

                log.write(f"Intento {intentos}: Username en la posición {medio} es '{username_medio}'. ")

                if username_medio == username_buscar:
                    log.write(f"Se encontró en {intentos} intentos.\n")
                    return usuarios[medio]
                elif username_medio < username_buscar:
                    log.write(f"Buscar en la derecha (posición {medio + 1} a {fin}).\n")
                    inicio = medio + 1
                else:
                    log.write(f"Buscar en la izquierda (posición {inicio} a {medio - 1}).\n")
                    fin = medio - 1

            log.write(f"No se encontró en {intentos} intentos.\n")
        return None

    @staticmethod
    def busqueda_secuencial_por_email(usuarios, email_buscar):
        """Búsqueda secuencial por Email mostrando cada intento por pantalla."""
        print(f"Búsqueda Secuencial por Email: buscando '{email_buscar}'")
        intentos = 0

        for usuario in usuarios:
            intentos += 1
            print(f"Intento {intentos}: {email_buscar} {'es igual' if usuario.email == email_buscar else 'es distinto'} a {usuario.email}")

            if usuario.email == email_buscar:
                print(f"Se encontró en {intentos} intentos.")
                return usuario

        print(f"No se encontró el email '{email_buscar}' en {intentos} intentos.")
        return None

    @staticmethod
    def busqueda_secuencial_por_username(usuarios, username_buscar):
        """Búsqueda secuencial por Username mostrando cada intento por pantalla."""
        print(f"Búsqueda Secuencial por Username: buscando '{username_buscar}'")
        intentos = 0

        for usuario in usuarios:
            intentos += 1
            es_igual = usuario.username == username_buscar
            comparacion = "igual" if es_igual else "distinto"
            
            # Mostrar cada intento y el resultado de la comparación
            print(f"Intento {intentos}: {username_buscar} es {comparacion} a {usuario.username}")
            
            if es_igual:
                # Usuario encontrado
                print(f"Se encontró en {intentos} intentos.")
                return usuario

        # Usuario no encontrado después de recorrer la lista completa
        print(f"No se encontró el username '{username_buscar}' en {intentos} intentos.")
        return None