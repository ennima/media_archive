/**
 * Model for Origins schema
 *
 * Developed by Enrique Nieto Martínez
 * 2019-03-07 23:09:23
 */

const db = require('../db');

/**
 * Get a number of total origins
 * @returns {Promise} Promise with data or error
 */
function count() {
  return db.runQuery('SELECT COUNT(*) as total_origins FROM media_archive.origins;', []);
}


/**
 * Find a Origin by ID
 * @param {String} origin_uid Origin uid
 * @returns {Promise} Promise with data or error
 */
function find(origin_uid) {
  return db.runQuery(`SELECT * FROM media_archive.origins
      WHERE media_archive.origins.origin_uid = ?;`, [origin_uid]);
}


/**
 * Insert Origin
 * @param {String} origin_uid Origin uid
 * @param {String} name Name
 * @param {String} description Description
 * @param {String} ftp Ftp
 * @param {String} ftp_user Ftp user
 * @param {String} ftp_pass Ftp pass
 * @param {String} ftp_host Ftp host
 * @param {String} cif Cif
 * @param {String} cif_user Cif user
 * @param {String} cif_pass Cif pass
 * @param {String} cif_host Cif host
 * @param {String} site_uid Site uid
 * @param {String} capacity_bytes Capacity bytes
 * @param {String} capacity_used Capacity used
 * @param {String} capacity_free Capacity free
 * @param {String} status Status
 * @returns {Promise} Promise with data or error
 */
function insert(name, description, ftp, ftp_user, ftp_pass, ftp_host, cif, cif_user, cif_pass, cif_host, site_uid, capacity_bytes, capacity_used, capacity_free, status) {
  return db.runQuery(`INSERT INTO media_archive.origins
        (name, description, ftp, ftp_user, ftp_pass, ftp_host, cif, cif_user, cif_pass, cif_host, site_uid, capacity_bytes, capacity_used, capacity_free, status)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);`, [
        name,
        description,
        ftp,
        ftp_user,
        ftp_pass,
        ftp_host,
        cif,
        cif_user,
        cif_pass,
        cif_host,
        site_uid,
        capacity_bytes,
        capacity_used,
        capacity_free,
        status
      ]);
}


/**
 * Get a list of origins
 * @returns {Promise} Promise with data or error
 */
function list() {
  return db.runQuery('SELECT * FROM media_archive.origins;', []);
}


/**
 * Delete Origin by Origin ID
 * @param {String} origin_uid Origin ID
 * @returns {Promise} Promise with data or error
 */
function remove(origin_uid) {
  return db.runQuery(`DELETE FROM media_archive.origins
  WHERE media_archive.origins.origin_uid = ?;`, [origin_uid]);
}


/**
 * Update Origin
 * @param {String} origin_uid Origin uid
 * @param {String} name Name
 * @param {String} description Description
 * @param {String} ftp Ftp
 * @param {String} ftp_user Ftp user
 * @param {String} ftp_pass Ftp pass
 * @param {String} ftp_host Ftp host
 * @param {String} cif Cif
 * @param {String} cif_user Cif user
 * @param {String} cif_pass Cif pass
 * @param {String} cif_host Cif host
 * @param {String} site_uid Site uid
 * @param {String} capacity_bytes Capacity bytes
 * @param {String} capacity_used Capacity used
 * @param {String} capacity_free Capacity free
 * @param {String} status Status
 * @returns {Promise} Promise with data or error
 */
function update(origin_uid, name, description, ftp, ftp_user, ftp_pass, ftp_host, cif, cif_user, cif_pass, cif_host, site_uid, capacity_bytes, capacity_used, capacity_free, status) {
  return db.runQuery(`UPDATE media_archive.origins
    SET origin_uid = ?, name = ?, description = ?, ftp = ?, ftp_user = ?, ftp_pass = ?, ftp_host = ?, cif = ?, cif_user = ?, cif_pass = ?, cif_host = ?, site_uid = ?, capacity_bytes = ?, capacity_used = ?, capacity_free = ?, status = ?
    WHERE media_archive.origins.origin_uid = ?;`, [
      origin_uid,
      name,
      description,
      ftp,
      ftp_user,
      ftp_pass,
      ftp_host,
      cif,
      cif_user,
      cif_pass,
      cif_host,
      site_uid,
      capacity_bytes,
      capacity_used,
      capacity_free,
      status,
      origin_uid
    ]);
}


/**
 * Update Origin only one column value
 * @param {String} origin_uid Origin ID
 * @param {String} col_name Name of property
 * @param {String} val New value for property
 * @returns {Promise} Promise with data or error
 */
function updateCol(origin_uid, col_name, val) {
  return db.runQuery(`UPDATE media_archive.origins
    SET ${col_name} = ?
    WHERE media_archive.origins.origin_uid = ?;`, [
      val,
      origin_uid
    ]);
}


module.exports = {
    count,
    find,
    insert,
    list,
    remove,
    update,
    updateCol
};
