#Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles.

n1 = int(input('digite 1º numero: '))
n2 = int(input('digite 2º numero: '))
n3 = int(input('digite 3º numero: '))

maior = 00
if n1 > n2 >n3:
    maior = n1
elif n2 > n1 > n3:
    maior = n2
elif n3 > n2 >n1:
    maior = n3 

print(f'O menor número digitado foi {maior}') 