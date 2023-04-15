from random import sample 
lista = list(range(100)) 

vectorcomb = sample(lista,8)
def combsort(vectorcomb):
    print("El vector a ordenar con comb es:",vectorcomb)
    
    largo = 0 
    
    for _ in vectorcomb:
        largo += 1
    diferencia = largo
    cambiar = True
    
    while diferencia > 1 or cambiar:
        diferencia = max(1, int(diferencia / 1.25))  
        cambiar = False
        for i in range(largo - diferencia):
            j = i+diferencia 
            if vectorcomb[i] > vectorcomb[j]:
                vectorcomb[i], vectorcomb[j] = vectorcomb[j], vectorcomb[i]
                cambiar = True
    
    print("El vector ordenado con comb es: ",vectorcomb)

combsort(vectorcomb)
