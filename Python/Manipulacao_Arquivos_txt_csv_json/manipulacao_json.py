## Json = javascript object notation
## ele é estruturado por chaves e valores (dicionario)
## Json é usado para troca de informaç~çoes entre sistemas backend
## é o formato utilizado peas Apis
## usa-se tanto nas apis Graphql e api rest

## capiturar uma informação da internet ##

import urllib.request
import json

url = 'http://api.open-notify.org/astros.json'

## capiturar as informações em dados json ##

pega_json =urllib.request.urlopen(url).read().decode()

## converter esses valores em dicionarios para manipulacao ##

dic_json = json.loads(pega_json)

## iterar os valores do dicionario

for c in dic_json.values():
    print(c)

print(dic_json)

for p in dic_json['people']:
    print(p['name'],p['craft'])


## cria um arquivo json com os valores extraidos
    
    with open('arquivos/names.json','w+') as f:
        json.dump(dic_json,f,indent=4)