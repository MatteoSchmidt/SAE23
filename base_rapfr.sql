-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : dim. 07 mai 2023 à 13:33
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `base_rapfr`
--

-- --------------------------------------------------------

--
-- Structure de la table `annonces`
--

DROP TABLE IF EXISTS `annonces`;
CREATE TABLE IF NOT EXISTS `annonces` (
  `N°annonces` int NOT NULL AUTO_INCREMENT,
  `Concert` text NOT NULL,
  `Date` date NOT NULL,
  `Lieu de départ` text NOT NULL,
  `Heure de départ` time NOT NULL,
  `Places` int NOT NULL,
  PRIMARY KEY (`N°annonces`),
  KEY `N°annonces` (`N°annonces`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `chanteurs`
--

DROP TABLE IF EXISTS `chanteurs`;
CREATE TABLE IF NOT EXISTS `chanteurs` (
  `N°rappeurs` int NOT NULL AUTO_INCREMENT,
  `Nom de scène` text NOT NULL,
  `Nom` text NOT NULL,
  `Prénom` text NOT NULL,
  `Date de naissance` date NOT NULL,
  `Lien Insta` text NOT NULL,
  `Date du 1er album` date NOT NULL,
  `Nom Groupe` text NOT NULL,
  PRIMARY KEY (`N°rappeurs`),
  KEY `N°rappeurs` (`N°rappeurs`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `concerts`
--

DROP TABLE IF EXISTS `concerts`;
CREATE TABLE IF NOT EXISTS `concerts` (
  `N°concerts` int NOT NULL AUTO_INCREMENT,
  `Chanteur` text NOT NULL,
  `Lieu` text NOT NULL,
  `Date` date NOT NULL,
  `Heure` time NOT NULL,
  `Durée` time NOT NULL,
  `Prix` int NOT NULL,
  PRIMARY KEY (`N°concerts`),
  KEY `N°concerts` (`N°concerts`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `groupes`
--

DROP TABLE IF EXISTS `groupes`;
CREATE TABLE IF NOT EXISTS `groupes` (
  `N°groupes` int NOT NULL AUTO_INCREMENT,
  `Nom du groupe` text NOT NULL,
  `Date de formation` date NOT NULL,
  `Date de 1er album` date NOT NULL,
  PRIMARY KEY (`N°groupes`),
  KEY `N°groupes` (`N°groupes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `musiques`
--

DROP TABLE IF EXISTS `musiques`;
CREATE TABLE IF NOT EXISTS `musiques` (
  `N°musiques` int NOT NULL AUTO_INCREMENT,
  `Nom` text NOT NULL,
  `Auteur` text NOT NULL,
  `Durée` time NOT NULL,
  `Date de sortie` date NOT NULL,
  `Genre` enum('Rap','Pop','Conscient') NOT NULL DEFAULT 'Rap',
  PRIMARY KEY (`N°musiques`),
  KEY `N°musiques` (`N°musiques`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `N°users` int NOT NULL AUTO_INCREMENT,
  `Nom` text NOT NULL,
  `Prénom` text NOT NULL,
  `Numéro tel` int NOT NULL,
  PRIMARY KEY (`N°users`),
  KEY `N°users` (`N°users`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `annonces`
--
ALTER TABLE `annonces`
  ADD CONSTRAINT `annonces_ibfk_1` FOREIGN KEY (`N°annonces`) REFERENCES `users` (`N°users`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `annonces_ibfk_2` FOREIGN KEY (`N°annonces`) REFERENCES `concerts` (`N°concerts`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Contraintes pour la table `chanteurs`
--
ALTER TABLE `chanteurs`
  ADD CONSTRAINT `chanteurs_ibfk_1` FOREIGN KEY (`N°rappeurs`) REFERENCES `groupes` (`N°groupes`) ON DELETE RESTRICT ON UPDATE RESTRICT;
  ADD CONSTRAINT `groupes_ibfk_1` FOREIGN KEY (`N°rappeurs`) REFERENCES `musiques` (`N°musiques`) ON DELETE RESTRICT ON UPDATE RESTRICT,
--
-- Contraintes pour la table `concerts`
--
ALTER TABLE `concerts`
  ADD CONSTRAINT `concerts_ibfk_1` FOREIGN KEY (`N°concerts`) REFERENCES `musiques` (`N°musiques`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `concerts_ibfk_2` FOREIGN KEY (`N°concerts`) REFERENCES `annonces` (`N°annonces`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Contraintes pour la table `groupes`
--
ALTER TABLE `groupes`
  ADD CONSTRAINT `groupes_ibfk_2` FOREIGN KEY (`N°groupes`) REFERENCES `chanteurs` (`N°rappeurs`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Contraintes pour la table `musiques`
--
ALTER TABLE `musiques`
  ADD CONSTRAINT `musiques_ibfk_1` FOREIGN KEY (`N°musiques`) REFERENCES `groupes` (`N°rappeurs`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `musiques_ibfk_2` FOREIGN KEY (`N°musiques`) REFERENCES `concerts` (`N°concerts`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Contraintes pour la table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`N°users`) REFERENCES `annonces` (`N°annonces`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
