-- phpMyAdmin SQL Dump
-- version 4.0.10deb1ubuntu0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 10, 2025 at 09:43 PM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `moviewatchlist`
--

-- --------------------------------------------------------

--
-- Table structure for table `DIRECTOR`
--

CREATE TABLE IF NOT EXISTS `DIRECTOR` (
  `Director_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Birthdate` date DEFAULT NULL,
  `Nationality` varchar(100) NOT NULL,
  `Movie_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Director_id`),
  UNIQUE KEY `Director_id` (`Director_id`),
  KEY `Movie_id` (`Movie_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=36 ;

--
-- Dumping data for table `DIRECTOR`
--

INSERT INTO `DIRECTOR` (`Director_id`, `Name`, `Birthdate`, `Nationality`, `Movie_id`) VALUES
(1, 'Christopher Nolan', '1970-07-30', 'British', 1),
(2, 'Quentin Tarantino', '1963-03-27', 'American', 2),
(3, 'Steven Spielberg', '1946-12-18', 'American', 3),
(4, 'Martin Scorsese', '1942-11-17', 'American', 4),
(5, 'Ridley Scott', '1937-11-30', 'British', 5),
(6, 'James Cameron', '1954-08-16', 'Canadian', 6),
(7, 'J.J. Abrams', '1966-06-27', 'American', 7),
(8, 'George Lucas', '1944-05-14', 'American', 8),
(9, 'Peter Jackson', '1961-10-31', 'New Zealand', 9),
(10, 'Tim Burton', '1958-08-25', 'American', 10),
(11, 'Andrew Stanton', '1965-12-03', 'American', 11),
(12, 'David Fincher', '1962-08-28', 'American', 12),
(13, 'Clint Eastwood', '1930-05-31', 'American', 13),
(14, 'Alfonso Cuarón', '1961-11-28', 'Mexican', 14),
(15, 'Robert Zemeckis', '1952-05-14', 'American', 15),
(16, 'John Carpenter', '1948-01-16', 'American', 16),
(17, 'Francis Ford Coppola', '1939-04-07', 'American', 17),
(18, 'Woody Allen', '1935-12-01', 'American', 18),
(19, 'Spike Lee', '1957-03-20', 'American', 19),
(20, 'Wes Anderson', '1969-05-01', 'American', 20),
(21, 'Danny Boyle', '1956-10-20', 'British', 21),
(22, 'Oliver Stone', '1946-09-15', 'American', 22),
(23, 'Ridley Scott', '1937-11-30', 'British', 23),
(24, 'Bong Joon-ho', '1969-09-14', 'South Korean', 24),
(25, 'Sam Mendes', '1965-08-01', 'British', 25),
(26, 'Kathryn Bigelow', '1951-11-27', 'American', 26),
(27, 'Guillermo del Toro', '1964-10-09', 'Mexican', 27),
(28, 'Zack Snyder', '1966-03-01', 'American', 28),
(29, 'James Wan', '1977-02-15', 'Australian', 29),
(30, 'Steven Soderbergh', '1963-01-14', 'American', 30);

-- --------------------------------------------------------

--
-- Table structure for table `GENRE`
--

CREATE TABLE IF NOT EXISTS `GENRE` (
  `Genre_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Movie_id` int(11) NOT NULL,
  PRIMARY KEY (`Genre_id`),
  UNIQUE KEY `Genre_id` (`Genre_id`),
  KEY `Movie_id` (`Movie_id`),
  KEY `Genre_id_2` (`Genre_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=36 ;

--
-- Dumping data for table `GENRE`
--

INSERT INTO `GENRE` (`Genre_id`, `Name`, `Movie_id`) VALUES
(1, 'Sci-Fi', 1),
(2, 'Action', 2),
(3, 'Sci-Fi', 3),
(4, 'Fantasy', 4),
(5, 'Drama', 5),
(6, 'Sci-Fi', 6),
(7, 'Adventure', 7),
(8, 'Crime', 8),
(9, 'Fantasy', 9),
(10, 'Crime', 10),
(11, 'Action', 11),
(12, 'Animation', 12),
(13, 'Action', 13),
(14, 'Drama', 14),
(15, 'Drama', 15),
(16, 'Sci-Fi', 16),
(17, 'Thriller', 17),
(18, 'Sci-Fi', 18),
(19, 'Action', 19),
(20, 'Sci-Fi', 20),
(21, 'Crime', 21),
(22, 'Drama', 22),
(23, 'Drama', 23),
(24, 'Horror', 24),
(25, 'Crime', 25),
(26, 'Sci-Fi', 26),
(27, 'Adventure', 27),
(28, 'Action', 28),
(29, 'Western', 29),
(30, 'Biography', 30);

-- --------------------------------------------------------

--
-- Table structure for table `MOVIE`
--

CREATE TABLE IF NOT EXISTS `MOVIE` (
  `Movie_id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(100) NOT NULL,
  `Run_time` int(11) NOT NULL,
  `Release_year` int(11) NOT NULL,
  `Genre_id` int(11) DEFAULT NULL,
  `Director_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Movie_id`),
  UNIQUE KEY `Movie_id` (`Movie_id`),
  KEY `Genre_id` (`Genre_id`),
  KEY `Director_id` (`Director_id`),
  KEY `Genre_id_2` (`Genre_id`),
  KEY `Director_id_2` (`Director_id`),
  KEY `Director_id_3` (`Director_id`),
  KEY `Genre_id_3` (`Genre_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=35 ;

--
-- Dumping data for table `MOVIE`
--

INSERT INTO `MOVIE` (`Movie_id`, `Title`, `Run_time`, `Release_year`, `Genre_id`, `Director_id`) VALUES
(1, 'Inception', 148, 2010, 1, 1),
(2, 'Pulp Fiction', 154, 1994, 2, 2),
(3, 'Jurassic Park', 127, 1993, 3, 3),
(4, 'The Irishman', 209, 2019, 4, 4),
(5, 'Gladiator', 155, 2000, 5, 5),
(6, 'Avatar', 162, 2009, 6, 6),
(7, 'Star Wars: The Force Awakens', 138, 2015, 7, 7),
(8, 'Star Wars: A New Hope', 121, 1977, 8, 8),
(9, 'The Lord of the Rings: The Fellowship of the Ring', 178, 2001, 9, 9),
(10, 'Beetlejuice', 92, 1988, 10, 10),
(11, 'Finding Nemo', 100, 2003, 11, 11),
(12, 'Se7en', 127, 1995, 12, 12),
(13, 'American Sniper', 132, 2014, 13, 13),
(14, 'Gravity', 91, 2013, 14, 14),
(15, 'Forrest Gump', 142, 1994, 15, 15),
(16, 'The Shining', 146, 1980, 16, 16),
(17, 'The Godfather', 175, 1972, 17, 17),
(18, 'Manhattan', 96, 1979, 18, 18),
(19, 'Do the Right Thing', 120, 1989, 19, 19),
(20, 'The Grand Budapest Hotel', 99, 2014, 20, 20),
(21, 'Trainspotting', 94, 1996, 21, 21),
(22, 'Platoon', 120, 1986, 22, 22),
(23, 'Gladiator', 155, 2000, 23, 23),
(24, 'Parasite', 132, 2019, 24, 24),
(25, 'Skyfall', 143, 2012, 25, 25),
(26, 'The Hurt Locker', 131, 2008, 26, 26),
(27, 'Pans Labyrinth', 118, 2006, 27, 27),
(28, '300', 117, 2006, 28, 28),
(29, 'The Conjuring', 112, 2013, 29, 29),
(30, 'Oceans Eleven', 116, 2001, 30, 30),
(34, 'sasa', 2313, 113, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `PLATFORM`
--

CREATE TABLE IF NOT EXISTS `PLATFORM` (
  `Platform_id` int(11) NOT NULL AUTO_INCREMENT,
  `Platform_name` varchar(255) NOT NULL,
  `Subscription_fee` decimal(10,2) NOT NULL,
  `Movie_id` int(11) NOT NULL,
  PRIMARY KEY (`Platform_id`),
  UNIQUE KEY `Platform_id` (`Platform_id`),
  KEY `fk_movie_id_platform` (`Movie_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=36 ;

--
-- Dumping data for table `PLATFORM`
--

INSERT INTO `PLATFORM` (`Platform_id`, `Platform_name`, `Subscription_fee`, `Movie_id`) VALUES
(1, 'Netflix', 10.99, 1),
(2, 'Amazon Prime', 7.99, 2),
(3, 'Disney+', 6.99, 3),
(4, 'Hulu', 4.99, 4),
(5, 'HBO Max', 3.99, 5),
(6, 'Apple TV+', 8.99, 6),
(7, 'Disney+', 6.99, 7),
(8, 'Hulu', 4.99, 8),
(9, 'Amazon Prime', 7.99, 9),
(10, 'YouTube', 0.00, 10),
(11, 'HBO Max', 5.99, 11),
(12, 'Apple TV+', 8.99, 12),
(13, 'Netflix', 10.99, 13),
(14, 'Disney+', 6.99, 14),
(15, 'HBO Max', 3.99, 15),
(16, 'Hulu', 4.99, 16),
(17, 'Amazon Prime', 7.99, 17),
(18, 'Apple TV+', 5.99, 18),
(19, 'Netflix', 10.99, 19),
(20, 'Youtube', 0.00, 20),
(21, 'Youtube', 0.00, 21),
(22, 'Amazon Prime', 7.99, 22),
(23, 'Hulu', 4.99, 23),
(24, 'Netflix', 10.99, 24),
(25, 'Mubi', 13.99, 25),
(26, 'Mubi', 13.99, 26),
(27, 'Mubi', 13.99, 27),
(28, 'Netflix', 10.99, 28),
(29, 'Amazon Prime', 7.99, 29),
(30, 'Netflix', 10.99, 30);

-- --------------------------------------------------------

--
-- Table structure for table `REVİEW`
--

CREATE TABLE IF NOT EXISTS `REVİEW` (
  `Review_id` int(11) NOT NULL AUTO_INCREMENT,
  `Review_date` date NOT NULL,
  `Rating` decimal(5,0) NOT NULL,
  `Comment` text NOT NULL,
  `Movie_id` int(11) NOT NULL,
  `User_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Review_id`),
  UNIQUE KEY `Review_id` (`Review_id`),
  KEY `Movie_id` (`Movie_id`),
  KEY `User_id` (`User_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=34 ;

--
-- Dumping data for table `REVİEW`
--

INSERT INTO `REVİEW` (`Review_id`, `Review_date`, `Rating`, `Comment`, `Movie_id`, `User_id`) VALUES
(1, '2024-01-01', 5, 'Amazing movie with mind-bending concepts!', 1, 1),
(2, '2024-01-02', 4, 'A masterpiece in storytelling and cinematography.', 2, 2),
(3, '2024-01-03', 3, 'Fun, but not as good as expected.', 3, 3),
(4, '2024-01-04', 5, 'Great film, long but worth it!', 4, 4),
(5, '2024-01-05', 4, 'A classic with an epic story.', 5, 5),
(6, '2024-01-06', 5, 'Incredible visuals and great world-building.', 6, 6),
(7, '2024-01-07', 2, 'Pacing could improve.', 7, 7),
(8, '2024-01-08', 1, 'It was boring.', 8, 8),
(9, '2024-01-09', 5, 'The best adaptation of Tolkien’s work!', 9, 9),
(10, '2024-01-10', 1, 'Dark and weird.', 10, 10),
(11, '2024-01-11', 5, 'A heartwarming and beautiful story.', 11, 11),
(12, '2024-01-12', 4, 'Intense and gripping, but disturbing at times.', 12, 12),
(13, '2024-01-13', 5, 'One of the best war movies ever made.', 13, 13),
(14, '2024-01-14', 5, 'Incredible cinematography and plot!', 14, 14),
(15, '2024-01-15', 3, 'A timeless classic, however not my cup of tea.', 15, 15),
(16, '2024-01-16', 4, 'Terrifying and atmospheric.', 16, 16),
(17, '2024-01-17', 5, 'An unforgettable experience!', 17, 17),
(18, '2024-01-18', 5, 'An emotional and brilliant film.', 18, 18),
(19, '2024-01-19', 3, 'A must-watch, but a little slow-paced.', 19, 19),
(20, '2024-01-20', 5, 'Unique and visually stunning.', 20, 20),
(21, '2024-01-21', 4, 'A powerful story with great performances.', 21, 21),
(22, '2024-01-22', 3, 'A brilliant war film, but a bit too long.', 22, 22),
(23, '2024-01-23', 2, 'One of the greatest waste of time of all time.', 23, 23),
(24, '2024-01-24', 5, 'A fantastic masterpiece, very emotional.', 24, 24),
(25, '2024-01-25', 5, 'A thrilling and intense movie.', 25, 25),
(26, '2024-01-26', 2, 'Great action but the plot is predictable.', 26, 26),
(27, '2024-01-27', 5, 'Brilliantly directed, a film to be remembered.', 27, 27),
(28, '2024-01-28', 4, 'A strong and intense action movie.', 28, 28),
(29, '2024-01-29', 4, 'The best horror movie in years.', 29, 29),
(30, '2024-01-30', 4, 'An entertaining and fun movie to watch.', 30, 30);

-- --------------------------------------------------------

--
-- Table structure for table `USER`
--

CREATE TABLE IF NOT EXISTS `USER` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Email` varchar(255) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Review_id` int(11) NOT NULL,
  `Movie_id` int(11) NOT NULL,
  PRIMARY KEY (`User_id`),
  UNIQUE KEY `User_id` (`User_id`),
  KEY `User_id_2` (`User_id`),
  KEY `User_id_3` (`User_id`),
  KEY `Review_id` (`Review_id`),
  KEY `Movie_id` (`Movie_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=35 ;

--
-- Dumping data for table `USER`
--

INSERT INTO `USER` (`User_id`, `Email`, `Username`, `Password`, `Review_id`, `Movie_id`) VALUES
(1, 'Martha97@hotmail.com', 'a', 'a', 1, 1),
(2, 'Glenn62@gmail.com', 'Glenn', 'a2451c4', 2, 2),
(3, 'Lillian.Homenick@gmail.com', 'Lillian', '27f260eb', 3, 3),
(4, 'Timmy.Kutch@hotmail.com', 'Timmy', '778cac7c', 4, 4),
(5, 'Lee_Robel93@hotmail.com', 'Lee', '-53c2ba15', 5, 5),
(6, 'Wilma.DAmore@gmail.com', 'Wilma', '65ade560', 6, 6),
(7, 'Ignacio.Fay11@yahoo.com', 'Ignacio', '-6908708a', 7, 7),
(8, 'Verna.Hills75@gmail.com', 'Verna', 'c1aba31', 8, 8),
(9, 'Jan_Anderson92@hotmail.com', 'Jan', '-1e89d95a', 9, 9),
(10, 'Abel.Koch9@gmail.com', 'Abel', '-3d483ff0', 10, 10),
(11, 'Gregg48@gmail.com', 'Gregg', '78d6fa56', 11, 11),
(12, 'Kay99@yahoo.com', 'Kay', '-6be500cb', 12, 12),
(13, 'Angelo.Hudson89@gmail.com', 'Angelo', 'c177e80', 13, 13),
(14, 'Frankie.Weissnat16@yahoo.com', 'Frankie', '-48d606a2', 14, 14),
(15, 'Jenny_Will54@hotmail.com', 'Jenny', '3aded860', 15, 15),
(16, 'Vicki66@yahoo.com', 'Vicki', '44a9b286', 16, 16),
(17, 'Rita86@yahoo.com', 'Rita', '-eb020c4', 17, 17),
(18, 'Angie.Willms@hotmail.com', 'Angie', '-269a2791', 18, 18),
(19, 'Yvonne.Bayer@yahoo.com', 'Yvonne', '6e6b599', 19, 19),
(20, 'Gertrude.Welch38@hotmail.com', 'Gertrude', '63ba99d0', 20, 20),
(21, 'Alton_Heathcote@yahoo.com', 'Alton', '-6b23db4b', 21, 21),
(22, 'Tammy.Wiegand55@yahoo.com', 'Tammy', '-15c1cb32', 22, 22),
(23, 'Bobbie.Von93@gmail.com', 'Bobbie', '1f1ae89b', 23, 23),
(24, 'Claude.Wehner61@hotmail.com', 'Claude', '3005b343', 24, 24),
(25, 'Rickey87@gmail.com', 'Rickey', '-3b071af2', 25, 25),
(26, 'Donna_Dickinson@yahoo.com', 'Donna', '-22c29b9a', 26, 26),
(27, 'Doris_McDermott6@hotmail.com', 'Doris', '-44956879', 27, 27),
(28, 'Garrett35@gmail.com', 'Garrett', '17b42b58', 28, 28),
(29, 'Mike66@hotmail.com', 'Mike', '-6fd5147c', 29, 29),
(30, 'Pablo52@hotmail.com', 'Pablo', '6907e784', 30, 30),
(34, 'b', 'b', 'b', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `WATCHLIST`
--

CREATE TABLE IF NOT EXISTS `WATCHLIST` (
  `Date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Watchlist_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `User_id` int(11) NOT NULL,
  PRIMARY KEY (`Watchlist_id`),
  UNIQUE KEY `Watchlist_id` (`Watchlist_id`),
  KEY `User_id` (`User_id`),
  KEY `User_id_2` (`User_id`),
  KEY `User_id_3` (`User_id`),
  KEY `User_id_4` (`User_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=35 ;

--
-- Dumping data for table `WATCHLIST`
--

INSERT INTO `WATCHLIST` (`Date_created`, `Watchlist_id`, `Name`, `User_id`) VALUES
('2023-12-31 21:00:00', 1, 'Movies to Watch with Family', 1),
('2024-01-01 21:00:00', 2, 'Favorite Movies', 2),
('2024-01-02 21:00:00', 3, 'Top Picks', 3),
('2024-01-03 21:00:00', 4, 'Weekend Watchlist', 4),
('2024-01-04 21:00:00', 5, 'Movie Night Collection', 5),
('2024-01-05 21:00:00', 6, 'Must-Watch Movies', 6),
('2024-01-06 21:00:00', 7, 'Best of the Best', 7),
('2024-01-07 21:00:00', 8, 'Classic Favorites', 8),
('2024-01-08 21:00:00', 9, 'Thriller Picks', 9),
('2024-01-09 21:00:00', 10, 'Comedy Night', 10),
('2024-01-10 21:00:00', 11, 'Drama Collection', 11),
('2024-01-11 21:00:00', 12, 'Family Favorites', 12),
('2024-01-12 21:00:00', 13, 'Sci-Fi Essentials', 13),
('2024-01-13 21:00:00', 14, 'Action Hits', 14),
('2024-01-14 21:00:00', 15, 'Romantic Movies', 15),
('2024-01-15 21:00:00', 16, 'Fantasy Adventures', 16),
('2024-01-16 21:00:00', 17, 'Horror Nights', 17),
('2024-01-17 21:00:00', 18, 'Animation Picks', 18),
('2024-01-18 21:00:00', 19, 'Award Winners', 19),
('2024-01-19 21:00:00', 20, 'Feel-Good Movies', 20),
('2024-01-20 21:00:00', 21, 'Crime Thrillers', 21),
('2024-01-21 21:00:00', 22, 'Cult Classics', 22),
('2024-01-22 21:00:00', 23, 'International Films', 23),
('2024-01-23 21:00:00', 24, 'Epic Stories', 24),
('2024-01-24 21:00:00', 25, 'Underrated Gems', 25),
('2024-01-25 21:00:00', 26, 'Holiday Movies', 26),
('2024-01-26 21:00:00', 27, 'Critic''s Choice', 27),
('2024-01-27 21:00:00', 28, 'Blockbusters', 28),
('2024-01-28 21:00:00', 29, 'Documentary Picks', 29),
('2024-01-29 21:00:00', 30, 'Indie Favorites', 30);

-- --------------------------------------------------------

--
-- Table structure for table `WATCHLIST_MOVIE`
--

CREATE TABLE IF NOT EXISTS `WATCHLIST_MOVIE` (
  `Watchlist_id` int(11) NOT NULL,
  `Movie_id` int(11) NOT NULL,
  PRIMARY KEY (`Watchlist_id`,`Movie_id`),
  KEY `fk_movie_id` (`Movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `WATCHLIST_MOVIE`
--

INSERT INTO `WATCHLIST_MOVIE` (`Watchlist_id`, `Movie_id`) VALUES
(1, 1),
(8, 4),
(9, 4),
(1, 5),
(8, 5),
(8, 6),
(9, 8),
(8, 9);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `GENRE`
--
ALTER TABLE `GENRE`
  ADD CONSTRAINT `addmovieid` FOREIGN KEY (`Movie_id`) REFERENCES `MOVIE` (`Movie_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `MOVIE`
--
ALTER TABLE `MOVIE`
  ADD CONSTRAINT `fk_genre_id` FOREIGN KEY (`Genre_id`) REFERENCES `GENRE` (`Genre_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_director_id` FOREIGN KEY (`Director_id`) REFERENCES `DIRECTOR` (`Director_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `PLATFORM`
--
ALTER TABLE `PLATFORM`
  ADD CONSTRAINT `fk_movie_id_platform` FOREIGN KEY (`Movie_id`) REFERENCES `MOVIE` (`Movie_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `REVİEW`
--
ALTER TABLE `REVİEW`
  ADD CONSTRAINT `fk_movie_id_review` FOREIGN KEY (`Movie_id`) REFERENCES `MOVIE` (`Movie_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_user_id_review` FOREIGN KEY (`User_id`) REFERENCES `USER` (`User_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `WATCHLIST`
--
ALTER TABLE `WATCHLIST`
  ADD CONSTRAINT `fk_user_id` FOREIGN KEY (`User_id`) REFERENCES `USER` (`User_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `WATCHLIST_MOVIE`
--
ALTER TABLE `WATCHLIST_MOVIE`
  ADD CONSTRAINT `fk_movie_id` FOREIGN KEY (`Movie_id`) REFERENCES `MOVIE` (`Movie_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_watchlist_id` FOREIGN KEY (`Watchlist_id`) REFERENCES `WATCHLIST` (`Watchlist_id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
