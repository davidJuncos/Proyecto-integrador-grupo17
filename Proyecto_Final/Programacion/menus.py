# menu.py
from sistema_usuarios import SistemaUsuarios
from registros_pluviales import RegistrosPluviales
from graficos_registros import Graficos
from usuario import Usuario, Acceso

def menu_graficos(registros, mes):
    while True: 
        print("\n--- Menú de Gráficos ---") 
        print("1. Gráfico de Lluvias Anual por Mes")
        print("2. Gráfico de Lluvias Diarias por Mes")
        print("3. Gráfico de Proporción de Lluvias por Mes")
        print("4. Gráfico de Precipitaciones por Día")
        print("5. Datos Estadísticos")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            Graficos.graficar_lluvias_anuales_barra(registros)
        elif opcion == "2":
            Graficos.graficar_dispersion_lluvias_dia_mes(registros)
        elif opcion == "3":
            Graficos.graficar_proporcion_lluvia_mes(registros)
        elif opcion == "4":
            Graficos.graficar_precipitaciones_por_dia(registros, mes)
        elif opcion == "5":
            max_precipitacion, min_precipitacion, promedio_precipitacion = Graficos.calcular_estadisticas_mes(registros, mes)
            print(f"\nEstadísticas de Precipitaciones para el Mes {mes}:")
            print(f"Máxima precipitación: {max_precipitacion} mm")
            print(f"Mínima precipitación: {min_precipitacion} mm")
            print(f"Promedio de precipitación: {promedio_precipitacion:.2f} mm")
        elif opcion == "6":
            break
        else: 
            print("Opción no válida")    

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
            new_dni = input("Nuevo DNI (dejar vacío para no modificar): ")    
            if new_dni:
                new_data['dni'] = new_dni
            SistemaUsuarios.modificar_usuario(username, new_data)
        
        elif opcion == '3':
            username_or_email = input("Ingresa el username o email del usuario a eliminar: ")
            SistemaUsuarios.eliminar_usuario(username_or_email)

        elif opcion == '4':
            print("\n--- Menú de Búsqueda de Usuarios ---")
            print("1) Buscar por Username")
            print("2) Buscar por DNI (búsqueda binaria)")
            print("3) Buscar por Email (búsqueda secuencial)")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                usuarios = SistemaUsuarios.cargar_usuarios()  # El CRUD garantiza que está ordenado por DNI
                username = input("Ingresa el username a buscar: ")
                SistemaUsuarios.busqueda_secuencial_por_username( usuarios, username)


            elif sub_opcion == "2":
                try:
                    dni_buscar = int(input("Ingrese el DNI a buscar: "))
                    usuarios = SistemaUsuarios.cargar_usuarios()  # El CRUD garantiza que está ordenado por DNI
                    SistemaUsuarios.busqueda_binaria_por_dni(usuarios, dni_buscar)
                except ValueError:
                    print("Error: Ingrese un número válido para el DNI.")
            
            elif sub_opcion == "3":
                usuarios = SistemaUsuarios.cargar_usuarios()  # El CRUD garantiza que está ordenado por DNI
                email = input("Ingresa el email a buscar: ")
                SistemaUsuarios.busqueda_secuencial_por_email(usuarios, email)
            
            else:
                print("Opción no válida. Intente nuevamente.")

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
            print("Saliendo del Menú de Principal.")
            break
        
        else:
            print("Opción no válida. Intenta nuevamente.")
