var input = require('readline-sync');

console.log(soma());
console.log(subtracao(14, 4));

function soma() {
    var n1 = Number(input.question('Digite o primeiro valor da soma: '));
    var n2 = Number(input.question('Digite o segundo valor da soma: '));
    var soma = (n1 + n2)

    console.log(`O valor da soma é ${soma}`);
}

function subtracao(){
    sub = (n3 - n4);
    return sub;
}