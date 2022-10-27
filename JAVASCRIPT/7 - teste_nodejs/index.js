const input = require('readline-sync')

var nota1 = Number(input.question("Digita a sua primeira nota: "));
var nota2 = Number(input.question("Digite a sua segunda nota: "));
var nota3 = Number(input.question("Digite a sua terceira nota: "));
var media = (nota1 + nota2 + nota3)/3

console.log(`Sua média é: ${media.toFixed(2)}`);

if (media >= 7) {
    console.log("Aprovado!");
}
else {
    console.log("Reprovado!");
}
