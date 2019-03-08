const express = require('express');
const router = express.Router();

const clips_ctrl = require('../services/clips');

/* GET home page. */
router.get('/', function(req, res) {
  clips_ctrl.listClips().
  then(function(val) {
    res.json(val);
  });

});

module.exports = router;
