
-- INYECCION DE DATOS EN TABLA CLIENTES
USE hoteles;
INSERT INTO cliente (dni, nombre, apellido, direccion, email, numeroTelefono) 
VALUES
(12345678, 'Juan', 'Pérez', 'Calle Falsa 123', 'juan.perez@example.com', '111-2345'),
(23456789, 'Ana', 'García', 'Av. Libertador 456', 'ana.garcia@example.com', '111-6789'),
(34567890, 'Luis', 'Rodríguez', 'Calle Colón 789', 'luis.rodriguez@example.com', '111-1122'),
(45678901, 'María', 'López', 'Calle San Martín 321', 'maria.lopez@example.com', '111-3344'),
(56789012, 'Carlos', 'Martínez', 'Av. Rivadavia 654', 'carlos.martinez@example.com', '111-5566'),
(67890123, 'Laura', 'González', 'Calle Sarmiento 987', 'laura.gonzalez@example.com', '111-7788'),
(78901234, 'Pedro', 'Gómez', 'Av. Belgrano 159', 'pedro.gomez@example.com', '111-9900'),
(89012345, 'Sofía', 'Fernández', 'Calle Mitre 753', 'sofia.fernandez@example.com', '111-2233'),
(90123456, 'Diego', 'Ramírez', 'Calle Moreno 456', 'diego.ramirez@example.com', '111-4455'),
(12345067, 'Valeria', 'Sosa', 'Calle Güemes 789', 'valeria.sosa@example.com', '111-6677'),
(23456178, 'Jorge', 'Silva', 'Av. Mitre 963', 'jorge.silva@example.com', '111-8899'),
(34567289, 'Carmen', 'Torres', 'Calle Belgrano 123', 'carmen.torres@example.com', '111-1111'),
(45678390, 'Ricardo', 'Flores', 'Av. San Juan 456', 'ricardo.flores@example.com', '111-3333'),
(56789401, 'Paula', 'Ríos', 'Calle Corrientes 789', 'paula.rios@example.com', '111-5555'),
(67890512, 'Esteban', 'Díaz', 'Calle Callao 159', 'esteban.diaz@example.com', '111-7777'),
(78901623, 'Marta', 'Cabrera', 'Av. Santa Fe 753', 'marta.cabrera@example.com', '111-9999'),
(89012734, 'Roberto', 'Medina', 'Calle Lavalle 456', 'roberto.medina@example.com', '111-2222'),
(90123845, 'Isabel', 'Vega', 'Calle Córdoba 789', 'isabel.vega@example.com', '111-4444'),
(12345956, 'Daniel', 'Castro', 'Av. Las Heras 963', 'daniel.castro@example.com', '111-6666'),
(23456167, 'Carolina', 'Suárez', 'Calle Roca 123', 'carolina.suarez@example.com', '111-8888'),
(34567278, 'Gonzalo', 'Molina', 'Av. Alberdi 456', 'gonzalo.molina@example.com', '111-0000'),
(45678389, 'Lucía', 'Reyes', 'Calle Pueyrredón 789', 'lucia.reyes@example.com', '111-1212'),
(56789490, 'Federico', 'Aguilar', 'Av. Jujuy 159', 'federico.aguilar@example.com', '111-3434'),
(67890501, 'Elena', 'Ortiz', 'Calle Urquiza 753', 'elena.ortiz@example.com', '111-5656'),
(78901612, 'Alberto', 'Paz', 'Av. Salta 456', 'alberto.paz@example.com', '111-7878'),
(89012723, 'Gabriela', 'Campos', 'Calle Mendoza 789', 'gabriela.campos@example.com', '111-9090'),
(90123834, 'Francisco', 'Núñez', 'Calle Tucumán 963', 'francisco.nunez@example.com', '111-1414'),
(12345945, 'Adriana', 'Romero', 'Av. Entre Ríos 123', 'adriana.romero@example.com', '111-3636'),
(23456156, 'Matías', 'Vargas', 'Calle San Juan 456', 'matias.vargas@example.com', '111-5858'),
(34567267, 'Silvina', 'Herrera', 'Av. Libertador 789', 'silvina.herrera@example.com', '111-7070'),
(45678378, 'Mariano', 'Méndez', 'Calle Alem 159', 'mariano.mendez@example.com', '111-9292'),
(56789489, 'Alejandra', 'Morales', 'Calle Moreno 753', 'alejandra.morales@example.com', '111-1313'),
(67890500, 'Hernán', 'Figueroa', 'Av. San Lorenzo 456', 'hernan.figueroa@example.com', '111-3535'),
(78901611, 'Rosa', 'Navarro', 'Calle Callao 789', 'rosa.navarro@example.com', '111-5757'),
(89012722, 'Emanuel', 'Peña', 'Av. 9 de Julio 963', 'emanuel.pena@example.com', '111-7979'),
(90123833, 'Claudia', 'Bustos', 'Calle Belgrano 123', 'claudia.bustos@example.com', '111-0101'),
(12345944, 'Andrés', 'Cortés', 'Av. Corrientes 456', 'andres.cortes@example.com', '111-2323'),
(23456155, 'Liliana', 'Juárez', 'Calle Sarmiento 789', 'liliana.juarez@example.com', '111-4545'),
(34567266, 'Pablo', 'Leiva', 'Av. Mitre 159', 'pablo.leiva@example.com', '111-6767'),
(45678377, 'Victoria', 'Correa', 'Calle Moreno 753', 'victoria.correa@example.com', '111-8989'),
(56789488, 'Iván', 'Barrios', 'Av. Callao 456', 'ivan.barrios@example.com', '111-0202'),
(67890509, 'Lorena', 'Moyano', 'Calle Pueyrredón 789', 'lorena.moyano@example.com', '111-2424'),
(78901620, 'Julio', 'Ferreyra', 'Calle Alem 159', 'julio.ferreyra@example.com', '111-4646'),
(89012731, 'Verónica', 'Miranda', 'Calle Mitre 753', 'veronica.miranda@example.com', '111-6868'),
(90123842, 'Tomás', 'Rivera', 'Calle Lavalle 456', 'tomas.rivera@example.com', '111-8080'),
(12345953, 'Camila', 'Ruiz', 'Calle Colón 789', 'camila.ruiz@example.com', '111-1414'),
(23456164, 'Fabián', 'Benítez', 'Av. 9 de Julio 963', 'fabian.benitez@example.com', '111-3636'),
(34567275, 'Patricia', 'Álvarez', 'Calle Güemes 456', 'patricia.alvarez@example.com', '111-5858'),
(45678386, 'Hugo', 'Sánchez', 'Av. San Juan 789', 'hugo.sanchez@example.com', '111-7070');

-- INYECCION DE DATOS EN TABLA HABITACIÓN
INSERT INTO habitacion (numeroHabitacion, idTipoHabitacion, idDisponibilidad) VALUES
(101, 1, 1),  -- Suite, disponible
(102, 1, 2),  -- Suite, reservada
(103, 2, 3),  -- Doble Estándar, ocupada
(104, 2, 1),  -- Doble Estándar, disponible
(105, 3, 4),  -- Individual, mantenimiento
(106, 3, 2),  -- Individual, reservada
(107, 4, 1),  -- Apartamento, disponible
(108, 4, 3),  -- Apartamento, ocupada
(109, 1, 2),  -- Suite, reservada
(110, 1, 3),  -- Suite, ocupada
(111, 2, 1),  -- Doble Estándar, disponible
(112, 2, 4),  -- Doble Estándar, mantenimiento
(113, 3, 1),  -- Individual, disponible
(114, 3, 3),  -- Individual, ocupada
(115, 4, 2),  -- Apartamento, reservada
(116, 4, 1),  -- Apartamento, disponible
(117, 1, 3),  -- Suite, ocupada
(118, 2, 4),  -- Doble Estándar, mantenimiento
(119, 3, 1),  -- Individual, disponible
(120, 3, 2),  -- Individual, reservada
(121, 4, 3),  -- Apartamento, ocupada
(122, 1, 2),  -- Suite, reservada
(123, 1, 1),  -- Suite, disponible
(124, 2, 3),  -- Doble Estándar, ocupada
(125, 2, 2),  -- Doble Estándar, reservada
(126, 3, 1),  -- Individual, disponible
(127, 4, 1),  -- Apartamento, disponible
(128, 4, 2),  -- Apartamento, reservada
(129, 1, 4),  -- Suite, mantenimiento
(130, 1, 1),  -- Suite, disponible
(131, 2, 3),  -- Doble Estándar, ocupada
(132, 2, 1),  -- Doble Estándar, disponible
(133, 3, 2),  -- Individual, reservada
(134, 4, 3),  -- Apartamento, ocupada
(135, 4, 2),  -- Apartamento, reservada
(136, 1, 1),  -- Suite, disponible
(137, 1, 3),  -- Suite, ocupada
(138, 2, 4),  -- Doble Estándar, mantenimiento
(139, 3, 1),  -- Individual, disponible
(140, 3, 3),  -- Individual, ocupada
(141, 4, 2),  -- Apartamento, reservada
(142, 1, 1),  -- Suite, disponible
(143, 2, 3),  -- Doble Estándar, ocupada
(144, 2, 2),  -- Doble Estándar, reservada
(145, 3, 4),  -- Individual, mantenimiento
(146, 3, 1),  -- Individual, disponible
(147, 4, 3),  -- Apartamento, ocupada
(148, 4, 2),  -- Apartamento, reservada
(149, 1, 1),  -- Suite, disponible
(150, 1, 3);  -- Suite, ocupada

-- INYECCIÓN DE DATOS EN TABLA ROL
INSERT INTO rol (rol) VALUES
('Recepcionista'),
('Gerente'),
('Personal de limpieza'),
('Mantenimiento'),
('Cocinero');

-- INYECCIÓN DE DATOS EN TABLA PERSONAL
INSERT INTO personal (nombre, apellido, horaEntrada, horaSalida, idRol) VALUES
('Juan', 'Pérez', '08:00:00', '16:00:00', 1),
('María', 'González', '09:00:00', '17:00:00', 1),
('Pedro', 'López', '08:00:00', '16:00:00', 2),
('Ana', 'Martínez', '10:00:00', '18:00:00', 3),
('Luis', 'Fernández', '07:00:00', '15:00:00', 4),
('Sofía', 'Ramírez', '11:00:00', '19:00:00', 5),
('Diego', 'Torres', '08:00:00', '16:00:00', 2),
('Claudia', 'Díaz', '09:00:00', '17:00:00', 3);

-- INYECCION DE DATOS EN TABLA MANTENIMIENTO
INSERT INTO mantenimiento (idHabitacion, idPersonal, descripcionProblema, fechaReporte, idEstadoMantenimiento) VALUES
(10, 4, 'Reparar fuga de agua en el baño', '2024-10-01', 1),  
(20, 4, 'Ajustar calefacción que no enciende', '2024-10-02', 2),  
(30, 4, 'Reemplazar bombilla del plafón', '2024-10-03', 3),  
(40, 4, 'Limpieza de aire acondicionado', '2024-10-01', 1),  
(5, 3, 'Pintura de pared desgastada', '2024-10-04', 2),  
(6, 2, 'Revisar cerradura de la puerta', '2024-10-05', 1),  
(7, 4, 'Reparar grifo que gotea', '2024-10-01', 3),  
(8, 4, 'Reemplazar colchón dañado', '2024-10-02', 1),  
(9, 4, 'Revisar sistema eléctrico', '2024-10-03', 2),  
(10, 3, 'Ajustar ventana que no cierra bien', '2024-10-04', 1),  
(11, 4, 'Inspeccionar fuga en el aire acondicionado', '2024-10-02', 3),  
(12, 4, 'Desinfectar moho en la pared', '2024-10-03', 1),  
(13, 4, 'Reparar tapa del inodoro', '2024-10-05', 2),  
(14, 3, 'Reemplazar cortinas rotas', '2024-10-01', 3),  
(15, 4, 'Ajustar radiador que no calienta', '2024-10-02', 1),  
(16, 4, 'Cambiar bombilla de la lámpara de lectura', '2024-10-03', 1),  
(17, 2, 'Reparar silla rota', '2024-10-04', 3),  
(18, 3, 'Desinfectar moho en el baño', '2024-10-01', 2),  
(19, 4, 'Inspeccionar fugas en la ducha', '2024-10-02', 1),  
(20, 2, 'Cambiar cerradura de la puerta principal', '2024-10-03', 3);  



-- INYECCIÓN DE DATOS EN TABLA RESERVA
INSERT INTO reserva (idPersonal, idHabitacion, idCliente, fechaEntrada, fechaSalida) VALUES
(1, 1, 1, '2024-10-10', '2024-10-15'),  -- Juan, habitación 101, cliente 1
(2, 2, 2, '2024-10-12', '2024-10-14'),  -- María, habitación 102, cliente 2
(3, 3, 3, '2024-10-11', '2024-10-16'),  -- Pedro, habitación 103, cliente 3
(4, 4, 1, '2024-10-05', '2024-10-09'),  -- Ana, habitación 104, cliente 1
(1, 20, 4, '2024-10-07', '2024-10-10'),  -- Juan, habitación 120, cliente 4
(5, 25, 2, '2024-10-09', '2024-10-13'),  -- Sofía, habitación 125, cliente 2
(6, 32, 5, '2024-10-01', '2024-10-05'),  -- Luis, habitación 132, cliente 5
(2, 35, 6, '2024-10-04', '2024-10-06');  -- María, habitación 135, cliente 6


-- INYECCIÓN DE DATOS EN TABLA SERVICIO
INSERT INTO servicio (nombreServicio, descripcion, precio) VALUES
('Desayuno', 'Desayuno buffet con opciones variadas', 15000),
('Almuerzo', 'Almuerzo a la carta en el restaurante', 25000),
('Cena', 'Cena gourmet con menú especial', 30000),
('Servicio de lavandería', 'Lavado y planchado de ropa', 10000),
('Servicio de limpieza', 'Limpieza diaria de la habitación', 8000);

-- INYECCIÓN DE DATOS EN TABLA SERVICIOCONSUMIDO
INSERT INTO servicioconsumido (idReserva, idServicio, cantidad, precioTotal) VALUES
(1, 1, 2, 30.00),  -- Reserva 1, 2 Desayunos
(1, 2, 1, 25.00),  -- Reserva 1, 1 Almuerzo
(2, 3, 1, 30.00),  -- Reserva 2, 1 Cena
(3, 1, 1, 15.00),  -- Reserva 3, 1 Desayuno
(6, 4, 3, 30.00),  -- Reserva 4, 3 Lavandería
(5, 5, 1, 5.00),   -- Reserva 5, 1 limpieza
(8, 1, 1, 15.00),  -- Reserva 6, 1 Desayuno
(8, 2, 2, 50.00);  -- Reserva 7, 2 Almuerzos

