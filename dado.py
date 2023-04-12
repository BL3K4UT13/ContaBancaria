#ia escolhem um numero de 1 a 6 e outra ia e vc tem que adivihar 
import random

def play():
    print('\nEscolha um numero de 1 a 6: ')
    player = int(input())
    while player < 1 or player > 6:
        print('Número invalido')
        print('\nEscolha um numero de 1 a 6: ')
        player = int(input())
    return player

def dificuldade():
    n = 0
    t = 0
    m = 0
    while n != 1 and n != 2 and n != 3:
        n = input('Selecione a dificuldade: \nFacil - 1 \nNormal - 2 \nDIficil- 3 \n')
        if n == 1:
            t = 2 
            m = random.randint(1,6)
        elif n == 2:
            t = 5
            m = random.randint(1,20)
        elif n == 3: 
            t = 10
            m = random.randint(1,50)
        else:
            print('valor invalido tente novamente')
        return t, m



tentativas,mestre = dificuldade()

print('\nO Mestre escolheu um número. E você, um grande vidente tem que descobri-lo.')

while tentativas > 0:
    print(f'\nVocê tem {tentativas} tentativas ')
    player = play()
    if mestre == player:
        print('\nVocê acertou! Parabens!')
        break
    elif player > mestre:
        print(f'\nVocê errou :c {player} é menor ↓ que o número que o mestre escolheu')
        tentativas -= 1
    elif player < mestre:
        print(f'\nVocê errou :c {player} é maior ↑ que o número que o mestre escolheu')
        tentativas -= 1
if tentativas == 0:
    print(f'\nVocê perdeu! O Mestre escolheu o numero: {mestre}!')