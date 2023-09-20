'''
Conversão de Notas: Escreva um programa que converte uma nota de 0 a 100 
em uma escala de conceitos: A (90-100), B (80-89), C (70-79), D (60-69) e F (0-59).
'''
nota = int(input('Digite sua nota(0 a 100): '))

if nota >= 0 and nota <= 59:
    print('Sua nota é F')
elif nota >= 60 and nota <=69: 
    print('Sua nota é D')
elif nota >= 70 and nota <= 79:
    print('Sua nota é C')
elif nota >= 80 and nota <= 89: 
    print('Sua nota é B')
elif nota >=90 and nota <= 100: 
    print('Sua nota é A')