class Animal:
    def PRINT(self):
        print("class Animal called")

class Fish(Animal):
    def __init__(self):
        super().__init__()#super refers to the inherited class
    def PRINTF(self):
        print("class Fish called")

a = Fish()
a.PRINTF()
a.PRINT()
