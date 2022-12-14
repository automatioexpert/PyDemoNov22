"""
Tuple-->
1.Called as Read only version of List
2.IMMUTABLE in nature (CRUD (Update) operations cannot be performed)
3.Order is preserved
4.Duplicate values are allowed
5.These are represented by ()
6.Hetergeneous objects are allowed
7.Indexing and slicing operations are allowed

"""
# How to create a tupe
a = (2, 3, 4, 5, "929", "Simon", 2382.2883, True, 2 + 283j)
print(type(a))
print(a)  # (2, 3, 4, 5, '929', 'Simon', 2382.2883, True, (2+283j))

# Tuple Packing - It automatically adds a parenthesis ()
print("==========================")
B = 1, 2, 4, 5.934, "Abhishek", 23832.347384
print(type(B))
print(B)

# Tuple Unpacking
C = (1, 3, 4, 5, 6, 9, "Steve")
a, b, c, d, d, e, f = C
print(C)

D= (1,)
print(type(D))





