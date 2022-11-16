// importando o express
const express = require('express');
const app = express();

// configurando o uso das rotas http
const usorota = require('./src/rotas')
app.use('/', usorota)

// servidor na porta 8081
app.listen(8081, function(){
    console.log("Servidor Rodando na url http://localhost:8081");
});