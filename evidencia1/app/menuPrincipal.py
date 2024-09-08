from datetime import datetime
import re
import captcha  # Asegúrate de tener el módulo captcha importado correctamente

# Diccionario que almacena usuarios y claves (de manera no persistente)
usuarios = {}

# Función para validar el nombre de usuario
def es_nombre_usuario_valido(nombre_usuario):
    if not (6 <= len(nombre_usuario) <= 12):
        raise ValueError("El nombre de usuario debe tener entre 6 y 12 caracteres.")
    return True

# Función para validar la clave
def es_clave_valida(clave):
    if len(clave) < 8:
        raise ValueError("La clave debe tener al menos 8 caracteres.")
    
    tiene_minuscula = re.search(r'[a-z]', clave)
    tiene_mayuscula = re.search(r'[A-Z]', clave)
    tiene_numero = re.search(r'[0-9]', clave)
    tiene_caracter_especial = re.search(r'[\W_]', clave)
    
    condiciones_cumplidas = sum([bool(tiene_minuscula), bool(tiene_mayuscula), bool(tiene_numero), bool(tiene_caracter_especial)])
    if condiciones_cumplidas < 2:
        raise ValueError("La clave debe cumplir al menos dos de las siguientes condiciones: minúscula, mayúscula, número, carácter especial.")
    
    return True

# Función para registrar un ingreso
def registrar_ingreso(nombre_usuario):
    fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ingresos.txt", "a") as file:
        file.write(f"Usuario: {nombre_usuario}, Fecha de ingreso: {fecha_ingreso}\n")
    print(f"Ingreso exitoso. Registro guardado en 'ingresos.txt'.")

# Función para iniciar sesión
def iniciar_sesion():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    
    if nombre_usuario not in usuarios:
        print("Usuario no encontrado. Regístrese primero.")
        return
    
    captcha.main()  # Valida el captcha antes de permitir el ingreso

    intentos_fallidos = 0
    while intentos_fallidos < 4:
        clave_ingresada = input("Ingresa tu clave: ")
        
        if clave_ingresada == usuarios[nombre_usuario]['clave']:
            print("Ingreso exitoso.")
            registrar_ingreso(nombre_usuario)
            # Registrar el acceso exitoso
            with open("ingresos.txt", "a") as file:
                file.write(f"Usuario: {nombre_usuario}, Fecha de acceso exitoso: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            break
        else:
            intentos_fallidos += 1
            print(f"Clave incorrecta. Intentos fallidos: {intentos_fallidos}/4.")
            
            if intentos_fallidos == 4:
                print("Usuario bloqueado por demasiados intentos fallidos.")
                # Registrar el bloqueo
                with open("log.txt", "a") as file:
                    file.write(f"Usuario: {nombre_usuario}, Bloqueado por 4 intentos fallidos el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                break

# Función de recuperación de contraseña (aún no implementada)
def olvido_contraseña():
    print("La funcionalidad de recuperación de contraseña aún no está implementada.")

# Función para crear un nuevo usuario
def crear_usuario():
    while True:
        try:
            nombre_usuario = input("Ingresa un nombre de usuario: ")

            # Validar el nombre de usuario
            es_nombre_usuario_valido(nombre_usuario)
            if nombre_usuario in usuarios:
                raise ValueError("El nombre de usuario ya está registrado.")

            # Validar la clave
            clave = input("Ingresa una contraseña: ")
            es_clave_valida(clave)
            
            captcha.main()  # Validar captcha antes de registrar el usuario

            # Agregar el usuario al diccionario
            usuarios[nombre_usuario] = {
                'clave': clave,
                'creado_el': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Registrar la creación del usuario
            with open("usuariosCreados.txt", "a") as file:
                file.write(f"Usuario: {nombre_usuario}, Clave: {clave}, Creado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            print("Usuario creado exitosamente.")
            break

        except ValueError as e:
            print(f"Error: {e}. Intenta de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}. Intenta de nuevo.")

# Menú principal
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Olvidé la contraseña")
        print("3. Crear un nuevo usuario")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            iniciar_sesion()
        elif opcion == '2':
            olvido_contraseña()
        elif opcion == '3':
            crear_usuario()
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()
