// função sem parâmetros definidos
function soma(){
    console.log('A soma de 2+2 é ', 2 + 2);
}

// função com parâmetros definidos
function sub(n1, n2){
    return n1 - n2;
}

// arrow function
mult = (n3, n4) => {
    return n3 * n4;
}

soma();
console.log('A diferença entre 8 e 2 é ', sub(8, 2));
console.log('A multiplicação de 10 por 2 é ', mult(10, 2));
