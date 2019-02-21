# 1. selection sort
# 2. insertion sort
# 3. shell sort
# 4. heap sort
# 5. merge sort
# 6. quick sort

import time
import random
import matplotlib.pyplot as plt

class Sorting(object):
    """Sorting class

    """

    def __init__(self):
        self.id = []


    def sort_init(self, N):
        """initialize the data structure

        """

        try:
            self.id = random.sample(range(1, N ** 3), N)
        except ValueError:
            print('Sample size exceeded population size.')


        #self.id = [random.randint(0, N - 1) for i in range(N)]

    def get_id(self):
        """initialize the data structure

        """

        return self.id


    def selection_sort(self):
        """Selection sort algorithm is an
        in-place comparison sort. It has O(n^2) time complexity, making it
        inefficient on large lists, and generally performs worse than the
        similar insertion sort

        """
        for i_idx, i_item in enumerate(self.id):
            min = i_idx

            for j_idx in range(i_idx+1, len(self.id)):

                if (self.id[j_idx] < self.id[min]):
                    min = j_idx

            # swap
            temp = self.id[i_idx]
            self.id[i_idx] = self.id[min]
            self.id[min] = temp


        return self.id

    def insertion_sort(self):
        """Insertion sort is a simple sorting algorithm that builds the final
        sorted array (or list) one item at a time. More efficient in practice
        than most other simple quadratic (i.e., O(n^2)) algorithms such as
        selection sort or bubble sort specifically an

        """
        for i in range(len(self.id)):
            location = self.id[i]
            j = i - 1
            while j >= 0 and location < self.id[j]:
                self.id[j + 1] = self.id[j]
                j -= 1
            self.id[j + 1] = location

        return self.id




    def shell_sort(self):
        """Shell sort also known as  or Shell's method, is an in-place comparison sort.
        It can be seen as either a generalization of sorting by exchange (bubble sort)
        or sorting by insertion (insertion sort).

        """
        n = len(self.id)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = self.id[i]
                j = i

                while j >= gap and self.id[j - gap] > temp:
                    self.id[j] = self.id[j - gap]
                    j -= gap

                self.id[j] = temp
            gap //= 2

        return self.id

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.id[i] < self.id[left]:
            largest = left

        if right < n and self.id[largest] < self.id[right]:
            largest = right

        if largest != i:
            self.id[i], self.id[largest] = self.id[largest], self.id[i]

            Sorting.heapify(self, n, largest)

    def heap_sort(self):
        """Heapsort is an improved selection sort: it divides its input into a sorted
        and an unsorted region, and it iteratively shrinks the unsorted region by
        extracting the largest element and moving that to the sorted region.

        """
        n = len(self.id)

        for i in range(n, -1, -1):
            Sorting.heapify(self, n, i)
        for i in range(n - 1, 0, -1):
            self.id[i], self.id[0] = self.id[0], self.id[i]
            Sorting.heapify(self, i, 0)

        return self.id

    def merge_sort(self):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        """
        if len(self.id) > 1:
            # FLOOR DIVISION
            mid = len(self.id) // 2
            # SPLIT THE ARRAY INTO TWO "EQUAL" SUBARRAYS
            L = self.id[:mid]
            R = self.id[mid:]
            # RECURSION TO GET TO LENGTH ONE, SO IT WILL BE NATURALLY SORTED
            Sorting.merge_sort(L)
            Sorting.merge_sort(R)

            # SETTING UP POINTERS FOR LEFT, RIGHT, AND THE FINAL ARRAY
            i = j = k = 0

            # CAN ONLY DO THIS AS LONG AS I AND J ARE LESS THAN THE LENGTHS OF THEIR RESPECTIVE ARRAYS
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    self.id[k] = L[i]
                    i = i + 1
                else:
                    self.id[k] = R[j]
                    j = j + 1
                k = k + 1

            while i < len(L):
                self.id[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                self.id[k] = R[j]
                j += 1
                k += 1

        return self.id

    def partition(self, low, high):
        i = low - 1
        pivot = self.id[high]

        for j in range(low, high):
            if self.id[j] <= pivot:
                i = i + 1
                self.id[i], self.id[j] = self.id[j], self.id[i]
        self.id[i + 1], self.id[high] = self.id[high], self.id[i + 1]
        return i + 1

    def sort(self, low, high):
        if high <= low:
            return
        temp = Sorting.partition(self, low, high)
        Sorting.sort(self, low, temp-1)
        Sorting.sort(self, temp + 1, high)

    def quick_sort(self):
        """Quicksort (sometimes called partition-exchange sort) is an efficient
        sorting algorithm. Developed by Tony Hoare in 1959. It is still a commonly
        used algorithm for sorting. When implemented well, it can be about two or
        three times faster than its main competitors, merge sort and heapsort.

        """
        random.shuffle(self.id)
        Sorting.sort(self, 0, len(self.id) - 1)

        return self.id

    # this plots things in log scale (pls google it), you need to add matplotlib
    # to your virtualenv first!

    # plot also python's sorted() function to see how well you do.
    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!



    # plt.plot(set_szs, timing)
    # plt.xscale('log')
    # plt.yscale('log')
    # plt.title('log')
    # plt.ylabel('some numbers')
    # plt.show()
