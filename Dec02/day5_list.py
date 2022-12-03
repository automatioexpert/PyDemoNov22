"""
LIST
    Holds a sequence of values
-->In a list order is preserved
-->Duplicate values are allowed
-->Should be inside [] -->Square brackets
-->Heterogenous values are alloweds
-->Indexing is applicable
-->Slicing is applicable
-->List is mutable in nature means we can perform  CREATE,READ,UPDATE AND DELETE
--()->paranthesis
[]-->Square brackets
{}-->Curley brackets

"""

# How to create a list
aa = ["Ashish", "1ME10EC078", 12, 50.5, True, 10 + 3j, [1, 2, 3, 4, 5]]
print(type(aa))
print(aa)
# Create an empty list
ab = []
print(ab)

# How to access / read a list
# Using index
print(aa[0])
# print(aa[100]) IndexError: list index out of range
# print(aa[2.38]) TypeError: list indices must be integers or slices, not float

print("----------------------------------")
print(aa[6][1])

for i in aa:
    print(i)

# Reassigning a list -->Updating a list
# Whenever we are reassigning a list.It creates a completely new memory location
aa = [2, 3, 4, 4, 5, 5, 99, "Steve Jobs", 38434.34384, 38348 + 348834j]
print(aa)
print(id(aa))

aa = ["Avi", "Don Breckenrdge", "Adam"]
print(aa)
print(id(aa))

# Concatenation
cd = [1, 2, 3, 4, 5]
ef = [6, 7, 8, 9, 10]
print(cd + ef)

# Multiplication -->Repetition

gh = ["Adam", 1]
print(gh * 10)  # print given list 10 times

# Multiplication
ij = [1, 2, 3, 4, 5]
print(11 in ij)  # False
print(11 not in ij)  # True

# Iterating a list
"""
sequence-->Sequence can be list, tuple,string,dictionary,set
for <var> in <sequence>
    ------------------------------
    ------------------------------
"""

kl = [1, 2, 3, 4, 5, "A", "B", "C"]

for k in kl:  # Value of k increments automatically
    print(k)

mn = [1, 2, 3, 4, 5, 6, 7, 8]
for i in mn:
    if i % 2 == 0:
        print("Even number: " + i)
    else:
        pass
        #print("Odd number: " + i)
