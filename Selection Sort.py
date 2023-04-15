def selectionSort(nums):
    for i in range(len(nums)):
        val_min = i
        for j in range (i+1,len(nums)):
            if nums[j]< nums [val_min]:
                val_min = j
        nums[i],nums[val_min]=nums[val_min],nums[i]

lista = [5,2,1,8,6]
selectionSort(lista)
print (lista)
