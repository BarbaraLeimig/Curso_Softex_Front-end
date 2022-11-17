//função que lista as propriedades do objeto
objPropriedades = (objeto) => {
    console.log('Propriedades do objeto Música: \n');
    for (const propriedades in objeto){
        console.log(`${propriedades}: ${objeto[propriedades]}`);
    }
    console.log('\n********************\n');
}

//função que lista os elementos do array
arrayElementos = (array) => {
    console.log('Elementos do array Mochila: \n');
    for (const elementos of array){
        console.log(elementos);
    }
}

//função prncipal que chamará as outras
main = () => {
    // criando o objeto
    var musica = {
        nome: 'Calm down',
        artista: 'Rema & Selena Gomez',
        gênero: 'Pop'
    }
    // criando o array
    var mochila = ['caderno', 'caneta', 'lápis', 'borracha']

    //chamando as funções de propriedades do objeto e elementos do array
    objPropriedades(musica)
    arrayElementos(mochila)
}

//chamando a função principal
main()