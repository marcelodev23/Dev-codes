#Escreva um programa que utilize um loop "for" para calcular a soma de todos os números ímpares de 1 a 10
somar = 0
for i in range(1,10):
    if (i % 2) != 0 :
        #print(i)
        somar += i
print(f'A somar de todos os números ímpares(1 a 10) = {somar}')