'''
Escreva um programa que peça ao usuário para digitar uma série de números (um por linha) e pare quando o usuário digitar um número negativo. 
Em seguida, calcule e imprima a média dos números digitados.
'''

acetor = True
soma = 0 
contador=0
while acetor:
    numero = int(input('Digite os numeros: '))
    if numero > -1:
        contador+=1
        soma += numero
    else:
        acetor = False
        soma=soma/contador
        break
print('A média dos números digitados é ',soma)