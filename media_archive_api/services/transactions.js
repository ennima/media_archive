/* eslint-disable sort-keys */
const transactions_model = require('../models/mysql/transactions');
var moment = require('moment');

console.log(moment().format('YYYY-MM-DD H:mm:ss'));

/**
 * List all transactions.
 * @param {*} req Request data.
 * @param {*} res  Response data.
 * @returns {bool} True if all its ok.
 */
function listTransactions(req, res) {
    const transactions = transactions_model.list();

    transactions.then(function(val) {
        res.json(val);
    });

    return true;
}


/**
 * Add transaction.
 * @param {*} req Request data.
 * @param {*} res  Response data.
 * @returns {bool} True if all its ok.
 */
function addTransaction(req, res) {
    console.log('Body',req.body)

    let clip = {
        'clip_uid': 1,
        'action': 'store',
        'date': moment().format('YYYY-MM-DD H:mm:ss'),
        'user_uid': 3,
        'host_uid': 2,
        'app_uid': 1,
        'description': 'Storing transaction'
        }

    transactions_model.insert(clip.clip_uid, clip.action, clip.date, clip.user_uid, clip.host_uid, clip.app_uid, clip.description).
    then(function(val) {
        res.json(val);
    });

}

module.exports = {
    listTransactions,
    addTransaction
};
