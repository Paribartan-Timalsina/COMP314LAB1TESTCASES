class Kruskals:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[]
    
    def add_edge(self,u,v,w):
        self.graph.append((u,v,w))

    def getEdge(self):
        return self.graph
    
    def make_set(self):
         self.sets = []
         for i in range(self.vertices):
          self.sets.append({i})

    def delete_set(self,graph):
        for s in self.sets:
            if graph in s:
             self.sets.remove(s)
    
    def find_set(self,graph):
        for s in self.sets:
            if graph in s:
                return s
        return None
    
    def union(self,vertex1,vertex2):
        x= self.find_set(vertex1)
        y= self.find_set(vertex2)
        z=x.union(y)
        self.delete_set(vertex1)
        self.delete_set(vertex2)
        self.sets.append(z)

    
    def kruskals_algo(self):
           self.A = []
           self.make_set()
           self.graph.sort(key=lambda x: x[2])
           self.sorted_order = self.graph
           for i in range(len(self.graph)):
                if(self.find_set(self.graph[i][0]) != self.find_set(self.graph[i][1])):
                     self.A.append(self.graph[i])
                     self.union(self.graph[i][0],self.graph[i][1])
           return self.A        

g = Kruskals(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)

print(g.getEdge())
print(g.kruskals_algo())
