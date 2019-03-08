const express = require('express');
const router = express.Router();

/* Run tricks */
const tricks = require('../utils/tricks');

if (process.env.DB_TYPE === 'mysql') {
  tricks.mysqlPollConnection();
}

const clips_ctrl = require('../services/clips');

/* GET home page. */
router.get('/', function(req, res) {
  clips_ctrl.listClips().
  then(function(val) {
    // console.log(val)
    res.json(val);
  });
  // res.render('index', { title: 'Express' });
});

module.exports = router;
