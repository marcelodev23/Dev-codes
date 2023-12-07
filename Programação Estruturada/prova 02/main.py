def processa_lista(valores):
    pares=[]
    impares=[]
    for valor in valores:
        if int(valor) % 2 ==0:
            pares.append(valor)
        else:
            impares.append(valor)
    return pares[-5:],impares[-5:]

def indice_menor(lista):
    pass

def organizar_alturas(lista):
    pass

def ler_valores():
    while True:
        numero = input(': ')
        if numero != '0' or None:
            n = numero
        else:
            return n

def formatar_alturas(lista):
    pass

def intercalar_listas(lista1, lista2):
    saida=[]
    if len(lista2) > len(lista1):
        for valor in range(0,len(lista2)):
                if valor < len(lista1):
                        saida.append(lista1[valor])
                saida.append(lista2[valor])
    else:
        for valor in range(0,len(lista1)):
                if valor < len(lista2):
                        saida.append(lista2[valor])
                saida.append(lista1[valor])
    return saida
        

def lista_maior18(pessoas):
    lista_pessoas = []
    for key,valor in pessoas.items():
        if valor >= 18:
            lista_pessoas.append(key)
    lista_pessoas.sort()
    return lista_pessoas
          
def q1(pessoas = {"Joao": 25, "Maria": 10,"Ola":20,"Aaa":22}):
    resultado = lista_maior18(pessoas)
    return(resultado)
    # resultado = lista_maior18(pessoas)
    # return resultado
    

def q2(lista1 = [1, 3, 5], lista2 = [2, 4, 6, 8, 10]):
    resultado_intercalado = intercalar_listas(lista1, lista2)
    return resultado_intercalado
    

def q3(valores = None):
     valores = [2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11, 0]
     pares, impares = processa_lista(valores)
     return pares, impares
    

def q4(valores = None):
    #valores = ler_valores()
    # lista_ambrosina = organizar_alturas(valores)
    # return formatar_alturas(lista_ambrosina)
    pass

print(q2())

def main():
    pass

if __name__ == "__main__":
    main()

