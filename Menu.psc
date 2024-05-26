Algoritmo GestionHotelera		
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
							Leer nombre
							Escribir "Ingrese el apellido del cliente: "
							Leer apellido
							Escribir "Ingrese el e-mail del cliente: "
							Leer email
							Escribir "Ingrese el numero de telefono del cliente: "
							Leer num
							Escribir "Ingrese la direccion del cliente: "
							Leer direccion
						2:
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
					Fin Segun
				Hasta Que menu1 == 4
			3:
				Repetir	
					Escribir "1- Agregar reserva"
					Escribir "2- Modificar reserva"
					Escribir "3- Eliminar reserva"
					Escribir "4- Salir"
					leer menu1
					Segun menu1 Hacer
						1:
							Escribir "Ingrese DNI de la persona que realizará la reserva: "
							Leer dni2
							Escribir "Ingrese fecha de entrada al hotel: "
							Leer entrada
							Escribir "Ingrese fecha de salida del hotel: "
							Leer salida
							Escribir "Ingrese estado de la reserva: "
							Leer estadoReserva
						2:
							Escribir "Ingrese DNI de la persona que realizo la reserva: "
							Leer dni3
							Escribir "Desea modificar la fecha de entrada al hotel: "
							Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese fecha de entrada al hotel: "
								FinSi
							Leer entrada
							Escribir "Desea modificar la fecha de salida del hotel: "
							Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese fecha de salida al hotel: "
								FinSi
							Leer salida
							Escribir "Desea modificar el estado de la reserva: "
							Leer condicion
								Si condicion = "SI" Entonces
									Escribir "Ingrese el estado de la reserva: "
								FinSi
							Leer estadoReserva
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
						
					Fin Segun
				Hasta Que menu1 == 4
		Fin Segun
	Hasta Que menu == 5
FinAlgoritmo

