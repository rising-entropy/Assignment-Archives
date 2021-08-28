# Q) Given an array A[0…n-1] of n numbers containing repetition of some number. Given an algorithm
# for checking whether there are repeated element or not. Assume that we are not allowed to use
# additional space (i.e., we can use a few temporary variable, O(1) storage).

A = [5, 6, 2, 1, 9, 3, 10, 4, 10, 3]

def areElementsRepeated(A):
  
  #sort the elements
  A.sort()
  
  prev = None
  for ele in A:
    if prev == ele:
      return True
    prev = ele
  return False

print(areElementsRepeated(A))
