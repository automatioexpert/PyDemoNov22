"""
Functions
-->Sequence of statement in a particular order , given a specific name
    function1
    --------------
    --------------
    --------------
    --------------
    ->Reusability- user can re-use  the group of statement multiple times
    print("Ashish")
    Syntax: def is a pre defined keyword
     def functionName():
        ------------------
        ------------------
        ------------------
There are two types of function:
1.Built in function - print() , len(),id()
->These are not defined by user but instead defined by programming language itself

2.User defined function



"""


# Defining or declaring a function
def hello():
    # This is called function documentation

    """
    This is a hello function written by Valmiki Vishwakarma Automation Expert
    :return: void
    """
    print("Hello God...I am executing the function!!")


# When we have to use we need to call the function explicitely
hello()
hello()
hello()


#The parameter acts as an input to the function
#While defining they are called parameter
#The parameter can be of any value type
def calculate(a,b):
    """
    This is addition
    :param a:This is the first number to be added
    :param b:This is the second number to be added
    :author: Valmiki Vishwakarma
    :return:
    """


    c = a + b
    print(c)


calculate(1,3) # while calling they are called arguments
calculate(10,30) # while calling they are called arguments
calculate("Steve","Jobs")
calculate('Bill','Gates')
calculate([1,2,3],[4,5,6])
calculate("Valmiki","10Crore")
calculate("Valmiki",'10000000')

#PYTHON is a generic language
#No matter means wherever u are on the code
#u can define any function, variable or a class anywhere
#We have NO restriction that it should be in the starting

"""
RETURN STATEMENT
output of one function as an input to another
"""
