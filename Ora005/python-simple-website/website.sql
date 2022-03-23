-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `images` (
  `id` int NOT NULL AUTO_INCREMENT,
  `filename` varchar(200) DEFAULT NULL,
  `published` tinyint(3) unsigned zerofill DEFAULT NULL,
  `alt` varchar(200) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `userId` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES (1,'./static/images/4.5_x_6.5.jpg',001,'Ahmet Murati','Ahmet Murati','1'),(2,'./static/images/4.5_x_6.5_small2a.jpg',001,'Ahmet Murati declaiming one of his poetry work in a literature evening','Ahmet Murati declaiming one of his poetry work in a literature evening','1'),(3,'./static/images/4.5_x_6.5_small.jpg',001,'Alta','a','1'),(4,'./static/images/4.5_x_6.5_small2a.jpg',001,'AhmetMurati','Ahmet Murati','1'),(5,'./static/images/2008.03.04_Certificate_of_Achievement_Sun_Microsystems.jpg',001,'Sun Microsystems','Sun Microsystems','1');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `body` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `user` int DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `titleIndex` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (17,'title','<p><a href=\"google.com\">ade&nbsp;</a></p>',1,'/static/images/icons8-login-64.png'),(18,'Title','<p><strong>Përmbajtja</strong></p>',1,'/static/images/Python-logo-notext.svg'),(19,'Titulli','<p><i>ad</i></p>',1,'/static/images/Python-logo-notext.svg'),(20,'Titulli','<p><i>ad</i></p>',1,'/static/images/Python-logo-notext.svg'),(21,'Përshëndetje','<p>Si jeni a jeni mirë?</p>',1,'/static/images/FOWcrgdXEAAqACp.jpg'),(22,'Përshëndetje nga Gjermania','<p><strong>P&euml;rsh&euml;ndetje</strong></p>\r\n\r\n<p><em>P&euml;rsh&euml;ndetje</em></p>\r\n\r\n<p>&nbsp;</p>\r\n',1,'./static/images/icons8-login-64.png'),(23,'Përshëndetje nga Gjermania','<p><strong>P&euml;rsh&euml;ndetje</strong></p>\r\n\r\n<p><em>P&euml;rsh&euml;ndetje</em></p>\r\n\r\n<p>&nbsp;</p>\r\n',1,'./static/images/icons8-login-64.png'),(24,'Përshëndetje nga Gjermania','<p><strong>P&euml;rsh&euml;ndetje</strong></p>\r\n\r\n<p><em>P&euml;rsh&euml;ndetje</em></p>\r\n\r\n<p>&nbsp;</p>\r\n',1,'./static/images/icons8-login-64.png');
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(200) DEFAULT NULL,
  `firstName` varchar(200) DEFAULT NULL,
  `lastName` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'am2022','Ahmet','Murati','ahmet.murati@live.com','LridTXn2hJ6n4PB','+4915123015776');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-23 20:23:37
