''''
Escreva um programa que peça ao usuário para adivinhar um número secreto entre 1 e 100. 
O programa deve informar se o palpite é muito alto, muito baixo ou correto. 
Continue pedindo ao usuário para adivinhar até que ele acerte o número utilizando um loop "while".
'''

from random import randint

numero_sorteado = 8

acetor = True 

numero_ = 1

while acetor :
    numero = int(input('Digite um palpite de numero (entre 1 e 100): '))

    if numero_ == 3:
        acetor = False
        print('Vocé não acetor o numero em 3 tentativa')
        break
    elif(numero== numero_sorteado):
        acetor = False
        print('Vocé acetor o numero')
        break
    elif numero < numero_sorteado:
        print('o seu palpite é muito baixo' )
        numero_+=1
    elif numero > numero_sorteado :
        numero_+=1
        print('o seu palpite é muito alto')
    
