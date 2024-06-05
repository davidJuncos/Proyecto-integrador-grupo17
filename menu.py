from menu import agregar, modificar, elimnar, mostrar

while True:
    print("1-CRUD-Clientes")
    print("2-CRUD-Personal")
    print("3-CRUD-Reservas")
    print("4-CRUD-Habitacion")
    print("5-Salir")
    
    menu = int(input("Seleccione una opcion"))
    
    if menu == 1:
        while True:
            print("1- Agregar cliente")
            print("2- Modificar cliente")
            print("3- Eliminar cliente")
            print("4- Mostrar cliente")
            print("5- Salir")
            
            menu1 = int(input("Selecccione una opcion"))
            
            if menu1 == 1:
                
                