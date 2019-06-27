/**
 * Model for Relations schema 
 * 
 * Developed by Enrique Nieto Martínez
 * 2019-06-26 21:28:12
 */

const db = require('./db');

/**
 * Get a number of total relations
 * @returns {Promise} Promise with data or error
 */
function count() {
  return db.runQuery('SELECT COUNT(*) as total_relations FROM media_archive.relations;', []);
}
 
 
/**
 * Find a Relation by ID
 * @param {String} relation_uid Relation uid
 * @returns {Promise} Promise with data or error
 */
function find( relation_uid ) {
  return db.runQuery(`SELECT * FROM media_archive.relations
      WHERE media_archive.relations.relation_uid = ?;`, [relation_uid]);
}
 
 
/**
 * Insert Relation
 * @param {Object} Relation Clip object whit data.
 * @returns {Promise} Promise with data or error
 */
function insert(relation) {
  return db.runQuery(`INSERT INTO media_archive.relations
        (relation_uid, clip_uid, action, date, user_uid, host_uid, app_uid, description)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?);`, [
        relation.relation_uid
, relation.clip_uid
, relation.action
, relation.date
, relation.user_uid
, relation.host_uid
, relation.app_uid
, relation.description
]);
}
 
 
/**
 * Get a list of relations
 * @returns {Promise} Promise with data or error
 */
function list() {
  return db.runQuery(`SELECT * FROM media_archive.relations;`, []);
}
 
 
/**
 * Delete Relation by Relation ID
 * @param {String} relation_uid Relation ID
 * @returns {Promise} Promise with data or error
 */
function remove(relation_uid) {
  return db.runQuery(`DELETE FROM media_archive.relations
  WHERE media_archive.relations.relation_uid = ?;`, [relation_uid]);
}
 
 
/**
 * Update Relation
 * @param {Object} Relation Clip object whit data.
 * @returns {Promise} Promise with data or error
 */
function update(relation) {
  return db.runQuery(`UPDATE media_archive.relations
    SET relation_uid = ?, clip_uid = ?, action = ?, date = ?, user_uid = ?, host_uid = ?, app_uid = ?, description = ?
    WHERE media_archive.relations.relation_uid = ?;`, [
    relation.relation_uid
, relation.clip_uid
, relation.action
, relation.date
, relation.user_uid
, relation.host_uid
, relation.app_uid
, relation.description
,relation_uid ]);
}
 
 
/**
 * Update Relation only one column value
 * @param {String} relation_uid Relation ID
 * @param {String} col_name Name of property
 * @param {String} val New value for property
 * @returns {Promise} Promise with data or error
 */
function updateCol(relation_uid, col_name, val) {
  return db.runQuery(`UPDATE media_archive.relations
    SET ${col_name} = ?
    WHERE media_archive.relations.relation_uid = ?;`, [
    val,relation_uid]);
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