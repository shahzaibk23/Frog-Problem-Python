# Operations
class FrogProblem:

    def __init__(self, state, lst):
        self.lst = lst
        self.states = state

    def moveRight(self,i):
        self.states += 1
        self.lst[i],self.lst[i+1] = self.lst[i+1],self.lst[i]
        print(self.lst)

    def jumpRight(self,i):
        self.states += 1
        self.lst[i],self.lst[i+2] = self.lst[i+2],self.lst[i]
        print(self.lst)

    def moveLeft(self,i):
        self.states += 1
        self.lst[i],self.lst[i-1] = self.lst[i-1],self.lst[i]
        print(self.lst)

    def jumpLeft(self,i):
        self.states += 1
        self.lst[i],self.lst[i-2] = self.lst[i-2],self.lst[i]
        print(self.lst)

# STEPS

o = FrogProblem(0,[1,1,1,0,2,2,2])

print(f"Initital State: {o.lst}")

o.moveLeft(4)
o.jumpRight(2)
o.moveRight(1)
o.jumpLeft(3)
o.jumpLeft(5)
o.moveLeft(6)
o.jumpRight(4)
o.jumpRight(2)
o.jumpRight(0)
o.moveLeft(1)
o.jumpLeft(3)
o.jumpLeft(5)
o.moveRight(4)
o.jumpRight(2)
o.moveLeft(3)

print(f"Final State: {o.lst}")
print(f"No of States: {o.states}")

