CREATE TABLE `media_archive`.`clips` (
  `clips_uid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) NULL,
  `size_bytes` INT UNSIGNED NULL,
  `duration` VARCHAR(15) NULL,
  `aspect` VARCHAR(7) NULL,
  `size_screen` VARCHAR(10) NULL,
  `created_date` DATE NULL,
  `modified_date` DATE NULL,
  `tags` TEXT NULL CHECK (JSON_VALID(`tags`)),
  `thumbnail` VARCHAR(500) NULL,
  `proxy` VARCHAR(500) NULL,
  `o_pxy_id` VARCHAR(40) NULL,
  `o_asset_type` VARCHAR(12) NULL,
  `format_uid` VARCHAR(45) NULL,
  `a_owner_uid` INT UNSIGNED NULL,
  `a_groups` TEXT NULL CHECK (JSON_VALID(`a_groups`)),
  `a_users` TEXT NULL CHECK (JSON_VALID(`a_users`)),
  `h_main_origin_uid` INT UNSIGNED NULL,
  `h_origins` TEXT NULL CHECK (JSON_VALID(`h_origins`)),
  `license` VARCHAR(50) NULL,
  `restored_count` INT NULL,
  PRIMARY KEY (`clips_uid`),
  UNIQUE INDEX `uid_clips_UNIQUE` (`clips_uid` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Content the relation of all clips in diferent storages\no_ -> Origin data\na_ -> Access data\nh_ -> Hosting data\n\nlicense is the copyrights text';




CREATE TABLE `media_archive`.`hosts` (
  `hosts_uid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `ips` VARCHAR(150) NULL,
  `cpu` VARCHAR(45) NULL,
  `ram` VARCHAR(45) NULL,
  `storage_total` VARCHAR(45) NULL,
  `storage_used` VARCHAR(45) NULL,
  `storage_free` VARCHAR(45) NULL,
  `software_vendor` TEXT(1000) NULL,
  `sofware_home` VARCHAR(300) NULL,
  `os` VARCHAR(100) NULL,
  `floor` VARCHAR(45) NULL,
  `area` VARCHAR(45) NULL,
  `users` VARCHAR(100) NULL,
  `company` VARCHAR(45) NULL,
  `support_area` VARCHAR(45) NULL,
  `install_date` DATETIME NULL,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (`hosts_uid`))
COMMENT = 'Computadoras que tienen interacción con la media.';