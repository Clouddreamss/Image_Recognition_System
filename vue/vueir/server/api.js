/* eslint-disable */
const connection = require('./db.js');

function getData(callback) {
  const sql = "SELECT * FROM detectimage.detection"; // 执行查询语句
  connection.query(sql, (err, result) => {
    if (err) {
      console.log(err);
      return
    }
    callback(result)
    console.log(result)
    // connection.destroy(); // 释放资源
  });
}
module.exports = {
  getData,
}