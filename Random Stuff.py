import random


def readFile(file):
    lines = open(file).read().splitlines()
    string = []
    processID = []
    action = []
    pagesRequired = []
    for val in range(len(lines)):
        temp = lines[val].split(' ')
        string.append(temp)

    for val in range(len(string)):
        if len(string[val]) is 2:
            processID.append(int(string[val][0]))
            action.append(string[val][1])
            pagesRequired.append(0)

        elif len(string[val]) is 3:
            processID.append(int(string[val][0]))
            action.append(string[val][1])
            pagesRequired.append(int(string[val][2]))
        else:
            print("Invalid Data")

    return [processID, action, pagesRequired]

def MemorySwapRand(file):
    pid, action, pages = readFile(file)
    physicalAddress = ["X"] * 20
    virtualAddress = {}
    physicalAddressIndex = -1
    notFull = False
    random.seed(9001)
    swap = {}

    for val in range(len(pid)):
        # Determine if the physical address list is full
        for j in range(len(physicalAddress)):
            if physicalAddress[j] == "X":
                notFull = True
                break
            else:
                notFull = False

        # Deal with the 2 actions that are not R,W, or A
        if action[val] is 'T':
            # Deletes pids from the virtual address tables,
            del virtualAddress[pid[val]]
            # need to check if the pid has a physical address in swap
            if pid[val] in swap:
                del swap[pid[val]]

            for j in range(len(physicalAddress)):
                if physicalAddress[j] == pid[val]:
                    physicalAddress[j] = "X"

        if action[val] is 'C':
            continue;

        # If the list is not full, we can go ahead and insert them into the physicalAddresses
        if notFull:
            # Determine the type of Action
            if action[val] is 'A':
                # Allocates the amount of pages to a pid
                for i in range(pages[val]):
                    # Modulus to implement the circular aspect of the list
                    virtualAddress[pid[val]] = val + random.randint(0, 10000)
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    while physicalAddress[physicalAddressIndex] != "X":
                        physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    physicalAddress[physicalAddressIndex] = pid[val]

            if action[val] is 'W':
                for i in range(pages[val]):
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    while physicalAddress[physicalAddressIndex] != "X":
                        physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    physicalAddress[physicalAddressIndex] = pid[val]

            if action[val] is 'R':
                for i in range(pages[val]):
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    while physicalAddress[physicalAddressIndex] != "X":
                        physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    physicalAddress[physicalAddressIndex] = pid[val]
        else:
            if action[val] is 'A':
                # Allocates the amount of pages to a pid
                for i in range(pages[val]):
                    # Modulus to implement the circular aspect of the list on a randomIndex
                    # need to implement a swap portion here
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    randIndex = random.randint(0, 100) % 20
                    swap[physicalAddress[randIndex]] = randIndex
                    physicalAddress[randIndex] = pid[val]

            if action[val] is 'W':
                for i in range(pages[val]):
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    randIndex = random.randint(0, 100) % 20
                    swap[physicalAddress[randIndex]] = randIndex
                    physicalAddress[randIndex] = pid[val]

            if action[val] is 'R':
                for i in range(pages[val]):
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    randIndex = random.randint(0, 100) % 20
                    swap[physicalAddress[randIndex]] = randIndex
                    physicalAddress[randIndex] = pid[val]
    return[physicalAddress, virtualAddress, swap]

def Max (a, b):
    if a > b:
        max = a
    if b > a:
        max = b
    if a is b:
        max = a
    return max

def MemorySwapFifo(file):

    pid, action, pages = readFile(file)
    physicalAddress = ["X"] * 20
    virtualAddress = {}
    physicalAddressIndex = -1
    notFull = False
    random.seed(9001)
    swap = {}
    FIFOIndex = 0

    for val in range(len(pid)):
        # Determine if the physical address list is full
        for j in range(len(physicalAddress)):
            if physicalAddress[j] == "X":
                notFull = True
                break
            else:
                notFull = False

        # Deal with the 2 actions that are not R,W, or A
        if action[val] is 'T':
            # Deletes pids from the virtual address tables,
            del virtualAddress[pid[val]]
            # need to check if the pid has a physical address in swap
            if pid[val] in swap:
                del swap[pid[val]]

            for j in range(len(physicalAddress)):
                if physicalAddress[j] == pid[val]:
                    physicalAddress[j] = "X"
                    FIFOIndex = Max(FIFOIndex, j)

        if action[val] is 'C':
            virtualAddress[pid[val]] = val + random.randint(0, 10000)

        # If the list is not full, we can go ahead and insert them into the physicalAddresses

        if notFull:
            # Determine the type of Action
            if action[val] is 'A':
                # Allocates the amount of pages to a pid
                for i in range(pages[val]):
                    # Modulus to implement the circular aspect of the list
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    while physicalAddress[physicalAddressIndex] != "X":
                        physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    physicalAddress[physicalAddressIndex] = pid[val]

            if action[val] is 'W':
                for i in range(pages[val]):
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    while physicalAddress[physicalAddressIndex] != "X":
                        physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    physicalAddress[physicalAddressIndex] = pid[val]

            if action[val] is 'R':
                for i in range(pages[val]):
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    while physicalAddress[physicalAddressIndex] != "X":
                        physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    physicalAddress[physicalAddressIndex] = pid[val]
        else:
            if action[val] is 'A':
                # Allocates the amount of pages to a pid
                for i in range(pages[val]):
                    # Modulus to implement the circular aspect of the list on a randomIndex
                    # need to implement a swap portion here

                    FIFOIndex = (FIFOIndex + 1) % 20
                    swap[physicalAddress[FIFOIndex]] = FIFOIndex
                    physicalAddress[FIFOIndex] = pid[val]

            if action[val] is 'W':
                for i in range(pages[val]):
                    FIFOIndex = (FIFOIndex + 1) % 20
                    swap[physicalAddress[FIFOIndex]] = FIFOIndex
                    physicalAddress[FIFOIndex] = pid[val]

            if action[val] is 'R':
                for i in range(pages[val]):
                    FIFOIndex = (FIFOIndex + 1) % 20
                    swap[physicalAddress[FIFOIndex]] = FIFOIndex
                    physicalAddress[FIFOIndex] = pid[val]

    return [physicalAddress, virtualAddress, swap]

def MemorySwapLRU(file):
    pid, action, pages = readFile(file)
    physicalAddress = ["X"] * 20
    virtualAddress = {}
    physicalAddressIndex = -1
    notFull = False
    random.seed(9001)
    swap = {}
    LRUIndex = 0
    count = 0
    IndexA = {" "}
    indexAfinal = [ ]
    IndexA.remove(" ")
    for val in range(len(action)):
        if action[val] is 'A':
            IndexA.add(val)

    for val in IndexA:
        indexAfinal.append(val)

    for val in range(len(pid)):
        # Determine if the physical address list is full
        for j in range(len(physicalAddress)):
            if physicalAddress[j] == "X":
                notFull = True
                break
            else:
                notFull = False

        # Deal with the 2 actions that are not R,W, or A
        if action[val] is 'T':
            # Deletes pids from the virtual address tables,
            del virtualAddress[pid[val]]
            # need to check if the pid has a physical address in swap
            if pid[val] in swap:
                del swap[pid[val]]

            for j in range(len(physicalAddress)):
                if physicalAddress[j] == pid[val]:
                    physicalAddress[j] = "X"

        if action[val] is 'C':
            virtualAddress[pid[val]] = val + random.randint(0, 10000)

        # If the list is not full, we can go ahead and insert them into the physicalAddresses

        if notFull:
            # Determine the type of Action
            if action[val] is 'A':
                # Allocates the amount of pages to a pid
                for i in range(pages[val]):
                    # Modulus to implement the circular aspect of the list
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    while physicalAddress[physicalAddressIndex] != "X":
                        physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    physicalAddress[physicalAddressIndex] = pid[val]

            if action[val] is 'W':
                for i in range(pages[val]):
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    while physicalAddress[physicalAddressIndex] != "X":
                        physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    physicalAddress[physicalAddressIndex] = pid[val]

            if action[val] is 'R':
                for i in range(pages[val]):
                    physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    while physicalAddress[physicalAddressIndex] != "X":
                        physicalAddressIndex = (physicalAddressIndex + 1) % 20
                    physicalAddress[physicalAddressIndex] = pid[val]
        else:
            if action[val] is 'W':
                if len(indexAfinal)>= 0:
                    physicalAddress[indexAfinal[count]] = pid[val]
                    del indexAfinal[count]
                    count = count + 1
                else:
                     LRUIndex = (LRUIndex + 1) % 20
                     swap[physicalAddress[LRUIndex]] = LRUIndex
                     physicalAddress[LRUIndex] = pid[val]

            if action[val] is 'R':
                 if len(indexAfinal)>= 0:
                     physicalAddress[indexAfinal[count]] = pid[val]
                     del indexAfinal[count]
                     count = count + 1
                 else:
                      LRUIndex = (LRUIndex + 1) % 20
                      swap[physicalAddress[LRUIndex]] = LRUIndex
                      physicalAddress[LRUIndex] = pid[val]

            if action[val] is 'A':
                LRUIndex = (LRUIndex + 1) % 20
                swap[physicalAddress[LRUIndex]] = LRUIndex
                physicalAddress[LRUIndex] = pid[val]
    return [physicalAddress, virtualAddress, swap]

pid, vadress, swap = MemorySwapFifo("memory.dat")

