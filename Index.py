from crud_cliente import agregar_cliente, modificar_cliente, eliminar_cliente, mostrar_cliente
from crud_personal import agregar_personal, modificar_personal, eliminar_personal, mostrar_personal
from crud_reserva import agregar_reserva, modificar_reserva, eliminar_reserva, mostrar_reserva
from crud_habitacion import agregar_habitacion, modificar_habitacion, eliminar_habitacion, mostrar_habitacion

while True:
    print("1-CRUD-Clientes")
    print("2-CRUD-Personal")
    print("3-CRUD-Reservas")
    print("4-CRUD-Habitacion")
    print("5-Salir")
    
    menu = int(input("Seleccione una opcion: "))
    
    if menu == 1:
        while True:
            print("1- Agregar cliente")
            print("2- Modificar cliente")
            print("3- Eliminar cliente")
            print("4- Mostrar cliente")
            print("5- Salir ")
            
            menu1 = int(input("Selecccione una opcion"))
            
            if menu1 == 1:
                agregar_cliente()
            elif menu1 == 2:
                modificar_cliente()
            elif menu1 == 3:
                eliminar_cliente()
            elif menu1 == 4:
                mostrar_cliente()
            elif menu1 == 5:
                break 
            
    elif menu == 2:
        while True:
            print("1- Agregar personal")
            print("2- Modificar personal")
            print("3- Eliminar personal")
            print("4- Mostrar personal")
            print("5- Salir ")
            
            menu1 = int(input("Selecccione una opcion"))
                
            if menu1 == 1:
                agregar_personal()
            elif menu1 == 2:
                modificar_personal()
            elif menu1 == 3:
                eliminar_personal()
            elif menu1 == 4:
                mostrar_personal()
            elif menu1 == 5:
                break
            
    elif menu == 3:
        while True:
            print("1- Agregar reservas")
            print("2- Modificar reservas")
            print("3- Eliminar reservas")
            print("4- Mostrar reservas")
            print("5- Salir ") 
            
            if menu1 == 1:
                agregar_reserva()
            elif menu1 == 2:
                modificar_reserva()
            elif menu1 == 3:
                eliminar_reserva()
            elif menu1 == 4:
                mostrar_reserva()
            elif menu1 == 5:
                break   
            
