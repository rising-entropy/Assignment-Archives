# Q) Let A and B tow arrays of n elements, each. Given a number K, give an O (nlogn) time algorithm
# for determining whether there exists a ϵ A and b ϵ B such that a+b =K.

A = [4, 5, 7, 1, 2]
B = [1, 3, 2, 9, 10]
K = 4

def binary_search(arr, x):
  low = 0
  high = len(arr) - 1
  mid = 0
  while low <= high:
    mid = (high + low) // 2
    if arr[mid] < x:
        low = mid + 1
    elif arr[mid] > x:
        high = mid - 1
    else:
        return mid
  return -1

def doesSumExist(A, B, K):
  B.sort()
  
  # Binary Search for reduced complexity
  for ele in A:
    if(binary_search(B, K-ele) > -1):
      return True
  return False
  
print(doesSumExist(A, B, K))
