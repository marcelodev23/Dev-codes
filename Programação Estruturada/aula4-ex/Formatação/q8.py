#Escreva um programa que solicite ao usuário uma palavra e imprima uma mensagem formatada mostrando a palavra em caixa alta e caixa baixa.

palavra = str(input('digite um palavra: '))  

print(f'Palavra em caixa alta: {palavra.upper()} Palavra em caixa baixa: {palavra.lower()}')