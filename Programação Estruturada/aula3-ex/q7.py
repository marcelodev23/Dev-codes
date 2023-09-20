'''
Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis. 
Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados.
'''

valor =  bool(input('Digite um valor para True ou aperte ENTER para False: '))
valor2 = bool(input('Digite um valor para True ou aperte ENTER para False: '))

print('Resultado do operador AND ',valor and valor2)
print('Resultado do operador OR',valor or valor2)
print('Resultado do operador NOT do primero valor ', not valor)
print('Resultado do operador NOT do segundo valor ', not valor2)