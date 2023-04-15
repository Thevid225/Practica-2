from random import sample 

lista = list(range(100))

vectorshell = sample(lista,8)

def shellsort(vectorshell):
    print("El vector a ordenar con shell es:", vectorshell)
    
    largo = 0
    
    for i in vectorshell:
        largo += 1
    
    distancia = largo // 2
    while distancia > 0:
        for i in range(distancia, largo):
            val = vectorshell[i]
            j = i
            while j >= distancia and vectorshell[j - distancia] > val:
                vectorshell[j] = vectorshell[j - distancia]
                j -= distancia
            vectorshell[j] = val
        distancia //= 2
    print("El vector ordenado con shell es: ", vectorshell)
    
shellsort(vectorshell)
    
