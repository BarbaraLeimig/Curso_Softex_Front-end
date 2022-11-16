const express = require ("express");
const app = express();

app.get("/", function(req, res){
    res.send("Teste do método GET - OK");
});

app.post("/", function(req, res){
    res.send("Teste do método POST - OK");
});

app.listen(8081, function(){
    console.log("Servidor Rodando na url http://localhost:8081");
});