
import time
import random


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
        if (self.root is None):
            self.init_bst(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if self.root is None:
            self.root = val
        else:
            if self.root.val < val:
                if self.root.right is None:
                    self.root.right = val
                else:
                    self.insertNode(self, self.root.right, val)
            else:
                if self.root.left is None:
                    self.root.left = val
                else:
                    self.insertNode(self, self.root.left, val)


        return False

    def bsearch(self, val):
        if self.root is None or self.root.val == val:
            return self.root
        if self.root.val < val:
            return self.bsearch(self.root.right, val)
        return self.bsearch(self.left, val)

        return False

    def searchNode(self, current, val):

        return False

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

    def is_red(self, current):
        if current is None:
            return False
        return current.color

        return False

    def rotate_left(self, current):
        x = self.current.right
        self.current.right = x.left
        x.left = current
        x.color = current.color
        current.color = RED
        return x


        return False

    def rotate_right(self, current):
        x = current.left
        current.left = x.right
        x.right = current
        x.color = current.color
        current.color = RED
        return x

        return False

    def flip_colors(self, current):
        current.color = RED
        current.left.color = BLACK
        current.right.color = BLACK

        return False

    def insert(self, val):
        if (self.root is None):
            self.init_rbbst(val, RED)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):




        return False

    def bsearch(self, val):

        return False

    def searchNode(self, current, val):

        return False

if __name__ == "__main__":


    set_sz = 10
    tut = BST()

    vals = random.sample(range(1, 100), set_sz)

    for idx in range(set_sz - 1):

        tut.insert(vals[idx])

    print (tut.bsearch(vals[1]))
    print(tut.bsearch(11))

    tut_rb = RBBST()

    for idx in range(set_sz - 1):

        tut_rb.insert(vals[idx])

    print (tut.bsearch(vals[1]))
    print(tut.bsearch(11))