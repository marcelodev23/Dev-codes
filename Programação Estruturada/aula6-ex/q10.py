# Escreva um programa que peça ao usuário para digitar uma senha e continue pedindo até que o usuário digite a senha correta. Quando a senha estiver correta, imprima uma mensagem de boas-vindas.

acetor = True
senha_='123'
while acetor:
    senha = input('Digite sua senha: ')
    if senha == senha_:
        acetor = False
        print('Boas-vindas')
    else:
        print('Senha incorreto')