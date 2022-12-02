
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