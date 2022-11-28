import random
import time


#Naive Search busqueda ingenua
def naive_search(lista, target):
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1

def binary_searches(lista, target, lim_inferior=None,lim_superior=None):
    
    if lim_inferior is None:
        lim_inferior = 0

    if lim_superior is None:
        lim_superior = len(lista)-1
    
    if lim_superior < lim_inferior:
        return -1

    punto_medio = (lim_inferior + lim_superior)//2 #divide y suma entre 2, lo convierte en un entero

    if lista[punto_medio] == target:
        return punto_medio
    elif target < lista[punto_medio]:
        return binary_searches(lista, target, lim_inferior, punto_medio-1)
    else:
        return binary_searches(lista, target, punto_medio +1, lim_superior)


if __name__=='__main__':
    
    #Crear lista ordenada con 1000 numeros aleatorios
    size = 10000 
    conjunto_inicial = set()

    while len(conjunto_inicial) < size:
        conjunto_inicial.add(random.randint(-3*size, 3*size))
    
    lista_ordenada = sorted(list(conjunto_inicial))

    #medir tiempo de busqueda ingenua
    inicio = time.time()
    for target in lista_ordenada:
        naive_search(lista_ordenada, target)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos")
    #medir tiempo de busqueda binaria
    inicio = time.time()
    for target in lista_ordenada:
        binary_searches(lista_ordenada, target)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin - inicio} segundos")