# Q) Given an array A of n elements, each of which is an integer in the range [1, n^2]. How do we sort
# the array in O(n) time?

A = [2, 4, 12, 7, 16, 30]

def sortMyArrayInRange(A):
  n = len(A)
  lst = [0]*((n*n)+1)
  for ele in A:
    lst[ele] += 1
  sortedArray = []
  for i in range(len(lst)):
    for j in range(lst[i]):
      sortedArray.append(i)
  return sortedArray
      
print(sortMyArrayInRange(A))