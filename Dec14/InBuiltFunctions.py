"""
IN BUILT FUNCTIONS / METHODS IN DICTIONARY
"""
db1 = {1: 22, 2: 5, 3: 4, 5: 100}
print(db1.keys()) #dict_keys([1, 2, 3, 5])
print(type(db1)) #<class 'dict'>

print(sorted(db1))
print(db1.values()) #Print all the values
print(db1.get(1)) #22
print(db1.get(500,"NOT FOUND!!")) #NOT FOUND!!
#print(db1.clear())
print(db1)

db2=db1.copy()
print(db2)
db1.pop(5)
print(db1)

db1.pop(5,"NOT FOUND")
print(db1)