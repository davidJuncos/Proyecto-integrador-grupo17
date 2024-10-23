-- SELECT
-- Nombres y apellidos de clientes con reservas
SELECT c.nombre, c.apellido 
FROM cliente c
JOIN reserva r ON c.id = r.idCliente;

-- todas las reservas que tienen fecha de entrada después del 10 de octubre de 2024
SELECT id 
FROM reserva 
WHERE fechaEntrada > '2024-10-10';

-- id, nombre y precio de todos los servicios
SELECT id, nombreServicio, precio 
FROM servicio 
ORDER BY id DESC;

-- Reservas con más de 2 noches de estancia
SELECT id, idCliente, fechaEntrada, fechaSalida
FROM reserva
WHERE DATEDIFF(fechaSalida, fechaEntrada) > 2;

-- Detalles de mantenimiento por estado "Pendiente":
SELECT m.id, m.idHabitacion, m.descripcionProblema, em.estado
FROM mantenimiento m
JOIN estadoMantenimiento em ON m.idEstadoMantenimiento = em.id
WHERE em.estado = 'Pendiente';

-- Nombre del personal encargado de las reservas de un cliente específico
SELECT p.nombre 
FROM personal p
JOIN reserva r ON p.id = r.idPersonal
WHERE r.idCliente = 1;


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

-- Inserciones múltiples de clientes
INSERT INTO cliente (dni, nombre, apellido, direccion, email, numeroTelefono) 
VALUES 
    (23456789, 'Ana', 'García', 'Calle Falsa 456', 'ana.garcia@example.com', '555-5678'),
    (34567890, 'Luis', 'Rodríguez', 'Calle Colón 789', 'luis.rodriguez@example.com', '555-9012'),
    (45678901, 'María', 'López', 'Calle San Martín 321', 'maria.lopez@example.com', '555-3456');

-- UPDATE

-- Actualizar dirección de clientes por DNI
UPDATE cliente 
SET 
    direccion = CASE 
        WHEN dni = 12345678 THEN 'Calle Nueva 456'
        WHEN dni = 23456789 THEN 'Calle Vieja 789'
        ELSE direccion
    END
WHERE dni IN (12345678, 23456789);

-- Cambiar disponibilidad de habitaciones tipo Suite
UPDATE habitacion 
SET idDisponibilidad = 2  -- Reservada
WHERE idTipoHabitacion = 1 AND idDisponibilidad = 1;

-- Aumentar precio de servicios consumidos más de dos veces
UPDATE servicio s
SET s.precio = s.precio * 1.10
WHERE EXISTS (
    SELECT 1
    FROM servicioConsumido sc
    WHERE sc.idServicio = s.id AND sc.cantidad > 2
);

-- DELETE

-- Eliminar un cliente por ID
DELETE FROM cliente WHERE id = 33;

-- Eliminar servicios con IDs específicos
DELETE FROM servicio WHERE id IN (1, 2, 3);

-- Eliminar habitaciones ocupadas de tipo Suite
DELETE FROM habitacion 
WHERE idDisponibilidad = 3 AND idTipoHabitacion = 1;

-- Eliminar servicios consumidos sin reservas asociadas
DELETE FROM servicioConsumido 
WHERE idReserva NOT IN (SELECT id FROM reserva);

-- Eliminar todos los registros de mantenimiento
DELETE FROM mantenimiento;

-- Eliminar reservas de un cliente específico por DNI
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
FROM reserva r
JOIN cliente c ON r.idCliente = c.id;

-- Obtener servicios consumidos junto con la reserva
SELECT 
    sc.idReserva,
    s.nombreServicio,
    sc.cantidad
FROM servicioConsumido sc
JOIN servicio s ON sc.idServicio = s.id
JOIN reserva r ON sc.idReserva = r.id;

-- Obtener habitaciones ocupadas con información del cliente
SELECT 
    h.numeroHabitacion,
    c.nombre AS nombreCliente,
    c.apellido AS apellidoCliente,
    r.fechaEntrada,
    r.fechaSalida
FROM habitacion h
JOIN reserva r ON h.id = r.idHabitacion
JOIN cliente c ON r.idCliente = c.id
WHERE h.idDisponibilidad = 3;
