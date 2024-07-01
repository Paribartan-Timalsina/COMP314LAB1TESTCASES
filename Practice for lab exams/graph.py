class Node:
    def __init__(self,data) -> None:
        self.info=data
        self.sideNodes=None
        self.downNodes=None

class AdjacencyList:
    def __init__(self) -> None:
        self.head=None

    def traverse(self):
        startPoint = self.head
        while startPoint is not None:
            print(f"Vertex {startPoint.info}: ", end="")
            sidePointer = startPoint.sideNodes
            while sidePointer is not None:
                print(f" -> {sidePointer.info}", end="")
                sidePointer = sidePointer.sideNodes
            print()
            startPoint = startPoint.downNodes
    
    def createdownList(self,data):
        if(self.head==None):
            newNode=Node(data)
            newNode.sideNodes=None
            newNode.downNodes=None
            self.head=newNode
        else:
            newNode=Node(data)
            newNode.info=data
            startPointer=self.head
            while(startPointer.downNodes!=None):
                startPointer=startPointer.downNodes
            startPointer.downNodes=newNode
            newNode.downNodes=None
            newNode.sideNodes=None

    def createsideList(self,data1,data2):
        startPointer=self.head
        while(startPointer!=None):
            if(startPointer.info==data1):
                break
            startPointer=startPointer.downNodes
        if startPointer is None:
            print(f"Vertex {data1} not found.")
            return
        
        newSideNode = Node(data2)
        newSideNode.info=data2
        if startPointer.sideNodes is None:
            
            startPointer.sideNodes = newSideNode
        else:
            sidePointer = startPointer.sideNodes
            while sidePointer.sideNodes is not None:
                sidePointer = sidePointer.sideNodes
            sidePointer.sideNodes = newSideNode
       
vertices=[1,2,3,4]
graph=[(1,2),(2,3),(3,4),(1,4),(2,4)]
list=AdjacencyList()

for element in vertices:
    list.createdownList(element)

for element in graph:
    list.createsideList(element[0],element[1])

list.traverse()