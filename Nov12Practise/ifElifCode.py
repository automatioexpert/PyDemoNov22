"""
if elif statement
if the given condtion is true, execute the block.
Otherwise  move to the next conditional  block
if
elif <condition>
    ----------------
    ----------------
elif <condition>
    ----------------
    ----------------

elif <condition>
    ----------------
    ----------------


"""
marks = 10
if marks > 90:
    print("Student passed with flying colors")
elif 80 <= marks <= 90:
    print("B+")

elif 70 < marks < 80:
    print("C+")

elif 60 < marks < 70:
    print("D+")
else:
    print("You are pagla and hence failed with marks !",marks)

print("Regular statement")

























