'''
Verificação de Triângulo: Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo. 
Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
'''

lado_a = int(input('Digite o lado A: '))
lado_b = int(input('Digite o lado B: '))
lado_c = int(input('Digite o lado C: '))

if lado_a == lado_b == lado_c:
    print('Triângulo equilátero')
elif lado_a == lado_b != lado_c or lado_b == lado_c != lado_a :
    print('Triângulo isósceles')
elif lado_a != lado_b != lado_c:
    print('triângulo escaleno')