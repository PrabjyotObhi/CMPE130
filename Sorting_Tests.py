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

def mergeSort(arr):
    if len(arr)>1:
        # FLOOR DIVISION
        mid = len(arr)//2
        # SPLIT THE ARRAY INTO TWO "EQUAL" SUBARRAYS
        L = arr[:mid]
        R = arr[mid:]
        # RECURSION TO GET TO LENGTH ONE, SO IT WILL BE NATURALLY SORTED
        mergeSort(L)
        mergeSort(R)

        # SETTING UP POINTERS FOR LEFT, RIGHT, AND THE FINAL ARRAY
        i = j = k = 0

        # CAN ONLY DO THIS AS LONG AS I AND J ARE LESS THAN THE LENGTHS OF THEIR RESPECTIVE ARRAYS
        while i < len(L) and j < len(R):
            # IF THE VALUE ON THE LEFT IS LESS THAN THE VALUE ON THE RIGHT, THE FINAL ARR AT INDEX K WOULD HAVE
            # THE VALUE FROM THE LEFT WHICH IS INDEXED WITH i. AFTER SETTING IT TO THE VALUE, YOU INCREMENT i

            # IF THE VALUE ON THE RIGHT IS LESS THAN THE VALUE ON THE LEFT, THE FINAL ARR AT INDEX K WOULD BE THE VALUE
            # FROM THE RIGHT. AFTER SETTING IT, YOU WOULD INCREMENT j

            # AFTER EITHER OF THEM, YOU INCREMENT K

            # THE LAST TWO WHILE LOOPS ARE TO CHECK IF ANY VALUE WAS LEFT OUT OF THE FINAL ARRAY
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i+1
            else:
                arr[k] = R[j]
                j = j+1
            k = k+1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



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

mergeSortArray = [560, 826, 649, 828, 897, 471, 162, 250, 907, 484, 605, 102, 600, 477, 747, 412]
print("Unsorted mergeSortArray: ", mergeSortArray)
mergeSort(mergeSortArray)
print("Sorted mergeSortArray: ", mergeSortArray)