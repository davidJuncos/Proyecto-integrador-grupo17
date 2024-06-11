import Base_datos


"""
def mostrar_roles():
    query = "SELECT * FROM Roles WHERE Rol LIKE '%%'"
    
    Base_datos.cursor.execute(query)
    roles = Base_datos.cursor.fetchall()  # Leer todas las filas del resultado

    print(Base_datos.cursor.rowcount, "Filas afectadas")

    if Base_datos.cursor.rowcount >= 1:
        for role in roles:
            print(role)
        return True
    else:
        print("No existen roles en la base de datos")
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


"""


def mostrar_roles():
    query = "SELECT * FROM Roles"

    Base_datos.cursor.execute(query)
    roles = Base_datos.cursor.fetchall()  # Obtener todas las filas

    if roles:  # Verificar si hay roles
        for role in roles:
            print(role)
        print(f"{len(roles)} Filas afectadas")
        return True
    else:
        print(f"No existe en la base de datos roles del personal")
        return False

def agregar_personal():
    Nombre = input("Ingrese nombre: ")
    Apellido = input("Ingrese apellido: ")


    while True:
        try:
            Horainicia = float(input("Ingrese horario de inicio (formato 24h, ej. 9.5 para 9:30): "))
            HoraFin = float(input("Ingrese horario de salida (formato 24h, ej. 17.0 para 17:00): "))
            break
        except ValueError:
            print("Por favor ingrese una hora válida en formato decimal.")

    if not mostrar_roles():
        return  # Si no hay roles, no continuar

    IdRol = input("Ingrese Id del rol: ")

    query = "INSERT INTO Personal (Nombre, Apellido, HoraInicia, HoraFin, Estado, IdRol) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (Nombre, Apellido, Horainicia, HoraFin, 1, IdRol)

    try:
        Base_datos.cursor.execute(query, values)
        Base_datos.conn.commit()
        print("Persona insertada con éxito.")
    except Exception as e:
        print(f"Error al insertar persona: {e}")
        Base_datos.conn.rollback()  # Revertir cambios en caso de error

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
