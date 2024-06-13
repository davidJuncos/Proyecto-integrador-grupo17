CREATE DATABASE  IF NOT EXISTS `hoteles` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hoteles`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: hoteles
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `DNI` int NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Apellido` varchar(100) NOT NULL,
  `Direccion` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `NumeroTelefono` varchar(100) NOT NULL,
  `Estado` int NOT NULL,
  PRIMARY KEY (`DNI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (36621991,'marta','suarez','rivadavia','martita20@gmail.com ','2336996581',1),(39871132,'Laura','Delfino','San Martin','laura12@gmail.com','35141120557',1),(41331454,'Cesar','Gutierrez','Colon','cesarrr2@gmail.com','2336267079',1),(45837754,'Rodrigo','Fuentes','San lorenzo','Rodrigo@gmail.com','2331409922',1);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disponibilidad`
--

DROP TABLE IF EXISTS `disponibilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disponibilidad` (
  `idDisponibilidad` int NOT NULL AUTO_INCREMENT,
  `Disponibilidad` varchar(100) NOT NULL,
  PRIMARY KEY (`idDisponibilidad`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disponibilidad`
--

LOCK TABLES `disponibilidad` WRITE;
/*!40000 ALTER TABLE `disponibilidad` DISABLE KEYS */;
INSERT INTO `disponibilidad` VALUES (1,'DISPONIBLE'),(2,'Ocupado');
/*!40000 ALTER TABLE `disponibilidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `habitaciones`
--

DROP TABLE IF EXISTS `habitaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `habitaciones` (
  `NroHabitacion` int NOT NULL,
  `TipoHabitacion` varchar(100) NOT NULL,
  `PrecioNoche` decimal(10,2) NOT NULL,
  `IdDisponibilidad` int NOT NULL,
  PRIMARY KEY (`NroHabitacion`),
  KEY `fk_Habitaciones_Disponibilidad` (`IdDisponibilidad`),
  CONSTRAINT `fk_Habitaciones_Disponibilidad` FOREIGN KEY (`IdDisponibilidad`) REFERENCES `disponibilidad` (`idDisponibilidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habitaciones`
--

LOCK TABLES `habitaciones` WRITE;
/*!40000 ALTER TABLE `habitaciones` DISABLE KEYS */;
INSERT INTO `habitaciones` VALUES (1,'DOBLE',15000.00,1),(2,'Triple',25000.00,1);
/*!40000 ALTER TABLE `habitaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal`
--

DROP TABLE IF EXISTS `personal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal` (
  `idPersonal` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) NOT NULL,
  `Apellido` varchar(100) NOT NULL,
  `HoraInicia` time NOT NULL,
  `HoraFin` time NOT NULL,
  `IdRol` int NOT NULL,
  `Estado` int NOT NULL,
  PRIMARY KEY (`idPersonal`),
  KEY `fk_Personas_Roles` (`IdRol`),
  CONSTRAINT `fk_Personas_Roles` FOREIGN KEY (`IdRol`) REFERENCES `roles` (`idRol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal`
--

LOCK TABLES `personal` WRITE;
/*!40000 ALTER TABLE `personal` DISABLE KEYS */;
INSERT INTO `personal` VALUES (1,'Juana','Paez','00:00:06','00:00:12',1,1),(2,'Santiago','Gomez','00:00:06','00:00:14',2,1);
/*!40000 ALTER TABLE `personal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservas`
--

DROP TABLE IF EXISTS `reservas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservas` (
  `idReserva` int NOT NULL AUTO_INCREMENT,
  `FechaEntrada` datetime NOT NULL,
  `FechaSalida` datetime NOT NULL,
  `EstadoReserva` int NOT NULL,
  `idPersonal` int NOT NULL,
  `DNI` int NOT NULL,
  `NroHabitacion` int NOT NULL,
  PRIMARY KEY (`idReserva`),
  KEY `fk_Reservas_Personas` (`idPersonal`),
  KEY `fk_Reservas_Habitaciones` (`NroHabitacion`),
  KEY `fk_Reservas_Clientes` (`DNI`),
  CONSTRAINT `fk_Reservas_Clientes` FOREIGN KEY (`DNI`) REFERENCES `clientes` (`DNI`),
  CONSTRAINT `fk_Reservas_Habitaciones` FOREIGN KEY (`NroHabitacion`) REFERENCES `habitaciones` (`NroHabitacion`),
  CONSTRAINT `fk_Reservas_Personas` FOREIGN KEY (`idPersonal`) REFERENCES `personal` (`idPersonal`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservas`
--

LOCK TABLES `reservas` WRITE;
/*!40000 ALTER TABLE `reservas` DISABLE KEYS */;
INSERT INTO `reservas` VALUES (1,'2024-04-20 00:00:00','2024-04-29 00:00:00',1,1,45837754,1),(2,'2025-09-02 00:00:00','2025-09-12 00:00:00',1,1,45837754,1),(3,'2024-07-20 00:00:00','2024-07-29 00:00:00',1,1,41331454,2);
/*!40000 ALTER TABLE `reservas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `idRol` int NOT NULL AUTO_INCREMENT,
  `Rol` varchar(100) NOT NULL,
  PRIMARY KEY (`idRol`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Secretaria'),(2,'Jardinero'),(3,'Recepcionista'),(4,'Limpieza'),(5,'Cocinero'),(6,'Guardia');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-12 23:23:05
