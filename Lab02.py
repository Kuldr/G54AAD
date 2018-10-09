import random
import time
import sys

# Meh Method but it could be useful
# import timeit
# print("Stupid Max Sub Array - TimeIt")
# print(timeit.timeit(stupidMaxSubArray, number=100000)/100000)

# Task 3 - Max Sub Array -------------------------------------------------------
sizeOfList = 10**4
randomList = random.sample(range(-sizeOfList,sizeOfList),sizeOfList)


# Last weeks implementation ----------------------------------------------------
def sumSubArray(array, intial, final):
    sum = 0
    for i in range(intial, final+1):
        sum = sum + array[i]
    return sum

def findSubarrays(array):
    resultsArr = []
    resultsArr = [(i,j,sumSubArray(array, i, j)) for i in range(0, len(array)) for j in range(i, len(array))]
    return resultsArr

def takeThird(elem):
    return elem[2]

def stupidMaxSubArray():
    allSubArrays = findSubarrays(randomList)
    allSubArrays.sort(key = takeThird, reverse = True)
    return allSubArrays[0]

print("Stupid Max Sub Array")
start = time.time()
print(stupidMaxSubArray())
end = time.time()
print(end - start)

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

print("\nO(n^2) Max Sub Array")
start = time.time()
print(betterMaxSubArray())
end = time.time()
print(end - start)

# Divide and Conquer implementation --------------------------------------------
def divAndConMaxSubArraySetup():
    return divAndConMaxSubArray(randomList, 0, len(randomList)-1)

def divAndConMaxSubArray(array, low, high):
    if( low == high ):
        return(low, high, array[low])
    else:
        mid = (low+high)//2
        (leftLow, leftHigh, leftSum) = divAndConMaxSubArray(array, low, mid)
        (rightLow, rightHigh, rightSum) = divAndConMaxSubArray(array, mid+1, high)
        (crossLow, crossHigh, crossSum) = maxCrossingSubArray(array, low, mid, high)
        if( (leftSum >= rightSum) and (leftSum >= crossSum) ):
            return (leftLow, leftHigh, leftSum)
        elif( (rightSum >= leftSum) and (rightSum >= crossSum) ):
            return (rightLow, rightHigh, rightSum)
        elif( (crossSum >= leftSum) and (crossSum >= rightSum) ):
            return (crossLow, crossHigh, crossSum)

def maxCrossingSubArray(array, low, mid, high):
    leftSum = - sys.maxsize - 1
    sum = 0
    maxLeft = 0
    for i in range(mid, low-1, -1):
        sum = sum + array[i]
        if( sum > leftSum ):
            leftSum = sum
            maxLeft = i
    rightSum = - sys.maxsize - 1
    sum = 0
    maxRight = 0
    for j in range(mid+1, high+1):
        sum = sum + array[j]
        if( sum > rightSum ):
            rightSum = sum
            maxRight = j
    return(maxLeft, maxRight, leftSum+rightSum)

print("\nDivide And Conquer Max Sub Array")
start = time.time()
print(divAndConMaxSubArraySetup())
end = time.time()
print(end - start)
