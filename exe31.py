from random import randint
from time import sleep

itens= ('pedra', 'papel', 'tesoura')

computador = randint(0, 2)
print('''SUAS OPÇOES
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador= int(input('Qual é a sua jogada ? '))

print('JO') 
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)


print('-= '* 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)

if computador == 0: # computador jogou Pedra
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE')

    elif jogador ==2:
        print(' COMPUTADOR VENCE')

    else:
        print('jogada invalida!')

elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
         
elif computador == 2: # computador jogou Tesoura 
    if jogador ==0:
        print('JOGADOR VENCE')
    elif jogador==1:
        print('COMPUTADOR VENCE')
    elif jogador==2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')