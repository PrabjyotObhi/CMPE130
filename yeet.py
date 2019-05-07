def findWaitingTimeRR(process, n, burst, wait, quanta):
    cpy_burst = []

    for val in range(n):
        cpy_burst[val] = burst[val]

    time = 0
    while (True):
        done = True

        for val in range(n):
            if cpy_burst[val] > 0:
                done = False
                if cpy_burst[val] > quanta:
                    time += quanta
                    cpy_burst[val] -= quanta
            else:
                time = time + cpy_burst[val]
                wait[val] = time - burst[val]
                cpy_burst[val] = 0
        if done is True:
            break


def findTurnAroundTimeRR(process, n, burst, wait, totalTurnAroundT):
    for val in range(n):
        totalTurnAroundT[val] = burst[val] + wait[val]


def findAvgTimeRR(process, n, burst, quanta):
    wait = []
    turnAroundT = []

    totalWait = 0
    totalTurnAroundTime = 0

    findWaitingTimeRR(process, n, burst, wait, quanta)
    findTurnAroundTimeRR(process, n, burst, wait, turnAroundT)
    print("Processes ", " Burst time ", " Waiting time ", " Turn around time")

    for val in range(n):
        totalWait = totalWait + wait[val]
        totalTurnaAroundTime = totalTurnAroundTime + turnAroundT[val]
        print(" ", val + 1, "\t\t", burst[val], "\t", wait[val], "\t\t", turnAroundT[val])

    print("Average Waiting Time = ", totalWait / n)
    print("Average turn around time = ", totalTurnAroundTime / n)


processes = [1, 2, 3]
n = len(processes)
burst_time = [10, 5, 8]
quantum = 2
findAvgTimeRR(processes, n, burst_time, quantum)