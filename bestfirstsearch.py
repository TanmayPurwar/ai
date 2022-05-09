from collections import defaultdict
from queue import PriorityQueue 

class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)
 
 
    def addEdge(self,u,v):
        self.graph[u].append([v]) 
  
    def BFS(self, start, goal, hn):
        q = PriorityQueue()
        path = {}
        visited = []
        q.put((hn[start], start, start))

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
                return res

            for node in self.graph[top[1]]:
                if node not in visited:
                    q.put((hn[node[0]], node[0], top[1]))
            

g = Graph()


print ("Best First Search: ")
g.addEdge('S', 'A')
g.addEdge('S', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('B', 'E')
g.addEdge('B', 'F')
g.addEdge('E', 'A')
g.addEdge('F', 'I')
g.addEdge('F', 'G')

hn = {'S': 13, 'A': 12, 'B': 4, 'C': 7, 'D': 3, 'E': 8,
            'F': 2, 'H': 4, 'I': 9, 'G': 0}
            
start = 'S'
end = 'G'

path = g.BFS(start, end, hn)
print("Shortest path of traversal => ", path)
