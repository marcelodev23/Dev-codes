'''
contador = -10 
while contador <= 10:
    print(f'Contador {contador}')
    contador += 1
'''

from time import sleep

fila = 10
while fila > 0:
  print(f'Continua esperando... [posição: {fila}]')
  sleep(2)
  fila -= 1
print('Sua vez chegou! Atendido!')