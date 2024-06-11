import Base_datos
from roles import mostrar_roles

def agregar_cliente ():
    print("AGREGADO")

def modificar_cliente ():
    print("MODIFICADO")
    
def eliminar_cliente ():
    print("ELIMINADO")

def mostrar_cliente ():
    pass


def agregar_personal():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return

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
        
        Base_datos.cursor.execute(query, values)
        Base_datos.conn.commit()
        print("Personal insertado con éxito.")
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al agregar personal: {error}")
