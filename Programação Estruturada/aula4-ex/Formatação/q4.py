'''
Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. 
Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."
'''
texto = 'Fulano de Tal'

print(f'{texto.split()[0][:1]}.{texto.split()[1][:1].upper()}.{texto.split()[2][0:1]}')