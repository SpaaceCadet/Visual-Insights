
CREATE DATABASE users;

USE users;

CREATE TABLE IF NOT EXISTS userss (
  `id` int(11) NOT NULL,
  `username` varchar(15) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `userss` (`id`, `username`, `email`, `password`) VALUES
(1, 'yahya', 'yahya@gmail.com', 'sgh'),
(2, 'sgh', 'sgh@yahya.com', 'sgh');

ALTER TABLE `userss`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

ALTER TABLE `userss`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;
GRANT ALL ON users.* TO 'yahya'@'%';

/* Make sure the privileges are installed */
FLUSH PRIVILEGES;
