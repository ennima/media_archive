/**
 * Get DateTime Now day-month-year hour-min-sec
 * @returns {String} "03-02-2018 00:12:03"
 */
function getDateTime() {

  const date = new Date();
  let hour = date.getHours();

  hour = (hour < 10 ? '0' : '') + hour;

  let min = date.getMinutes();

  min = (min < 10 ? '0' : '') + min;

  let sec = date.getSeconds();

  sec = (sec < 10 ? '0' : '') + sec;

  const year = date.getFullYear();
  let month = date.getMonth() + 1;

  month = (month < 10 ? '0' : '') + month;

  let day = date.getDate();

  day = (day < 10 ? '0' : '') + day;

  return `${day}-${month}-${year} ${hour}:${min}:${sec}`;

}

/**
 * Get DateTime Now year-month-day hour-min-sec
 * Mysql stores correct this format
 * @returns {String} "2018-02-03 00:12:03"
 */
function getDateTimeDb() {

  const date = new Date();
  let hour = date.getHours();

  hour = (hour < 10 ? '0' : '') + hour;

  let min = date.getMinutes();

  min = (min < 10 ? '0' : '') + min;

  let sec = date.getSeconds();

  sec = (sec < 10 ? '0' : '') + sec;

  const year = date.getFullYear();
  let month = date.getMonth() + 1;

  month = (month < 10 ? '0' : '') + month;

  let day = date.getDate();

  day = (day < 10 ? '0' : '') + day;

  return `${year}-${month}-${day} ${hour}:${min}:${sec}`;

}

/**
 * Get data from MySQL query
 * if returns only one row, returns one Object
 * @param {List} data Is the query data returns
 * @returns {Object} {}
 */
function getReturnData(data) {

  if (data.rows.length === 1) {
   return data.rows[0];
  }

  return data.rows;

}

/**
 * Get data from request
 * @param {Object} req Is the request
 * @returns {Object} request params
 */
function getParams(req) {

  let result = {};

  if (Object.keys(req.body).length > 0) {
    result = req.body;
  } else if (Object.keys(req.query).length > 0) {
    result = req.query;
  } else {
    result = false;
  }

  return result;

}

module.exports = {
  getDateTime,
  getDateTimeDb,
  getParams,
  getReturnData

};
