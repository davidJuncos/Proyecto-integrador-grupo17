Algoritmo Algoritmo GestionHotelera		
		//Falta diccionario para que funcione correctamente.
		
		Repetir	
			Escribir "1-CRUD-Clientes"
			Escribir "2-CRUD-Personal"
			Escribir "3-CRUD-Reservas"
			Escribir "4-CRUD-Habitacion"
			Escribir "5-Salir"
			leer menu
			
			
			Segun menu Hacer
				1:
					Repetir	
						Escribir "1- Agregar cliente"
						Escribir "2- Modificar cliente"
						Escribir "3- Eliminar cliente"
						Escribir "4- Salir"
						leer menu1
						Segun menu1 Hacer
							1:
								Escribir "Ingrese DNI: "
								Leer dni
								Escribir "Ingrese el nombre del cliente: "
								Leer nombre_cliente
								Escribir "Ingrese el apellido del cliente: "
								Leer apellido_cliente
								Escribir "Ingrese el e-mail del cliente: "
								Leer email_cliente
								Escribir "Ingrese el numero de telefono del cliente: "
								Leer num_cliente
								Escribir "Ingrese la direccion del cliente: "
								Leer direccion_cliente
							2:
								Escribir "Ingrese DNI de la persona que quieres modicar: "
								Leer dni
								Escribir "Desea modificar el nombre: "
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese el nombre del cliente: "
									Leer nombre_cliente
								FinSi
								
								Escribir "Desea modificar el apellido: "
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese el apellido del cliente: "
									Leer apellido_cliente
								FinSi
								
								Escribir "Desea modificar el e-mail del cliente: "
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese el e-mail del cliente: "
									Leer email_cliente
								FinSi
								
								Escribir "Desea modificar el numero de telefono del cliente: "
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese el numero de telefono del cliente "
									Leer num_cliente
								FinSi
								
								Escribir "Desea modificar el numero de telefono del cliente: "
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese la direccion del cliente "
									Leer direccion_cliente
								FinSi
							3:
								Escribir "Ingrese DNI de la persona que quieres eliminar: "
								Leer dni
								Escribir "Desea eliminar : ", nombre_cliente
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "ELIMINADO"
								FinSi
								
								
						Fin Segun
					Hasta Que menu1 == 4
				2:
					Repetir	
						Escribir "1- Registrar personal"
						Escribir "2- Modificar datos personal"
						Escribir "3- Eliminar personal"
						Escribir "4- Salir"
						leer menu1
						Segun menu1 Hacer
							1:
								Escribir "Ingrese DNI: "
								Leer dni1
								Escribir "Ingrese nombre del empleado: "
								Leer nombreEmpleado
								Escribir "Ingrese apellido del empleado: "
								Leer apellidoEmpleado
								Escribir "Ingrese horarios a cumplir: "
								Leer horario
								Escribir "Ingresar cargo: "
								Leer rol
							2:
								Escribir "Ingrese DNI del personal: "
								Leer dni1
								Escribir "Desea modificar datos del personal: "
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese datos del personal: "
									Leer nombreEmpleado
								FinSi
								Escribir "Desea modificar el apellido del personal: "
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese el apellido del personal: "
									Leer apellidoEmepleado
								FinSi
								Escribir "Desea modificar el horario del personal: "
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese horario que desea seleccionar: "
									Leer horario
								FinSi
								
								Escribir "Desea modificar el cargo del personal: "
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese el cargo que desea ocupar: "
									Leer rol
								FinSi
							3:
								Escribir "Ingrese DNI de personal que desea eliminar: "
								Leer dni1
								Escribir "Desea eliminar : ", nombreEmpleado
								Leer condicion
								Si condicion = "SI" Entonces
									Escribir "ELIMINADO"
								FinSi
								
						Fin Segun
					Hasta Que menu1 == 4
				3:
							Escribir "Ingrese DNI de la persona que quieres eliminar: "
							Leer dni
							Escribir "Desea eliminar : ", nombre_cliente
							Leer condicion
							Si condicion = "SI" Entonces
								Escribir "ELIMINADO"
							FinSi
					Fin Segun
				Hasta Que menu1 == 4
			4: 
				Repetir	
					Escribir "1- Agregar habitación"
					Escribir "2- Modificar habitación"
					Escribir "3- Eliminar habitación"
					Escribir "4- Salir"
					leer menu1
					Segun menu1 Hacer
						1:
							Escribir "Ingrese numero de habitación: "
							Leer nroHabitacion
							Escribir "Ingrese tipo de habitación: "
							Leer tipoHabitacion
							Escribir "Ingrese precio por noche: "
							Leer precioNoche
							Escribir "Ingrese disponibilidad: "
							Leer disponibilidad
						2:	
							Escribir "Ingrese el numero de habitación que quieres modicar: "
							Leer nroHabitacion
							Escribir "Desea modificar el numero de habitación: "
							Leer condicion
							Si condicion = "SI" Entonces
								Escribir "Ingrese el numero de habitación: "
								Leer nroHabitacion
							FinSi
							
							
							Escribir "Desea modificar el tipo de habitación: "
							Leer condicion
							Si condicion = "SI" Entonces
								Escribir "Ingrese el numero de habitación: "
								Leer tipoHabitacion
							FinSi
							
							Escribir "Desea modificar el precio de habitación: "
							Leer condicion
							Si condicion = "SI" Entonces
								Escribir "Ingrese el precio de habitación: "
								Leer precioNoche
							FinSi
							
							
							Escribir "Desea modificar la disponibilidad: "
							Leer condicion
							Si condicion = "SI" Entonces
								Escribir "Ingrese la disponibilidad: "
								Leer disponibilidad
							FinSi
						3:
							Escribir "Ingrese nro de habitacion: "
							Leer nroHabitacion
							Escribir "Desea eliminar : ", nroHabitacion
							Leer condicion
							Si condicion = "SI" Entonces
								Escribir "ELIMINADO"
							FinSi
					Fin Segun
				Hasta Que menu1 == 4
		Fin Segun
	Hasta Que menu == 5
FinAlgoritmo
