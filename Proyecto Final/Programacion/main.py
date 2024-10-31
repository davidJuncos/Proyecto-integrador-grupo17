# main.py
from menus import menu_usuarios, menu_graficos
from registros_pluviales import RegistrosPluviales

def main():
    registros = None 
    while True:
        print("\n--- Menú Principal ---")
        print("1. Menú de Usuarios")
        print("2. Cargar Registros Pluviales")
        print("3. Menú de Gráficos")
        print("4. Estadísticas")
        print("5. Salir")
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
                menu_graficos(registros, mes)
            else:
                print("Primero debes cargar los registros pluviales antes de generar gráficos.")
        elif opcion == '4':
            if registros:
                max_precipitacion, min_precipitacion, promedio_precipitacion = RegistrosPluviales.calcular_estadisticas_mes(registros, mes)
                print(f"\nEstadísticas de Precipitaciones para el Mes {mes}:")
                print(f"Máxima precipitación: {max_precipitacion} mm")
                print(f"Mínima precipitación: {min_precipitacion} mm")
                print(f"Promedio de precipitación: {promedio_precipitacion:.2f} mm")
            else:
                print("Primero debes cargar los registros pluviales antes de generar gráficos.")

        elif opcion == '5':
            print("Saliendo de la aplicación.")
            break
        else:
            
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
