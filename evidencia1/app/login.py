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

def iniciar_app():    
    while True:
        print("1-CRUD-Clientes")
        print("2-CRUD-Personal")
        print("3-CRUD-Reservas")
        print("4-CRUD-Habitacion")
        print("5-Salir")
        
        try:
            menu = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        
        if menu == 1:
            while True:
                print("1- Agregar cliente")
                print("2- Modificar cliente")
                print("3- Eliminar cliente")
                print("4- Mostrar clientes")
                print("5- Buscar cliente")
                print("6- Salir ")
                
                try:
                    menu1 = int(input("Seleccione una opcion: "))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
                
                if menu1 == 1:
                    agregar_cliente()
                elif menu1 == 2:
                    modificar_cliente()
                elif menu1 == 3:
                    eliminar_cliente()
                elif menu1 == 4:
                    mostrar_clientes_completo()                
                elif menu1 == 5:
                    mostrar_un_cliente()
                elif menu1 == 6:
                    break 
                else:
                    print("Opción no válida.")
                
        elif menu == 2:
            while True:
                print("1- Agregar personal")
                print("2- Modificar personal")
                print("3- Eliminar personal")
                print("4- Mostrar todo el personal")
                print("5- Buscar personal")
                print("6- Salir ")
                
                try:
                    menu1 = int(input("Seleccione una opcion: "))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
                
                if menu1 == 1:
                    agregar_personal()
                elif menu1 == 2:
                    modificar_personal()
                elif menu1 == 3:
                    eliminar_personal()
                elif menu1 == 4:
                    mostrar_personal_completo()
                elif menu1 == 5:
                    mostrar_personal_unico()
                elif menu1 == 6:
                    break
                else:
                    print("Opción no válida.")
                
        elif menu == 3:
            while True:
                print("1- Agregar reservas")
                print("2- Modificar reservas")
                print("3- Eliminar reservas")
                print("4- Mostrar reservas")
                print("5- Buscar reservas")
                print("6- Salir") 
                
                try:
                    menu1 = int(input("Seleccione una opcion: "))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
                
                if menu1 == 1:
                    agregar_reserva()
                elif menu1 == 2:
                    modificar_reserva()
                elif menu1 == 3:
                    eliminar_reserva()
                elif menu1 == 4:
                    mostrar_reserva_completa()
                elif menu1 == 5:
                    mostrar_reserva()
                elif menu1 == 6:
                    break  
                else:
                    print("Opción no válida.")
        elif menu == 4:
            while True:
                print("1- Agregar habitacion")
                print("2- Modificar habitacion")
                print("3- Eliminar habitacion")
                print("4- Mostrar habitaciones")
                print("5- Buscar habitacion")
                print("6- Salir ")
                
                try:
                    menu1 = int(input("Seleccione una opcion: "))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
                
                if menu1 == 1:
                    agregar_habitacion()
                elif menu1 == 2:
                    modificar_habitacion()
                elif menu1 == 3:
                    eliminar_habitacion()
                elif menu1 == 4:
                    mostrar_todas_habitaciones()
                elif menu1 == 5:
                    mostrar_habitacion_unica()
                elif menu1 == 6:
                    break
                else:
                    print("Opción no válida.")
        elif menu == 5:
            print("Programa finalizado!")
            break
        else:
            print("Opción no válida.")

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
        iniciar_app()  # Se puede llamar correctamente ahora
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