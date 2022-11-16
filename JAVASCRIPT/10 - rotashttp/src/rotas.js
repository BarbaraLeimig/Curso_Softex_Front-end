// importando o express depois de instalado
const express = require ("express");
const rota = express();

// método get
rota.get("/", function(req, res){
    res.send("Teste do método GET - OK");
});

// método post
rota.post("/", function(req, res){
    res.send("Teste do método POST - OK");
});

module.exports = rota;