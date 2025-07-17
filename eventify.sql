-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 19, 2025 at 04:36 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eventify`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add organizer', 7, 'add_organizer'),
(26, 'Can change organizer', 7, 'change_organizer'),
(27, 'Can delete organizer', 7, 'delete_organizer'),
(28, 'Can view organizer', 7, 'view_organizer'),
(29, 'Can add user', 8, 'add_user'),
(30, 'Can change user', 8, 'change_user'),
(31, 'Can delete user', 8, 'delete_user'),
(32, 'Can view user', 8, 'view_user'),
(33, 'Can add event', 9, 'add_event'),
(34, 'Can change event', 9, 'change_event'),
(35, 'Can delete event', 9, 'delete_event'),
(36, 'Can view event', 9, 'view_event'),
(37, 'Can add event pics', 10, 'add_eventpics'),
(38, 'Can change event pics', 10, 'change_eventpics'),
(39, 'Can delete event pics', 10, 'delete_eventpics'),
(40, 'Can view event pics', 10, 'view_eventpics'),
(41, 'Can add event category', 11, 'add_eventcategory'),
(42, 'Can change event category', 11, 'change_eventcategory'),
(43, 'Can delete event category', 11, 'delete_eventcategory'),
(44, 'Can view event category', 11, 'view_eventcategory'),
(45, 'Can add event tickets', 12, 'add_eventtickets'),
(46, 'Can change event tickets', 12, 'change_eventtickets'),
(47, 'Can delete event tickets', 12, 'delete_eventtickets'),
(48, 'Can view event tickets', 12, 'view_eventtickets'),
(49, 'Can add customize event theme', 13, 'add_customizeeventtheme'),
(50, 'Can change customize event theme', 13, 'change_customizeeventtheme'),
(51, 'Can delete customize event theme', 13, 'delete_customizeeventtheme'),
(52, 'Can view customize event theme', 13, 'view_customizeeventtheme'),
(53, 'Can add customize event', 14, 'add_customizeevent'),
(54, 'Can change customize event', 14, 'change_customizeevent'),
(55, 'Can delete customize event', 14, 'delete_customizeevent'),
(56, 'Can view customize event', 14, 'view_customizeevent'),
(57, 'Can add event request', 15, 'add_eventrequest'),
(58, 'Can change event request', 15, 'change_eventrequest'),
(59, 'Can delete event request', 15, 'delete_eventrequest'),
(60, 'Can view event request', 15, 'view_eventrequest');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customize_events`
--

CREATE TABLE `customize_events` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `cover_image` varchar(100) NOT NULL,
  `organizer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customize_events`
--

INSERT INTO `customize_events` (`id`, `name`, `description`, `cover_image`, `organizer_id`) VALUES
(1, 'Birthday Bash', 'We also organize birthday party in every part of india.', 'organizer/customize_event_cover_images/birthday-party1.jpg', 2),
(2, 'Mandap Murat', 'We also organize mandap murat funtion in marriages.', 'organizer/customize_event_cover_images/mandap-murat-cover.jpg', 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(14, 'myapp', 'customizeevent'),
(13, 'myapp', 'customizeeventtheme'),
(9, 'myapp', 'event'),
(11, 'myapp', 'eventcategory'),
(10, 'myapp', 'eventpics'),
(15, 'myapp', 'eventrequest'),
(12, 'myapp', 'eventtickets'),
(7, 'myapp', 'organizer'),
(8, 'myapp', 'user'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-02-14 04:30:51.940030'),
(2, 'auth', '0001_initial', '2025-02-14 04:30:52.454153'),
(3, 'admin', '0001_initial', '2025-02-14 04:30:52.572241'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-02-14 04:30:52.582581'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-02-14 04:30:52.590036'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-02-14 04:30:52.674305'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-02-14 04:30:52.733733'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-02-14 04:30:52.753056'),
(9, 'auth', '0004_alter_user_username_opts', '2025-02-14 04:30:52.756184'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-02-14 04:30:52.795945'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-02-14 04:30:52.801038'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-02-14 04:30:52.803324'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-02-14 04:30:52.821487'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-02-14 04:30:52.835103'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-02-14 04:30:52.850099'),
(16, 'auth', '0011_update_proxy_permissions', '2025-02-14 04:30:52.854365'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-02-14 04:30:52.872035'),
(18, 'myapp', '0001_initial', '2025-02-14 04:30:52.979883'),
(19, 'sessions', '0001_initial', '2025-02-14 04:30:53.020136'),
(20, 'myapp', '0002_event_state', '2025-02-14 05:47:48.019796'),
(21, 'myapp', '0003_event_price', '2025-02-14 06:08:39.352634'),
(22, 'myapp', '0004_eventpics', '2025-02-14 06:26:54.419031'),
(23, 'myapp', '0005_event_cover_image', '2025-02-15 06:12:04.306723'),
(24, 'myapp', '0006_eventcategory_event_event_category', '2025-02-15 06:55:49.529624'),
(25, 'myapp', '0007_eventcategory_cat_image', '2025-02-16 04:10:56.580171'),
(26, 'myapp', '0008_eventcategory_cat_desc', '2025-02-16 04:18:38.429713'),
(27, 'myapp', '0009_eventtickets', '2025-02-16 10:50:43.377721'),
(28, 'myapp', '0010_event_total_tickets', '2025-02-16 11:09:07.888817'),
(29, 'myapp', '0011_alter_eventtickets_event_id', '2025-02-16 14:34:10.989815'),
(30, 'myapp', '0012_alter_eventtickets_event_id', '2025-02-16 14:38:01.973063'),
(31, 'myapp', '0013_customizeevent_customizeeventtheme', '2025-02-17 13:11:39.131840'),
(32, 'myapp', '0014_eventrequest', '2025-02-18 14:40:35.102951'),
(33, 'myapp', '0015_eventrequest_location_eventrequest_state', '2025-02-18 14:44:59.253961'),
(34, 'myapp', '0016_eventrequest_organizer', '2025-02-19 14:04:47.628647'),
(35, 'myapp', '0017_alter_eventrequest_organizer', '2025-02-19 14:04:48.658531');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('a5hr29xgciwo4ttvxggaxe7fin65014c', '.eJyrVsovSk_My6xKLYpPzU3MzFGyUipJLCrNSyotzsxLLS42dEgHCesl5-cq6SiVFiOpq0wszsjOSMwGEUUmpqZIKmsBtaEgPA:1tklMj:itF7r0tTd9-Cf1e_dnyO2gDzb4H5skedMwlHB1vgPQI', '2025-03-05 14:47:57.385435');

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

CREATE TABLE `event` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `location` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `organizer_id` int(11) NOT NULL,
  `state` varchar(40) NOT NULL,
  `price` varchar(6) NOT NULL,
  `cover_image` varchar(100) NOT NULL,
  `event_category_id` bigint(20) NOT NULL,
  `total_tickets` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `event`
--

INSERT INTO `event` (`id`, `name`, `date`, `time`, `location`, `description`, `organizer_id`, `state`, `price`, `cover_image`, `event_category_id`, `total_tickets`) VALUES
(5, 'New Year Bash', '2024-12-31', '20:00:00.000000', 'Seasons Hotel, Rajkot', 'Welcoming 2025 with Grand Celebration\r\nTiming: 8:00 pm to 12:00 am\r\nDinner: Included (unlimited)', 2, 'Gujarat', '500', 'organizer/event_cover_images/new-year-party_fZzPCut.jpg', 3, '1000'),
(8, 'Music Feat', '2025-02-27', '19:00:00.000000', 'Imperial Hotel, Rajkot', 'Artist: Diljit Dosanjh\r\nTiming: 7:00 pm to 9:00 pm', 2, 'Gujarat', '1000', 'organizer/event_cover_images/music-concert.jpg', 1, '40000'),
(9, 'Arijit Singh concert', '2025-02-02', '19:00:00.000000', 'Seasons Hotel, Rajkot', 'Artist: Arijit Singh\r\nTimings: 7:00 pm to 9:00 pma', 2, 'Gujarat', '1000', 'organizer/event_cover_images/arjit-singh.jpg', 1, '50000'),
(11, 'Tech Conference 2025', '2025-02-28', '09:00:00.000000', 'Imperial Hotel, Rajkot', 'Tech Conference 2025\r\nGlobal Top 100 companies to visit\r\nTimings: 9:00 am to 5:00 pm', 2, 'Gujarat', '100', 'organizer/event_cover_images/tech-conf_RwoOinZ.jpg', 2, '1000');

-- --------------------------------------------------------

--
-- Table structure for table `event_category`
--

CREATE TABLE `event_category` (
  `id` bigint(20) NOT NULL,
  `cat_name` varchar(255) NOT NULL,
  `cat_image` varchar(100) NOT NULL,
  `cat_desc` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `event_category`
--

INSERT INTO `event_category` (`id`, `cat_name`, `cat_image`, `cat_desc`) VALUES
(1, 'Music Concert', 'category_pics/music_concert.jpg', 'Join us for an unforgettable night of live music and entertainment.'),
(2, 'Tech Conference', 'category_pics/tech_conference.jpg', 'Explore the latest trends and innovations in technology.'),
(3, 'New Year Party', 'category_pics/new_year_party.jpg', 'Welcome the New Year with Grand Celebration.'),
(4, 'Business Seminar', 'category_pics/business_seminar.jpg', 'Network with industry leaders and gain insights at our business seminar.'),
(5, 'Charity Event', 'category_pics/charity_event.jpg', 'Make a difference by participating in our charity event.');

-- --------------------------------------------------------

--
-- Table structure for table `event_request`
--

CREATE TABLE `event_request` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `suggestions` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `theme_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `location` varchar(255) NOT NULL,
  `state` varchar(50) NOT NULL,
  `organizer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `event_request`
--

INSERT INTO `event_request` (`id`, `date`, `time`, `suggestions`, `status`, `theme_id`, `user_id`, `location`, `state`, `organizer_id`) VALUES
(5, '2025-02-28', '08:00:00.000000', 'I want exact theme as shown.', 'Accepted', 4, 1, 'Kings Party plot, Rajkot', 'Gujarat', 2);

-- --------------------------------------------------------

--
-- Table structure for table `event_tickets`
--

CREATE TABLE `event_tickets` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `no_of_tickets` varchar(1) NOT NULL,
  `total_amount` varchar(6) NOT NULL,
  `event_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `event_tickets`
--

INSERT INTO `event_tickets` (`id`, `date`, `time`, `no_of_tickets`, `total_amount`, `event_id_id`, `user_id_id`) VALUES
(1, '2025-02-16', '16:35:37.738135', '2', '2000', 8, 1),
(3, '2025-02-16', '20:24:34.546981', '1', '1000', 8, 1),
(4, '2025-02-16', '20:33:42.315047', '1', '1000', 8, 1),
(5, '2025-02-16', '20:35:04.071886', '1', '1000', 8, 1),
(6, '2025-02-16', '20:35:19.371526', '1', '1000', 8, 1),
(7, '2025-02-16', '20:39:19.520443', '1', '1000', 8, 1),
(8, '2025-02-17', '17:23:54.553216', '1', '100', 11, 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_customizeeventtheme`
--

CREATE TABLE `myapp_customizeeventtheme` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` varchar(10) NOT NULL,
  `customize_event_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_customizeeventtheme`
--

INSERT INTO `myapp_customizeeventtheme` (`id`, `image`, `price`, `customize_event_id`) VALUES
(1, 'organizer/event_theme/birthday-party1.jpg', '2000', 1),
(2, 'organizer/event_theme/birthday-party2.jpg', '3000', 1),
(3, 'organizer/event_theme/birthday-party3.jpg', '10000', 1),
(4, 'organizer/event_theme/mandap-theme-1.jpg', '20000', 2);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_eventpics`
--

CREATE TABLE `myapp_eventpics` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `event_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_eventpics`
--

INSERT INTO `myapp_eventpics` (`id`, `image`, `event_id`) VALUES
(7, 'organizer/event_images/new-year-party1_L9xcJeo.jpg', 5),
(9, 'organizer/event_images/new-year-party.jpg', 5);

-- --------------------------------------------------------

--
-- Table structure for table `organizer`
--

CREATE TABLE `organizer` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone_number` varchar(10) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_picture` varchar(100) NOT NULL,
  `company_logo` varchar(100) NOT NULL,
  `about_us` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `organizer`
--

INSERT INTO `organizer` (`id`, `name`, `company_name`, `email`, `phone_number`, `password`, `profile_picture`, `company_logo`, `about_us`) VALUES
(2, 'Tarun Sheth', 'TS Oragnizer', 'tarunbusiness1@gmail.com', '8080809090', 'tarun123', 'organizer/profile_pics/person.avif', 'organizer/company_logo/kd-weddings.jpg', 'Been in industry over last 10 years. Organized over 200+ weddings includeng functions like mandap, mehndi, dj nights, pool party, wedding day, reception and what not!');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_picture` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `password`, `profile_picture`) VALUES
(1, 'Yash Khakhar', 'yashkhakhkhar455@gmail.com', 'yash123', 'profile_pics/BlR10.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `customize_events`
--
ALTER TABLE `customize_events`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customize_events_organizer_id_fa272368_fk_organizer_id` (`organizer_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`id`),
  ADD KEY `event_organizer_id_95964402_fk_organizer_id` (`organizer_id`),
  ADD KEY `event_event_category_id_36d60f54_fk_event_category_id` (`event_category_id`);

--
-- Indexes for table `event_category`
--
ALTER TABLE `event_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `event_request`
--
ALTER TABLE `event_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `event_request_theme_id_91bbc548_fk_myapp_customizeeventtheme_id` (`theme_id`),
  ADD KEY `event_request_user_id_8d8e7d09_fk_user_id` (`user_id`),
  ADD KEY `event_request_organizer_id_d9db11d8_fk_organizer_id` (`organizer_id`);

--
-- Indexes for table `event_tickets`
--
ALTER TABLE `event_tickets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `event_tickets_user_id_id_3f284785_fk_user_id` (`user_id_id`),
  ADD KEY `event_tickets_event_id_id_79ddc4b1_fk_event_id` (`event_id_id`);

--
-- Indexes for table `myapp_customizeeventtheme`
--
ALTER TABLE `myapp_customizeeventtheme`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_customizeevent_customize_event_id_102232b1_fk_customize` (`customize_event_id`);

--
-- Indexes for table `myapp_eventpics`
--
ALTER TABLE `myapp_eventpics`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_eventpics_event_id_e00ba39b_fk_event_id` (`event_id`);

--
-- Indexes for table `organizer`
--
ALTER TABLE `organizer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customize_events`
--
ALTER TABLE `customize_events`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `event`
--
ALTER TABLE `event`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `event_category`
--
ALTER TABLE `event_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `event_request`
--
ALTER TABLE `event_request`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `event_tickets`
--
ALTER TABLE `event_tickets`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `myapp_customizeeventtheme`
--
ALTER TABLE `myapp_customizeeventtheme`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `myapp_eventpics`
--
ALTER TABLE `myapp_eventpics`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `organizer`
--
ALTER TABLE `organizer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `customize_events`
--
ALTER TABLE `customize_events`
  ADD CONSTRAINT `customize_events_organizer_id_fa272368_fk_organizer_id` FOREIGN KEY (`organizer_id`) REFERENCES `organizer` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `event`
--
ALTER TABLE `event`
  ADD CONSTRAINT `event_event_category_id_36d60f54_fk_event_category_id` FOREIGN KEY (`event_category_id`) REFERENCES `event_category` (`id`),
  ADD CONSTRAINT `event_organizer_id_95964402_fk_organizer_id` FOREIGN KEY (`organizer_id`) REFERENCES `organizer` (`id`);

--
-- Constraints for table `event_request`
--
ALTER TABLE `event_request`
  ADD CONSTRAINT `event_request_organizer_id_d9db11d8_fk_organizer_id` FOREIGN KEY (`organizer_id`) REFERENCES `organizer` (`id`),
  ADD CONSTRAINT `event_request_theme_id_91bbc548_fk_myapp_customizeeventtheme_id` FOREIGN KEY (`theme_id`) REFERENCES `myapp_customizeeventtheme` (`id`),
  ADD CONSTRAINT `event_request_user_id_8d8e7d09_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `event_tickets`
--
ALTER TABLE `event_tickets`
  ADD CONSTRAINT `event_tickets_event_id_id_79ddc4b1_fk_event_id` FOREIGN KEY (`event_id_id`) REFERENCES `event` (`id`),
  ADD CONSTRAINT `event_tickets_user_id_id_3f284785_fk_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `myapp_customizeeventtheme`
--
ALTER TABLE `myapp_customizeeventtheme`
  ADD CONSTRAINT `myapp_customizeevent_customize_event_id_102232b1_fk_customize` FOREIGN KEY (`customize_event_id`) REFERENCES `customize_events` (`id`);

--
-- Constraints for table `myapp_eventpics`
--
ALTER TABLE `myapp_eventpics`
  ADD CONSTRAINT `myapp_eventpics_event_id_e00ba39b_fk_event_id` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
