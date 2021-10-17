from collections import defaultdict

theGraph = [
    ('A', 'B', 15),
    ('A', 'D', 19),
    ('A', 'C', 10),
    ('B', 'D', 7),
    ('C', 'D', 16),
    ('B', 'E', 17),
    ('D', 'E', 12),
    ('C', 'F', 14),
    ('D', 'G', 3),
    ('D', 'F', 6),
    ('F', 'G', 9),
    ('E', 'G', 20),
    ('E', 'H', 13),
    ('F', 'I', 5),
    ('G', 'H', 4),
    ('G', 'I', 1),
    ('G', 'J', 11),
    ('H', 'J', 2),
    ('I', 'J', 18),
]

# Structure for cycle-detection
class Graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self,v,visited,parent):
        visited[v]= True
        for i in self.graph[v]:
            if  visited[i]==False :
                if(self.isCyclicUtil(i,visited,v)):
                    return True
            elif  parent!=i:
                return True
        return False

    def isCyclic(self):
        visited =[False]*(self.V)
        for i in range(self.V):
            if visited[i] ==False:
                if(self.isCyclicUtil(i,visited,-1)) is True:
                    return True
        return False

def checkCycle(theGraph):
    numberOfPoints = []
    for i in theGraph:
        numberOfPoints.append(i[0])
        numberOfPoints.append(i[1])
    suchAList = list(set(numberOfPoints))
    theGraphMap = {}
    for i in range(len(suchAList)):
        theGraphMap[suchAList[i]] = i
    numberOfPoints = len(suchAList)
    g = Graph(numberOfPoints)
    for i in theGraph:
        g.addEdge(theGraphMap[i[0]], theGraphMap[i[1]])
    return g.isCyclic()

theGraph2 = [
    ('A', 'D', 19),('D', 'G', 3),('G', 'J', 11)
]

def kruskalMST(graph):

    # Sort based on weight
    graph = sorted(graph, key=lambda item: item[2])
    theMinimumSpan = []
    for i in graph:
        theMinimumSpan.append(i)
        if checkCycle(theMinimumSpan):
            theMinimumSpan.pop()

    return theMinimumSpan

theRequiredMST = kruskalMST(theGraph)
print(theRequiredMST)

theCost = 0
for i in theRequiredMST:
    theCost += i[2]
print("The cost is "+str(theCost))