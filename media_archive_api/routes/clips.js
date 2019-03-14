const express = require('express');
const router = express.Router();

const clips_ctrl = require('../services/clips');

/* GET home page. */
router.get('/', clips_ctrl.listClips);


router.post('/', clips_ctrl.addClip);

module.exports = router;
