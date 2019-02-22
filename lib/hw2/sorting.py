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

    def merge(self, low, mid, high):
        temporary = mid - low + 1
        temporary2 = high - mid

        rightArray = [0] * temporary2
        leftArray = [0] * temporary

        for i in range(0, temporary):
            leftArray[i] = self.id[low + i]
        for i in range(0, temporary2):
            rightArray[i] = self.id[mid + 1 + i]

        first = second = 0
        combined = low

        while first < temporary and second < temporary2:
            if leftArray[first] <= rightArray[second]:
                self.id[combined] = leftArray[first]
                first += 1
            else:
                self.id[combined] = rightArray[second]
                second +=1
            combined += 1

        while first < temporary:
            self.id[combined] = leftArray[first]
            first += 1
            combined += 1

        while second < temporary2:
            self.id[combined] = rightArray[second]
            second += 1
            combined += 1

        return self.id

    def merge_together(self, low, high):
        if low < high:
            mid = round(((high - 1) + low)/2)
            Sorting.merge_together(self, low, mid)
            Sorting.merge_together(self, mid + 1, high)
            Sorting.merge(self, low, mid, high)
        return self.id

    def merge_sort(self):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        """
        Sorting.merge_together(self, 0, len(self.id) - 1)
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

if __name__ == "__main__":

    set_szs = [10]
    timing = [[], [], [], [], [], []]
    x = [10 ** i for i in range(1, 5)]
        # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in x:
            # initialize network nodes
        inodes = Sorting()
        inodes.sort_init(set_sz)

        t0 = time.time()

        inodes.selection_sort()

        t1 = time.time()

        total_time = t1 - t0

        timing[0].append(total_time)

        print(total_time)


    for set_sz in x:
            # initialize network nodes
        inodes = Sorting()
        inodes.sort_init(set_sz)

        t0 = time.time()

        inodes.insertion_sort()

        t1 = time.time()

        total_time = t1 - t0

        timing[1].append(total_time)

        print(total_time)
    for set_sz in x:
            # initialize network nodes
        inodes = Sorting()
        inodes.sort_init(set_sz)

        t0 = time.time()

        inodes.merge_sort()

        t1 = time.time()

        total_time = t1 - t0

        timing[2].append(total_time)

        print(total_time)
    for set_sz in x:
            # initialize network nodes
        inodes = Sorting()
        inodes.sort_init(set_sz)

        t0 = time.time()

        inodes.shell_sort()

        t1 = time.time()

        total_time = t1 - t0

        timing[3].append(total_time)

        print(total_time)
    for set_sz in x:
            # initialize network nodes
        inodes = Sorting()
        inodes.sort_init(set_sz)

        t0 = time.time()

        inodes.heap_sort()

        t1 = time.time()

        total_time = t1 - t0

        timing[4].append(total_time)

        print(total_time)
    for set_sz in x:
            # initialize network nodes
        inodes = Sorting()
        inodes.sort_init(set_sz)

        t0 = time.time()

        inodes.quick_sort()

        t1 = time.time()

        total_time = t1 - t0

        timing[5].append(total_time)

        print(total_time)

    plt.plot(x, timing[0], label="Selection_Sort")
    plt.plot(x, timing[1], label="Insertion_Sort")
    plt.plot(x, timing[2], label="Merge_Sort")
    plt.plot(x, timing[3], label="Shell_Sort")
    plt.plot(x, timing[4], label="Heap_Sort")
    plt.plot(x, timing[5], label="Quick_Sort")
    plt.legend()


    plt.xscale('log')
    plt.yscale('log')
    plt.title('log')
    plt.ylabel('some numbers')
    plt.show()
