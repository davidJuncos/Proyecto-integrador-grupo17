# main.py
from menus import menu_usuarios, menu_graficos
from usuario import Usuario, Acceso
from registros_pluviales import RegistrosPluviales
import os
from datetime import datetime

def main():
    registros = None  # Inicializar variable para almacenar registros pluviales

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

        elif opcion == '3':
            if registros:
                menu_graficos(registros)
            else:
                print("Primero debes cargar los registros pluviales antes de generar gráficos.")

        elif opcion == '4':
            print("Saliendo de la aplicación.")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
