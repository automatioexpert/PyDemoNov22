class Calculator:
    num = 100

    # default constructor - if we dnt defined any constructor , default constructor is called

    def __int__(self):
        print("No params contructor is called!!")

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically---Constructor")

    def getData(self):
        print('I am now executing method in class')

    def summation(self):
        return self.firstNumber + self.secondNumber+self.num


obj = Calculator(0,0)  # Syntax to create object in python =>Contructor is called only when we create the object
obj.getData()
print(obj.num)

print('======================')
obj2 = Calculator(4, 5)  # Syntax to create object in python =>Contructor is called only when we create the object
obj2.getData()
print(obj2.num)
a = obj2.summation()
print("Summation is : ", a)

