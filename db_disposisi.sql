-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 08 Nov 2019 pada 07.47
-- Versi Server: 5.7.27-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_disposisi`
--
CREATE DATABASE IF NOT EXISTS `db_disposisi` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `db_disposisi`;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `auth_permission`
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
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add jenis dokumen', 6, 'add_jenisdokumen'),
(22, 'Can change jenis dokumen', 6, 'change_jenisdokumen'),
(23, 'Can delete jenis dokumen', 6, 'delete_jenisdokumen'),
(24, 'Can view jenis dokumen', 6, 'view_jenisdokumen'),
(25, 'Can add klasifikasi', 7, 'add_klasifikasi'),
(26, 'Can change klasifikasi', 7, 'change_klasifikasi'),
(27, 'Can delete klasifikasi', 7, 'delete_klasifikasi'),
(28, 'Can view klasifikasi', 7, 'view_klasifikasi'),
(29, 'Can add fungsi', 8, 'add_fungsi'),
(30, 'Can change fungsi', 8, 'change_fungsi'),
(31, 'Can delete fungsi', 8, 'delete_fungsi'),
(32, 'Can view fungsi', 8, 'view_fungsi'),
(33, 'Can add dokumen', 9, 'add_dokumen'),
(34, 'Can change dokumen', 9, 'change_dokumen'),
(35, 'Can delete dokumen', 9, 'delete_dokumen'),
(36, 'Can view dokumen', 9, 'view_dokumen'),
(37, 'Can add user', 10, 'add_user'),
(38, 'Can change user', 10, 'change_user'),
(39, 'Can delete user', 10, 'delete_user'),
(40, 'Can view user', 10, 'view_user');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(10, 'accounts', 'user'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(9, 'dokumen', 'dokumen'),
(8, 'dokumen', 'fungsi'),
(6, 'dokumen', 'jenisdokumen'),
(7, 'dokumen', 'klasifikasi'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'accounts', '0001_initial', '2019-11-07 11:28:24.274423'),
(2, 'accounts', '0002_auto_20191031_0252', '2019-11-07 11:28:25.554004'),
(3, 'accounts', '0003_remove_user_staff', '2019-11-07 11:28:25.662648'),
(4, 'accounts', '0004_user_staff', '2019-11-07 11:28:25.783391'),
(5, 'accounts', '0005_auto_20191031_0810', '2019-11-07 11:28:26.010350'),
(6, 'accounts', '0006_remove_user_user_menerima_disposisi', '2019-11-07 11:28:26.102789'),
(7, 'accounts', '0007_auto_20191031_0815', '2019-11-07 11:28:26.140981'),
(8, 'accounts', '0008_auto_20191031_0816', '2019-11-07 11:28:26.173850'),
(9, 'accounts', '0009_remove_user_user_status', '2019-11-07 11:28:26.290151'),
(10, 'accounts', '0010_user_fungsi_kode', '2019-11-07 11:28:26.405223'),
(11, 'accounts', '0011_remove_user_fungsi_kode', '2019-11-07 11:28:26.519678'),
(12, 'contenttypes', '0001_initial', '2019-11-07 11:28:26.626431'),
(13, 'admin', '0001_initial', '2019-11-07 11:28:26.699494'),
(14, 'admin', '0002_logentry_remove_auto_add', '2019-11-07 11:28:26.996196'),
(15, 'admin', '0003_logentry_add_action_flag_choices', '2019-11-07 11:28:27.003415'),
(16, 'contenttypes', '0002_remove_content_type_name', '2019-11-07 11:28:27.201689'),
(17, 'auth', '0001_initial', '2019-11-07 11:28:27.386756'),
(18, 'auth', '0002_alter_permission_name_max_length', '2019-11-07 11:28:27.935007'),
(19, 'auth', '0003_alter_user_email_max_length', '2019-11-07 11:28:27.947670'),
(20, 'auth', '0004_alter_user_username_opts', '2019-11-07 11:28:27.957179'),
(21, 'auth', '0005_alter_user_last_login_null', '2019-11-07 11:28:27.966326'),
(22, 'auth', '0006_require_contenttypes_0002', '2019-11-07 11:28:27.969011'),
(23, 'auth', '0007_alter_validators_add_error_messages', '2019-11-07 11:28:27.977329'),
(24, 'auth', '0008_alter_user_username_max_length', '2019-11-07 11:28:27.986672'),
(25, 'auth', '0009_alter_user_last_name_max_length', '2019-11-07 11:28:27.996118'),
(26, 'auth', '0010_alter_group_name_max_length', '2019-11-07 11:28:28.008175'),
(27, 'auth', '0011_update_proxy_permissions', '2019-11-07 11:28:28.026955'),
(28, 'dokumen', '0001_initial', '2019-11-07 11:28:28.255289'),
(29, 'dokumen', '0002_auto_20191105_1457', '2019-11-07 11:28:29.223441'),
(30, 'sessions', '0001_initial', '2019-11-07 11:28:29.277337');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('cfgpmngncyyxr9zhkow4ycjvv0f4yw3k', 'OGJlNTVhMzc3ZDEyNmM3Yjg2NzBhODQyZTczNjhhNmFlZmYwMzI5MTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwM2FiMTMyNzkwNjMxZDE5Y2NjYjVjOTE5MDM2YTU5OTE0MGFhNWJmIiwiRlVMTE5BTUUiOiJhZG1pbiIsIlVTRVJOQU1FIjoiYWRtaW4iLCJJRF9VU0VSIjoxLCJGT1RPIjoiIn0=', '2019-11-21 11:47:40.510334'),
('vlu12csxw42lykka1j75upu4b06zvohj', 'OGJlNTVhMzc3ZDEyNmM3Yjg2NzBhODQyZTczNjhhNmFlZmYwMzI5MTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwM2FiMTMyNzkwNjMxZDE5Y2NjYjVjOTE5MDM2YTU5OTE0MGFhNWJmIiwiRlVMTE5BTUUiOiJhZG1pbiIsIlVTRVJOQU1FIjoiYWRtaW4iLCJJRF9VU0VSIjoxLCJGT1RPIjoiIn0=', '2019-11-21 11:32:22.313831');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_dokumen`
--

DROP TABLE IF EXISTS `tbl_dokumen`;
CREATE TABLE `tbl_dokumen` (
  `id` int(11) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `nomor_surat_lengkap` varchar(255) DEFAULT NULL,
  `nomor_surat` int(11) NOT NULL,
  `tanggal` date NOT NULL,
  `pejabat_penandatangan` varchar(255) NOT NULL,
  `perihal` longtext,
  `file_dokumen` varchar(100) NOT NULL,
  `fungsi_id` int(11) NOT NULL,
  `jenis_dokumen_id` int(11) NOT NULL,
  `klasifikasi_id` int(11) NOT NULL,
  `tujuan_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `tbl_dokumen`
--

INSERT INTO `tbl_dokumen` (`id`, `slug`, `nomor_surat_lengkap`, `nomor_surat`, `tanggal`, `pejabat_penandatangan`, `perihal`, `file_dokumen`, `fungsi_id`, `jenis_dokumen_id`, `klasifikasi_id`, `tujuan_id`, `user_id`) VALUES
(1, 'd1kp11201903', 'D.1/KP/11/2019/03', 1, '2019-11-07', 'xxx', 'xxxx', 'document/2019-11-07/undangan_rapat_HUT_TNI_KAMIS_3_OKT.pdf', 23, 1, 2, 22, 1),
(2, 'd1ma11201905', 'D.1/MA/11/2019/05', 1, '2019-11-07', 'Agus Badrul Jamal', 'Nota Diplomatik kemlu malaysia', 'document/2019-11-07/undangan_rapat_HUT_TNI_KAMIS_3_OKT_DDM5L50.pdf', 25, 1, 12, 22, 1),
(3, 'nd1lm11201910', 'ND.1/LM/11/2019/10', 1, '2019-11-15', 'Dubes', 'dasda', 'document/2019-11-07/NOTA-DL-002-20191031-8158fc0d052d16703cd11c0a04bcbc52.pdf', 30, 4, 5, 40, 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_fungsi`
--

DROP TABLE IF EXISTS `tbl_fungsi`;
CREATE TABLE `tbl_fungsi` (
  `id` int(11) NOT NULL,
  `kode` varchar(10) NOT NULL,
  `fungsi` varchar(100) NOT NULL,
  `koordinator_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `tbl_fungsi`
--

INSERT INTO `tbl_fungsi` (`id`, `kode`, `fungsi`, `koordinator_id`) VALUES
(21, '01', 'Duta Besar', 1),
(22, '02', 'Wakil Kepala Perwakilan', 1),
(23, '03', 'Kepala Kanselerai', 1),
(24, '04', 'Fungsi Konsuler', 1),
(25, '05', 'Fungsi Politik', 1),
(26, '06', 'Fungsi Ekonomi', 1),
(27, '07', 'Fungsi Pensosbud', 1),
(28, '08', 'Fungsi Protokol', 1),
(29, '09', 'Atase Pertahanan', 1),
(30, '10', 'Atase Imigrasi', 1),
(31, '11', 'Atase Perdagangan', 1),
(32, '12', 'Atase Perhubungan', 1),
(33, '13', 'Atase Tenaga Kerja', 1),
(34, '14', 'Atase Pendidikan', 1),
(35, '15', 'Atase Polisi', 1),
(36, '16', 'Atase Hukum', 1),
(37, '17', 'Atase Riset', 1),
(38, '18', 'Komunikasi', 1),
(39, '19', 'Bendaharawan', 1),
(40, '20', 'BPKRT', 1),
(41, '21', 'PALAKHARKAM', 1),
(42, '22', 'Manajer Kinerja Perwakilan', 1),
(43, '23', 'POKJA Pengadaan Jasa/Barang', 1),
(44, '24', 'Arsiparis', 1),
(45, '25', 'Kepala SIKL', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_jenis_dokumen`
--

DROP TABLE IF EXISTS `tbl_jenis_dokumen`;
CREATE TABLE `tbl_jenis_dokumen` (
  `id` int(11) NOT NULL,
  `kode` varchar(10) NOT NULL,
  `jenis_dokumen` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `tbl_jenis_dokumen`
--

INSERT INTO `tbl_jenis_dokumen` (`id`, `kode`, `jenis_dokumen`) VALUES
(1, 'D', 'Nota Diplomatik'),
(2, 'SP', 'Surat Perintah '),
(3, 'SPK', 'Surat Perintah Kerja'),
(4, 'ND', 'Nota Dinas'),
(5, 'SD', 'Surat Dinas');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_klasifikasi`
--

DROP TABLE IF EXISTS `tbl_klasifikasi`;
CREATE TABLE `tbl_klasifikasi` (
  `id` int(11) NOT NULL,
  `kode` varchar(5) NOT NULL,
  `nama_klasifikasi` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `tbl_klasifikasi`
--

INSERT INTO `tbl_klasifikasi` (`id`, `kode`, `nama_klasifikasi`) VALUES
(1, 'DL', 'Pendidikan dan Pelatihan'),
(2, 'KP', 'Kepegawaian'),
(3, 'KU', 'Keuangan'),
(4, 'LA', 'Layanan Administrasi KEMENLU & Perwakilan'),
(5, 'LM', 'Layanan Administrasi Menteri'),
(6, 'PL', 'Perlengkapan'),
(7, 'PW', 'Pengawasan'),
(8, 'RO', 'Perencanaan dan Organisasi'),
(9, 'JB', 'Pengkajian dan Pengembangan'),
(10, 'BK', 'Hubungan Bilateral dan Intra Kawasan'),
(11, 'KA', 'Kerjasama ASEAN'),
(12, 'MA', 'Mitrawicara dan Antar Kawasan'),
(13, 'TI', 'Penanganan Isu Internasional'),
(14, 'PK', 'Protokol dan Konsuler'),
(15, 'FD', 'Fasilitas Diplomatik'),
(16, 'WN', 'Perlindungan WNI dan BHI'),
(17, 'HI', 'Layanan Hukum dan Perjanjian Internasional'),
(18, 'KM', 'Pengelolaan Komunikasi'),
(19, 'DM', 'Kebijakan Diplomasi Publik, Informasi dan Media'),
(20, 'AD', 'Keamanan Diplomatik');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_user`
--

DROP TABLE IF EXISTS `tbl_user`;
CREATE TABLE `tbl_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_foto` varchar(255) NOT NULL,
  `user_nama_lengkap` varchar(255) NOT NULL,
  `user_notifikasi_email` varchar(2) NOT NULL,
  `staff` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `tbl_user`
--

INSERT INTO `tbl_user` (`id`, `password`, `last_login`, `email`, `user_name`, `admin`, `timestamp`, `user_foto`, `user_nama_lengkap`, `user_notifikasi_email`, `staff`) VALUES
(1, 'pbkdf2_sha256$150000$DGWZP5cv7tDn$YgjCkLXrNIecZT5EJvfRw8GZDduD/gsKtNi3dj5sreA=', '2019-11-07 11:47:40.506778', 'admin_enodin@kbrikl.org', 'admin', 1, '2019-11-07 11:30:04.918339', '', 'admin', '', 1);

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
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_tbl_user_id` (`user_id`);

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
-- Indexes for table `tbl_dokumen`
--
ALTER TABLE `tbl_dokumen`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `tbl_dokumen_fungsi_id_2844b6b2_fk_tbl_fungsi_id` (`fungsi_id`),
  ADD KEY `tbl_dokumen_jenis_dokumen_id_60a6d7f6_fk_tbl_jenis_dokumen_id` (`jenis_dokumen_id`),
  ADD KEY `tbl_dokumen_klasifikasi_id_e0f8c128_fk_tbl_klasifikasi_id` (`klasifikasi_id`),
  ADD KEY `tbl_dokumen_tujuan_id_5894ee39_fk_tbl_fungsi_id` (`tujuan_id`),
  ADD KEY `tbl_dokumen_user_id_502d6cf9_fk_tbl_user_id` (`user_id`);

--
-- Indexes for table `tbl_fungsi`
--
ALTER TABLE `tbl_fungsi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tbl_fungsi_koordinator_id_7ffbd6ab_fk_tbl_user_id` (`koordinator_id`);

--
-- Indexes for table `tbl_jenis_dokumen`
--
ALTER TABLE `tbl_jenis_dokumen`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_klasifikasi`
--
ALTER TABLE `tbl_klasifikasi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_user`
--
ALTER TABLE `tbl_user`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `tbl_dokumen`
--
ALTER TABLE `tbl_dokumen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `tbl_fungsi`
--
ALTER TABLE `tbl_fungsi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
--
-- AUTO_INCREMENT for table `tbl_jenis_dokumen`
--
ALTER TABLE `tbl_jenis_dokumen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `tbl_klasifikasi`
--
ALTER TABLE `tbl_klasifikasi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `tbl_user`
--
ALTER TABLE `tbl_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ketidakleluasaan untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `tbl_dokumen`
--
ALTER TABLE `tbl_dokumen`
  ADD CONSTRAINT `tbl_dokumen_fungsi_id_2844b6b2_fk_tbl_fungsi_id` FOREIGN KEY (`fungsi_id`) REFERENCES `tbl_fungsi` (`id`),
  ADD CONSTRAINT `tbl_dokumen_jenis_dokumen_id_60a6d7f6_fk_tbl_jenis_dokumen_id` FOREIGN KEY (`jenis_dokumen_id`) REFERENCES `tbl_jenis_dokumen` (`id`),
  ADD CONSTRAINT `tbl_dokumen_klasifikasi_id_e0f8c128_fk_tbl_klasifikasi_id` FOREIGN KEY (`klasifikasi_id`) REFERENCES `tbl_klasifikasi` (`id`),
  ADD CONSTRAINT `tbl_dokumen_tujuan_id_5894ee39_fk_tbl_fungsi_id` FOREIGN KEY (`tujuan_id`) REFERENCES `tbl_fungsi` (`id`),
  ADD CONSTRAINT `tbl_dokumen_user_id_502d6cf9_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `tbl_fungsi`
--
ALTER TABLE `tbl_fungsi`
  ADD CONSTRAINT `tbl_fungsi_koordinator_id_7ffbd6ab_fk_tbl_user_id` FOREIGN KEY (`koordinator_id`) REFERENCES `tbl_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
