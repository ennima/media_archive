/**
 * Funciones que parchan errores de los modulos npm
 */
const db = require('../models/db.js');

/**
 * Run SQL query on mysql every process.env.DB_POLL_TIME
 * This is a trick to fix mysql lost connection problem
 * @returns {void}
 */
function mysqlPollConnection() {

  setInterval(function () {
    const query = 'SELECT ?;';

    db.executeQuery(query, [1] ,function(error, data) {

      if (error === null) {
        console.log('-- Poll connection --');
        console.log(`Data: ${data.rows[0]}`);
      } else {
        console.log(error);
      }

    });

  }, process.env.DB_POLL_TIME);

}

module.exports = {
    mysqlPollConnection
};
