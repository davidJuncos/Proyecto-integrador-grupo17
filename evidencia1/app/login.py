import re

# Diccionario que almacena usuarios y claves (de manera no persistente)
usuarios = {}

def es_nombre_usuario_valido(nombre_usuario):
    assert 6 <= len(nombre_usuario) <= 12, "El nombre de usuario debe tener entre 6 y 12 caracteres."
    return True

def es_clave_valida(clave):
    assert len(clave) >= 8, "La clave debe tener al menos 8 caracteres."
    
    tiene_minuscula = re.search(r'[a-z]', clave)
    tiene_mayuscula = re.search(r'[A-Z]', clave)
    tiene_numero = re.search(r'[0-9]', clave)
    tiene_caracter_especial = re.search(r'[\W_]', clave)
    
    # Debe cumplir al menos 2 de las condiciones
    condiciones_cumplidas = sum([bool(tiene_minuscula), bool(tiene_mayuscula), bool(tiene_numero), bool(tiene_caracter_especial)])
    
    assert condiciones_cumplidas >= 2, "La clave debe cumplir al menos dos de las siguientes condiciones: minúscula, mayúscula, número, carácter especial."
    return True

def agregar_usuario():
    while True:
        try:
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            
            # Validar que el DNI sea único y numérico
            while True:
                dni = input("Ingrese DNI: ")
                assert dni.isdigit(), "El DNI debe ser numérico."
                assert dni not in [user['dni'] for user in usuarios.values()], "El DNI ya está registrado."
                break

            email = input("Ingrese Email: ")
            fecha_nacimiento = input("Ingrese Fecha de Nacimiento: ")
            
            # Validar que el nombre de usuario sea único y tenga longitud adecuada
            # while True:

            #     nombreUsuario = input("Ingrese nombre de usuario: ")

            #     assert es_nombre_usuario_valido(nombreUsuario), "El nombre de usuario debe tener entre 6 y 12 caracteres."
            #     assert nombreUsuario not in usuarios, "El nombre de usuario ya está registrado."
            #     break

            while True:
                try:
                    nombreUsuario = input("Ingrese nombre de usuario: ")
                    assert es_nombre_usuario_valido(nombreUsuario), "El nombre de usuario debe tener entre 6 y 12 caracteres."
                    assert nombreUsuario not in usuarios, "El nombre de usuario ya está registrado."
                    break  # Salimos del bucle si pasa todas las validaciones
                except AssertionError as e:
                    print(f"Error: {e}. Por favor, intente nuevamente.")

            # Validar clave
            while True:
                clave = input("Ingrese clave: ")

                assert es_clave_valida(clave)

                break
            
            # Agregar el usuario al diccionario
            usuarios[nombreUsuario] = {
                'nombre': nombre,
                'apellido': apellido,
                'dni': dni,
                'email': email,
                'fecha_nacimiento': fecha_nacimiento,
                'clave': clave
            }
            print("Usuario registrado con éxito.")
            break
        except AssertionError as e:
            print(f"Error: {e}")

def iniciar_sesion():
    print("¡Bienvenido al sistema! Por favor, ingrese sus datos de acceso.")
    
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    
    if usuario in usuarios and usuarios[usuario]['clave'] == clave:
         # Se puede llamar correctamente ahora
        print("Acceso Correcto.") 
    else:
        print("Acceso denegado. Usuario o clave incorrectos.")

# Ejecución principal
while True:
    print("1- Iniciar sesión")
    print("2- Registrar usuario")
    print("3- Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    
    if opcion == 1:
        iniciar_sesion()
    elif opcion == 2:
        agregar_usuario()
    elif opcion == 3:
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")