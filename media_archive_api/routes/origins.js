const express = require('express');
const router = express.Router();

const origins_ctrl = require('../services/origins');

router.get('/', function(req, res) {
    origins_ctrl.listOrigins().
    then(function(val) {
        res.json(val);
    });
});

router.post('/', function(req, res) {
    origins_ctrl.addOrigin().
    then(function(val) {
        res.json(val);
    });
});

module.exports = router;
