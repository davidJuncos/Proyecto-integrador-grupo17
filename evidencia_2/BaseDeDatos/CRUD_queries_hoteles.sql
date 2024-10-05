-- SELECT
-- nombres y apellidos de clientes que tienen reservas
SELECT p.nombre, p.apellido 
FROM personal p 
JOIN reserva r ON p.id = r.idPersonal;

-- todas las reservas que tienen fecha de entrada después del 10 de octubre de 2024
SELECT id 
FROM reserva 
WHERE fechaEntrada > '2024-10-10';

-- id, nombre y precio de todos los servicios
SELECT id, nombreServicio, precio 
FROM servicio 
ORDER BY id DESC;

-- detalles de las reservas con más de 2 noches de estancia
SELECT id, idCliente, fechaEntrada, fechaSalida 
FROM reserva 
WHERE DATEDIFF(fechaSalida, fechaEntrada) > 2;

-- Detalles de mantenimiento por estado específico
SELECT id, idHabitacion, descripcionProblema 
FROM mantenimiento 
WHERE idEstadoMantenimiento = 1;  -- Estado "Pendiente"

-- Nombre del personal encargado de las reservas de un cliente específico
SELECT p.nombre 
FROM personal p 
WHERE p.id IN (SELECT r.idPersonal FROM reserva r WHERE r.idCliente = 1);

-- INSERT
-- Nuevo cliente
INSERT INTO cliente (dni, nombre, apellido, direccion, email, numeroTelefono) 
VALUES (12345678, 'Carlos', 'Mendoza', 'Calle Ejemplo 123', 'carlos.mendoza@example.com', '555-1234');

-- Nuevo personal
INSERT INTO personal (nombre, apellido, horaEntrada, horaSalida, idRol) 
VALUES ('Laura', 'Sánchez', '08:00:00', '16:00:00', 1);

-- Nuevo servicio
INSERT INTO servicio (nombreServicio, descripcion, precio) 
VALUES ('Masaje Relajante', 'Masaje de 60 minutos para relajación', 10000);

INSERT INTO cliente (dni, nombre, apellido, direccion, email, numeroTelefono) 
VALUES 
    (23456789, 'Ana', 'García', 'Calle Falsa 456', 'ana.garcia@example.com', '555-5678'),
    (34567890, 'Luis', 'Rodríguez', 'Calle Colón 789', 'luis.rodriguez@example.com', '555-9012'),
    (45678901, 'María', 'López', 'Calle San Martín 321', 'maria.lopez@example.com', '555-3456');
    
-- UPDATE
-- Cambiar dirección de cliente
UPDATE cliente 
SET 
    direccion = CASE 
        WHEN dni = 12345678 THEN 'Calle Nueva 456'
        WHEN dni = 23456789 THEN 'Calle Vieja 789'
        ELSE direccion
    END
WHERE dni IN (12345678, 23456789);

-- Cambiar disponibilidad de un tipo de habitación
UPDATE habitacion 
SET idDisponibilidad = 2  -- Reservada
WHERE idTipoHabitacion = 1 AND idDisponibilidad = 1;  -- Solo habitaciones disponibles

-- Actualizar precio de servicios 
UPDATE servicio 
SET precio = precio * 1.10  -- Aumentar el precio en un 10%
WHERE id IN (SELECT idServicio FROM servicioconsumido WHERE cantidad > 2);

-- DELETE
-- Eliminar datos de un cliente
DELETE FROM cliente 
WHERE id = 33;  -- Eliminar el cliente con id 33

DELETE FROM servicio 
WHERE id IN (1, 2, 3);  -- Eliminar servicios con id 1, 2 y 3


-- Elminar habitaciones ocupadas de tipo suite
DELETE FROM habitacion 
WHERE idDisponibilidad = 3 AND idTipoHabitacion = 1; 

-- Eliminar registros de servicios consumidos que no tienen reservas asociadas
DELETE FROM servicioconsumido 
WHERE idReserva NOT IN (SELECT id FROM reserva);

-- Eliminar todos los registros de la tabla mantenimiento
DELETE FROM mantenimiento; 

-- Eliminar reservas de un cliente específico
DELETE r 
FROM reserva r
JOIN cliente c ON r.idCliente = c.id
WHERE c.dni = 12345678; 

-- JOIN
-- Obtener todas las reservas con detalles del cliente
SELECT 
    r.id AS idReserva,
    c.nombre AS nombreCliente,
    c.apellido AS apellidoCliente,
    r.fechaEntrada,
    r.fechaSalida
FROM 
    reserva r
JOIN 
    cliente c ON r.idCliente = c.id;

-- Obtener servicios consumidos junto con la reserva
SELECT 
    sc.idReserva,
    s.nombreServicio,
    sc.cantidad,
    sc.precioTotal
FROM 
    servicioconsumido sc
JOIN 
    servicio s ON sc.idServicio = s.id
JOIN 
    reserva r ON sc.idReserva = r.id;

-- Obtener habitaciones ocupadas junto con la información del cliente
SELECT 
    h.numeroHabitacion,
    c.nombre AS nombreCliente,
    c.apellido AS apellidoCliente,
    r.fechaEntrada,
    r.fechaSalida
FROM 
    habitacion h
JOIN 
    reserva r ON h.id = r.idHabitacion
JOIN 
    cliente c ON r.idCliente = c.id
WHERE 
    h.idDisponibilidad = 3;  -- Solo habitaciones ocupadas





