const express = require('express');

const route = require('./routes/crud');


const server = express()

server
.get('/', route.get)
.post('/', route.post)
.put('/', route.put)
.delete('/', route.delete)


server.listen(5000)