from OopsPrinciples import ClassThree


class ChildClass(ClassThree):
    num4 = 200

    def __init__(self):
        ClassThree.__init__(self,2,10)
    def getCompleteData(self):
        return self.num4 + self.num3 + self.Summation()

obj1 = ChildClass()
print(obj1.getCompleteData())