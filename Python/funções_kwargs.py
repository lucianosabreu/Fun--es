
def saudacao(**kwargs):
    print(kwargs)

#chamar a função
    
saudacao(manha='bom dia',tarde='Boa Tarde',noite='Boa Noite')

def saudacoes_dia(**kwargs):
    for turno,saudação in kwargs.items():
        print(f'Durante a {turno} dizemos {saudacao}')

saudacoes_dia(manha='bom dia',tarde= 'Boa tarde')