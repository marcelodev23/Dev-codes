#Escreva um programa que solicite ao usuário duas strings e verifique se elas são iguais. Imprima uma mensagem informando o resultado da comparação.

texto1 = str(input('Digite um string: '))
texto2 = str(input('Digite outro string: '))

if texto1 == texto2:
    print('strings são iguais')
else:
    print('Não são iguais')