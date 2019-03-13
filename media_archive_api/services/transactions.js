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
    // console.log('Body',req.body)

    const clip = req.body

    const new_clip = {
        'clip_uid': clip.clip_uid,
        'action': clip.action,
        'date': moment().format('YYYY-MM-DD H:mm:ss'),
        'user_uid': clip.user_uid,
        'host_uid': clip.host_uid,
        'app_uid': clip.app_uid,
        'description': clip.description
        };

    transactions_model.insert(new_clip).
    then(function(val) {
        res.json(val);
    });

}

module.exports = {
    listTransactions,
    addTransaction
};
