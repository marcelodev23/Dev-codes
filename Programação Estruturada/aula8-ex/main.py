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

