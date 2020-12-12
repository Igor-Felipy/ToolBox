const Database = require('sqlite-async');

function execute(db) {
    return db.exec(`
        CREATE TABLE IF NOT EXISTS test_table (
            id INTEGER PRYMARY KEY AUTOINCREMENT,
            MESSAGE TEXT
        );
    `)
}

module.exports = Database.open(__dirname + '/database.sqlite').then(execute)