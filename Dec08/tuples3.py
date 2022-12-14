
#HOW TO READ/ACCESS A TUPLE
E=(1,2,3,4,5,"Ashish",True)
print(E)
print(E[0])
print(E[1])
print(E[1:3:1])

#HOW TO UPDATE A TUPLE
#E[1]=100 #TypeError: 'tuple' object does not support item assignment
#print(E) #TypeError: 'tuple' object does not support item assignment

"""
In tuple values cannot be updated. It is not allowed.
But in List the values can be updated
Tuple is just read only which means we can store values which are constant and cannot be updated
If we try to update the values in Tuple , We get the TypeError at the Run Time
So, if we want to have the constant values which should be used across then we can go for Tuple
TUPLE--> TUPLE IS IMMUTABLE IN NATURE - SINCE TUPLE CANNOT BE MODIFIED
"""

#How to delete a tuple
del E
#print(E) #NameError: name 'E' is not defined -->Because the values are deleted completely so we are getting this error

E=(1,200)
del[E[0]] #TypeError: 'tuple' object doesn't support item deletion
print(E)
