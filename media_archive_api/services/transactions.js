const transactions_model = require('../models/mysql/transactions')
var moment = require('moment');

console.log(moment().format('YYYY-MM-DD H:mm:ss'));

async function listTransactions(){
    return transactions_model.list()
}

async function addTransaction(){
    return transactions_model.insert("clip_uid", "action3", moment().format('YYYY-MM-DD H:mm:ss'), "user_uid", "host_uid", "app_uid", "description")
}

module.exports = {
    listTransactions,
    addTransaction
}