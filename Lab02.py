import random
import time
import sys
import timeit

# Meh Method but it could be useful
# print("Stupid Max Sub Array - TimeIt")
# print(timeit.timeit(stupidMaxSubArray, number=100000)/100000)

# Task 3 - Max Sub Array -------------------------------------------------------
# Constants
sizeOfList = 10**9
numberToAverage = 100
doFixedTiming = True
doAverageTiming = False

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

# Linear implementation --------------------------------------------------------
def linearMaxSubArrayRnd():
    rndList = random.sample(range(-sizeOfList,sizeOfList),sizeOfList)
    linearMaxSubArray(rndList)

def linearMaxSubArray(array):
    i = iMax = jMax = 0
    maxSum = - sys.maxsize - 1
    # Considering 1 element at a time
    for j in range(0, len(array)):
        # newElement on its own
        elemAloneSum = array[j]
        # subArray with new element (only if the element can be added to subArray)
        if( jMax+1 == j ):
            subWithNewElem = maxSum + array[j]
        else:
            subWithNewElem = - sys.maxsize - 1

        if( (elemAloneSum >= maxSum) and (elemAloneSum >= subWithNewElem) ):
            iMax, jMax, maxSum = j, j, elemAloneSum
        elif( (subWithNewElem >= maxSum) and (subWithNewElem >= elemAloneSum) ):
            jMax, maxSum = j, subWithNewElem

    return(iMax, jMax, maxSum)

# Kadane's implementation ------------------------------------------------------
def kadaneMaxSubArrayRnd():
    rndList = random.sample(range(-sizeOfList,sizeOfList),sizeOfList)
    kadaneMaxSubArray(rndList)

def kadaneMaxSubArray(array):
    maxEndSum = maxBest = - sys.maxsize - 1
    maxEndi = maxEndj = maxBesti = maxBestj = 0
    for j in range(0, len(array)-1):
        # find the max sub array ending at j
        if( array[j] >= maxEndSum + array[j] ):
            maxEndSum = array[j]
            maxEndi = maxEndj = j
        else:
            maxEndSum = maxEndSum + array[j]
            maxEndj = j
        # find the max array so far
        if( maxEndSum >= maxBest ):
            maxBest = maxEndSum
            maxBesti = maxEndi
            maxBestj = maxEndj

    return (maxBesti, maxBestj, maxBest)

# Timing Code ------------------------------------------------------------------
print("Size of problem %d" % sizeOfList)
print("Number to Average %d" % numberToAverage)

startAll = time.time()

#Timing and solution for same problem
if( doFixedTiming ):
    print("\n--------------------Fixed Problem--------------------")
    setList = random.sample(range(-sizeOfList//2,sizeOfList//2),sizeOfList)

    # print("Stupid Max Sub Array")
    # start = time.time()
    # print(stupidMaxSubArray(setList))
    # end = time.time()
    # print(end - start)
    # print("O(n^2) Max Sub Array")
    # start = time.time()
    # print(betterMaxSubArray(setList))
    # end = time.time()
    # print(end - start)
    # print("Divide And Conquer Max Sub Array")
    # start = time.time()
    # print(divAndConMaxSubArraySetup(setList))
    # end = time.time()
    # print(end - start)
    # print("Linear Max Sub Array")
    # start = time.time()
    # print(linearMaxSubArray(setList))
    # end = time.time()
    # print(end - start)
    print("Kadane's Max Sub Array")
    start = time.time()
    print(kadaneMaxSubArray(setList))
    end = time.time()
    print(end - start)

# Average timing over multiple runs and with random lists
if( doAverageTiming ):
    print("\n----Average Timing w/ Random List | Over %d Runs-----" % numberToAverage)
    # print("Stupid Max Sub Array")
    # print(timeit.timeit(stupidMaxSubArrayRnd, number=numberToAverage)/numberToAverage)
    # print("O(n^2) Max Sub Array")
    # print(timeit.timeit(betterMaxSubArrayRnd, number=numberToAverage)/numberToAverage)
    # print("Divide And Conquer Max Sub Array")
    # print(timeit.timeit(divAndConMaxSubArrayRnd, number=numberToAverage)/numberToAverage)
    # print("Linear Max Sub Array")
    # print(timeit.timeit(linearMaxSubArrayRnd, number=numberToAverage)/numberToAverage)
    print("Kadane's  Max Sub Array")
    print(timeit.timeit(kadaneMaxSubArrayRnd, number=numberToAverage)/numberToAverage)

endAll = time.time()
print("\nTotal Runtime = %d" % (endAll - startAll))
