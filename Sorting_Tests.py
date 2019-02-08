# selection sort
import random
import sys

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        # loop from j starting from i+1 ending at the length of the array
        for j in range(i+1,len(arr)):
            if arr[minIndex]>arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

def insertionSort(arr):
    for i in range(len(arr)):
        location = arr[i]
        j = i-1
        while j >= 0 and location < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = location

'''
print(selectionSortArray)
lst = ['apples', 'bananas', 'oranges']
print(lst)
'''

'''
generateNumbers = []

for x in range(15):
    generateNumbers.append(random.randint(0 , 1000))
    print(x+1, "numbers entered")

print("Aye this is the random numbers", generateNumbers)
'''

selectionSortArray = [765, 281, 687, 225, 253, 441, 30, 790, 788, 436, 80, 290, 655, 243, 848]
print("Unsorted selectionSortArray: ", selectionSortArray)
selectionSort(selectionSortArray)
print("Sorted selectionSortArray: ", selectionSortArray, "\n")


insertionSortArray = [698, 986, 841, 691, 266, 704, 695, 552, 59, 335, 938, 254, 857, 320, 48]
print("Unsorted insertionSortArray: ", insertionSortArray)
insertionSort(insertionSortArray)
print("Sorted insertionSortArray: ", insertionSortArray, "\n")

