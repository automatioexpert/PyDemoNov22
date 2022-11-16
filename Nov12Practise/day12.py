"""
Exception Handling:
-->Error is the super class. It is more of compile time issues
-->Exceptions are the logical errors which can be raised at the run time
"""
from builtins import ValueError

"""
try - except block
-->Statement which can raise the  exception  are kept inside the try block
-->Statement which can handle the exception are kept inside the except block

"""
try:
    amount1 = int(input("Enter the amount 1"))
    daysWorked = int(input("Enter the daysWorked"))
    totalSalary = amount1 / daysWorked  # ZeroDivisionError: division by zero
    print(totalSalary)  # ValueError: invalid literal for int() with base 10: ' Steve Jobs'

except  ZeroDivisionError as e:
    print("You are dividing the number")
    print(e.__traceback__())
    print(e.__str__())

except ValueError:
    print("Something went wrong ValueError")

else:
    print("I am the best Expert on the Planet...Thank God!!")

finally:
    print("No matter what...I am the World Champion...Thank God!!!!!!!!!!!")
print("This is the regular workflow of the code.")