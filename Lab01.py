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
# Create a random list of 100 ints between 0 and 10
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
        r[j],r[minIndex]=r[minIndex],r[j]
print(r)

# Task 3 - Insertion Sort ------------------------------------------------------
# Create a random list of 100 ints between 0 and 10
