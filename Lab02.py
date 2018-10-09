import random
import time
import sys
import timeit

# Meh Method but it could be useful
# print("Stupid Max Sub Array - TimeIt")
# print(timeit.timeit(stupidMaxSubArray, number=100000)/100000)

# Task 3 - Max Sub Array -------------------------------------------------------
# Constants
sizeOfList = 10**1
numberToAverage = 1000

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

def stupidMaxSubArray(array):
    allSubArrays = findSubarrays(array)
    allSubArrays.sort(key = takeThird, reverse = True)
    return allSubArrays[0]

def stupidMaxSubArrayRnd():
    rndList = random.sample(range(-sizeOfList,sizeOfList),sizeOfList)
    stupidMaxSubArray(rndList)

# O(n^2) implementation --------------------------------------------------------
def betterMaxSubArray(array):
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

def betterMaxSubArrayRnd():
    rndList = random.sample(range(-sizeOfList,sizeOfList),sizeOfList)
    betterMaxSubArray(rndList)

# Divide and Conquer implementation --------------------------------------------
def divAndConMaxSubArrayRnd():
    rndList = random.sample(range(-sizeOfList,sizeOfList),sizeOfList)
    divAndConMaxSubArraySetup(rndList)

def divAndConMaxSubArraySetup(array):
    return divAndConMaxSubArray(array, 0, len(array)-1)

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

# Timing Code ------------------------------------------------------------------
print("Size of problem %d" % sizeOfList)
print("Number to Average %d" % numberToAverage)

#Timing and solution for same problem
print("\n--------------------Fixed Problem--------------------")
setList = random.sample(range(-sizeOfList,sizeOfList),sizeOfList)

print("Stupid Max Sub Array")
start = time.time()
print(stupidMaxSubArray(setList))
end = time.time()
print(end - start)

print("O(n^2) Max Sub Array")
start = time.time()
print(betterMaxSubArray(setList))
end = time.time()
print(end - start)

print("Divide And Conquer Max Sub Array")
start = time.time()
print(divAndConMaxSubArraySetup(setList))
end = time.time()
print(end - start)

# Average timing over multiple runs and with random lists
print("\n----Average Timing w/ Random List | Over %d Runs-----" % numberToAverage)
print("Stupid Max Sub Array")
print(timeit.timeit(stupidMaxSubArrayRnd, number=numberToAverage)/numberToAverage)
print("Stupid Max Sub Array")
print(timeit.timeit(betterMaxSubArrayRnd, number=numberToAverage)/numberToAverage)
print("Stupid Max Sub Array")
print(timeit.timeit(divAndConMaxSubArrayRnd, number=numberToAverage)/numberToAverage)
