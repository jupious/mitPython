class Test():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def printArgs(self):
        print("뭐가문제야",self.a,self.b)

testing = Test('say','something')
testing.printArgs()