# Divide and Conquer method for matrix multiplication
# N*N matrices of power 2

m1 = [[1, 3], [2, -7]]
m2 = [[3, 4], [1, 1]]

m3 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

def matrixByFour(m):
    n = len(m)
    n2 = n // 2

    a11 = [[0 for i in range(n2)] for j in range(n2)]
    a12 = [[0 for i in range(n2)] for j in range(n2)]
    a21 = [[0 for i in range(n2)] for j in range(n2)]
    a22 = [[0 for i in range(n2)] for j in range(n2)]

    for i in range(n2):
        for j in range(n2):
            a11[i][j] = m[i][j]
    
    for i in range(n2):
        for j in range(n2, n):
            a12[i][j-n2] = m[i][j]

    for i in range(n2, n):
        for j in range(n2):
            a21[i-n2][j] = m[i][j]
    
    for i in range(n2, n):
        for j in range(n2, n):
            a22[i-n2][j-n2] = m[i][j]

    return a11, a12, a21, a22

def mergeMatrix(c11, c12, c21, c22):
    n = 2*len(c11)
    c = [[0 for i in range(n)] for j in range(n)]

    for i in range(n//2):
        for j in range(n//2):
            c[i][j] = c11[i][j]

    for i in range(n//2):
        for j in range(n//2, n):
            c[i][j] = c12[i][j-n//2]

    for i in range(n//2, n):
        for j in range(n//2):
            c[i][j] = c21[i-n//2][j]

    for i in range(n//2, n):
        for j in range(n//2, n):
            c[i][j] = c22[i-n//2][j-n//2]

    return c

def matrixMultiply(m1, m2):
    n = len(m1)
    if n==1:
        return m1[0][0] * m2[0][0]
    else:
        # Dividing matrix in 4 sub-parts
        a11, a12, a21, a22 = matrixByFour(m1)
        b11, b12, b21, b22 = matrixByFour(m2)
        
        c11 = [matrixMultiply(a11, b11)] + [matrixMultiply(a12, b21)]
        c12 = [matrixMultiply(a11, b12)] + [matrixMultiply(a12, b22)]
        c21 = [matrixMultiply(a21, b11)] + [matrixMultiply(a22, b21)]
        c22 = [matrixMultiply(a21, b12)] + [matrixMultiply(a22, b22)]

        return c11, c12, c21, c22
        c = mergeMatrix(c11, c12, c21, c22)

        return c

# print(mergeMatrix([[1, 2], [1, 2]], [[3, 4], [3, 4]], [[1, 2], [1, 2]], [[3, 4], [3, 4]]))

print(matrixMultiply(m3, m3))