from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, s):
        visited=[False]*(max(self.graph)+1)
        q=[]
        q.append(s)
        visited[s]=True
        while q:
            s=q.pop(0)
            print(s,end="  ")
            for i in self.graph[s]:
                if visited[i]==False:
                    visited[i]=True
                    q.append(i)
    
    def DFS(self, s):
        visited=[False]*(max(self.graph)+1)
        self.DFSUtil(s,visited)
    
    def DFSUtil(self, s, visited):
        visited[s]=True
        print(s, end="  ")

        for i in self.graph[s]:
            if visited[i]==False:
                self.DFSUtil(i, visited)


g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print("BFS from vertex 2: ",end="")
g.BFS(2)
print("\nDFS from vertex 2: ", end="")
g.DFS(2)