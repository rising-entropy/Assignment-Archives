import math
import copy

maxi = float('inf')

theMatrix = [[maxi, 10, 5, 3],
       [8, maxi, 9, 7],
       [1, 6, maxi, 9],
       [2, 3, 8, maxi]]

N = 4

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def rowMin(lst):
    mini = 9999999999999999999
    for i in lst:
        if i != maxi:
            if i < mini:
                mini = i
    return mini

def firstReduction(mat):
    theCost = 0
    # reduction in rows
    for row in mat:
        minimumRowValue = rowMin(row)
        theCost += minimumRowValue
        for j in range(len(row)):
            try:
                row[j] = int(row[j] - minimumRowValue)
            except:
                row[j] = maxi
    mat = transpose(copy.deepcopy(mat))
    
    # reduction in cols
    for col in mat:
        minimumColValue = rowMin(col)
        theCost += minimumColValue
        for j in range(len(col)):
            try:
                col[j] = int(col[j] - minimumColValue)
            except:
                col[j] = maxi
    mat = transpose(copy.deepcopy(mat))
    return mat, theCost

def whatPointsLeftToReach(route, N):
    lst = []
    for i in range(N):
        if i not in route:
            lst.append(i)
    return lst

# since we know the 1st point would be 0 and the last would the one that remained,
# we run the code to find the intermediate route

# function taking in the predecessor cost, matrix and the current ele and target route. It returns the reduction cost
def getReductionCost(mat, curr, tar, predecessorCost):
    for i in range(N):
        for j in range(N):
            if i == curr or j == curr or i == tar or j == tar:
                mat[i][j] = maxi
    global theMatrix
    mat2, c = firstReduction(copy.deepcopy(mat))
    print(predecessorCost, c, theMatrix[curr][tar])
    reductionCost = predecessorCost + c + theMatrix[curr][tar]
    return reductionCost, mat2, tar

# function that gets a matrix, its predecessor cost and route, current index it returns the reduction matrix with least cost
# def getLeastCostingMatrix(mat, preCost, routeToExplore):

def matrixToMinimumReduction(mat, predecessorCost, route, curr):
    route = whatPointsLeftToReach(copy.deepcopy(route), N)
    miniCost = 9999999999999999
    lstOfMats = []
    for r in route:
        temp = getReductionCost(copy.deepcopy(mat), curr, r, predecessorCost)
        if temp is not None:
            lstOfMats.append(temp)
    #print(lstOfMats)
    for ele in lstOfMats:
        if ele[0] < miniCost:
            miniCost = ele[0]
    for ele in lstOfMats:
        if ele[0] == miniCost:
            return ele[0], ele[1], ele[2]

mat, preCost = firstReduction(copy.deepcopy(theMatrix))
route = [0]
curr = 0
for i in range(N-2):
    try:
        redC, mat, tar  = matrixToMinimumReduction(copy.deepcopy(mat), preCost, copy.deepcopy(route), curr)
        preCost = redC
        route.append(tar)
    except:
        pass
    
#print(route)
