# Funçoes decoradoras potencializam ou modificam a logica de
# outra função ou metodo

# Uma função decoradora e quando utilizamos o @ em cims de uma função

#Exemplo

# @decoradora - decorada potencializa a funcao oi com os recursos dela
# def oi():
# print('oi')

## Criar uma funcao decoradora

def master(msg):
    def imprime():
        print("esse e a funcao dcoradora")
    msg()
    return imprime

# criar uma função qua vai receber a decoradora

@master
def chama_funcao():
    print("Esta esta Chamando a Funcao Real")

# Chamando a função
    
chama_funcao()
