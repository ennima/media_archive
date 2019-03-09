const express = require('express');
const router = express.Router();

const transactions_ctrl = require('../services/transactions')

router.get('/', function(req, res) {
    transactions_ctrl.listTransactions().
    then(function(val) {
        res.json(val);
    });
});


router.post('/', function(req, res) {
    transactions_ctrl.addTransaction().
    then(function(val) {
        res.json(val);
    });
});

module.exports = router;
