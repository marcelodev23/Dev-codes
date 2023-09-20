'''
Escreva um programa que solicite ao usuário uma frase e 
imprima uma mensagem formatada mostrando a quantidade de caracteres, palavras e linhas na frase.
'''
frase = str(input('Digite um frase: '))
print(f'A quantidade de caracteres: {len(frase)} {frase.split()} linha 1') 