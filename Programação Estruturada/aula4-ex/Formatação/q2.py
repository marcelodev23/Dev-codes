''''
Escreva um programa que solicite ao usuário dois números e imprima uma mensagem formatada mostrando a soma, subtração, multiplicação e divisão dos números. 
Por exemplo: "A soma de {num1} e {num2} é {soma}."
'''
num1 = int(input('Digite primero numero: '))
num2 = int(input('Digite segundo numero: ')) 

soma = num1 + num2 
divisão = num1 - num2
subtração = num1 - num2
multiplicação = num1 * num2 

print(f"A soma de {num1} e {num2} é {soma}.") 
print(f"A subtração de {num1} e {num2} é {subtração}.") 
print(f"A multiplicação de {num1} e {num2} é {multiplicação}.") 
print(f"A divisão de {num1} e {num2} é {divisão}.") 

