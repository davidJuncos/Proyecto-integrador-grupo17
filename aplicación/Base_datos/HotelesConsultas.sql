SELECT * FROM habitaciones;
SELECT * FROM clientes;
SELECT * FROM personal;
SELECT * FROM reservas;
SELECT * FROM roles;
SELECT * FROM disponibilidad;
SELECT Nombre, HoraInicia, HoraFin FROM personal;
SELECT TipoHabitacion FROM habitaciones WHERE PrecioNoche > 15000;
SELECT * FROM personal WHERE HoraInicia BETWEEN 6 AND 9 ;
SELECT DNI FROM clientes WHERE Nombre LIKE '%Laura%';
SELECT * FROM clientes WHERE NumeroTelefono LIKE '%2331%' LIMIT 2;
SELECT * FROM habitaciones inner join disponibilidad ON habitaciones.IdDisponibilidad = disponibilidad.idDisponibilidad;
SELECT  * FROM reservas WHERE FechaEntrada BETWEEN '2024-04-20 00:00:00' AND '2024-07-30 00:00:00';



