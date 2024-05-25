Algoritmo sin_titulo
	
	Repetir	
		Escribir "1-CRUD-Clientes"
		Escribir "2-CRUD-Personal"
		Escribir "3-CRUD-Reservas"
		Escribir "4-CRUD-Habitacion"
		Escribir "4-Salir"
		leer menu
		
		
		Segun menu Hacer
			1:
				Repetir	
					Escribir "1-Agregar cliente"
					Escribir "2-Modicar cliente"
					Escribir "3-Eliminar cliente"
					Escribir "4-Salir"
					leer menu1
					Segun menu1 Hacer
						1:
							Escribir "Ingrese DNI"
							Leer dni
							Escribir "Ingrese el nombre del cliente"
							Leer nombre
							Escribir "Ingrese el apellido del cliente"
							Leer apellido
							Escribir "Ingrese el e-mail del cliente"
							Leer email
							Escribir "Ingrese el numero de telefono del cliente"
							Leer num
							Escribir "Ingrese la direccion del cliente"
							Leer direccion
						2:
					Fin Segun
				Hasta Que menu1 == 4
				
			2:
				
			3:
				
			4: 
				Repetir	
					Escribir "1-Agregar habitación"
					Escribir "2-Modicar habitación"
					Escribir "3-Eliminar habitación"
					Escribir "4-Salir"
					leer menu1
					Segun menu1 Hacer
						1:
							Escribir "Ingrese Nro Habitación"
							Leer nroHabitacion
							Escribir "Ingrese Tipo de Habitación"
							Leer tipoHabitacion
							Escribir "Ingrese precio por Noche"
							Leer precioNoche
							Escribir "Ingrese Disponibilidad"
							Leer disponibilidad
						2:
					Fin Segun
				Hasta Que menu1 == 4
				
				
		Fin Segun
		
	Hasta Que menu == 4
FinAlgoritmo
