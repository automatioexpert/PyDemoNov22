name = "Valmiki Vishwakarma"
i = 0
for x in name:
    # print(f"index = {i} and value = {x}")
    i = i + 1
# print("I am the top expert on the Planet..Thank God!!")

"""
index = 0 and value = V
index = 1 and value = a
index = 2 and value = l
index = 3 and value = m
index = 4 and value = i
index = 5 and value = k
index = 6 and value = i
index = 7 and value =  
index = 8 and value = V
index = 9 and value = i
index = 10 and value = s
index = 11 and value = h
index = 12 and value = w
index = 13 and value = a
index = 14 and value = k
index = 15 and value = a
index = 16 and value = r
index = 17 and value = m
index = 18 and value = a
I am the top expert on the Planet..Thank God!!

"""
# In the above example sequence was the string

# Sequence => Sequence = LIST

j = 0
for b in ["steve", 1, 3, 4, 6, True, [8, 834, 384489, 84834999], "Bill gates"]:
    # print(f"index ={j} and value ={b}")
    # print(b.upper())
    j += 1
# SEQUENCE --> TUPLE () ,In Tuple values are placed inside brackets
for c in (1, 3, 5, 5.99, [1, 2, 5], "Ashish"):
    print(c)
# SEQUENCE -->DICTIONARY
d = {
    1: "Ashish",
    "name": 2
}

"""
Range:
1.range(n)-->This reprsents numbers from 0 to n-1
2.range(m,n)-->This represents  numbers from 0 to n-1
3.range(m,n,inc/dec)

break:break statement is used to break the statement when condition is satisfied
continue : skip the current execution iteration

"""
for k in range(20,40,2):
    if k == 36:
        continue
    print(k)
else:
    print("I am only executed when the loop is completed")

print("Complete loop is executed...Thank God!!")

