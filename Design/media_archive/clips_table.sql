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
