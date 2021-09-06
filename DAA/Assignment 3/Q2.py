
gridSize = 2**4
countOfL = 0

thePointX = 3
thePointY = 4

initialList = [[0 for i in range(gridSize)] for j in range(gridSize)]

initialList[thePointX][thePointY] = -1

def makeAnL(lst, x1, y1, x2, y2, x3, y3):
    global countOfL
    countOfL += 1
    lst[x1][y1] = countOfL
    lst[x2][y2] = countOfL
    lst[x3][y3] = countOfL
    return lst

def buildLTiles(theMatrix, n, pointX, pointY):
    global countOfL
    r = 0
    c = 0

    # Base case
    # For the 2*2 square -> make every 0 -> count and that one -1 remains
    if n==2:
        countOfL += 1
        for i in range(n):
            for j in range(n):
                if theMatrix[pointX + i][pointY + j] == 0:
                    theMatrix[pointX + i][pointY + j] = countOfL
        return theMatrix
    
    for i in range(pointX, pointX + n):
        for j in range(pointY, pointY + n):
            if (theMatrix[i][j] != 0):
                r = i
                c = j

    # Placing an L in square such that 3 parts without the point will get the L
    if (r < pointX + n // 2 and c < pointY + n // 2):
        makeAnL(theMatrix, pointX + int(n / 2), pointY + int(n / 2) - 1, pointX + int(n / 2), pointY + int(n / 2), pointX + int(n / 2) - 1, pointY + int(n / 2))
    elif(r >= pointX + int(n / 2) and c < pointY + int(n / 2)):
        makeAnL(theMatrix, pointX + int(n / 2) - 1, pointY + int(n / 2), pointX + int(n / 2), pointY + int(n / 2), pointX + int(n / 2) - 1, pointY + int(n / 2) - 1)
    elif(r < pointX + int(n / 2) and c >= pointY + int(n / 2)):
        makeAnL(theMatrix, pointX + int(n / 2), pointY + int(n / 2) - 1, pointX + int(n / 2), pointY + int(n / 2), pointX + int(n / 2) - 1, pointY + int(n / 2) - 1)
    elif(r >= pointX + int(n / 2) and c >= pointY + int(n / 2)):
        makeAnL(theMatrix, pointX + int(n / 2) - 1, pointY + int(n / 2), pointX + int(n / 2), pointY + int(n / 2) - 1, pointX + int(n / 2) - 1, pointY + int(n / 2) - 1)
    
    # Recurse the 4 parts of the square
    theMatrix = buildLTiles(theMatrix, int(n / 2), pointX, pointY + int(n / 2))
    theMatrix = buildLTiles(theMatrix, int(n / 2), pointX, pointY)
    theMatrix = buildLTiles(theMatrix, int(n / 2), pointX + int(n / 2), pointY)
    theMatrix = buildLTiles(theMatrix, int(n / 2), pointX + int(n / 2), pointY + int(n / 2))

    return theMatrix

result = buildLTiles(initialList, gridSize, 0, 0)

for x in result:
    for y in x:
        print(y, end=' ')
    print()