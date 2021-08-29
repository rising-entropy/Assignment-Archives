from copy import deepcopy

# Find steps to solve 15 Puzzle Problem using Heuristic

finalState = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, None]
]

def calculateHeuristic(matrix):
  h = 0
  for i in range(len(finalState)):
    for j in range(len(finalState[i])):
      if matrix[i][j] != finalState[i][j]:
        h += 1 
  return h

def possibleOptions(matrix):
  lst = []
  for i in range(len(finalState)):
    for j in range(len(finalState[i])):
      if matrix[i][j] == None:
        # Up
        if i-1 > -1:
          lst.append("UP")
          
        # Down
        if i+1 < len(finalState):
          lst.append("DOWN") 
        
        # Left
        if j-1 > -1:
          lst.append("LEFT")
        
        # Right
        if j+1 < len(finalState[0]):
          lst.append("RIGHT")
  return lst

def matrixUP(matrix):
  bufferMatrix = matrix.copy()
  for i in range(len(finalState)):
    for j in range(len(finalState[i])):
      if bufferMatrix[i][j] == None:
        temp = bufferMatrix[i-1][j]
        bufferMatrix[i-1][j] = None
        bufferMatrix[i][j] = temp
        return bufferMatrix
      
def matrixDOWN(matrix):
  bufferMatrix = matrix.copy()
  for i in range(len(finalState)):
    for j in range(len(finalState[i])):
      if bufferMatrix[i][j] == None:
        temp = bufferMatrix[i+1][j]
        bufferMatrix[i+1][j] = None
        bufferMatrix[i][j] = temp
        return bufferMatrix

def matrixLEFT(matrix):
  bufferMatrix = matrix.copy()
  for i in range(len(finalState)):
    for j in range(len(finalState[i])):
      if bufferMatrix[i][j] == None:
        temp = bufferMatrix[i][j-1]
        bufferMatrix[i][j-1] = None
        bufferMatrix[i][j] = temp
        return bufferMatrix
      
def matrixRIGHT(matrix):
  bufferMatrix = matrix
  for i in range(len(finalState)):
    for j in range(len(finalState[i])):
      if bufferMatrix[i][j] == None:
        temp = bufferMatrix[i][j+1]
        bufferMatrix[i][j+1] = None
        bufferMatrix[i][j] = temp
        #print(bufferMatrix)
        return bufferMatrix

def getAllOptionStates(matrix, typeList):
  optionMatrices = []
  
  # UP
  if "UP" in typeList:
    optionMatrices.append(matrixUP(deepcopy(matrix)))
  
  #DOWN
  if "DOWN" in typeList:
    optionMatrices.append(matrixDOWN(deepcopy(matrix)))
  
  #LEFT
  if "LEFT" in typeList:
    optionMatrices.append(matrixLEFT(deepcopy(matrix)))
  
  #RIGHT
  if "RIGHT" in typeList:
    optionMatrices.append(matrixRIGHT(deepcopy(matrix)))

  return optionMatrices

def matrixOfMinimalHeuristic(listOfMatrices):
  theHeuristics = []
  for mat in listOfMatrices:
    theHeuristics.append(calculateHeuristic(mat))
  minimumHeu = min(theHeuristics)
  for i in range(len(theHeuristics)):
    if theHeuristics[i] == minimumHeu:
      return listOfMatrices[i]

problem = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, None, 11],
  [13, 14, 15, 12]
]

print(matrixOfMinimalHeuristic(getAllOptionStates(problem, possibleOptions(problem))))