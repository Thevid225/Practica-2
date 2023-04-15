from random import sample 
lista = list(range(100)) # Creamos la lista base con números del 1 al 100

vectorheap = sample(lista,8)

def heapsort(vectorheap):
    print("El vector a ordenar con heap es:", vectorheap)
    largo = 0 
        
    for _ in vectorheap:
        largo += 1
        
    def amontonar(vectorheap, n, i): 
        mas_largo = i 
        izq = 2 * i + 1      
        der = 2 * i + 2    
    
        if izq < n and vectorheap[i] < vectorheap[izq]: 
            mas_largo = izq 
    
        if der < n and vectorheap[mas_largo] < vectorheap[der]: 
            mas_largo = der 
            
    
        if mas_largo != i: 
            vectorheap[i],vectorheap[mas_largo] = vectorheap[mas_largo],vectorheap[i]  
            amontonar(vectorheap, n, mas_largo)
            
    def heap(vectorheap):
        
        n = largo
        for i in range(n//2 - 1, -1, -1): 
            amontonar(vectorheap, n, i) 
        for i in range(n-1, 0, -1): 
            vectorheap[i], vectorheap[0] = vectorheap[0], vectorheap[i] 
            amontonar(vectorheap, i, 0)
        
    heap(vectorheap)
    print("El vector ordenado con heap es:", vectorheap)

heapsort(vectorheap)
