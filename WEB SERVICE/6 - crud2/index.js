const express = require('express');

const server = express();

server.use(express.json());

const funcionarios = ['funcionario-3337', 'funcionario-9090', 'funcionario-4554']
//GET one       READ
server.get('/funcionarios/:index', (req, res) => {
    const {index} = req.params;

    return res.json(funcionarios[index]);
});
//GET all of them
server.get('/funcionarios', (req, res) => {
    return res.json(funcionarios)
});

//POST          CREATE
server.post('/funcionarios', (req, res) => {
    const { name } = req.body;
    funcionarios.push(name)

    return res.json(funcionarios)
});
//PUT           UPDATE
server.put('/funcionarios/:index', (req, res) => {
    const {index} = req.params;
    const {name} = req.body;

    funcionarios[index] = name;
    
    return res.json(funcionarios);
})
//DELETE        DELETE
server.delete('/funcionarios/:index', (req, res) => {
    const {index} = req.params;
    
    funcionarios.splice(index, 1);
    return res.json({ message: 'O funcinário está fora do escritório'})
})




server.listen(7777);
