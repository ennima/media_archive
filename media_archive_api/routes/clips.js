const express = require('express');
const router = express.Router();

const clips_ctrl = require('../services/clips');

/* GET home page. */
router.get('/', clips_ctrl.listClips);

router.get('/find', clips_ctrl.findClip);

router.post('/', clips_ctrl.addClip);

router.patch('/', clips_ctrl.changeProp);

module.exports = router;
