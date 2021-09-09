
# Naive method for matrix multiplication

m1 = [[3, 4]]
m2 = [[3, 1], [5, 6]]

def matrixMultiply(m1, m2):
    if len(m1[0]) != len(m2):
        print("Matrix Multiplication is not possible for this matrix.")
        return []
    res = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            for k in range(len(m1[0])):
                res[i][j] += m1[i][k]*m2[k][j]
    return res

ans = matrixMultiply(m1, m2)
for i in ans:
    for j in i:
        print(j, end=' ')
    print()
