/**
 * Model for Transactions schema
 *
 * Developed by Enrique Nieto Martínez
 * 2019-03-08 21:00:31
 */

const db = require('../db');

/**
 * Get a number of total transactions
 * @returns {Promise} Promise with data or error
 */
function count() {
  return db.runQuery('SELECT COUNT(*) as total_transactions FROM media_archive.transactions;', []);
}


/**
 * Find a Transaction by ID
 * @param {String} transaction_uid Transaction uid
 * @returns {Promise} Promise with data or error
 */
function find(transaction_uid) {
  return db.runQuery(`SELECT * FROM media_archive.transactions
      WHERE media_archive.transactions.transaction_uid = ?;`, [transaction_uid]);
}


/**
 * Insert Transaction.
 * @param {String} transaction Clip object whit data.
 * @returns {Promise} Promise with data or error
 */
function insert(transaction) {
  return db.runQuery(`INSERT INTO media_archive.transactions
        (clip_uid, action, date, user_uid, host_uid, app_uid, description)
        VALUES( ?, ?, ?, ?, ?, ?, ?);`, [
        transaction.clip_uid,
        transaction.action,
        transaction.date,
        transaction.user_uid,
        transaction.host_uid,
        transaction.app_uid,
        transaction.description
      ]);
}


/**
 * Get a list of transactions
 * @returns {Promise} Promise with data or error
 */
function list() {
  return db.runQuery(`SELECT * FROM media_archive.transactions;`, []);
}


/**
 * Delete Transaction by Transaction ID
 * @param {String} transaction_uid Transaction ID
 * @returns {Promise} Promise with data or error
 */
function remove(transaction_uid) {
  return db.runQuery(`DELETE FROM media_archive.transactions
  WHERE media_archive.transactions.transaction_uid = ?;`, [transaction_uid]);
}


/**
 * Update Transaction
 * @param {String} transaction_uid Transaction uid
 * @param {String} clip_uid Clip uid
 * @param {String} action Action
 * @param {String} date Date
 * @param {String} user_uid User uid
 * @param {String} host_uid Host uid
 * @param {String} app_uid App uid
 * @param {String} description Description
 * @returns {Promise} Promise with data or error
 */
function update(transaction_uid, clip_uid, action, date, user_uid, host_uid, app_uid, description) {
  return db.runQuery(`UPDATE media_archive.transactions
    SET transaction_uid = ?, clip_uid = ?, action = ?, date = ?, user_uid = ?, host_uid = ?, app_uid = ?, description = ?
    WHERE media_archive.transactions.transaction_uid = ?;`, [
    transaction_uid, clip_uid, action, date, user_uid, host_uid, app_uid, description,transaction_uid ]);
}


/**
 * Update Transaction only one column value
 * @param {String} transaction_uid Transaction ID
 * @param {String} col_name Name of property
 * @param {String} val New value for property
 * @returns {Promise} Promise with data or error
 */
function updateCol(transaction_uid, col_name, val) {
  return db.runQuery(`UPDATE media_archive.transactions
    SET ${col_name} = ?
    WHERE media_archive.transactions.transaction_uid = ?;`, [
    val,
    transaction_uid
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