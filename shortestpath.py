from collections import defaultdict
from queue import PriorityQueue 

class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v,w):
        self.graph[u].append([v,w]) 
  
    def UCS(self, start, goal):
        q = PriorityQueue()
        path = {}
        visited = []
        q.put((0, start, start))

        while q:
            top = q.get()
            visited.append(top[1])
            if top[1] not in path:
                path[top[1]] = top[2]

            if top[1] == goal:
                res = []
                i = goal
                while i != start:
                    res.append(i)
                    i = path[i]
                res.append(start)
                res.reverse()
                return top[0], res

            for node in self.graph[top[1]]:
                if node not in visited:
                    q.put((top[0]+node[1], node[0], top[1]))
            
g = Graph()
g.addEdge('A', 'B', 4)
g.addEdge('A', 'C', 1)
g.addEdge('B', 'D', 3)
g.addEdge('B', 'E', 8)
g.addEdge('C', 'D', 2)
g.addEdge('C', 'F', 6)
g.addEdge('D', 'E', 4)
g.addEdge('E', 'G', 2)
g.addEdge('F', 'G', 8)
 
print ("Uniform Cost Search: ")
start = 'A'
end = 'G'
minCost, path = g.UCS(start, end)
print("Minimum cost from %s to %s => " % (start,end), minCost)
print("Path of traversal => ", path)
