import bisect
import random

# Task 1 - Reviewing Lists -----------------------------------------------------
# Append at beginning
a = [2,3,4,5]
a = [1] + a
print(a)
# Append at the end
b = [1,2,3,4]
b.append(5)
print(b)
# Concatenating lists
c1 = [1,2,3]
c2 = [4,5]
c3 = c1 + c2
print(c3)
# Inserting a new element into an ordered list
d = [1,2,4,5]
el = 3
bisect.insort(d, el)
print(d)

# Task 2 - Selection Sort ------------------------------------------------------
# Create a random list of 10 ints between 0 and 100
r = random.sample(range(1,100),10)
print(r)

# For all elements in the list loop
for j in range(0, len(r)):
    # Assume the min element is the first one you see
    minIndex = j
    for i in range(j+1, len(r)):
        if( r[i] < r[minIndex] ):
            minIndex = i
    if( minIndex != j ):
        r[j],r[minIndex] = r[minIndex],r[j]
print(r)

# Task 3 - Insertion Sort ------------------------------------------------------
# Create a random list of 10 ints between 0 and 100
r = random.sample(range(1,100),10)
print(r)

for i in range(1, len(r)):
    j = i
    for j in range(i, 0, -1):
        if( r[j-1] > r[j] ):
            r[j],r[j-1] = r[j-1],r[j]
print(r)

# Task 4 - Merge Sort ----------------------------------------------------------
# Create a random list of 10 ints between 0 and 100
r = random.sample(range(1,100),10)
print(r)

def mergeSort(list):
    # Base Case
    if( len(list) <= 1 ):
        return list
    # Reucursive Case
    listL = list[:len(list)//2]
    listR = list[len(list)//2:]
    listL = mergeSort(listL)
    listR = mergeSort(listR)
    return merge(listL, listR)

def merge(left, right):
    result = []
    while( (len(left) != 0) and (len(right) != 0) ):
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    #Add the rest of the lists to the result
    while( len(left) != 0 ):
        result.append(left.pop(0))
    while( len(right) != 0 ):
        result.append(right.pop(0))
    # Return the result
    return result

# Actually do the merge sort
rprime = mergeSort(r)
print(rprime)

# Task 4 - Quick Sort ----------------------------------------------------------
# Create a random list of 10 ints between 0 and 100
r = random.sample(range(1,100),10)
print(r)

def quickSort(list, lo, hi):
    if( lo < hi ):
        p = partition(list, lo, hi)
        quickSort(list, lo, p-1)
        quickSort(list, p+1, hi)

def partition(list, lo, hi):
    pivot = list[hi]
    i = lo
    for j in range(lo, hi):
        if( list[j] < pivot ):
            list[j],list[i] = list[i],list[j]
            i = i + 1
    list[hi],list[i] = list[i],list[hi]
    return i

#Actually do the quickSort
quickSort(r, 0, len(r)-1)
print(r)

# Task 5 - Max Sub Array -------------------------------------------------------
givenList = [13, -3, -25, -20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

# The number of sub arrays is the triangle number relating to the length of the list
# This naive approach runs in O(n^3) time as it takes n time to calcualate the sumSubArray
#       and it takes n^2 time to run findSubarrays.
#       There is also time to sort the list at the end but that could run in a linear sweep

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

allSubArrays = findSubarrays(givenList)
allSubArrays.sort(key = takeThird, reverse = True)
print(allSubArrays)
print(len(allSubArrays))
print(allSubArrays[0])
