class Stack:
    def __init__(self):
        self.array=[0]*100
        self.top_element=0
    
    def push(self,data):
        self.array[self.top_element]=data
        self.top_element+=1
    def pop(self):
        self.array[self.top_element]=0
        self.top_element-=1
    def top(self):
        return self.array[self.top_element]
    def isEmpty(self):
        if(self.top_element==0):
            return True
        else:
            return False

stack=Stack()
pattern="(()()()))"
for element in pattern:
    if(element=="("):
        stack.push(element)
    elif(element==")"):
        value=stack.top()
        if(value==")"):
            print("the pattern is unmatched")
            break
        else:
            stack.pop()
if(stack.isEmpty()):
    print("The pattern is matched")
else:
    print("Not")
        
    




