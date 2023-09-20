#Escreva um programa em Python que solicite ao usuário dois números inteiros e troque os valores das variáveis. Em seguida, imprima os valores atualizados.

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

print(f'Valores antes da troca: numero1 = {n1}, numero2 = {n2}')

n1= n1+n2
n2= n1-n2
n1 =n1-n2

print(f'Valores depois da troca: numero1 = {n1}, numero2 = {n2}')