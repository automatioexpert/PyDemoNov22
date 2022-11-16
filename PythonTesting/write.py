#read the file and store and store all the lines in a list
#reverse the list
#write the list back to the file

with open('read.txt','r') as reader:
    content=reader.readlines()
    reversed(content)

    with open('read.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)
