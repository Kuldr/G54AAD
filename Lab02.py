import random
import time
import sys


# Meh Method but it could be useful
# import timeit
# print("Stupid Max Sub Array - TimeIt")
# print(timeit.timeit(stupidMaxSubArray, number=100000)/100000)

# Task 3 - Max Sub Array -------------------------------------------------------
sizeOfList = 10**3
randomList = random.sample(range(-(sizeOfList*10),(sizeOfList*10)),sizeOfList)


# Last weeks implementation ----------------------------------------------------
def sumSubArray(list, intial, final):
    sum = 0
    for i in range(intial, final+1):
        sum = sum + list[i]
    return sum

def findSubarrays(list):
    resultsArr = []
    resultsArr = [(i,j,sumSubArray(list, i, j)) for i in range(0, len(list)) for j in range(i, len(list))]
    return resultsArr

def takeThird(elem):
    return elem[2]

def stupidMaxSubArray():
    allSubArrays = findSubarrays(randomList)
    allSubArrays.sort(key = takeThird, reverse = True)
    return allSubArrays[0]

# print("Stupid Max Sub Array")
# start = time.time()
# print(stupidMaxSubArray())
# end = time.time()
# print(end - start)

# O(n^2) implementation --------------------------------------------------------
def betterMaxSubArray():
    array = randomList
    imax = jmax = 0
    maxSum = - sys.maxsize - 1 # -∞

    for i in range(0, len(array)):
        parSum = 0
        for j in range(i, len(array)):
            parSum = parSum + array[j]
            if parSum > maxSum:
                maxSum = parSum
                imax, jmax = i, j

    return(imax, jmax, sum(array[imax:jmax+1]))

print("\nBetter Max Sub Array")
start = time.time()
print(betterMaxSubArray())
end = time.time()
print(end - start)

# Divide and Conquer implementation --------------------------------------------
