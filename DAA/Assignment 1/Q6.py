# Given an M*N matrix in which each row and each column is sorted in ascending order, write a
# method to find an element.

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
elementToSearch = 1

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

def searchSortedMatrix(matrix, ele):
  for i in range(len(matrix)):
    if matrix[i][len(matrix[0])-1] >= ele:
      theColIndex = binary_search(matrix[i], 0, len(matrix[i]), ele)
      if theColIndex == -1:
        return "Element does not exist."
      return "Element found at position ("+str(i)+", "+str(theColIndex)+")"
  return "Element does not exist."
        
print(searchSortedMatrix(matrix, elementToSearch))

