/* eslint-disable */
// 数据库连接配置
// db.js——用来添加 mysql 配置
// 引入mysql模块
const mysql = require('mysql');

// 创建数据库连接
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '123456',
    database: 'detectimage'
});

// 连接到数据库
connection.connect((err) => {
    if (err) {
        console.error('无法连接到数据库:', err);
    } else {
        console.log('成功连接到数据库');
        // 在这里可以进行数据库操作
        // 例如查询数据、插入数据等
    }
});

// 结束连接（在完成数据库操作后）
connection.end((err) => {
    if (err) {
        console.error('无法关闭数据库连接:', err);
    } else {
        console.log('成功关闭数据库连接');
    }
});
