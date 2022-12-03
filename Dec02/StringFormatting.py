
"""
a = input("Enter a")
b = input("Enter b")
c = a/b
print(f"Result is {c}") #TypeError: unsupported operand type(s) for /: 'str' and 'str'
"""
from builtins import float

a = float(input("Enter a")) #It should be typecasted to pick only integer
b = input("Enter b")
#c = a/b
#print(f"Result is {c}")

#print(10+"123")
print("10"+"10")

a="SteveJobs"
print(len(a))

"""
mul=19239
print(type(mul))
print(str(mul))
print(mul.lower())
print(mul.upper()) """

bb="sd334"
print(bb.isdigit())
bs=334364
print(bs.isDigit())

print("God" ==  "God")