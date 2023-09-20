#Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário um número e verifica se ele é par ou ímpar.

numero  =  int(input('Digite um numero: '))

if (numero & 2) == 0:
    print('Esse numero é par')
else:
    print('Esse numero é ímpar')

