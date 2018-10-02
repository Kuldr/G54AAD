import bisect

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
