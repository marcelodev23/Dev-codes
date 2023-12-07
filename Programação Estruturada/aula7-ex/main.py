def saudacao(nome):
    #Escreva uma função chamada saudacao que aceita um nome como argumento e imprime "Olá, [nome]!".
    return f"Olá, {nome}!"

def dobro(numero):
    #Crie uma função dobro que aceita um número como argumento e retorna o dobro desse número.
    return numero*2

def saudacao_personalizada(nome,idioma):
    '''Crie uma função chamada saudacao_personalizada que aceita um nome e um idioma como argumentos. 
       O idioma é opcional e padrão para "inglês". 
       A função deve retornar uma saudação no idioma especificado.'''
    match idioma:
        case 'inglês':
            return f'Hello, {nome}!'
        case 'espanhol':
            return f'Hola, {nome}!'
        case 'francês':
            return f'Bonjour, {nome}!'
        
def potencia(numero,expoente):
    #Escreva uma função potencia que aceita uma base e um expoente (com expoente padrão igual a 2) e retorna a base elevada ao expoente
    return numero**expoente

def idade_valida(idade):
    #Crie uma função chamada idade_valida que verifica se a idade fornecida como argumento é um número inteiro válido entre 0 e 150.
    if idade >= 0 and idade <= 150:
        return True
    else:
        return False
    
def validar_email(email):
    '''Implemente uma função validar_email que verifica se uma string fornecida como argumento representa um endereço de e-mail válido. 
       Considere que um email válido não deve ter espaços, deve conter 01 arroba e terminar com .com'''    
    
    if '@' in email and email[email.index('@')+1:] != '.com':
        return True
    else:
        return False
    
def calcular_pagamento(horas_trabalhadas,taxa_hora):
#Escreva uma função calcular_pagamento que aceita os parâmetros nomeados horas_trabalhadas e taxa_hora e retorna o pagamento total.
    return horas_trabalhadas*taxa_hora

def contagem_letras(text):
#Escreva uma função em Python function que aceita uma string e retorna a quantidade de letras maiúsculas e minúsculas.
    maiusculas = 0
    minusculas = 0
    for i in text:
        if i.isupper():
            maiusculas+=1
        elif i.islower() :
            minusculas+=1
    return(maiusculas,minusculas)

def len_custom(num):
    '''Crie uma função chamada len_custom que aceita um iterável (por exemplo, uma lista ou uma string) como argumento e retorna o número de elementos no iterável. 
       Ela deve ter o mesmo comportamento que a função embutida len().'''
    resultado=0
    for i in num:
        resultado+=1
    return resultado

def sum_custom(num):
    '''Crie uma função chamada sum_custom que aceita uma lista de números como argumento e retorna a soma de todos os números na lista. 
       Ela deve ter o mesmo comportamento que a função embutida sum().'''
    resultado = 0
    for i in num:
        resultado+=i
    return resultado

def max_custom(lista):
    '''Crie uma função chamada max_custom que aceita uma lista de números como argumento e retorna o maior número na lista. 
       Ela deve ter o mesmo comportamento que a função embutida max().'''
    if lista != [] : 
        maior = lista[0]
        for numero in lista:
            if numero > maior:
                maior = numero
        return maior
    else:
        return None
    
def min_custom(lista):
    '''Crie uma função chamada min_custom que aceita uma lista de números como argumento e retorna o menor número na lista. 
       Ela deve ter o mesmo comportamento que a função embutida min().'''
    if lista != []:
        menor = lista[0]
        for numero in lista:
            if numero < menor:
                menor = numero
        return menor
    else:
        return None
    
def startswith_custom(string,prefixo):
    ''' Crie uma função chamada startswith_custom que aceita uma string e um prefixo como argumentos e retorna True 
        se a string começar com o prefixo, caso contrário, retorna False. 
        Ela deve ter o mesmo comportamento que o método str.startswith().'''
    if string[:len(prefixo)] == prefixo:
        return True
    else:
        return False
    
def endswith_custom(string,sufixo):  
    '''Crie uma função chamada endswith_custom que aceita uma string e um sufixo como argumentos e retorna True 
       se a string terminar com o sufixo, caso contrário, retorna False. 
       Ela deve ter o mesmo comportamento que o método str.endswith(). '''
    if string[-len(sufixo):] == sufixo:
        return True
    else:
        return False
    
def split_custom(string,caractere = ' '):
    ''' Crie uma função chamada split_custom que aceita uma string e um caractere de separação como argumentos e retorna 
        uma lista de substrings separadas pelo caractere de separação.
        Ela deve ter o mesmo comportamento que o método str.split().'''
    lista = list()
    lista_local = []
    local = [0,0]
    new1=''
    print(string[:string.index(' ')])
    print(string[string.index(' ')+1:])
 

    for i in range(0,len(string)):
        if string[i] == caractere:
            print(string)












def strip_custom(string,caractere = ''):
    '''Crie uma função chamada strip_custom que aceita uma string e caracteres de remoção como argumentos e retorna 
       uma nova string com os caracteres de remoção removidos dos extremos da string. 
       Ela deve ter o mesmo comportamento que o método str.strip().'''
    new_string = ''
    for i in string:
        if i != caractere:
            new_string += i
    return new_string

def replace_custom(string,substring_antiga,substring_nova):
    lista = []
    new_string = ''
    tamanho_substring_antiga= len(substring_antiga)
    
    for i in range(len(string)):
        lista.append(string[i])
    for l in range(0,len(lista)):
        print(lista[l])
        if lista[l] == substring_antiga:
            lista.pop(l)
            lista.insert(l, substring_nova)
    for i in lista:
        new_string+=i
    return(new_string)
