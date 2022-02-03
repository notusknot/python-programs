import random, time

def bubbleSort(listToSort):
    passes = len(listToSort)-1
    while passes > 0:
       for i in range(passes):
           if listToSort[i] > listToSort[i+1]:
               temp = listToSort[i]
               listToSort[i] = listToSort[i+1]
               listToSort[i+1] = temp
       passes = passes-1

listToSort = []

for loop in range(1000):
    listToSort.append(random.randint(0,1000))

start = time.time()

bubbleSort(listToSort)

stop = time.time()

print(stop - start)
