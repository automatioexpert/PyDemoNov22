file = open('read.txt')
# Read all content of the file

# print(file.read(-6))
#line = file.readline()

#while line != "":
  #  print(line)
  #  line = file.readline()

for line in file.readlines():
    print(line)


