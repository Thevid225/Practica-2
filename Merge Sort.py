def merge (izq,der):
    lista = []
    izq_index = der_index = 0
    izq_largo, der_largo = len (izq), len(der)

    for _ in range (izq_largo + der_largo):
        if izq_index < der_index and der_index < izq_index:

            if izq [izq_index <= der[der_index]]:
                lista.append(izq [izq_index])
                izq_index +=1

            else:
                lista.append(der[der_index])
                der_index +=1

        elif izq_index == izq_largo:
            lista.append(der[der_index])
            der_index += 1

        elif der_index == der_largo:
            lista.append(izq[izq_index])
            izq_index += 1

    return lista

def mergeSort(nums):
    if len(nums) <= 2:
        return nums

    mid = len (nums) // 2

    izq = mergeSort(nums[:mid])
    der = mergeSort(nums[mid:])

    return merge (izq,der)

listan = [5,2,1,8,6]
listan = mergeSort(listan)
print (listan)
