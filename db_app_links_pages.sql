-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: db_app
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `links_pages`
--

DROP TABLE IF EXISTS `links_pages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `links_pages` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `User_ID` int NOT NULL,
  `Page_Path` varchar(120) NOT NULL,
  `Referral_Path` varchar(120) NOT NULL,
  `Time` datetime NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID_UNIQUE` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links_pages`
--

LOCK TABLES `links_pages` WRITE;
/*!40000 ALTER TABLE `links_pages` DISABLE KEYS */;
INSERT INTO `links_pages` VALUES (1,1,'link_1','link_2','2020-06-24 20:58:18'),(2,1,'link_1','link_4','2020-06-24 20:58:18'),(3,1,'link_1','link_5','2020-06-24 20:58:18'),(4,1,'link_1','link_6','2020-06-24 20:58:18'),(5,1,'link_2','link_3','2020-06-24 20:58:18'),(6,1,'link_2','link_4','2020-06-24 20:58:18'),(7,1,'link_3','link_5','2020-06-24 20:58:18'),(8,1,'link_4','link_5','2020-06-24 20:58:18'),(9,1,'link_5','link_1','2020-06-24 20:58:18'),(10,1,'link_5','link_4','2020-06-24 20:58:18'),(11,1,'link_6','link_5','2020-06-24 20:58:18');
/*!40000 ALTER TABLE `links_pages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-26  1:14:29
