"""
Datastructures:
List
Dictionary
Tuple
Set
"""
#Which is true and false

a=['Bill','Gates']
b=a
c=['Gates','Bill']

print(a==b)
print(a is b)

print(a==c)
print(a is c)

print("===========================")
d="steve"
e="steve"
print(id(d))
print(id(e))

#Check if each word in the string begins with a capital letter
aa="Thank God"
ab="Thank god"
print(aa.istitle())
print(ab.istitle())

#How to find the index of the first occurences of a string in a string
ac="This is Python and Python"
print(ac.find("Pythons"))


#Count the number of specific characters
ad="There are sea shells in the sea shores"
print(ad.count("s"))

#Uppercase the first and last characters of the string
ae="abhishekss"
print(ae[0].upper()+ae[1:-1]+ae[-1].upper())

#Replace each word with a new word "AutomationPower"
af="Hi my name is my name is my name is"
af=af.replace('name',"AutomationPower78")
print(af)

#Replace each character with a given character
ag="My favorite fruits is Mango. I love to visit the farms"
print(ag.replace("a","1").replace("i","2").replace("f","3"))



