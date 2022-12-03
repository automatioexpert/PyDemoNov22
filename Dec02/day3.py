
name='VTU' #SyntaxError: unterminated string literal (detected at line 2)
#print(name[1000]) IndexError: string index out of range

print("My name is \"Ashish\"")
print('My name is \'Ashish\'')

name='My name is "Ashish"'
print(name) #My name is "Ashish"

name2=  """
    +====================================================================
              ||  PYTHON CODER - KEEP CALM AND CODE ||
    =====================================================================
"""

print(name2)

name3="My" \
      "name" \
      "is" \
      "Steve"
print(name3)

name4="My \nname \nis \nSteve"
print(name4)

"My name is steve"

name4="stevz"
print(name4[-1])
#print(name4[-100000]) #IndexError: string index out of range

print(name4[+3])

"""
String formatters

input-Input is a function used to take user input

String formatters type:
      format() method
      
      2.Operator 
      %d -->Integers
      %s -->Strings
      %f -->float
      
      3.f String methods
"""
print("My salary is Rs 10000000")

sal=input("Please enter your salary") #<class 'str'> By defualt everything is treated as a string
print(sal)
print("Salary is %s and address is %s" %(sal,"USA"))
print(type(sal))
print("My salary is : {0} and name is {1}".format(sal,"steve"))

print("Welecome to {a}".format(a="AutomationExpertWorld"))

print("My id is {0} and value is {1}".format("11002033974949479", 473734347437347))

a="Thank God"
print(f"My name is {a} and salary is {a}")









