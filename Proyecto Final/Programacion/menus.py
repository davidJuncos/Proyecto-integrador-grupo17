# menu.py
from sistema_usuarios import SistemaUsuarios
from registros_pluviales import RegistrosPluviales
from graficos_registros import Graficos
from usuario import Usuario, Acceso



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
        print("8. Iniciar Sesión")
        print("9. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            SistemaUsuarios.crear_usuario()
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
            SistemaUsuarios.iniciar_sesion()
        elif opcion == '9':
            print("Saliendo del menú de usuarios.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
