from PythonTesting.OOPSDemo import Calculator


class ChildImpl(Calculator):
    num2 = 100

    def __int__(self):
        Calculator.__int__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


obj = ChildImpl(29,20)
obj.getCompleteData()
