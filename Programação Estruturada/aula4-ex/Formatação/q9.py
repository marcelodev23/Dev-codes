'''
Escreva um programa que solicite ao usuário um nome e um número inteiro e imprima uma mensagem formatada repetindo o nome o número de vezes especificado. 
Por exemplo, se o nome for "João" e o número for 3, o programa deve imprimir "JoãoJoãoJoão".
'''

nome = str(input('Digite um nome: '))
numero= int(input('Digite um número'))
test = ''
for i in range(numero):
    test = test + nome 

print(test)
