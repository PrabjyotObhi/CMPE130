# selection sort
import random
import sys
'''''
generateNumbers = []

for x in range(15):
    generateNumbers.append(random.randint(0 , 1000))
    print(x+1, "numbers entered")

print("Aye this is the random numbers", generateNumbers)
'''

selectionSortArray = [765, 281, 687, 225, 253, 441, 30, 790, 788, 436, 80, 290, 655, 243, 848]

'''
print(selectionSortArray)
lst = ['apples', 'bananas', 'oranges']
print(lst)
'''

# loop from i to the length of the array
for i in range(len(selectionSortArray)):
    minIndex = i
    # loop from j starting from i+1 ending at the length of the array
    for j in range(i+1,len(selectionSortArray)):
        if selectionSortArray[minIndex]>selectionSortArray[j]:
            minIndex = j
    selectionSortArray[i], selectionSortArray[minIndex] = selectionSortArray[minIndex], selectionSortArray[i]

# print the array as an array

print("Sorted array:", selectionSortArray)
