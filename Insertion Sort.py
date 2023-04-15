def insertionSort(nums):

    for i in range (1,len(nums)):
        numero = nums[i]
        j=i-1

        while j>=0 and nums[j]> numero:
            nums [j+1] = nums [j]
            j -=1
            nums[j+1] = numero

lista = [5,2,1,8,6]
insertionSort(lista)
print (lista)
