# A funcao Map tem o objetivo aplicar uma funcao ou acao
# em todos os elementos de uma estrutura de dados retornando
# uma nova sequencia ou resultado

lista =[1,5,3,15,78]

def soma(x):
    return x+2
print(list(map(soma,lista)))
