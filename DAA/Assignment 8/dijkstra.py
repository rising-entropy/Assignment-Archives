# Dijkstra's algorithm is very similar to Prim's algo.
# We shall make use of the same code with the modification 
# for the path finding between the 2 nodes

def checkIfPointAlreadyExists(theSP, thePoint):
    theListOfPoints = []
    for i in theSP:
        theListOfPoints.append(i[0])
        theListOfPoints.append(i[1])
    theListOfPoints = list(set(theListOfPoints))
    if thePoint in theListOfPoints:
        return True
    return False

theGraph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('A', 1), ('C', 1), ('E', 2), ('D', 3)],
    'C': [('A', 2), ('B', 1), ('D', 1), ('E', 2)],
    'D': [('B', 3), ('C', 1), ('E', 4), ('F', 3)],
    'E': [('C', 2), ('B', 2), ('D', 4), ('F', 3)],
    'F': [('D', 3), ('E', 3)]
}

def nextBestEdge(theGraph, theSP):

    # we only look for the possible edges of previous destination
    theListOfPoints = []
    theListOfPoints.append(theSP[len(theSP)-1][1])
    theListOfEdges = []
    for i in theListOfPoints:
        for j in theGraph[i]:
            theListOfEdges.append((i, j[0], j[1]))
    theListOfEdges = sorted(theListOfEdges, key=lambda item: item[2])
    for i in theListOfEdges:
        if not checkIfPointAlreadyExists(theSP, i[0]):
            return i
        if not checkIfPointAlreadyExists(theSP, i[1]):
            return i

theSP = []

def dijkstrasAlgo(theGraph, theSP, source, destination):
    if len(theSP) == 0:
        edgesOfSource = []
        for i in theGraph[source]:
            edgesOfSource.append((source, i[0], i[1]))
        edgesOfSource = sorted(edgesOfSource, key=lambda item: item[2])
        theSP.append(edgesOfSource[0])
    elif len(theSP) == len(theGraph) - 1:
        return theSP
    elif theSP[len(theSP)-1][1] == destination:
        return theSP
    else:
        theSP.append(nextBestEdge(theGraph, theSP))
    return dijkstrasAlgo(theGraph, theSP, source, destination)

# Source and Destination
source = 'A'
destination = 'F'

theRequiredMST = dijkstrasAlgo(theGraph, theSP, source, destination)
print(theRequiredMST)

theCost = 0
for i in theRequiredMST:
    theCost += i[2]
print("The cost is "+str(theCost))