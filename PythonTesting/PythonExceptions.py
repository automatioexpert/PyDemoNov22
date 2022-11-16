
itemsInCart=-2

#2 items will be added to the cart

if itemsInCart!=2: # raise Exception("VV raising exception for No items in cart")
    pass

#assert(itemsInCart == 0)

print("Exceptions AREA Restricted!!")

try:
    with open('read2.txt', 'r') as reader:
        print(reader.read())

except Exception as e:
    print("Executing except block Boss..FILE NOT FOUND!!!", e)

# try - catch - In python there is no catch block we have except block

finally:
    print("Finally..Cleaning up the resource ...Thank You God!!")






















