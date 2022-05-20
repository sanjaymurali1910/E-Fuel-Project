-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 12, 2022 at 03:04 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `efueldb`
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
(25, 'Can add bunk', 7, 'add_bunk'),
(26, 'Can change bunk', 7, 'change_bunk'),
(27, 'Can delete bunk', 7, 'delete_bunk'),
(28, 'Can view bunk', 7, 'view_bunk'),
(29, 'Can add category', 8, 'add_category'),
(30, 'Can change category', 8, 'change_category'),
(31, 'Can delete category', 8, 'delete_category'),
(32, 'Can view category', 8, 'view_category'),
(33, 'Can add product', 9, 'add_product'),
(34, 'Can change product', 9, 'change_product'),
(35, 'Can delete product', 9, 'delete_product'),
(36, 'Can view product', 9, 'view_product'),
(37, 'Can add bunk_booked', 10, 'add_bunk_booked'),
(38, 'Can change bunk_booked', 10, 'change_bunk_booked'),
(39, 'Can delete bunk_booked', 10, 'delete_bunk_booked'),
(40, 'Can view bunk_booked', 10, 'view_bunk_booked'),
(41, 'Can add user_registration', 11, 'add_user_registration'),
(42, 'Can change user_registration', 11, 'change_user_registration'),
(43, 'Can delete user_registration', 11, 'delete_user_registration'),
(44, 'Can view user_registration', 11, 'view_user_registration'),
(45, 'Can add payment', 12, 'add_payment'),
(46, 'Can change payment', 12, 'change_payment'),
(47, 'Can delete payment', 12, 'delete_payment'),
(48, 'Can view payment', 12, 'view_payment'),
(49, 'Can add admin_contact', 13, 'add_admin_contact'),
(50, 'Can change admin_contact', 13, 'change_admin_contact'),
(51, 'Can delete admin_contact', 13, 'delete_admin_contact'),
(52, 'Can view admin_contact', 13, 'view_admin_contact'),
(53, 'Can add owner_contact', 14, 'add_owner_contact'),
(54, 'Can change owner_contact', 14, 'change_owner_contact'),
(55, 'Can delete owner_contact', 14, 'delete_owner_contact'),
(56, 'Can view owner_contact', 14, 'view_owner_contact'),
(57, 'Can add order', 15, 'add_order'),
(58, 'Can change order', 15, 'change_order'),
(59, 'Can delete order', 15, 'delete_order'),
(60, 'Can view order', 15, 'view_order'),
(61, 'Can add shipping address', 16, 'add_shippingaddress'),
(62, 'Can change shipping address', 16, 'change_shippingaddress'),
(63, 'Can delete shipping address', 16, 'delete_shippingaddress'),
(64, 'Can view shipping address', 16, 'view_shippingaddress'),
(65, 'Can add order item', 17, 'add_orderitem'),
(66, 'Can change order item', 17, 'change_orderitem'),
(67, 'Can delete order item', 17, 'delete_orderitem'),
(68, 'Can view order item', 17, 'view_orderitem');

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

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$6yCPayrrKKmRVlege0b2kB$IBptcinr4wLCcerqKMmrjMeBg8NRmf0ZfJgick1T47I=', NULL, 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2022-05-12 12:54:32.811385');

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
(13, 'efuelapp', 'admin_contact'),
(7, 'efuelapp', 'bunk'),
(10, 'efuelapp', 'bunk_booked'),
(8, 'efuelapp', 'category'),
(15, 'efuelapp', 'order'),
(17, 'efuelapp', 'orderitem'),
(14, 'efuelapp', 'owner_contact'),
(12, 'efuelapp', 'payment'),
(9, 'efuelapp', 'product'),
(16, 'efuelapp', 'shippingaddress'),
(11, 'efuelapp', 'user_registration'),
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
(1, 'contenttypes', '0001_initial', '2022-05-12 12:52:01.669912'),
(2, 'auth', '0001_initial', '2022-05-12 12:52:02.252834'),
(3, 'admin', '0001_initial', '2022-05-12 12:52:02.392730'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-05-12 12:52:02.400011'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-12 12:52:02.410722'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-05-12 12:52:02.493578'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-05-12 12:52:02.562482'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-05-12 12:52:02.590390'),
(9, 'auth', '0004_alter_user_username_opts', '2022-05-12 12:52:02.602321'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-05-12 12:52:02.657114'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-05-12 12:52:02.661905'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-05-12 12:52:02.676142'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-05-12 12:52:02.711864'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-05-12 12:52:02.739590'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-05-12 12:52:02.767134'),
(16, 'auth', '0011_update_proxy_permissions', '2022-05-12 12:52:02.780705'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-05-12 12:52:02.805509'),
(18, 'efuelapp', '0001_initial', '2022-05-12 12:52:02.845268'),
(19, 'efuelapp', '0002_category_product', '2022-05-12 12:52:02.960765'),
(20, 'efuelapp', '0003_auto_20220427_1257', '2022-05-12 12:52:03.061975'),
(21, 'efuelapp', '0004_user_registration', '2022-05-12 12:52:03.097540'),
(22, 'efuelapp', '0005_alter_user_registration_status', '2022-05-12 12:52:03.106516'),
(23, 'efuelapp', '0006_auto_20220428_1703', '2022-05-12 12:52:03.309902'),
(24, 'efuelapp', '0007_bunk_booked_bunkowner_ide', '2022-05-12 12:52:03.346172'),
(25, 'efuelapp', '0008_alter_bunk_booked_bunkowner_ide', '2022-05-12 12:52:03.355250'),
(26, 'efuelapp', '0009_alter_bunk_booked_bunkowner_ide', '2022-05-12 12:52:03.362527'),
(27, 'efuelapp', '0010_alter_bunk_booked_bunkowner_ide', '2022-05-12 12:52:03.421189'),
(28, 'efuelapp', '0011_alter_bunk_booked_bunkowner_ide', '2022-05-12 12:52:03.429167'),
(29, 'efuelapp', '0012_alter_bunk_owner_ide', '2022-05-12 12:52:03.494027'),
(30, 'efuelapp', '0013_payment', '2022-05-12 12:52:03.530813'),
(31, 'efuelapp', '0014_alter_user_registration_status', '2022-05-12 12:52:03.539784'),
(32, 'efuelapp', '0015_admin_contact_owner_contact', '2022-05-12 12:52:03.601495'),
(33, 'efuelapp', '0016_order_orderitem_shippingaddress', '2022-05-12 12:52:03.968387'),
(34, 'efuelapp', '0017_auto_20220506_0055', '2022-05-12 12:52:04.046143'),
(35, 'sessions', '0001_initial', '2022-05-12 12:52:04.089835');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_admin_contact`
--

CREATE TABLE `efuelapp_admin_contact` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(240) DEFAULT NULL,
  `subject` varchar(100) NOT NULL,
  `message` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_bunk`
--

CREATE TABLE `efuelapp_bunk` (
  `id` bigint(20) NOT NULL,
  `owner_ide` varchar(240) DEFAULT NULL,
  `bunk_name` varchar(100) NOT NULL,
  `vehicle_type` varchar(100) NOT NULL,
  `connector` varchar(100) NOT NULL,
  `email` varchar(240) DEFAULT NULL,
  `phone` varchar(240) DEFAULT NULL,
  `address` varchar(225) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `pincode` varchar(240) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `efuelapp_bunk`
--

INSERT INTO `efuelapp_bunk` (`id`, `owner_ide`, `bunk_name`, `vehicle_type`, `connector`, `email`, `phone`, `address`, `city`, `state`, `country`, `pincode`, `image`) VALUES
(1, '1', 'kochin bunk', 'car,bike,', 'Type 3A,Type 3C,TeslaR,', 'kochin@gmail.com', '9856545654', 'kochin address', 'kochi', 'kerala', 'india', '678765', 'images/ebunk1_jdTMmxw.jpg'),
(2, '1', 'kollam bunk', 'bike,auto,', 'CHAdMO,CCS 1,CCS 2,', 'kollam@gmail.com', '9809090987', 'kollam address', 'kollam', 'kerala', 'india', '678764', 'images/ebunk2_7HCGjbR.jpg'),
(3, '1', 'thiruvalla bunk', 'car,bike,auto,', 'Type 3C,CCS 1,CCS 2,EU-Schuko,', 'thiruvalla@gmail.com', '9876123456', 'thiruvalla address', 'thiruvalla', 'kerala', 'india', '678765', 'images/ebunk3_4a21n76.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_bunk_booked`
--

CREATE TABLE `efuelapp_bunk_booked` (
  `id` bigint(20) NOT NULL,
  `user_ide` int(11) DEFAULT NULL,
  `name` varchar(240) DEFAULT NULL,
  `email` varchar(240) DEFAULT NULL,
  `phone` varchar(240) DEFAULT NULL,
  `uservehicle_type` varchar(100) NOT NULL,
  `userconnector` varchar(100) NOT NULL,
  `date` date DEFAULT NULL,
  `time` time(6) DEFAULT NULL,
  `status` varchar(240) DEFAULT NULL,
  `Bunk_id` bigint(20) DEFAULT NULL,
  `bunkowner_ide` varchar(240) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_category`
--

CREATE TABLE `efuelapp_category` (
  `id` bigint(20) NOT NULL,
  `category_name` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_order`
--

CREATE TABLE `efuelapp_order` (
  `id` bigint(20) NOT NULL,
  `date_ordered` datetime(6) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `transaction_id` varchar(100) DEFAULT NULL,
  `customer_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_orderitem`
--

CREATE TABLE `efuelapp_orderitem` (
  `id` bigint(20) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  `order_id` bigint(20) DEFAULT NULL,
  `product_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_owner_contact`
--

CREATE TABLE `efuelapp_owner_contact` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(240) DEFAULT NULL,
  `subject` varchar(100) NOT NULL,
  `message` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_payment`
--

CREATE TABLE `efuelapp_payment` (
  `id` bigint(20) NOT NULL,
  `user_ide` varchar(240) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `payment` varchar(240) DEFAULT NULL,
  `bank` varchar(240) DEFAULT NULL,
  `accountnumber` varchar(240) DEFAULT NULL,
  `ifse` varchar(240) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_product`
--

CREATE TABLE `efuelapp_product` (
  `id` bigint(20) NOT NULL,
  `product_name` varchar(40) NOT NULL,
  `product_image` varchar(100) DEFAULT NULL,
  `price` int(10) UNSIGNED NOT NULL CHECK (`price` >= 0),
  `description` varchar(40) NOT NULL,
  `category_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_shippingaddress`
--

CREATE TABLE `efuelapp_shippingaddress` (
  `id` bigint(20) NOT NULL,
  `address` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `state` varchar(200) NOT NULL,
  `zipcode` varchar(200) NOT NULL,
  `date_added` datetime(6) NOT NULL,
  `customer_id` bigint(20) DEFAULT NULL,
  `order_id` bigint(20) DEFAULT NULL,
  `email` varchar(240) DEFAULT NULL,
  `items` varchar(240) DEFAULT NULL,
  `name` varchar(240) DEFAULT NULL,
  `price` varchar(240) DEFAULT NULL,
  `user_ide` varchar(240) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `efuelapp_user_registration`
--

CREATE TABLE `efuelapp_user_registration` (
  `id` bigint(20) NOT NULL,
  `fullname` varchar(240) DEFAULT NULL,
  `pincode` varchar(240) DEFAULT NULL,
  `district` varchar(240) DEFAULT NULL,
  `state` varchar(240) DEFAULT NULL,
  `country` varchar(240) DEFAULT NULL,
  `mobile` varchar(240) DEFAULT NULL,
  `email` varchar(240) DEFAULT NULL,
  `password` varchar(240) DEFAULT NULL,
  `status` varchar(240) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `efuelapp_user_registration`
--

INSERT INTO `efuelapp_user_registration` (`id`, `fullname`, `pincode`, `district`, `state`, `country`, `mobile`, `email`, `password`, `status`) VALUES
(1, 'test', '678765', 'kottayam', 'kerala', 'india', '9876456543', 'test@gmail.com', 'testpassword', 'owner'),
(2, 'testuser', '654345', 'kollam', 'kerala', 'india', '9876776765', 'user@gmail.com', 'testpassword', 'user');

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
-- Indexes for table `efuelapp_admin_contact`
--
ALTER TABLE `efuelapp_admin_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `efuelapp_bunk`
--
ALTER TABLE `efuelapp_bunk`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `efuelapp_bunk_booked`
--
ALTER TABLE `efuelapp_bunk_booked`
  ADD PRIMARY KEY (`id`),
  ADD KEY `efuelapp_bunk_booked_Bunk_id_a4ae73f2_fk_efuelapp_bunk_id` (`Bunk_id`);

--
-- Indexes for table `efuelapp_category`
--
ALTER TABLE `efuelapp_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `efuelapp_order`
--
ALTER TABLE `efuelapp_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `efuelapp_order_customer_id_5fbd0bf5_fk_efuelapp_` (`customer_id`);

--
-- Indexes for table `efuelapp_orderitem`
--
ALTER TABLE `efuelapp_orderitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `efuelapp_orderitem_order_id_4c99c57f_fk_efuelapp_order_id` (`order_id`),
  ADD KEY `efuelapp_orderitem_product_id_400eeaea_fk_efuelapp_product_id` (`product_id`);

--
-- Indexes for table `efuelapp_owner_contact`
--
ALTER TABLE `efuelapp_owner_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `efuelapp_payment`
--
ALTER TABLE `efuelapp_payment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `efuelapp_product`
--
ALTER TABLE `efuelapp_product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `efuelapp_product_category_id_a601121b_fk_efuelapp_category_id` (`category_id`);

--
-- Indexes for table `efuelapp_shippingaddress`
--
ALTER TABLE `efuelapp_shippingaddress`
  ADD PRIMARY KEY (`id`),
  ADD KEY `efuelapp_shippingadd_customer_id_1402f121_fk_efuelapp_` (`customer_id`),
  ADD KEY `efuelapp_shippingaddress_order_id_9daf7ec3_fk_efuelapp_order_id` (`order_id`);

--
-- Indexes for table `efuelapp_user_registration`
--
ALTER TABLE `efuelapp_user_registration`
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `efuelapp_admin_contact`
--
ALTER TABLE `efuelapp_admin_contact`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `efuelapp_bunk`
--
ALTER TABLE `efuelapp_bunk`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `efuelapp_bunk_booked`
--
ALTER TABLE `efuelapp_bunk_booked`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `efuelapp_category`
--
ALTER TABLE `efuelapp_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `efuelapp_order`
--
ALTER TABLE `efuelapp_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `efuelapp_orderitem`
--
ALTER TABLE `efuelapp_orderitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `efuelapp_owner_contact`
--
ALTER TABLE `efuelapp_owner_contact`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `efuelapp_payment`
--
ALTER TABLE `efuelapp_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `efuelapp_product`
--
ALTER TABLE `efuelapp_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `efuelapp_shippingaddress`
--
ALTER TABLE `efuelapp_shippingaddress`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `efuelapp_user_registration`
--
ALTER TABLE `efuelapp_user_registration`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `efuelapp_bunk_booked`
--
ALTER TABLE `efuelapp_bunk_booked`
  ADD CONSTRAINT `efuelapp_bunk_booked_Bunk_id_a4ae73f2_fk_efuelapp_bunk_id` FOREIGN KEY (`Bunk_id`) REFERENCES `efuelapp_bunk` (`id`);

--
-- Constraints for table `efuelapp_order`
--
ALTER TABLE `efuelapp_order`
  ADD CONSTRAINT `efuelapp_order_customer_id_5fbd0bf5_fk_efuelapp_` FOREIGN KEY (`customer_id`) REFERENCES `efuelapp_user_registration` (`id`);

--
-- Constraints for table `efuelapp_orderitem`
--
ALTER TABLE `efuelapp_orderitem`
  ADD CONSTRAINT `efuelapp_orderitem_order_id_4c99c57f_fk_efuelapp_order_id` FOREIGN KEY (`order_id`) REFERENCES `efuelapp_order` (`id`),
  ADD CONSTRAINT `efuelapp_orderitem_product_id_400eeaea_fk_efuelapp_product_id` FOREIGN KEY (`product_id`) REFERENCES `efuelapp_product` (`id`);

--
-- Constraints for table `efuelapp_product`
--
ALTER TABLE `efuelapp_product`
  ADD CONSTRAINT `efuelapp_product_category_id_a601121b_fk_efuelapp_category_id` FOREIGN KEY (`category_id`) REFERENCES `efuelapp_category` (`id`);

--
-- Constraints for table `efuelapp_shippingaddress`
--
ALTER TABLE `efuelapp_shippingaddress`
  ADD CONSTRAINT `efuelapp_shippingadd_customer_id_1402f121_fk_efuelapp_` FOREIGN KEY (`customer_id`) REFERENCES `efuelapp_user_registration` (`id`),
  ADD CONSTRAINT `efuelapp_shippingaddress_order_id_9daf7ec3_fk_efuelapp_order_id` FOREIGN KEY (`order_id`) REFERENCES `efuelapp_order` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
