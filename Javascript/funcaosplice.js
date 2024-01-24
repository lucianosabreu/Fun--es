// A função Splice ela altera um array, ela pode remover elementos como tambem pode
// substituir elementos de um array
// remover um elemento a partir da posição 2 do indice de memória

let numeros= [1,2,3,4,5]

numeros.splice(2,1)
console.log("Resultado remoções",numeros);

let numeros2 =[1,2,3,4,5]

numeros2.splice(2,1,500);

console.log("Resultado Substituição Array", numeros2);