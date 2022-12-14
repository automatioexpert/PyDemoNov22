"""
Built in Functions

"""
L = [1, 2, 3, 4, 50, 6, 7, 8, 9]
print(L)

# Find the length
print(len(L))

# Maximum in the list
print(max(L))

print("========================")
K = ['1', '2', '3', '4', '5', '6']

# Print maximum in the list
print(max(K))

M = ['Ashish', 'Zebra', 'Priti', 'Ravi', 'Bhuvan']
print(max(M))

# Minimum in the list
print(min(M))

# How to sort  a list
print(sorted(M))
print(sorted(M))

# How to sort a list (Ascending order)
print(sorted(L))
print(sorted(M))

# Convert a string into a list
N = "Abhishek"
print(N)

print('------------------')
# Verify the list contains True values
# Any->It return true if even one item in the list is True
# True=1,False=0
P = ["", "", 2 > 1, "Ashish", 1, 2, 3]
print(any(P))

# Verify the list contains no null values or all true values
Q = ["", "", 100]
print(all(Q))

# Add one item in the end of the list
R = [1, 2, 3, 4, 5, 6]
R.append(10000000)
R.append("VVPyTest")
print(R)

print(any(R))
print(any([]))

