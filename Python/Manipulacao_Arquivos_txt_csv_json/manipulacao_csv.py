## importar o  modulo csv

import csv


## criar  um arquivo csv com as funcoes  writer e writerow

with open('arquivos/nomes.csv','w+',newline="",encoding='utf-8') as fcsv:
    escreve = csv.writer(fcsv,delimiter=',')
    escreve.writerow(("nome","sobrenome","idade"))
    escreve.writerow(('Joao',"Ricardo","39"))
    escreve.writerow(('Jose',"Antonio","45"))
    escreve.writerow(('Alberto',"Cunha","16"))
   

## ler o arquivo CSV criado
    
with open('arquivos/nomes.csv','r') as fcsv:
    ler = csv.reader(fcsv)
    lista1 = list(ler)
    print(lista1)

    for c in lista1:
        print(c)

## transformar a saida em dicionario com o metodo dictreader

with open('arquivos/nomes.csv','r') as fcsv2:
            ler_dic =csv.DictReader(fcsv2)

# iterar os valores

for d in ler_dic:
    print(d["Nome"])