#Escreva um programa que dado um dia, mes e ano calcule o valor em termos de UNIX Epoch Time (o número de segundos desde 00:00 de 01 de Janeiro de 1970)

anos = 2023 - 1970
mes = 8 - 1
dias = 18 - 1
hs = 14
min = 36

total_segundos = (min * 60) + (hs * 60 * 60) + (dias * 24 * 60 * 60) + (mes * 30 * 24 * 60 * 60) + (anos * 365 * 24 * 60 * 60 )
print(total_segundos)
