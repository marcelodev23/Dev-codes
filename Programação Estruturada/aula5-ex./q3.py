#Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) e retorna o resultado dessa operação.

n1 = float(input('Digite primero numero: '))
op =  input('digite o tipo de operação (+, -, *, /)')
n2 = float(input('Digite segundo numero: '))
 
match op:
    case "+":
        print(f'A soma entre os numero {n1} + {n2} = {n1+n2}')
    case "-":
        print(f'A subtração entre os numero {n1} + {n2} = {n1-n2}')
    case "*":
        print(f'A multiplicação entre os numero {n1} + {n2} = {n1*n2}')
    case "/":
        print(f'A divisão entre os numero {n1} + {n2} = {n1/n2}')
    case _:
            print("Tipo de operação não reconhecido.")