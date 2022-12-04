"""
Built in methods to help manipulating a list
"""
cars = [ "bmw", "honda", "audi"]
lengthOfCars=len(cars)
print(lengthOfCars)

#Append method is used to add values to a given list

cars.append("Benz")
print(cars)

cars.insert(1,"Jeep") #['bmw', 'honda', 'audi', 'Benz']
print(cars) #['bmw 0', 'Jeep 1', 'honda 2', 'audi 3', 'Benz 4
y = cars.pop()# ']

x = cars.index("honda")
print(x)


y = cars.pop()
print(y)
print(cars)

cars.remove("Jeep")
print(cars)

slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)

print("*#"*20)
print(cars)
cars.sort()

print(cars)

