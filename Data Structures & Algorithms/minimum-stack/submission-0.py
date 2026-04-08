class MinStack:    
    def __init__(self):
        self.elements = []
        self.extra = []
    def push(self, val: int) -> None:
        self.elements.append(val)
        if(len(self.extra) == 0 or val<self.extra[len(self.extra)-1]):
            self.extra.append(val)
        else:
            self.extra.append(self.extra[len(self.extra)-1])
    def pop(self) -> None:
        self.elements.pop()
    def top(self) -> int:
        return self.elements[len(self.elements)-1]
    def getMin(self) -> int:
        return self.extra[len(self.elements)-1]
#So if the size of extra isn't zero and 
# the value pushed onto the regular stack is less than the top of the 
#extra stack, then we want to push that passed value onto the top of both stacks.
#Otherwise, we want to keep on pushing the top of extra to the top of extra
#