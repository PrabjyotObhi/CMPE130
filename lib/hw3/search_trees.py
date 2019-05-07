
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