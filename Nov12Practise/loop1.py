"""
FOR LOOP
--->Repetition statement performed on any type of sequence
--->Executing a group of statement multiple times
SEQUENCE-->string,list, tuple, dictionary,set and range()

SYNTAX: -->
    for x in sequence:
        ---------------------
        ---------------------

"""
loop = "Ashish"
i=0;
for x in loop: ## x is loop variable which is the value  not the index. Index is taken automatically
            #loop variable is the value in the sequence
    print(f"Index = {i} and value at index ={x}");
    i=i+1;
print("out of the loop")