from math import ceil
from operator import itemgetter



class MinHeap:
    
    elementOfGraph = []

    def insert(self, element):
        
        self.elementOfGraph.append(element)
        self.elementOfGraph = sorted(self.elementOfGraph, key=itemgetter(1))

    def existing(self, findElement):
       
        for n in self.elementOfGraph:
            if n[0] == findElement:
                return True

        return False

    def pop(self):
        if len(self.elementOfGraph) > 0:
            result = self.elementOfGraph.pop(0)
            self.elementOfGraph = sorted(self.elementOfGraph, key=itemgetter(1))
            return result
        else:
            return None

    def updateWeight(self, target_node, d_value):
        
        if self.existing(target_node):
            for n in self.elementOfGraph:
                if n[0] == target_node:
                    n[1] = d_value
        self.elementOfGraph = sorted(self.elementOfGraph, key=itemgetter(1))


class Graph:
    graph_stru = []
    no_vertices = 0
    no_edges = 0

    
    def __init__(self, vertices, edges):
        self.no_nodes = vertices
        self.no_edges = edges
        for num in range(1, vertices + 1):
            self.graph_stru.append([])

    def addEdge(self, start, end, weight):
        self.graph_stru[start-1 ].append([end-1, weight])
        self.graph_stru[end-1 ].append([start-1 , weight])
        

    def print(self):
        for n in self.graph_stru:
            print(n)

    def findMaximumEdge(self):
        
        weights = []
        for n in self.graph_stru:
            for e in n:
                weights.append(e[1])

        
        newWeights = sorted(weights, reverse=True)
        if len(newWeights) > 0:
            return newWeights[0]
        else:
            return -1

    def getPosibleweight(self, source, dest):
        for e in self.graph_stru[source - 1]:
            if e[0] == dest - 1:
                return e[1]

        return -1

    def dijkstra(self, source, dest):
        
        maxEdge = self.findMaximumEdge() + 1

        for n in self.graph_stru:
            for e in n:
                e[1] = maxEdge - e[1]

        
        heap = MinHeap()
       
        
        currentDestAmount = []

        for num in range(len(self.graph_stru)):
            if source - 1 == num:
                heap.insert([source - 1, 0])
                currentDestAmount.append([0, 0])
            else:
                heap.insert([num, maxEdge * self.no_edges])
                currentDestAmount.append([-1, maxEdge * self.no_edges])

        process = []

        while len(process) < len(self.graph_stru):
            node = heap.pop()
            for edge in self.graph_stru[node[0]]:
                
                if heap.existing(edge[0]) and node[1] + edge[1] < currentDestAmount[edge[0]][1]:
                    currentDestAmount[edge[0]][1] = node[1] + edge[1]  
                    currentDestAmount[edge[0]][0] = node[0]  
                    heap.updateWeight(edge[0], currentDestAmount[edge[0]][1])

            process.append(node)

        
        for n in self.graph_stru:
            for e in n:
                e[1] = maxEdge - e[1]

        
        found = False
        tWeight = []
        nodePath = []
        finalNode = dest - 1
        nodePath.append(finalNode + 1)
        while True:
            parent = currentDestAmount[finalNode][0]
            tWeight.append(self.getPosibleweight(parent + 1, finalNode + 1))
            nodePath.append(parent + 1)

            if parent == source - 1:
                break
            finalNode = parent

        
        for i in range(len(nodePath) - 1, -1, -1):
            print(nodePath[i], end=" ")

        print()
       
        mini = min(tWeight)
        print(int(ceil(125 / mini)))



foreignStudents = int(input("Enter the number of foreign students: "))
aiesecStudents = int(input("Enter the number of AIESEC students: "))

n,r = input().split(" ")
n = int(n)
r = int(r)

newGraph = Graph(n, r)

    
for n in range(1, r + 1):
    start,end,weight = input().split(" ")
    start = int(start)
    end = int(end)
    weight = int(weight)
       
    newGraph.addEdge(start, end, weight)


source,dest,w = input().split(" ")
source = int(source)
dest = int(dest)
newGraph.dijkstra(source, dest)

