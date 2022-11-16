"""
return- Exit the current function  and hand back the output  to the caller
return statements are the last statement in the function
and since return statements are the last statements in the function and so exits the function then and there.
It is not important,that all function should have some value
By default , value none is returned
"""


def calculate(a, b):
    return a + b


print("The addition of number is: ", calculate(10, 29))

print("==========================================================================")

def addition(a, b):
    """
    This function performs the addition and return the sum
    :param a: first parameter
    :param b: second parameter
    :return: sum
    """
    c = a + b
    return c


print("The addition of the number is : ", addition(10, 30))
