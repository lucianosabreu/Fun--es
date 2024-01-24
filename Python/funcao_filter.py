# funcao filter, filtra elementos de uma estrutura de dados
# e filtra o valor que queremos encontrar

listamista = ['1',"Joao","Pedro",53]

def busca(x):
    return x == "Joao"



print(list(filter(busca,listamista)))



print(list(filter(lambda x: x == "Pedro",listamista)))
