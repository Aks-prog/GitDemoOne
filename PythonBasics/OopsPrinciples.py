# Classes are user defined blueprint or prototype.
# Classes have methods, class variables, instance variables, constructor,etc.
# self keyword is mandatory for calling variables in methods.
# Instance and Class variables have whole different purpose.
# Constructor name should be '__init__'.
# 'new' keyword is not required when we create object.

class ClassOne:
    num1 = 100 # class variable

    def getData1(self):
        print("I am now executing as method in class.")

class ClassTwo:
    num2 = 100

    def __init__(self): # Constructor
        print("I am called automatically when object is created.")

    def getData2(self):
        print("I am now executing as method in class.")

class ClassThree():
    num3 = 100

    def __init__(self, a, b): # Parameterized Constructor
        self.firstNumber = a # instance variable
        self.secondNumber = b # instance variable
        print("I am called automatically when object is created.")

    def Summation(self):
        return self.firstNumber + self.secondNumber + ClassThree.num3

obj1 = ClassOne() # syntax to create objects in Python.
obj1.getData1()
print(obj1.num1)

obj2 = ClassTwo()
obj2.getData2()

obj3 = ClassThree(2,3)
print(obj3.Summation())

obj4 = ClassThree(4,5)
print(obj4.Summation())