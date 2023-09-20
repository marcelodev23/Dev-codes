#Escreva um programa que peça ao usuário para digitar uma frase e, em seguida, conte quantas vogais (a, e, i, o, u) existem na frase utilizando um loop "for".

texto = str(input('Digite uma frase: '))
somar = 0
for frase in texto:
    if frase == 'a':
        somar = somar + 1
    elif frase == 'e':
        somar = somar + 1
    elif frase == 'i':
        somar = somar + 1
    elif frase == 'o':
        somar = somar + 1
    elif frase == 'u':
        somar = somar + 1

print(f'A quantidade de vogais são {somar}')