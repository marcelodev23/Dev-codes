#Crie uma string com seu nome completo e imprima somente o primeiro nome.

nome = str(input('Digite seu nome: '))

print(nome[:nome.index(' ')])
