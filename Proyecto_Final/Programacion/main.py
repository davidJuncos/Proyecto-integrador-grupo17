<<<<<<< HEAD
=======
<<<<<<< HEAD
# main.py
import subprocess
import os
=======
# import subprocess
# import os

# # Agregar el directorio 'Proyecto_Final' a la ruta de búsqueda de módulos
# from menus import menu_usuarios, menu_graficos
# from usuario import Usuario, Acceso
# from registros_pluviales import RegistrosPluviales
# import os
# from datetime import datetime

# def main():
#     registros = None  # Inicializar variable para almacenar registros pluviales

#     while True:
#         print("\n--- Menú Principal ---")
#         print("1. Menú de Usuarios")
#         print("2. Cargar Registros Pluviales")
#         print("3. Menú de Gráficos")
#         print("4. Salir")
#         print("5. Acceder a Base de Datos")
#         opcion = input("Selecciona una opción: ")

#         if opcion == '1':
#             menu_usuarios()

#         elif opcion == '2':
#             try:
#                 anio = int(input("Ingresa el año para cargar registros pluviales: "))
#                 registros = RegistrosPluviales.cargar_o_generar_registros(anio)
                
#                 mes = int(input("Ingresa el mes para mostrar los registros (1-12): "))
#                 if 1 <= mes <= 12:
#                     RegistrosPluviales.mostrar_registros_por_mes(registros, mes)
#                 else:
#                     print("Mes no válido. Ingresa un número entre 1 y 12.")
#             except ValueError:
#                 print("Error: Debes ingresar un número válido para el año y el mes.")

#         elif opcion == '3':
#             if registros:
#                 menu_graficos(registros)
#             else:
#                 print("Primero debes cargar los registros pluviales antes de generar gráficos.")

#         elif opcion == '4':
#             print("Saliendo de la aplicación.")
#             break

#         elif opcion == '5':
#             print("Accediendo al Menú de Base de Datos.")
#              # Accede a `Back_CRUD.py` como un proceso independiente
#             try:
#                 # Define la ruta completa a `Back_CRUD.py`
#                 path_back_crud = os.path.join(os.path.dirname(__file__), '..', 'BD', 'Back_CRUD.py')
                
#                 # Ejecuta `Back_CRUD.py` usando `subprocess`
#                 subprocess.run(['python', path_back_crud])
#             except Exception as e:
#                 print(f"Error al intentar acceder al menú CRUD: {e}")
            
        
#         else:
#             print("Opción no válida. Intenta nuevamente.")

# if __name__ == "__main__":
#     main()

>>>>>>> a5f2921e2a08b6970c06b8cc945adf2db95f1e5a
import subprocess
import os
# Agregar el directorio 'Proyecto_Final' a la ruta de búsqueda de módulos
>>>>>>> fe300d5c1329c82307f2690b14f963de1fa06f34
from menus import menu_usuarios, menu_graficos
from usuario import Usuario, Acceso
from registros_pluviales import RegistrosPluviales
import os
from datetime import datetime


def main():
    
    #SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    
    
    #BASE_DATOS_DIR = os.path.join(SCRIPT_DIR, '..',"Proyecto_Final/Bd")
    #FILE_NAME_LOGS_BASE_DE_DATOS = os.path.join(BASE_DATOS_DIR,"Back_CRUD")
    registros = None  # Inicializar variable para almacenar registros pluviales

    while True:
        print("\n--- Menú Principal ---")
        print("1. Menú de Usuarios")
        print("2. Ingresar al sistema con los datos de usuario")
        print("3. Análisis de datos")
        print("4. Salir")
<<<<<<< HEAD
        
=======

>>>>>>> fe300d5c1329c82307f2690b14f963de1fa06f34
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            menu_usuarios()
<<<<<<< HEAD
        
        elif opcion == "2": 
            #print("Accediendo al Menú de Base de Datos.")
             # Accede a Back_CRUD.py como un proceso independiente
            try:
                # Define la ruta completa a Back_CRUD.py               
                pathbackcrud = os.path.join(os.path.dirname(__file__), '..', 'BD', 'Back_CRUD1.py')
                
            except FileNotFoundError as e:
                print(f"Error: {e}")
                print("a")
            except Exception as e:
                print(f"Ocurrió un error al cambiar de directorio: {e}")
           #FILE_NAME_LOGS_BASE_DE_DATOS,menu1()
           #FILE_NAME_LOGS_BASE_DE_DATOS,main1()

=======
        elif opcion == "2":
            # print("Accediendo al Menú de Base de Datos.")
            # Accede a `Back_CRUD.py` como un proceso independiente
            try:
                # Define la ruta completa a `Back_CRUD.py`
                path_back_crud = os.path.join(os.path.dirname(__file__), '..', 'BD', 'Back_CRUD.py')
                
                # Ejecuta `Back_CRUD.py` usando `subprocess`
                subprocess.run(['python', path_back_crud])
            except Exception as e:
                print(f"Error al intentar acceder al menú CRUD: {e}")
                
>>>>>>> fe300d5c1329c82307f2690b14f963de1fa06f34
        elif opcion == '3':
            try:
                anio = int(input("Ingresa el año para cargar registros pluviales: "))
                registros = RegistrosPluviales.cargar_o_generar_registros(anio)

                mes = int(input("Ingresa el mes para mostrar los registros (1-12): "))
                if 1 <= mes <= 12:
                    RegistrosPluviales.mostrar_registros_por_mes(registros, mes)
                else:
                    print("Mes no válido. Ingresa un número entre 1 y 12.")
            except ValueError:
                print("Error: Debes ingresar un número válido para el año y el mes.")
<<<<<<< HEAD
                
=======

            if registros:
                menu_graficos(registros)
            else:
                print("Primero debes cargar los registros pluviales antes de generar gráficos.")
        elif opcion == '3':
>>>>>>> fe300d5c1329c82307f2690b14f963de1fa06f34
            if registros:
                menu_graficos(registros)
            else:
                print("Primero debes cargar los registros pluviales antes de generar gráficos.")
<<<<<<< HEAD
        elif opcion == '3':
            if registros:
                menu_graficos(registros)
            else:
                print("Primero debes cargar los registros pluviales antes de generar gráficos.")    
           
=======

>>>>>>> fe300d5c1329c82307f2690b14f963de1fa06f34
        elif opcion == "4": 
            print("Saliendo del menú de usuarios.")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
