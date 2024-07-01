import sys
class Graph:
    def __init__(self,vertices) -> None:
        self.vertices=vertices
        self.graph=[]
    
    def find_min_key(self,key,mstSet):
        min=sys.maxsize
        min_index=0
        for i in range(self.vertices):
            if(key[i]<min and mstSet[i]==False):
                min=key[i]
                min_index=i
        return min_index

    
    def primMST(self):
        key=[sys.maxsize]*self.vertices
        parent=[None]*self.vertices
        key[0]=0
        parent[0]=-1
        mstSet=[False]*self.vertices
        for v in range(1,self.vertices):
            min_vertex=self.find_min_key(key,mstSet)
            mstSet[min_vertex]=True
            for adj_vertices in range(self.vertices):
                if(self.graph[min_vertex][adj_vertices]>0 and mstSet[adj_vertices]==False and self.graph[min_vertex][adj_vertices]<key[adj_vertices]):
                    key[adj_vertices]=self.graph[min_vertex][adj_vertices]
                    parent[adj_vertices]=min_vertex


        print(parent)
            







g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
g.primMST()
