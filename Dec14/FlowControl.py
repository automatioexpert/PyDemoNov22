"""
FLOW CONTROL:
Major categories:
1.Selection statements: If, else , if else, if elif, if elif else
2.Interactive statement: for loop , while loop
3.Transfer statement: break , continue
Note:No switch statement in python 3.9
"""

"""
If
    If the condition is true,Python will execute the if block or else it will skip it
    
    INDENTATION: They are the whitespaces which specifies the scope of the block
"""
a = 10
b = 20

if a > b:
    print("a is greater") #IndentationError: expected an indented block after 'if' statement on line 19
else:
    print("a is smaller")


print("This is regular code")
