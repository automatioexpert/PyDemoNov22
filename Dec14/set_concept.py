"""
SET
1.Set is also used to represent a key value pair
2.Order is not preserved
3.Indexing and slicing is not allowed
4.Heterogenous objects are not allowed
5.Mutable in nature (Can update a Set)
6.Set is represented by using a {} curley braces
7.We cannot create an empty set without using a set function
8.We can add the elements in the Set using the add method
9.DUPLICATE Keys are not allowed
10.Key values pairs are not there

List: [1,2,3,4,5]
Set: {1,2,3,4,5}

"""
a = {1, 2, 3, 4, 5}  # <class 'set'>
print(type(a))

"""
Creating an empty set 
"""
# Empty set
db = set()
print(type(db))

# Set using values
s1 = {1, 2, 3, 4, 5}
print(type(s1))  # <class 'set'>

# Set using the Set function
li = [1, 2, 4, 5, 6, 9]  # Convert list to Set
set2 = set(li)
print(set2)
print(type(set2))

dup={1,3,4,4,5,6,6,9,"Abegail",True}
print(dup)
print(type(dup))
dup.discard(100)
dup.remove(2)

"""
NESTED SET IS NOT ALLOWED
dup2={1,2,3,
    {
        1,4,5,6,100
        


    }


}
print(dup2)

"""