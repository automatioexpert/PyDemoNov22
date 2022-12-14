# List Concepts:

# Add an item at a specicific position
R = [1, 3, 5, 0, 4, 78]
print(R)
R.insert(200, "Steve Jobs")
print(R)

# Add an item in the end of the list
R.append("Bill Gates")
print(R)

# Remove the first instance of the item from the list
R.remove(4)
print(R)
# Remove the element at a specific position
R.pop(-5)
print(R)

# Clear all the values from the list
# R.clear()
print(R)

# Find the first matching index of an item
S = [1, 2, 3, "Steve", 4, 9, 6, 2, 'Simon']
# S.index("Ashish")

print(S)

# Sorting a list
print("My Life is sorted")
# print(S.sort())

a = [1, 0, -2, 6, 5, 4]
print(a.sort())

# Reverse a list
a = a.reverse();
print(a)
