-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Hoteles
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Hoteles
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Hoteles` DEFAULT CHARACTER SET utf8 ;
USE `Hoteles` ;

-- -----------------------------------------------------
-- Table `Hoteles`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hoteles`.`Clientes` (
  `DNI` INT NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  `Apellido` VARCHAR(100) NOT NULL,
  `Direccion` VARCHAR(100) NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `NumeroTelefono` VARCHAR(100) NOT NULL,
  `Estado` INT NOT NULL,
  PRIMARY KEY (`DNI`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Hoteles`.`Reservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hoteles`.`Reservas` (
  `idReserva` INT NOT NULL,
  `FechaEntrada` DATETIME NOT NULL,
  `FechaSalida` DATETIME NOT NULL,
  `EstadoReserva` INT NOT NULL,
  `idPersona` INT NOT NULL,
  `DNI` INT NOT NULL,
  `NroHabitacion` INT NOT NULL,
  PRIMARY KEY (`idReserva`),
  UNIQUE INDEX `DNI_UNIQUE` (`DNI` ASC) VISIBLE,
  CONSTRAINT `NroHabitacion`
    FOREIGN KEY ()
    REFERENCES `Hoteles`.`Reservas` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Hoteles`.`Habitaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hoteles`.`Habitaciones` (
  `NroHabitacion` INT NOT NULL,
  `TipoHabitacion` VARCHAR(100) NOT NULL,
  `PrecioNoche` DECIMAL(10,2) NOT NULL,
  `IdDisponibilidad` INT NOT NULL,
  PRIMARY KEY (`NroHabitacion`),
  CONSTRAINT `NroHabitacion`
    FOREIGN KEY ()
    REFERENCES `Hoteles`.`Reservas` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Hoteles`.`Personas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hoteles`.`Personas` (
  `idPersona` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(100) NOT NULL,
  `Apellido` VARCHAR(100) NOT NULL,
  `HoraInicia` TIME NOT NULL,
  `HoraFin` TIME NOT NULL,
  `IdRol` INT NOT NULL,
  `Estado` INT NOT NULL,
  PRIMARY KEY (`idPersona`),
  CONSTRAINT `idReseva`
    FOREIGN KEY (`idPersona`)
    REFERENCES `Hoteles`.`Reservas` (`idReserva`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Hoteles`.`Disponibilidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hoteles`.`Disponibilidad` (
  `idDisponibilidad` INT NOT NULL AUTO_INCREMENT,
  `Disponibilidad` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idDisponibilidad`),
  CONSTRAINT `idDisponibilidad`
    FOREIGN KEY (`idDisponibilidad`)
    REFERENCES `Hoteles`.`Habitaciones` (`NroHabitacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Hoteles`.`Roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hoteles`.`Roles` (
  `idRol` INT NOT NULL AUTO_INCREMENT,
  `Rol` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idRol`),
  CONSTRAINT `IdRol`
    FOREIGN KEY (`idRol`)
    REFERENCES `Hoteles`.`Personas` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
