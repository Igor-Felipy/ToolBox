const Db = require('./db')

module.export = {
    async get(request,response) {
            await Db.run(`
                SELECT * FROM test_table WHERE id = ${id}
            `);
        return response.send(JSON.jasonify(data))
    },
    async post(request,response) {
        Db.run(`
            INSERT INTO test_table (
                MESSAGE
            ) VAlUES (
                "${message}"
            )
        `);
    },
    async put(request,response) {
        Db.run(`
            UPDATE test_table SET MESSAGE=${message} WHERE id = ${id}
        `);
    },
    async delete(request,response) {
        Db.run(`
            DELETE FROM test_table WHERE id = ${id}   
        `);
    }
}