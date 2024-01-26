## vamos abrir um arquivo txt

arq1 = open('arquivos/arquivo.txt','r')

print(arq1.read())

## Voltar o cursor ao início

arq1.seek(0,0)

print(arq1.read())

## fechar o arquivo

arq1.close()

## Usar um arquivo de modo gravacao

arq2 = open('arquivos/arquivo.txt','w+')

## gravar no arquivo

arq2.write("tem novo conteudo\n")
arq2.write("gravei outra linha\n")

arq2.seek(0,0)
print(arq2.read())

arq2.close()


# abrir uma nova manipulcao de alteracao de arquivo

arq3 = open('arquivos/arquivo.txt','a+')

arq3.write("novo conteudo sem apagar o arquivo\n")

arq3.seek(0.0)

print(arq3.read())

arq3.close()

## Gerenciador de Contexto de arquivos

with open("arquivos/arquivo1.txt",'w+') as f:
    f.write('primeira linha\n')
    f.write('segunda linha\n')
    f.seek(0,0)
    grava =str(f.read())
    f.seek(0,0)
    print(f.read())

# Gravar informacoes em um 2 arquivos
    
    with open('arquivos/arquivo2.txt','w+') as f2:
        f2.write(grava)
        f2.seek(0,0)
        print(f2.read())

        

