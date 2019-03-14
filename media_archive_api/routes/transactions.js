const express = require('express');
const router = express.Router();

const transactions_ctrl = require('../services/transactions');

router.get('/', transactions_ctrl.listTransactions);


router.post('/', transactions_ctrl.addTransaction);

module.exports = router;
