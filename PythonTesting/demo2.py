values = [1, 23, 3838, "Bill Gates", 5, 399]

print(values[0])
print(values[3])
print(values[-1])
print(values[1:3])
values.insert(3, "Steve Jobs")
print(values[3])
values.append("Mark")
print(values)  # [1, 23, 3838, 'Steve Jobs', 'Bill Gates', 5, 399, 'Mark']
del(values[0])
print(values)

print("=========================================")

# Dictionary
dic = {"a": 2, 4: "bcd", "c": "hello world"}
print(dic)
print(dic["c"])
print(dic[4])

print("=======================================")
dict = {}
dict["firstname"]="Rahul"
dict["lastname"]="Kumar"
print(dict)