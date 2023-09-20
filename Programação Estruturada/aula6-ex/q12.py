#Dada a lista de frutas e a lista de cores abaixo, utilize a função zip() e um loop "for" para imprimir cada fruta com sua respectiva cor.

frutas = ['maçã', 'banana', 'laranja']
cores = ['vermelho', 'amarelo', 'laranja']

for fruta, cor in zip(frutas, cores):
    print(f"{fruta} é da cor {cor}")
