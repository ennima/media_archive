/**
 * Model for Clips schema
 *
 * Developed by Enrique Nieto Martínez
 * 2019-03-07 22:10:25
 */

const db = require('../db');

/**
 * Get a number of total clips
 * @returns {Promise} Promise with data or error
 */
function count() {
  return db.runQuery('SELECT COUNT(*) as total_clips FROM media_archive.clips;', []);
}


/**
 * Find a Clip by ID
 * @param {String} clip_uid Clips uid
 * @returns {Promise} Promise with data or error
 */
function find(clip_uid) {
  return db.runQuery(`SELECT * FROM media_archive.clips
      WHERE media_archive.clips.clip_uid = ?;`, [clip_uid]);
}

/**
 * Find a Clip by Key:val
 * @param {String} key Clip property.
 * @param {string} val Value of property.
 * @returns {Promise} Promise with data or error
 */
function findKey(key, val) {
  return db.runQuery(`SELECT * FROM media_archive.clips
      WHERE media_archive.clips.${key} LIKE '%${val}%';`);
}

/**
 * Find a Clip by Key:val
 * @param {String} key Clip property.
 * @param {string} val Value of property.
 * @returns {Promise} Promise with data or error
 */
function findKeyStrict(key, val) {
  return db.runQuery(`SELECT * FROM media_archive.clips
      WHERE media_archive.clips.${key} LIKE ?;`, [val]);
}


/**
 * Insert Clip
 * @param {String} clip_uid Clips uid
 * @param {String} name Name
 * @param {String} size_bytes Size bytes
 * @param {String} duration Duration
 * @param {String} aspect Aspect
 * @param {String} size_screen Size screen
 * @param {String} created_date Created date
 * @param {String} modified_date Modified date
 * @param {String} tags Tags
 * @param {String} thumbnail Thumbnail
 * @param {String} proxy Proxy
 * @param {String} o_pxy_id O pxy id
 * @param {String} o_asset_type O asset type
 * @param {String} format_uid Format uid
 * @param {String} a_owner_uid A owner uid
 * @param {String} a_groups A groups
 * @param {String} a_users A users
 * @param {String} h_main_origin_uid H main origin uid
 * @param {String} h_origins H origins
 * @param {String} license License
 * @param {String} restored_count Restored count
 * @returns {Promise} Promise with data or error
 */
function insert(clip) {
  return db.runQuery(`INSERT INTO media_archive.clips
        (name, size_bytes, duration, aspect, size_screen, created_date, modified_date, tags, thumbnail, proxy, o_pxy_id, o_asset_type, format_uid, a_owner_uid, a_groups, a_users, h_main_origin_uid, h_origins, license, restored_count)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);`, [
          clip.name,
          clip.size_bytes,
          clip.duration,
          clip.aspect,
          clip.size_screen,
          clip.created_date,
          clip.modified_date,
          clip.tags,
          clip.thumbnail,
          clip.proxy,
          clip.o_pxy_id,
          clip.o_asset_type,
          clip.format_uid,
          clip.a_owner_uid,
          clip.a_groups,
          clip.a_users,
          clip.h_main_origin_uid,
          clip.h_origins,
          clip.license,
          clip.restored_count
          ]
         );
}


/**
 * Get a list of clips
 * @returns {Promise} Promise with data or error
 */
function list() {
  return db.runQuery('SELECT * FROM media_archive.clips;', []);
}


/**
 * Delete Clip by Clip ID
 * @param {String} clip_uid Clip ID
 * @returns {Promise} Promise with data or error
 */
function remove(clip_uid) {
  return db.runQuery(`DELETE FROM media_archive.clips
  WHERE media_archive.clips.clip_uid = ?;`, [clip_uid]);
}


/**
 * Update Clip
 * @param {String} clip_uid Clips uid
 * @param {String} name Name
 * @param {String} size_bytes Size bytes
 * @param {String} duration Duration
 * @param {String} aspect Aspect
 * @param {String} size_screen Size screen
 * @param {String} created_date Created date
 * @param {String} modified_date Modified date
 * @param {String} tags Tags
 * @param {String} thumbnail Thumbnail
 * @param {String} proxy Proxy
 * @param {String} o_pxy_id O pxy id
 * @param {String} o_asset_type O asset type
 * @param {String} format_uid Format uid
 * @param {String} a_owner_uid A owner uid
 * @param {String} a_groups A groups
 * @param {String} a_users A users
 * @param {String} h_main_origin_uid H main origin uid
 * @param {String} h_origins H origins
 * @param {String} license License
 * @param {String} restored_count Restored count
 * @returns {Promise} Promise with data or error
 */
function update(clip_uid, name, size_bytes, duration, aspect, size_screen, created_date, modified_date, tags, thumbnail, proxy, o_pxy_id, o_asset_type, format_uid, a_owner_uid, a_groups, a_users, h_main_origin_uid, h_origins, license, restored_count) {
  return db.runQuery(`UPDATE media_archive.clips
    SET clip_uid = ?, name = ?, size_bytes = ?, duration = ?, aspect = ?, size_screen = ?, created_date = ?, modified_date = ?, tags = ?, thumbnail = ?, proxy = ?, o_pxy_id = ?, o_asset_type = ?, format_uid = ?, a_owner_uid = ?, a_groups = ?, a_users = ?, h_main_origin_uid = ?, h_origins = ?, license = ?, restored_count = ?
    WHERE media_archive.clips.clip_uid = ?;`, [
    clip_uid, name, size_bytes, duration, aspect, size_screen, created_date, modified_date, tags, thumbnail, proxy, o_pxy_id, o_asset_type, format_uid, a_owner_uid, a_groups, a_users, h_main_origin_uid, h_origins, license, restored_count,clip_uid ]);
}


/**
 * Update Clip only one column value
 * @param {String} clip_uid Clip ID
 * @param {String} col_name Name of property
 * @param {String} val New value for property
 * @returns {Promise} Promise with data or error
 */
function updateCol(clip_uid, col_name, val) {
  return db.runQuery(`UPDATE media_archive.clips
    SET ${col_name} = ?
    WHERE media_archive.clips.clip_uid = ?;`, [
    val,
    clip_uid
    ]);
}


module.exports = {
    count,
    find,
    findKey,
    findKeyStrict,
    insert,
    list,
    remove,
    update,
    updateCol
};
