
import time
import random
import matplotlib.pyplot as plt

class Array_Search:
    def __init__(self, array):
        self.array = array

    def init_array_search(self, val_array):
        self.array = Array_Search(val_array)

    def squential_search(self, key):

        idx = 0
        for num in self.array:
            if num == key:
                return idx
            idx = idx+1
        return False

    def bsearch(self, val):
        first = 0
        last = len(self.array)

        while first <= last:
            mid = (last - first) / 2
            if self.array[mid] == val:
                return mid
            if self.array[mid] > val:
                last = mid - 1
            else:
                first = mid + 1

        return False


class BST_Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def init_bst(self, val):
        self.root = BST_Node(val)

    def insert(self, val):
        # non-recursive
        if (self.root == None):             # if no value already assigned for root, initialize the node with value
            self.init_bst(val)
        else:
            self.insertNode(self.root, val) # otherwise insert as a new node

    def insertNode(self, current, val):
        # recursive function
        # to begin inserting as a new node, we make sure we are inserting in correct place
        # and that value is not already held in another node

        if val == current.val:
            print("Value in tree already, unable to add to tree")
        elif val < current.val:                       # if our val is less than current nodes value, go left
            if current.left == None:                # if current.left node is empty, make new node there
                current.left = BST_Node(val)
            else:                                   # else, recursively call setting left node to new current node
                self.insertNode(current.left, val)
        # we found that val is greater than current value, so go right
        # same procedure taken if on right side of tree
        else:
            if current.right == None:
                current.right = BST_Node(val)
            else:
                self.insertNode(current.right, val)

    def search(self, val):
        # non-recursive
        if self.root != None:                           # if root is has a value, call recursive search function
            return self.searchNode(self.root, val)
        else:                                           # else, tree is empty
            print("Empty tree")

    def searchNode(self, current, val):
        # recursive function
        if val == current.val:                              # if value is found at current location, return the value
            return current
        elif val > current.val and current.right != None:   # if value is greater than current location, and right child occupied,
            return self.searchNode(current.right, val)      # recursively call on right side
        elif val < current.val and current.left != None:    # if not greater or equal, must be less than. recursively call on left side
            return self.searchNode(current.left, val)

    def delete(self, val):
        if val < self.root.val:
            self.root.left = self.delete(self.root.left, val)
        elif val > self.root.val:
            self.root.right = self.delete(self.root.right, val)
        else:
            if self.root.left is None:
                temp = self.root.right
                self.root.right = None
                return temp
            elif self.root.right is None:
                temp = self.root.left
                self.root.left = None
                return temp
            while self.temp.left is not None:
                self.temp = self.temp.left

        return False

class RBBST_Node:
    def __init__(self, val, color):
        self.val = val
        self.left = None
        self.right = None
        self.color = color


RED = True
BLACK = False


class RBBST:
    def __init__(self):
        self.root = None

    def init_rbbst(self, val, color):
        self.root = RBBST_Node(val, color)

    @staticmethod
    def is_red(current):
        red = False
        if current:
            red = current.color == RED
        return red

    def rotate_left(self, current):
        x = current.right
        current.right = x.left
        x.left = current

        x.color = current.color
        current.color = RED

    def rotate_right(self, current):
        x = current.left
        current.left = x.left
        x.right = current

        x.color = current.color
        current.color = RED

    def flip_colors(self, current):
        current.right.color = current.color
        current.color = current.left.color
        current.left.color = current.right.color

    def insert(self, val):
        if self.root is None:
            self.init_rbbst(val, RED)
        else:
            self.root = self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if current is None:
            return RBBST_Node(val, RED)

        if val == current.val:
            return current
        elif val > current.val:
            current.right = self.insertNode(current.right, val)
        else:
            current.left = self.insertNode(current.left, val)

        if self.is_red(current.right) and not self.is_red(current.left):
            self.rotate_left(current)
        if self.is_red(current.left) and self.is_red(current.left.left):
            self.rotate_right(current)
        if self.is_red(current.left) and self.is_red(current.right):
            self.flip_colors(current)
        return current

    def bsearch(self, val):
            return self.searchNode(self.root, val)

    def searchNode(self, current, val):
        if current is None:
            return None

        if val > current.val:
            return self.searchNode(current.right, val)
        elif val < current.val:
            return self.searchNode(current.left, val)
        else:
            return current.val


if __name__ == "__main__":

    set_s = 10
    tut = BST()

    vals = random.sample(range(1, 100), set_s)

    set_szz = 10
    set_szs = [10 ** 1, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
    bst = []
    rbbst = []
    bs = []

    for set_sz in set_szs:
        vals = random.sample(range(1, set_sz * 10), set_sz)
        sort = sorted(vals)
        array_object = Array_Search(sort)



    tut_bst = BST()
    for idx in range(set_szz):
        tut_bst.insert(vals[idx])
    for set_sz in set_szs:
        # vals = random.sample(range(1, 100), set_szz)
        vals = random.sample(range(1, set_sz * 10), set_sz)
        # initialize network nodes
        inodes = BST()

        inodes.init_bst(set_sz)

        t0 = time.time()

        inodes.search(vals[set_sz - 1])

        t1 = time.time()

        total_time = t1 - t0

        bst.append(total_time)

    print("BST search time:  " + str(bst[0]))

    tut_rbbst = RBBST()
    for idx in range(set_szz):
        tut_rbbst.insert(vals[idx])
    for set_sz in set_szs:
        # initialize network nodes
        # vals = random.sample(range(1, 100), set_szz)
        vals = random.sample(range(1, set_sz * 10), set_sz)
        inodes = RBBST()
        inodes.init_rbbst(set_sz, RED)

        t0 = time.time()

        inodes.bsearch(vals[set_sz - 1])

        t1 = time.time()

        total_time = t1 - t0

        rbbst.append(total_time)

    print("RBBST search time:  " + str(rbbst[0]))

    plt.plot(set_szs, bst, label='BST', marker='o')
    plt.plot(set_szs, rbbst, label='RBBST', marker='o')

    plt.xscale('log')
    plt.yscale('log')
    plt.title('Different Run Times')
    plt.ylabel('Run Time')
    plt.xlabel('10 ^ i')
    plt.legend()
    plt.show()