#Verificação de Ano Bissexto: Escreva um programa que verifica se um ano fornecido pelo usuário é bissexto ou não.

ano = int(input('Digite um ano: '))

if (ano % 4) == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')