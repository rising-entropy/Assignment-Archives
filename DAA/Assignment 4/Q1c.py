
import numpy as np

def read_input(input):
    array = np.loadtxt(input,dtype='i',delimiter=' ')
    array_first,array_second = np.split(array,2,axis=0)
    return array_first, array_second 

def save_ouput(output):
    output_array = np.savetxt("output.txt",output.astype(int), fmt='%i', delimiter=' ')

def splitMatrix(matrix):
    # Split matrix into quarters
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def matrixMultiplicationStrassen(m1, m2):
    # Base case
    if len(m1) == 1:
        return m1 * m2
    
    a, b, c, d = splitMatrix(m1)
    e, f, g, h = splitMatrix(m2)

    p1 = matrixMultiplicationStrassen(a, f - h) 
    p2 = matrixMultiplicationStrassen(a + b, h)       
    p3 = matrixMultiplicationStrassen(c + d, e)       
    p4 = matrixMultiplicationStrassen(d, g - e)       
    p5 = matrixMultiplicationStrassen(a + d, e + h)       
    p6 = matrixMultiplicationStrassen(b - d, g + h) 
    p7 = matrixMultiplicationStrassen(a - c, e + f) 

    # From the diagram
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    # Combining the quadrants
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    
    return c


array_first,array_second = read_input('input.txt')
ans = matrixMultiplicationStrassen(array_first, array_second)
save_ouput(ans)
