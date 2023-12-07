def q1(cidades):
    resultado_esperado = []
    for key,valor in cidades.items():
        if(valor >= 100):
            resultado_esperado.append(key)
    return resultado_esperado

def q2(lista1, lista2):
    lista = lista1 + lista2
    soma = 0
    new_lista=[]
    for valor in lista:
        if valor > 0 :
            soma+=valor
            new_lista.append(valor)
    new_lista.sort()
    return f'{soma},{new_lista}'

def q3():

    def ler_valores():
        lista = []
        while True:
            valor = int(input(': '))
            if valor == 0:
                break
            else:
                lista.append(valor)
        return lista    

    def processa_lista(lista):
        pares = []
        impares = []
        for valor in lista:
            if valor % 2 == 0:
                pares.append(valor)
            else:
                impares.append(valor) 
        return pares,impares
    
    return processa_lista(ler_valores())

def q4():
    def ler_03_alturas():
         lista = []
         while True:
            valor = int(input(': '))
            if valor == 0:
                break
            else:
                lista.append(valor)
            return lista
    def organizar_alturas(lista):
        if lista[0] < lista[1] < lista[2]:
            pass

    return []

def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print('-'*35)
    print("q1:", resultado)
    print('-'*35)
    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)
    print('-'*35)
    print('q3: ',q3())
    print('-'*35)
    


if __name__ == "__main__":
    main()

