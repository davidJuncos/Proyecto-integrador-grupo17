import Base_datos
def mostrar_roles():
    query = "SELECT * FROM Roles WHERE Rol LIKE '%%'"
    
    Base_datos.cursor.execute(query)
    roles = Base_datos.cursor.fetchone()

    print(Base_datos.cursor.rowcount, "Filas afectadas")

    if(Base_datos.cursor.rowcount >= 1):
        print(roles)
        return True
    else:
        print(f"No existe en la base de datos roles del personal")
        return False


def agregar_personal ():
    Nombre = input("Ingrese nombre: ")
    Apellido = input("Ingrese apellido: ")
    Horainicia = float(input("Ingrese horario de inicio: "))
    HoraFin = float(input("Ingrese horario de salida: "))
    mostrar_roles()
    IdRol = input("Ingrese rol: ")
    query = "INSERT INTO Personal (Nombre, Apellido, HoraInicia, HoraFin, Estado, IdRol) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (Nombre, Apellido, Horainicia, HoraFin, 1,IdRol)
    
    Base_datos.cursor.execute(query, values)
    Base_datos.conn.commit() 
    print("Persona insertada con éxito.")


def modificar_personal ():
    print("MODIFICADO")
    
def eliminar_personal ():
    print("ELIMINADO")

def mostrar_personal ():
    query = "SELECT * FROM Personal WHERE id = %s"
    values = (id,)
    Base_datos.cursor.execute(query,values)
    personaUnica = Base_datos.cursor.fetchone()

    print(Base_datos.cursor.rowcount, "Filas afectadas")

    if(Base_datos.cursor.rowcount == 1):
        print(personaUnica)
        return True
    else:
        print(f"No existe en la base de datos la persona con id: {id}")
        return False

print(agregar_personal())

