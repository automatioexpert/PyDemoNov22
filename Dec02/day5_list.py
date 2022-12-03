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

#How to create a list
aa=["Ashish","1ME10EC078",12,50.5,True,10+3j,[1,2,3,4,5]]
print(type(aa))
print(aa)
#Create an empty list
ab=[]
print(ab)

#How to access / read a list
#Using index
print(aa[0])
#print(aa[100]) IndexError: list index out of range
#print(aa[2.38]) TypeError: list indices must be integers or slices, not float

print(aa[6][1])
