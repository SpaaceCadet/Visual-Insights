
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



CREATE TABLE IF NOT EXISTS userss (
  `id` int(11) NOT NULL,
  `username` varchar(15) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `userss`
--

INSERT INTO `userss` (`id`, `username`, `email`, `password`) VALUES
(1, 'yahya', 'yahya@gmail.com', 'sgh'),
(2, 'sgh', 'sgh@yahya.com', 'sgh');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `userss`
--
ALTER TABLE `userss`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `userss`
--
ALTER TABLE `userss`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
