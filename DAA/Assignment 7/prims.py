def checkIfPointAlreadyExists(theMST, thePoint):
    theListOfPoints = []
    for i in theMST:
        theListOfPoints.append(i[0])
        theListOfPoints.append(i[1])
    theListOfPoints = list(set(theListOfPoints))
    if thePoint in theListOfPoints:
        return True
    return False

theGraph = {
    'A': [('B', 15), ('C', 10), ('D', 19)],
    'B': [('A', 15), ('D', 7), ('E', 17)],
    'C': [('A', 10), ('D', 16), ('F', 14)],
    'D': [('B', 7), ('A', 19), ('C', 16), ('F', 6), ('E', 12), ('G', 3)],
    'E': [('B', 17), ('D', 12), ('G', 20), ('H', 13)],
    'F': [('C', 14), ('D', 6), ('G', 9), ('I', 5)],
    'G': [('E', 20), ('D', 3), ('F', 9), ('H', 4), ('J', 11), ('I', 1)],
    'H': [('E', 13), ('J', 2), ('G', 4)],
    'I': [('F', 5), ('G', 1), ('J', 18)],
    'J': [('H', 2), ('G', 11), ('I', 18)]
}

# Lets assume we start with A
theMST = []

def nextBestEdge(theGraph, theMST):
    theListOfPoints = []
    for i in theMST:
        theListOfPoints.append(i[0])
        theListOfPoints.append(i[1])
    theListOfPoints = list(set(theListOfPoints))
    theListOfEdges = []
    for i in theListOfPoints:
        for j in theGraph[i]:
            theListOfEdges.append((i, j[0], j[1]))
    theListOfEdges = sorted(theListOfEdges, key=lambda item: item[2])
    for i in theListOfEdges:
        if not checkIfPointAlreadyExists(theMST, i[0]):
            return i
        if not checkIfPointAlreadyExists(theMST, i[1]):
            return i

def primsAlgo(theGraph, theMST):
    if len(theMST) == 0:
        # Assume A to be starting point
        edgesOfA = []
        for i in theGraph['A']:
            edgesOfA.append(('A', i[0], i[1]))
        edgesOfA = sorted(edgesOfA, key=lambda item: item[2])
        theMST.append(edgesOfA[0])
    elif len(theMST) == len(theGraph) - 1:
        return theMST
    else:
        theMST.append(nextBestEdge(theGraph, theMST))
    return primsAlgo(theGraph, theMST)


theRequiredMST = primsAlgo(theGraph, theMST)
print(theRequiredMST)

theCost = 0
for i in theRequiredMST:
    theCost += i[2]
print("The cost is "+str(theCost))