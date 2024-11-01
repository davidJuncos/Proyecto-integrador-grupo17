
import mysql.connector
from mysql.connector import Error
from db_conn import DBConn
from registro_de_cliente import Cliente
from reservas import Reserva
from informes import Informe

def menu1():
    print("\nIngresó a la Gestión de Base de datos de Gestión hotelera")
    print("--- Sistema de Gestión del Hotel ---")
    print("1. Registrar cliente")
    print("2. Hacer reserva")
    print("3. Consultar disponibilidad")
    print("4. Generar informe de mantenimientos")
    print("5. Generar informe de reservas activas")
    print("6. Buscar Cliente por DNI")
    print("7. Salir")
    return input("Seleccione una opción: ")

def main1():
    db_conn = DBConn()
    
    with db_conn.connect_to_mysql() as connection:
        if not connection:
            raise ConnectionError("No se pudo establecer una conexión a la base de datos.")
        
        cliente = Cliente(connection)
        reserva = Reserva(connection)
        informe = Informe(connection)

        while True:
            opcion = menu1()

            if opcion == '1':
                # Registro de cliente
                dni = input("Ingrese DNI: ")
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese apellido: ")
                direccion = input("Ingrese dirección: ")
                email = input("Ingrese email: ")
                numeroTelefono = input("Ingrese número de teléfono: ")
                try:
                    cliente.registrar_cliente(dni, nombre, apellido, direccion, email, numeroTelefono)
                except Exception as e:
                    print(f"Error al registrar cliente: {e}")
        
            elif opcion == '2':
                # Hacer reserva
                idPersonal = int(input("Ingrese ID del personal que hace la reserva: "))
                idHabitacion = int(input("Ingrese ID de la habitación: "))
                idCliente = int(input("Ingrese ID del cliente: "))
                fechaEntrada = input("Ingrese fecha de entrada (YYYY-MM-DD HH:MM): ")
                fechaSalida = input("Ingrese fecha de salida (YYYY-MM-DD HH:MM): ")
                try:
                    reserva.hacer_reserva(idPersonal, idHabitacion, idCliente, fechaEntrada, fechaSalida)
                except Exception as e:
                    print(f"Error al hacer la reserva: {e}")

            elif opcion == '3':
                # Consultar disponibilidad
                fechaEntrada = input("Ingrese fecha de entrada (YYYY-MM-DD HH:MM): ")
                fechaSalida = input("Ingrese fecha de salida (YYYY-MM-DD HH:MM): ")
                try:
                    habitaciones_disponibles = reserva.consultar_disponibilidad(fechaEntrada, fechaSalida)
                    if habitaciones_disponibles:
                        for habitacion in habitaciones_disponibles:
                            print(f"Habitación {habitacion['numeroHabitacion']} - Tipo: {habitacion['tipo']} - Precio: {habitacion['precioNoche']}")
                    else:
                        print("No hay habitaciones disponibles para esas fechas.")
                except Exception as e:
                    print(f"Error al consultar la disponibilidad: {e}")
        
            elif opcion == '4':
                # Generar informe de mantenimientos
                try:
                    informe.generar_informe_mantenimientos()
                except Exception as e:
                    print(f"Error al generar el informe de mantenimientos: {e}")
            elif opcion == '5':
                #Generarr informe de reservas activas
                try: 
                    informe.generar_informe_reservas_activas()
                except Exception as e:
                    print(f"Error al generar el informe de reservas actias")
            
            elif opcion == '6':
                # Buscar cliente por DNI
                dni = input("Ingrese el DNI del cliente: ")
                try:
                    cliente_info = cliente.buscar_cliente_por_dni(dni)
                    if cliente_info:
                        cliente.mostrar_cliente(cliente_info)  # Mostrar cliente usando rich
                    else:
                        print("Cliente no encontrado.")
                except Exception as e:
                    print(f"Error al buscar cliente: {e}")
            
            elif opcion == '7':
                print("Saliendo del sistema.")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main1()
