'''
Escreva um programa que solicite ao usuário uma quantidade de horas, minutos e segundos, e imprima uma mensagem formatada mostrando o total de segundos. 
Por exemplo: "O total de segundos é {total_segundos}."
'''
horas = int(input('Digite quantidade de horas: '))
minutos = int(input('Digite quantidade de minutos: '))
segundos=  int(input('Digite quantidade de segundos: '))

minutos_segundos = minutos * 60 
horas_segundos = horas * 60 * 60
total_segundos = horas_segundos + minutos_segundos + segundos

print(f"O total de segundos é {total_segundos}.")