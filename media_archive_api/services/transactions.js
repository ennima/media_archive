/* eslint-disable sort-keys */
const transactions_model = require('../models/mysql/transactions');
var moment = require('moment');

const date_format_store = 'YYYY-MM-DD H:mm:ss';
const date_format_display = 'DD-MM-YYYY H:mm:ss';


/**
 * List all transactions.
 * @param {*} req Request data.
 * @param {*} res  Response data.
 * @returns {bool} True if all its ok.
 */
function listTransactions(req, res) {
    const transactions = transactions_model.list();

    transactions.then(function(val) {

        const clip_transactions = Object.keys(val).map(function (key) {
            const new_transaction = {
                'clip_uid': val[key].clip_uid,
                'action': val[key].action,
                'date': moment(val[key].date).format(date_format_display),
                'user_uid': val[key].user_uid,
                'host_uid': val[key].host_uid,
                'app_uid': val[key].app_uid,
                'description': val[key].description
                };

            return new_transaction;
        });


        res.json(clip_transactions);
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

    const transaction = req.body

    const new_transaction = {
        'clip_uid': transaction.clip_uid,
        'action': transaction.action,
        'date': moment().format(date_format_store),
        'user_uid': transaction.user_uid,
        'host_uid': transaction.host_uid,
        'app_uid': transaction.app_uid,
        'description': transaction.description
        };

    transactions_model.insert(new_transaction).
    then(function(val) {
        res.json(val);
    });

}

module.exports = {
    listTransactions,
    addTransaction
};
