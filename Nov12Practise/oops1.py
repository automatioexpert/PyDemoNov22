"""
OOPS concepts:
-->Procedural language
-----------------
-----------------
-----------------
-----------------

Object-Oriented programming
->Class
->Objects
->Constructors
->Inheritance
->Polymorphism
->Encapsulation
->Abstract Class


"""
"""
Class:
-->It is a blueprint that is used to create objects 
-->It is the logical representation of the Object 
-->A class is used to represent the properties and actions
-->Properties are variables
-->Actions are declared as methods

Syntax:
class <className>:
    ---------------------
    ---------------------
    ---------------------
    
"""


class car:
    """
    This is the documentation for the car class
    """

    def __int__(self,carColor,carsType,carWheels):
        self.carColor=carColor
        self.carsType=carsType
        self.carWheels=carWheels



    def carSeats(self):
        print("The car seats are 360 degree rotatable")

    def carType(self):
        print("The car tyres are always puncture free")

    def carRadio(self):
        print("The car have the best radio in the town")

#car1 object
car1 = car()
car1.carSeats()
car1.carType()
car1.carRadio()
car1.carRadio()
print(f"The car style is {car1.carsType} carColor ={car1.carColor} carWheel={car1.carWheels} carType={car1.carTypes}")

print("-------------------------------------------------------------")
#car2 object
car2 = car()
car2.carSeats()
car2.carType()
car2.carRadio()
car2.carRadio()
print(f"The car style is {car2.carsType} carColor ={car2.carColor} carWheel={car2.carWheels} carType={car2.carTypes}")
