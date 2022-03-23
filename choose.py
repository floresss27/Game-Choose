import random
print('                      --- CHOOSE FOR ME ---')
print('                        --- DESCRIÇÃO ---'
'\n--- Eu sou o Choose for me, você digita suas escolhas e eu escolho por você ---')
def choose():
    e1 = input('Você deve: ')
    e2 = input('Você deve: ')
    e3 = input('Você deve: ')
    e4 = input('Você deve: ')
    lista = [e1, e2, e3, e4]
    escolha = random.choice(lista)
    print('->>>> Você deve {}'.format(escolha))
    x = input('Se quiser jogar novamente aperte qualquer tecla !!!')
    return choose()
choose()