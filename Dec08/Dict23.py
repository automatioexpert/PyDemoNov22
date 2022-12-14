db1={1:2,2:3,3:"Steve Jobs"}
#Delete a specific value:
print(db1)
del db1[1]
print(db1)

"""
In Built functions in Dictionary

"""

db2={1:2,-1:9,2:3,3:4,-9999:10000000}
print(len(db2))
print(any(db2))
print(all(db2))
print(sorted(db2))
