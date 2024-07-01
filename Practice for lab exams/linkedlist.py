class Node:
    def __init__(self,data) -> None:
        self.info=data
        self.nextnode=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def addToHead(self,data):
        if(self.head==None):
            newNode=Node(data)
            newNode.nextnode=None
            self.head=newNode
        else:
            newNode=Node(data)
            newNode.info=data
            newNode.nextnode=self.head
            self.head=newNode

    def traverse(self):
        startPoint=self.head
        while(startPoint!=None):
            print(startPoint.info)
            startPoint=startPoint.nextnode

list=LinkedList()
list.addToHead(5)
list.addToHead(10)
list.traverse()