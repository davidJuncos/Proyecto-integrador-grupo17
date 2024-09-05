from datetime import datetime
import captcha # Importa el módulo captcha

def registrar_ingreso(nombre_usuario):
    fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ingresos.txt", "a") as file:
        file.write(f"Usuario: {nombre_usuario}, Fecha de ingreso: {fecha_ingreso}\n")
    print(f"Ingreso exitoso. Registro guardado en 'ingresos.txt'.")

def iniciar_sesion():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    clave_correcta = "Registro1."  # Aquí debes verificar la clave real del usuario desde la base de datos o un archivo
    
    captcha.main() # Valida el captcha antes de permitir el ingreso

    intentos_fallidos = 0
    
    while intentos_fallidos < 4:
        clave_ingresada = input("Ingresa tu clave: ")
        
        if clave_ingresada == clave_correcta:
            print("Ingreso exitoso.")
            registrar_ingreso(nombre_usuario)
            break
        else:
            intentos_fallidos += 1
            print(f"Clave incorrecta. Intentos fallidos: {intentos_fallidos}/4.")
            
            if intentos_fallidos == 4:
                print("Usuario bloqueado por demasiados intentos fallidos.")
                with open("log.txt", "a") as file:
                    file.write(f"Usuario: {nombre_usuario}, Bloqueado por 4 intentos fallidos el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                break

def olvido_contraseña():
    print("La funcionalidad de recuperación de contraseña aún no está implementada.")
    pass

def crear_usuario():
    nombre_usuario = input("Ingresa un nombre de usuario: ")
    clave = input("Ingresa una contraseña: ")
    
    captcha.main() # Valida el captcha para permitir la creación del usuario

    with open("usuariosCreados.txt", "a") as file:
        file.write(f"Usuario: {nombre_usuario}, Clave: {clave}, Creado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print("Usuario creado. Registro guardado en 'usuariosCreados.txt'")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Olvidó la contraseña")
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