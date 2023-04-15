def bubbleSort(nums):

    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(nums)-1):
            if nums[i] > nums [i+1]:

                nums[i], nums[i+1] = nums [i+1],nums[i]

                intercambio = True

lista=[5,2,1,8,6]
bubbleSort(lista)
print(lista)
