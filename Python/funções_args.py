## Funções são usadas quando não sabemos quantos argumentos
# teremos na chamada da funções
# *args ou *var
# ** kwargs ou *vars

def vlsoma(*args):
    print(args)


# chamar a função
    
vlsoma(1,443,12,33,12,89)

# somar os valores declarados na função

def soma_total(*args):
    total = 0
    for numero in args:
        total = numero+total
    return total
    
print(soma_total(31,51,89,12,89,10))
