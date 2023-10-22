-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: caro
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `match_result`
--

DROP TABLE IF EXISTS `match_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match_result` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userID` int NOT NULL,
  `score` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_match_result_user_idx` (`userID`),
  CONSTRAINT `fk_match_result_user` FOREIGN KEY (`userID`) REFERENCES `user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_result`
--

LOCK TABLES `match_result` WRITE;
/*!40000 ALTER TABLE `match_result` DISABLE KEYS */;
INSERT INTO `match_result` VALUES (1,1,17,1,'2023-10-02 14:25:08'),(2,4,24,1,'2023-10-02 14:25:44'),(3,4,9,0,'2023-10-02 14:26:00'),(4,1,24,1,'2023-10-02 14:58:32'),(5,1,25,0,'2023-10-02 14:59:58'),(6,4,17,0,'2023-10-02 15:05:18'),(7,2,9,1,'2023-10-02 15:05:48'),(8,4,24,1,'2023-10-02 15:07:58'),(9,1,12,0,'2023-10-02 15:08:39'),(10,5,14,0,'2023-10-02 15:17:59'),(11,5,25,1,'2023-10-02 15:18:29'),(12,8,11,1,'2023-10-02 15:19:19'),(13,15,19,1,'2023-10-02 15:22:34'),(14,14,14,1,'2023-10-02 15:30:27'),(15,14,3,0,'2023-10-02 15:31:23'),(16,13,6,0,'2023-10-02 15:32:58'),(17,13,13,1,'2023-10-02 15:33:16'),(18,12,7,1,'2023-10-02 15:33:53'),(19,1,14,1,'2023-10-02 15:36:37'),(20,2,6,0,'2023-10-02 16:00:23'),(21,21,11,1,'2023-10-02 16:03:19'),(22,20,10,1,'2023-10-02 16:05:25'),(23,11,25,0,'2023-10-02 16:37:06'),(24,11,17,1,'2023-10-02 16:37:29'),(25,10,13,1,'2023-10-02 16:49:02'),(26,10,13,0,'2023-10-02 16:49:57'),(27,9,23,0,'2023-10-02 16:50:44'),(28,9,33,1,'2023-10-02 16:51:21'),(29,1,8,0,'2023-10-02 16:54:33'),(30,18,13,1,'2023-10-02 20:01:25'),(31,18,12,0,'2023-10-02 20:04:28'),(32,1,15,1,'2023-10-02 20:16:04'),(33,1,5,0,'2023-10-02 20:19:07'),(34,1,38,0,'2023-10-02 20:20:33'),(35,2,11,1,'2023-10-02 20:21:44'),(36,2,12,0,'2023-10-02 20:22:12'),(37,2,9,0,'2023-10-02 20:23:31'),(38,3,23,1,'2023-10-02 20:25:04'),(39,1,8,1,'2023-10-02 20:28:00'),(40,2,5,0,'2023-10-02 20:28:47'),(41,2,10,0,'2023-10-02 20:29:03'),(42,19,35,0,'2023-10-02 20:29:58'),(43,19,8,1,'2023-10-02 20:30:10'),(44,8,8,0,'2023-10-02 20:40:09'),(45,1,14,1,'2023-10-02 20:40:59'),(46,1,21,0,'2023-10-03 06:59:54'),(47,10,15,1,'2023-10-03 07:04:06'),(48,1,10,0,'2023-10-03 07:09:26'),(49,22,13,1,'2023-10-03 07:11:39'),(50,17,27,0,'2023-10-03 07:19:13'),(51,17,34,1,'2023-10-03 07:19:51'),(52,1,24,1,'2023-10-03 07:24:18'),(53,1,40,1,'2023-10-03 20:22:40'),(54,12,11,1,'2023-10-03 20:24:12'),(55,9,34,1,'2023-10-03 20:45:10'),(56,3,19,0,'2023-10-03 20:48:28'),(57,2,24,1,'2023-10-04 07:42:12'),(58,11,10,1,'2023-10-04 08:04:37'),(59,13,20,1,'2023-10-04 08:15:36'),(60,1,5,0,'2023-10-04 08:16:55'),(61,1,6,0,'2023-10-04 08:18:36'),(62,1,7,0,'2023-10-04 08:23:28'),(63,1,14,0,'2023-10-04 08:24:56'),(64,2,15,1,'2023-10-04 08:25:49'),(65,16,25,1,'2023-10-04 08:33:41'),(66,6,4,0,'2023-10-04 08:42:51'),(67,6,16,1,'2023-10-04 08:43:16'),(68,7,11,1,'2023-10-04 08:44:01'),(69,7,28,0,'2023-10-04 08:45:57'),(70,7,29,0,'2023-10-04 08:46:40'),(71,7,21,1,'2023-10-04 08:47:10'),(72,7,40,1,'2023-10-04 08:50:49'),(73,7,2,0,'2023-10-04 08:52:38'),(74,7,25,1,'2023-10-04 08:53:14'),(75,7,17,1,'2023-10-04 08:56:29'),(76,23,7,0,'2023-10-04 09:10:32'),(77,23,30,1,'2023-10-04 09:11:27'),(78,23,3,0,'2023-10-04 09:12:27'),(79,23,37,1,'2023-10-04 09:13:39'),(80,1,17,1,'2023-10-04 09:15:39'),(81,23,8,1,'2023-10-04 09:16:14'),(82,1,8,0,'2023-10-04 09:27:13'),(83,24,12,1,'2023-10-04 09:27:44'),(84,1,34,1,'2023-10-04 21:18:29'),(85,1,19,0,'2023-10-06 14:56:19'),(86,1,2,0,'2023-10-06 14:56:33'),(87,2,8,1,'2023-10-06 15:15:04'),(88,2,9,0,'2023-10-06 15:57:46'),(89,1,49,1,'2023-10-06 20:00:40'),(90,17,44,1,'2023-10-06 20:04:56'),(91,1,11,0,'2023-10-06 20:07:31'),(92,1,7,0,'2023-10-06 20:28:48'),(93,1,23,0,'2023-10-06 20:45:13'),(94,1,38,0,'2023-10-06 20:46:03'),(95,2,11,0,'2023-10-06 20:55:16'),(96,1,20,1,'2023-10-06 20:57:40'),(97,1,3,0,'2023-10-06 21:02:08'),(98,1,3,0,'2023-10-06 21:02:23'),(99,16,64,0,'2023-10-06 21:11:03'),(100,16,21,0,'2023-10-06 21:14:20'),(101,16,36,0,'2023-10-06 21:15:04'),(102,16,16,1,'2023-10-06 21:15:30'),(103,1,11,1,'2023-10-06 21:17:39'),(104,1,6,0,'2023-10-06 21:24:24'),(105,2,4,0,'2023-10-06 21:29:08'),(106,2,14,1,'2023-10-06 21:29:38'),(107,25,10,0,'2023-10-06 21:30:51'),(108,25,12,1,'2023-10-06 21:31:18'),(109,2,35,0,'2023-10-07 07:02:34'),(110,1,38,0,'2023-10-07 07:02:43'),(111,2,22,0,'2023-10-07 07:05:03'),(112,5,27,0,'2023-10-07 07:05:07'),(113,1,30,0,'2023-10-07 07:05:13'),(114,1,12,0,'2023-10-07 18:58:39'),(115,1,17,1,'2023-10-08 15:20:44'),(116,1,13,0,'2023-10-08 15:21:16'),(117,8,6,0,'2023-10-08 15:21:43'),(118,1,21,1,'2023-10-08 16:24:52'),(119,1,12,0,'2023-10-08 20:01:18'),(120,1,68,1,'2023-10-08 20:04:11'),(121,1,28,1,'2023-10-09 09:39:13'),(122,12,31,1,'2023-10-09 20:00:30'),(123,1,40,1,'2023-10-10 07:30:56'),(124,1,7,0,'2023-10-10 20:35:19'),(125,1,5,0,'2023-10-12 16:09:52'),(126,1,4,0,'2023-10-12 16:10:44'),(127,17,26,1,'2023-10-12 16:13:41'),(128,17,23,0,'2023-10-12 16:15:15'),(129,17,8,0,'2023-10-12 16:17:10'),(130,17,13,1,'2023-10-12 16:17:23'),(131,17,15,1,'2023-10-12 16:32:52'),(132,1,4,0,'2023-10-12 16:33:52'),(133,1,13,0,'2023-10-12 16:34:07'),(134,1,10,0,'2023-10-12 16:35:05'),(135,1,25,1,'2023-10-12 16:35:36'),(136,1,7,0,'2023-10-12 16:38:30'),(137,1,9,0,'2023-10-12 16:44:50'),(138,1,17,1,'2023-10-12 16:45:11'),(139,1,12,0,'2023-10-12 16:51:52'),(140,1,5,0,'2023-10-12 16:52:54'),(141,1,14,1,'2023-10-12 16:53:28'),(142,1,45,0,'2023-10-12 16:55:28'),(143,1,6,0,'2023-10-12 17:01:50'),(144,1,5,0,'2023-10-12 17:05:47'),(145,1,71,1,'2023-10-12 17:06:59'),(146,1,3,0,'2023-10-12 17:10:51'),(147,1,9,0,'2023-10-12 17:12:45'),(148,1,6,0,'2023-10-12 21:27:44'),(149,1,39,1,'2023-10-12 21:28:37'),(150,1,6,0,'2023-10-13 16:35:52'),(151,1,15,1,'2023-10-13 16:36:26'),(152,1,4,0,'2023-10-13 16:36:58'),(153,1,8,0,'2023-10-13 16:38:25'),(154,1,34,1,'2023-10-13 19:38:50'),(155,1,9,0,'2023-10-13 19:39:03'),(156,1,7,0,'2023-10-14 21:48:14'),(157,1,9,0,'2023-10-16 15:40:12'),(158,1,6,0,'2023-10-16 15:40:22'),(159,1,12,0,'2023-10-16 15:40:49'),(160,1,10,1,'2023-10-16 20:22:44'),(161,1,2,0,'2023-10-16 20:22:55'),(162,1,5,0,'2023-10-16 20:23:11'),(163,1,44,1,'2023-10-16 20:24:56'),(164,1,25,1,'2023-10-16 20:26:41'),(165,1,3,0,'2023-10-16 20:26:58'),(166,1,6,0,'2023-10-16 20:27:48'),(167,1,8,0,'2023-10-16 20:28:49'),(168,1,9,1,'2023-10-16 20:30:01'),(169,1,3,0,'2023-10-16 20:30:14'),(170,1,8,0,'2023-10-16 20:30:39'),(171,1,10,1,'2023-10-16 20:31:09'),(172,1,6,0,'2023-10-16 20:31:22'),(173,1,16,1,'2023-10-16 20:31:44'),(174,1,10,0,'2023-10-16 20:34:52'),(175,1,16,1,'2023-10-16 20:35:15'),(176,1,14,0,'2023-10-16 20:35:38'),(177,1,6,0,'2023-10-17 08:27:10'),(178,1,14,0,'2023-10-17 08:29:32'),(179,1,15,1,'2023-10-17 08:29:56'),(180,1,10,1,'2023-10-17 08:42:08'),(181,1,6,1,'2023-10-17 08:42:21'),(182,1,6,0,'2023-10-17 08:42:40'),(183,1,14,1,'2023-10-17 08:44:10'),(184,1,11,0,'2023-10-17 08:50:22'),(185,1,21,0,'2023-10-17 08:51:58'),(186,1,24,1,'2023-10-17 08:53:46'),(187,1,15,0,'2023-10-17 09:02:34'),(188,1,7,0,'2023-10-17 09:02:47'),(189,1,24,1,'2023-10-17 09:03:13'),(190,1,22,1,'2023-10-17 09:08:10'),(191,1,12,0,'2023-10-17 09:15:56'),(192,1,9,0,'2023-10-17 09:23:32'),(193,1,14,1,'2023-10-18 08:37:00'),(194,1,11,1,'2023-10-18 08:40:58'),(195,1,17,1,'2023-10-18 12:55:43'),(196,1,6,0,'2023-10-18 12:57:49'),(197,1,7,0,'2023-10-18 12:58:14'),(198,1,15,0,'2023-10-18 13:01:09'),(199,1,10,0,'2023-10-18 14:21:36'),(200,1,5,0,'2023-10-18 14:22:21');
/*!40000 ALTER TABLE `match_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `highScore` int DEFAULT '10000',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'sa','123','test@gmail.com',6),(2,'sa2','123','test@gmail.com',8),(3,'lekiengaming','12345','test@gmail.com',23),(4,'nguyenvu','12345','test@gmail.com',24),(5,'sa3','123','test@gmail.com',25),(6,'dd','123','test@gmail.com',16),(7,'ddd','123','test@gmail.com',11),(8,'sa4','123','test@gmail.com',11),(9,'sa5','123','test@gmail.com',33),(10,'sa6','123','test@gmail.com',13),(11,'sa7','123','test@gmail.com',10),(12,'sa8','123','test@gmail.com',7),(13,'sa9','123','test@gmail.com',13),(14,'sa10','123','test@gmail.com',14),(15,'sa11','123','test@gmail.com',19),(16,'sa12','123','test@gmail.com',16),(17,'sa13','123','test@gmail.com',13),(18,'sa14','123','test@gmail.com',13),(19,'sa15','123','test@gmail.com',8),(20,'kienle','123','test@gmail.com',10),(21,'levankien','123','test@gmail.com',11),(22,'sa16','123','test@gmail.com',13),(23,'sa19','123','test@gmail.com',8),(24,'sa17','123','test@gmail.com',12),(25,'sa18','123','test@gmail.com',12);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-18 14:38:53