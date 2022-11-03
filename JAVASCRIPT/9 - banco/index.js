// importando o readline-sync para interação com o usuário
const input = require('readline-sync');

// criando o objeto Banco com seus parâmetros e métodos, respectivamente
function Banco(agencia, conta, tipo_conta) {  // parâmetros
  this.agencia = agencia;
  this.conta = conta;
  this.tipo_conta = tipo_conta;
  this.saldo = 0;

  this.buscar_saldo = function () {            // métodos
    return this.saldo;
  }
  this.deposito = function (valor) {
    return this.saldo += valor;
  }
  this.saque = function (valor) {
    try {                                    // tratamento de exceção caso o valor de saque exceda o saldo
      if (valor > this.saldo) throw ('Voce nao tem saldo suficiente!\n');
      else
        this.saldo -= valor;
    }
    catch (error) {
      console.log('\nErro: ', error);
    }
  }
  this.buscar_agencia = function () {
    return this.agencia;
  }
  this.buscar_conta = function () {
    return this.conta;
  }
  this.buscar_tipo_conta = function () {
    return this.tipo_conta;
  }
  this.extrato = function () {
    console.log('');
    console.log('EXTRATO ');
    console.log('Agencia: ', this.buscar_agencia());
    console.log('Numero da conta: ', this.buscar_conta());
    console.log('Tipo de conta: ', this.buscar_tipo_conta());
    console.log('Saldo: R$ ', this.buscar_saldo())
  }
}

// criando a função menu do banco, para realizar as transações
function menu() {
  console.log('MENU');
  console.log('1 - Criar Conta');
  console.log('2 - Depósito');
  console.log('3 - Saque');
  console.log('4 - Extrato')
  console.log('0 - Sair')
}

// função principal que chamará todas as outras 
function main() {
  var opcao = 0;
  var banco = null;
  do {
    menu()
    opcao = Number(input.question('Insira o numero da operacao desejada: '));

    switch (opcao) {
      case 1:                                                                          // opção criar conta
        var agencia = Number(input.question('Digite o numero da sua agencia: '));
        var conta = Number(input.question('Digite o numero da sua conta: '));
        var tipo_conta = input.question('Digite o tipo da sua conta: ');

        banco = new Banco(agencia, conta, tipo_conta);                                // instanciando novo objeto
        console.log('\nConta criada com sucesso!\n');
        break

      case 2:                                                                         // opção depósito
        if (banco === null)                                                           // verifica se o novo objeto banco foi criado
          console.log('Crie sua conta antes de realizar um deposito');
        else
          banco.deposito(Number(input.question('Digite a quantia que deseja depositar: ')));
        break

      case 3:
        if (banco === null)                                                           // // verifica se o novo objeto banco foi criado
          console.log('Crie sua conta antes de realizar um saque');
        else
          banco.saque(Number(input.question('Digite o valor que deseja sacar: ')));
        break

      case 4:
        if (banco === null)
          console.log('Crie sua conta antes de solicitar o extrato bancario');
        else
          banco.extrato();
        break

      case 0:
        console.log('Caixa encerrado!');
        break

      default:
        console.log('Opcao invalida!')
        break
    }

  }
  while (opcao !== 0);
}

// chamando a função principal
main()