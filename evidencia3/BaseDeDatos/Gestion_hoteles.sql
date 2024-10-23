CREATE SCHEMA IF NOT EXISTS `hoteles`;
USE `hoteles`;

-- -----------------------------------------------------
-- Tabla `cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cliente` (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  dni VARCHAR(10) NOT NULL UNIQUE, 
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  direccion VARCHAR(100) NOT NULL,
  email VARCHAR(50) NOT NULL UNIQUE, 
  numeroTelefono VARCHAR(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- -----------------------------------------------------
-- Tabla `disponibilidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `disponibilidad` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  disponibilidad VARCHAR(100) NOT NULL UNIQUE 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Valores iniciales para `disponibilidad`
INSERT INTO `disponibilidad` (disponibilidad) VALUES 
('Disponible'), ('Reservada'), ('Ocupada'), ('Mantenimiento');

-- -----------------------------------------------------
-- Tabla `tipoHabitacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tipoHabitacion` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  tipo VARCHAR(30) NOT NULL,
  precioNoche DECIMAL(10,2) NOT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Valores iniciales para `tipoHabitacion`
INSERT INTO `tipoHabitacion` (tipo, precioNoche) VALUES 
('Suite', 100000), ('Doble Estándar', 25000), ('Individual', 18000), ('Apartamento', 50000);

-- -----------------------------------------------------
-- Tabla `rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rol` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  rol VARCHAR(100) NOT NULL UNIQUE 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- -----------------------------------------------------
-- Tabla `habitacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habitacion` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  numeroHabitacion INT NOT NULL UNIQUE, 
  idTipoHabitacion INT NOT NULL,
  idDisponibilidad INT NOT NULL,
  FOREIGN KEY (idDisponibilidad) REFERENCES `disponibilidad`(id),
  FOREIGN KEY (idTipoHabitacion) REFERENCES `tipoHabitacion`(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- -----------------------------------------------------
-- Tabla `personal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `personal` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  correo VARCHAR(50) UNIQUE, 
  numeroTelefono VARCHAR(15), 
  horaEntrada TIME NOT NULL,
  horaSalida TIME NOT NULL,
  idRol INT NOT NULL,
  FOREIGN KEY (idRol) REFERENCES `rol`(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE IF NOT EXISTS `estadoMantenimiento` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  estado VARCHAR(30) NOT NULL UNIQUE 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Valores iniciales para `estadoMantenimiento`
INSERT INTO `estadoMantenimiento` (estado) VALUES 
('Pendiente'), ('En Proceso'), ('Completado');

-- -----------------------------------------------------
-- Tabla `reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reserva` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  idPersonal INT NOT NULL,
  idHabitacion INT NOT NULL,
  idCliente INT NOT NULL,
  fechaEntrada DATETIME NOT NULL,
  fechaSalida DATETIME NOT NULL,
  estadoReserva ENUM('activa', 'completada', 'cancelada') DEFAULT 'activa', 
  FOREIGN KEY (idCliente) REFERENCES `cliente`(id) ON DELETE CASCADE,
  FOREIGN KEY (idHabitacion) REFERENCES `habitacion`(id),
  FOREIGN KEY (idPersonal) REFERENCES `personal`(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- -----------------------------------------------------
-- Tabla `servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombreServicio VARCHAR(45),
  descripcion VARCHAR(85),
  precio DECIMAL(10,2) NOT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- -----------------------------------------------------
-- Tabla `servicioConsumido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicioConsumido` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  idReserva INT NOT NULL,
  idServicio INT NOT NULL,
  cantidad INT NOT NULL,
  FOREIGN KEY (idReserva) REFERENCES `reserva`(id),
  FOREIGN KEY (idServicio) REFERENCES `servicio`(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;