// importando o sequelize
const Sequelize = require('sequelize')

// configuração do sequelize com os dados do banco de dados
const sequelize = new Sequelize('sequelize', 'root', '', {
        host: 'localhost',
        dialect: 'mysql'
})

// teste para autenticação com o banco.
sequelize.authenticate().then(() => {
    console.log('Conexão realizada com sucesso');
 }).catch((error) => {
    console.error('Não foi possível realizar a conexão com o banco de dados: ', error);
 });

 // exportação dos dados do sequelize
 module.exports = sequelize;