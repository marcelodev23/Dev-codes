'''
Calculadora de IMC: Peça ao usuário seu peso e altura e calcule o índice de massa corporal (IMC). 
Em seguida, mostre uma mensagem indicando se a pessoa está abaixo do peso, com peso normal, com sobrepeso, obesa ou muito obesa.
'''

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso/(altura*altura)

if imc < 18.50:
    print('Magreza')
elif imc >= 18.50 and imc <= 24.90:
    print('Normal')
elif imc >= 25.00 and imc < 29.9:
    print('Sobrepeso')
elif imc >= 30 and imc >= 39.99:
    print('obesa')
elif imc >= 40.00:
    print('muito obesa')