#Escreva um programa que peça ao usuário para digitar uma palavra e, em seguida, imprima a palavra ao contrário utilizando um loop "for".

palavra = str(input('Digite uma palavra: '))
p = ''
for i in reversed(palavra):
    p+=i

print(p)