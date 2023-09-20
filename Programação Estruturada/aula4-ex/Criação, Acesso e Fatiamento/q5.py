#Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar".

texto = str(input('digite uma entrada: '))

if texto == texto[::-1]:
    print('A palavra é um palíndromo')
else:
    print('A palavra não é um palíndromo')