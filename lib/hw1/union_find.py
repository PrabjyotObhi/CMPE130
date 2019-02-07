# Prabjyot CMPE130

# 1. quick-find
# 2. quick-union
# 3. weighted QU
# 4. QU + path compression
# 5. weighted QU + path compression

import time
import random
import matplotlib.pyplot as plt


class UF(object):
    """Union Find class

    """

    def __init__(self):
        self.id = []
        self.sz = []

    def qf_init(self, N):
        """initialize the data structure

        """
        for x in range(N):
            self.id.append(x)
        self.sz = [1] * N

    def qf_union(self, p, q):
        """Union operation for Quick-Find Algorithm.

        connect p and q. You need to
        change all entries with id[p] to id[q]
        (linear number of array accesses)

        """
        pid = self.id[p]
        qid = self.id[q]
        for x in range(len(self.id)):
            if self.id[x] is pid:
                self.id[x] = qid
        return 1

    def qf_connected(self, p, q):
        """Find operation for Quick-Find Algorithm.
        simply test whether p and q are connected

        """
        # if they are connected the values in them should be equal
        return self.id[p] == self.id[q]

        return True

        # qu_find Function
    def qu_find(self, i):
        while i != self.id[i]:
            i = self.id[i]

        return i

        # qu_union function
    def qu_union(self, p, q):
        """Union operation for Quick-Union Algorithm.
         connect p and q.

         """
        i = self.qu_find(p)
        j = self.qu_find(q)
        self.id[i] = j
        return 1

    def qu_connected(self, p, q):
        """Find operation for Quick-Union Algorithm.
         test whether p and q are connected

         """
        return self.id[p] == self.id[q]

    # weighted quick union uses the same find as quick union
    def wqu_union(self, p, q):
        """Union operation for Weighted Quick-Union Algorithm.
         connect p and q.

         """
        i = self.qu_find(p)
        j = self.qu_find(q)
        if i == j:
            return;

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            id[j] = i
            self.sz[i] += self.sz[j]

        return 1

    def wqu_connected(self, p, q):
        """Find operation for Weighted Quick-Union Algorithm.
         test whether p and q are connected

         """
        i = self.pq_find(p)
        j = self.pq_find(q)
        return i is j


    # Need a new path compression find function
    def pq_find(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        return i

    # pqunion uses the new pq_find function with the logic from qu
    def pqu_union(self, p, q):
        """Union operation for path compressed Quick-Union Algorithm.
         connect p and q.

         """
        i = self.pq_find(p)
        j = self.pq_find(q)
        self.id[i] = j
        return 1

    def pqu_connected(self, p, q):
        """Find operation for path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        return self.id[p] == self.id[q]

    # weighted quick union process with the path compression find function

    def wpqu_union(self, p, q):
        """Union operation for Weighted path compressed Quick-Union Algorithm.
         connect p and q.

         """
        i = self.pq_find(p)
        j = self.pq_find(q)
        if i == j:
            return;

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

        return 1


    def wpqu_connected(self, p, q):
        """Find operation for Weighted path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        return self.id[p] == self.id[q]


if __name__ == "__main__":

    # iteration
    set_szs = [10]
    timing = []

    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            inodes.qf_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!

    plt.plot(set_szs, timing)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('log')
    plt.ylabel('some numbers')
    plt.show()
