def Questao_01():
    '''Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) está no vetor. 
       Caso o valor x não seja encontrado, o programa deve imprimir o valor -1
       Crie uma lista de 5 elementos e preencha com uma iteração sobre a lista com valores lidos do teclado
       Leia um número do teclado
       Compare se este número está na lista'''
    Lista_numeros = list()
    x=0
    for i in range(0,5):
        numero = int(input(': '))
        Lista_numeros.append(numero)
    numero1 = int(input('Numero para pesquisa em lista: ')) 
    for i in range(0,len(Lista_numeros)):
        if numero1 == Lista_numeros[i]:
            x = i
            break
        else:
            x = '-1'
    print(x)
    
def Questao_02():
    '''Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. 
       Faça um programa que determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos.
       Crie uma lista com tamanho 50 e armazene nesta lista valores gerados aleatóriamente
       Faça uma iteração na lista para verificar quantos destes números são iguais à 6 '''
    from random import randint
    lista_numeros =[randint(1,6) for i in range(1,50)]
    cont=0
    for i in lista_numeros:
        if i == 6:
            cont+=1
    print(f'{cont/50*100:.0f}%')  

def Questao_03():
    from random import randint
    '''Faça um programa que preenche um vetor de 10 posições com números aleatórios entre 0 e 20. 
       Após o preenchimento, o programa deve manipular os valores de cada posição do vetor da seguinte forma: cada célulaé a soma dela mesma e das células anteriores. 
       Imprima o vetor antes e depois da manipulação. Exemplo:
       Vetor original [2, 1, 20,5, 17,19,14,4, 18,2]
       Vetor manipulado [2, 3, 25,35,82,166, 327, 644, 1302,2588]'''
    Vetor_original = [randint(0,20) for i in range(0,10)]
    Vetor_manipulado= list()
    soma = 0
    for i in range(0,len(Vetor_original)):
        soma+= Vetor_original[i]
        Vetor_manipulado.append(soma)
    print(Vetor_original)
    print(Vetor_manipulado)    

def Questao04():
    #Dada uma lista de números, utilize map() com uma função lambda para criar uma nova lista onde cada número é multiplicado por 2, mas apenas se for maior que 5
  numeros = [22,54,66,323,44,32]
  multiplicado = lambda i: i*2 if i >= 5 else i
  print(list(map(multiplicado,numeros)))


def Questao05():
    #Crie uma lista de quadrados dos números de 1 a 10 usando list comprehension.
    lista = [i for i in range(1,11)]
    for i in lista:
        print(f'{i**2}',end=' ')

def Questao06():
    '''Faça um programa que converta uma lista de temperaturas de Fahrenheit para Celsius, 
       em seu programa o usuário deverá inserir uma sequência de valores que representam a temperatura em graus Fahrenheit, 
       seu programa deve receber esses valores e armazenar em uma lista até que o valor inserido pelo usuário seja um valor em branco (uma string vazia).
       Converta todos os valores presentes na lista para graus Celsius usando a função map e imprima na tela em uma formatação amigável ao usuário.'''
    lista_temperaturas_Fahrenheit=[]
    lista_temperaturas_Celsius=[]
    dado= input('Digite temperatura(Fahrenheit): ')
    while(dado!=''):
        dado= input('Digite temperatura(Fahrenheit): ')
        if dado != '':
            lista_temperaturas_Fahrenheit.append(float(dado))

    def converte(temperatura):
        return (temperatura-32)/1.8
    
    lista_temperaturas_Celsius = list(map(converte,lista_temperaturas_Fahrenheit))
    print('-'*30)
    print('Temperaturas de Fahrenheit')
    for Fahrenheit in lista_temperaturas_Fahrenheit:
        print(f'{Fahrenheit}°F',end=' ')
    print()
    print('-'*30)
    print('Temperaturas de Celsius')
    for Celsius in lista_temperaturas_Celsius:
        print(f'{Celsius:.2f}°C',end = ' ')
    print()
    print('-'*30)
    
def Questao07():
    '''A partir do dicionário de nomes e idades de pessoas a seguir, 
       faça um programa que imprima em ordem a partir dos nomes das pessoas, 
       mostre a soma das idades, a média das idades e a pessoa mais velha.'''
    people = {
        "Rafael": 41,
        "Anne": 28,
        "Jen": 32,
        "Satan": 2000000,
        "Frank": 12,
        "Sally": 19,
        "Bob": 42,
        "Sue": 21,
        "Jill": 32,
        "Jack": 32,
    }
    nomes = []
    soma = 0
    maior = 0
    for i in people.keys():
        nomes.append(i)
    for i in people.values():
        soma+=i
        if i > maior:
            maior = i 
    nomes.sort()        
    print('-'*35)
    print(f'A soma de todas as idades: {soma}')
    print(f'A média de todas as idades: {soma/len(people)}')
    print(f'A pessoa mais velha : {maior}')
    print('-'*35)
    print('Nomes das pessoas: ')
    for nome in nomes:
        print(nome)

