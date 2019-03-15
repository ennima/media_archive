const express = require('express');
const router = express.Router();

const origins_ctrl = require('../services/origins');

router.get('/', origins_ctrl.listOrigins);

router.post('/', origins_ctrl.addOrigin);

module.exports = router;
