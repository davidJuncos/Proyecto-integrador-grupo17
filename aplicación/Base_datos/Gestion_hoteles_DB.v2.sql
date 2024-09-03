-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hoteles`;
USE `hoteles`;

-- -----------------------------------------------------
-- Table `cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cliente` (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  dni INT(10),
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  direccion VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  numeroTelefono VARCHAR(100) NOT NULL
);

-- -----------------------------------------------------
-- Table `disponibilidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `disponibilidad` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  disponibilidad VARCHAR(100) NOT NULL UNIQUE
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- Inserción de valores por defecto para tabla disponibilidad
INSERT INTO `disponibilidad` (disponibilidad) VALUES 
('Disponible'),
('Reservada'),
('Ocupada'),
('Mantenimiento');

-- Restricción para evitar modificaciones
DELIMITER //
CREATE TRIGGER `no_modificar_disponibilidad`
BEFORE UPDATE ON `disponibilidad`
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'No se permite modificar los valores de disponibilidad';
END;
//
DELIMITER ;

-- Restricción para evitar eliminaciones
DELIMITER //
CREATE TRIGGER `no_eliminar_disponibilidad`
BEFORE DELETE ON `disponibilidad`
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'No se permite eliminar los valores de disponibilidad';
END;
//
DELIMITER ;

-- Restricción para evitar inserciones
DELIMITER //
CREATE TRIGGER `no_insertar_disponibilidad`
BEFORE INSERT ON `disponibilidad`
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'No se permite insertar nuevos valores en la tabla disponibilidad';
END;
//
DELIMITER ;

-- -----------------------------------------------------
-- Table `habitacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habitacion` (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  numeroHabitacion INT,
  idTipoHabitacion VARCHAR(100) NOT NULL,
  precioNoche DECIMAL(10,2) NOT NULL,
  idDisponibilidad INT NOT NULL,
  FOREIGN KEY (idDisponibilidad)
	REFERENCES `disponibilidad`(id),
  FOREIGN KEY (idTipoHabitacion)
	REFERENCES tipoHabitacion(id)
);


-- -----------------------------------------------------
-- Table `tipoHabitacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tipoHabitacion` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  tipo VARCHAR(30) NOT NULL
);

-- Inserción de valores por defecto
INSERT INTO `tipoHabitacion` (tipo) VALUES 
('Suite'),
('Doble Estándar'),
('Individual'),
('Apartamento');

-- Restricción para evitar modificaciones de la tabla tipoHabitacion
DELIMITER //
CREATE TRIGGER `no_modificar_tipoHabitacion`
BEFORE UPDATE ON `tipoHabitacion`
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'No se permite modificar los valores de tipo de habitación';
END;
//
DELIMITER ;

-- Restricción para evitar eliminaciones
DELIMITER //
CREATE TRIGGER `no_eliminar_tipoHabitacion`
BEFORE DELETE ON `tipoHabitacion`
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'No se permite eliminar los valores de tipo de habitación';
END;
//
DELIMITER ;

-- Restricción para evitar inserciones
DELIMITER //
CREATE TRIGGER `no_insertar_tipoHabitacion`
BEFORE INSERT ON `tipoHabitacion`
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'No se permite insertar nuevos valores en la tabla tipoHabitacion';
END;
//
DELIMITER ;

-- -----------------------------------------------------
-- Table `rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rol` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  rol VARCHAR(100) NOT NULL
);

-- -----------------------------------------------------
-- Table `personal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `personal` (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  horaEntrada TIME NOT NULL,
  horaSalida TIME NOT NULL,
  idRol INT NOT NULL,
  FOREIGN KEY (idRol)
    REFERENCES `rol`(id)
);

-- -----------------------------------------------------
-- Table `reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reserva` (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  idPersonal INT NOT NULL,
  idHabitacion INT NOT NULL,
  idCliente INT NOT NULL,
  fechaEntrada DATETIME NOT NULL,
  fechaSalida DATETIME NOT NULL,
  
  FOREIGN KEY (idCliente)
    REFERENCES `cliente`(id),
  FOREIGN KEY (idHabitacion)
    REFERENCES `habitacion`(id),
  FOREIGN KEY (idPersonal)
    REFERENCES `personal`(id)
);

-- -----------------------------------------------------
-- Table `servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicio` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombreServicio VARCHAR(45),
  descripcion VARCHAR(85),
  precio DECIMAL(10,2)
);

-- -----------------------------------------------------
-- Table `servicioConsumido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servicioConsumido` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  idReserva INT NOT NULL,
  idServicio INT NOT NULL,
  cantidad INT NOT NULL,
  precioTotal DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (idReserva) REFERENCES reserva(id), 
  FOREIGN KEY (idServicio) REFERENCES servicio(id) 
);

-- -----------------------------------------------------
-- Table `mantenimiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mantenimiento` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  idHabitacion INT NOT NULL,
  idPersonal INT NOT NULL,
  descripcionProblema TEXT NOT NULL,
  fechaReporte DATE NOT NULL,
  fechaResolucion DATE, 
  estado VARCHAR(50) NOT NULL,
  FOREIGN KEY (idHabitacion) REFERENCES habitacion(id), 
  FOREIGN KEY (idPersonal) REFERENCES personal(id),
  FOREIGN KEY (idEstadoMantenimiento) REFERENCES estadoMantenimiento(id)
);

-- -----------------------------------------------------
-- Table `estadoMantenimiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estadoMantenimiento` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  estado VARCHAR(30) NOT NULL
);

-- Inserción de valores por defecto
INSERT INTO `estadoMantenimiento` (estado) VALUES 
('Pendiente'),
('En Proceso'),
('Completado');

-- Restricción para evitar modificaciones de la tabla estadoMantenimiento
DELIMITER //
CREATE TRIGGER `no_modificar_estadoMantenimiento`
BEFORE UPDATE ON `estadoMantenimiento`
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'No se permite modificar los valores de estado del mantenimiento';
END;
//
DELIMITER ;

-- Restricción para evitar eliminaciones
DELIMITER //
CREATE TRIGGER `no_eliminar_estadoMantenimiento`
BEFORE DELETE ON `estadoMantenimiento`
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'No se permite eliminar los valores de estado del mantenimiento';
END;
//
DELIMITER ;

-- Restricción para evitar inserciones
DELIMITER //
CREATE TRIGGER `no_insertar_estadoMantenimiento`
BEFORE INSERT ON `estadoMantenimiento`
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'No se permite insertar nuevos valores en la tabla estadoMantenimiento';
END;
//
DELIMITER ;
