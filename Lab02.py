import random
import time


# Meh Method but it could be useful
# import timeit
# print("Stupid Max Sub Array - TimeIt")
# print(timeit.timeit(stupidMaxSubArray, number=100000)/100000)

# Task 3 - Max Sub Array -------------------------------------------------------
sizeOfList = 10**1
randomList = random.sample(range(-(sizeOfList*10),(sizeOfList*10)),sizeOfList)


# Last weeks implementation
givenList = [13, -3, -25, -20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

# The number of sub arrays is the triangle number relating to the length of the list
# This naive approach runs in O(n^3) time as it takes n time to calcualate the sumSubArray
#       and it takes n^2 time to run findSubarrays.
#       There is also time to sort the list at the end but that could run in a linear sweep theorecitcally
#           We could also keep track the maximum while we go too so that the whole thing is only n^3

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

print("Stupid Max Sub Array")
start = time.time()
print(stupidMaxSubArray())
end = time.time()
print(end - start)
