-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema hoteles
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hoteles
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hoteles` DEFAULT CHARACTER SET utf8mb3 ;
USE `hoteles` ;

-- -----------------------------------------------------
-- Table `hoteles`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hoteles`.`clientes` (
  `DNI` INT NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  `Apellido` VARCHAR(100) NOT NULL,
  `Direccion` VARCHAR(100) NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `NumeroTelefono` VARCHAR(100) NOT NULL,
  `Estado` INT NOT NULL,
  PRIMARY KEY (`DNI`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hoteles`.`disponibilidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hoteles`.`disponibilidad` (
  `idDisponibilidad` INT NOT NULL AUTO_INCREMENT,
  `Disponibilidad` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idDisponibilidad`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hoteles`.`habitaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hoteles`.`habitaciones` (
  `NroHabitacion` INT NOT NULL,
  `TipoHabitacion` VARCHAR(100) NOT NULL,
  `PrecioNoche` DECIMAL(10,2) NOT NULL,
  `IdDisponibilidad` INT NOT NULL,
  PRIMARY KEY (`NroHabitacion`),
  INDEX `fk_Habitaciones_Disponibilidad` (`IdDisponibilidad` ASC) ,
  CONSTRAINT `fk_Habitaciones_Disponibilidad`
    FOREIGN KEY (`IdDisponibilidad`)
    REFERENCES `hoteles`.`disponibilidad` (`idDisponibilidad`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hoteles`.`roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hoteles`.`roles` (
  `idRol` INT NOT NULL AUTO_INCREMENT,
  `Rol` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idRol`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hoteles`.`personal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hoteles`.`personal` (
  `idPersonal` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(100) NOT NULL,
  `Apellido` VARCHAR(100) NOT NULL,
  `HoraInicia` TIME NOT NULL,
  `HoraFin` TIME NOT NULL,
  `IdRol` INT NOT NULL,
  `Estado` INT NOT NULL,
  PRIMARY KEY (`idPersonal`),
  INDEX `fk_Personas_Roles` (`IdRol` ASC) ,
  CONSTRAINT `fk_Personas_Roles`
    FOREIGN KEY (`IdRol`)
    REFERENCES `hoteles`.`roles` (`idRol`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hoteles`.`reservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hoteles`.`reservas` (
  `idReserva` INT NOT NULL,
  `FechaEntrada` DATETIME NOT NULL,
  `FechaSalida` DATETIME NOT NULL,
  `EstadoReserva` INT NOT NULL,
  `idPersonal` INT NOT NULL,
  `DNI` INT NOT NULL,
  `NroHabitacion` INT NOT NULL,
  PRIMARY KEY (`idReserva`),
  INDEX `fk_Reservas_Personas` (`idPersonal` ASC) ,
  INDEX `fk_Reservas_Habitaciones` (`NroHabitacion` ASC) ,
  CONSTRAINT `fk_Reservas_Clientes`
    FOREIGN KEY (`DNI`)
    REFERENCES `hoteles`.`clientes` (`DNI`),
  CONSTRAINT `fk_Reservas_Habitaciones`
    FOREIGN KEY (`NroHabitacion`)
    REFERENCES `hoteles`.`habitaciones` (`NroHabitacion`),
  CONSTRAINT `fk_Reservas_Personas`
    FOREIGN KEY (`idPersonal`)
    REFERENCES `hoteles`.`personal` (`idPersonal`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;