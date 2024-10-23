# main.py
from menus import menu_usuarios, menu_graficos
from usuario import Usuario  
from registros_pluviales import RegistrosPluviales
import pickle

def main():
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
    main()
