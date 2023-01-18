const soap = require('soap')
const url = 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'

soap.createClient(url, (err, client) => {
    if(err){
        console.log(err)
    }else{
        console.log('ok')
        client.consultaCEP({
            cep: '50030210'
        }, (err, res) => {
            console.log(res)
        })
    }
})
