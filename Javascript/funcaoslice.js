// a funcao slice ela retorna uma copia da parte de um array
// para outro array (subarray)
// ele ira copiar a parter de um array da posição 1 a 4 e colocar
// em outro array

let carros = ["Gol","Fusca","Ford ka","Sandero","Uno"]

let garagem = carros.slice(1,5);

console.log("Carros na Garagem", garagem);