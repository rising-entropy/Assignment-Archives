# You are given two sorted array, A and B, where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order.

emptySpace = None

A = [1, 2, 3, 9, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace]
B = [4, 5, 6, 7, 8]

elementsA = 4
elementsB = 5

def mergeBintoA(A, B, cA, cB):
  last = cA + cB - 1
  indexA = cA - 1
  indexB = cB - 1
  
  while (indexB >= 0) :
    # End of a is greater than end
    # of b
    if (indexA >= 0 and A[indexA] > B[indexB]):
        # Copy Element
        A[last] = A[indexA]
        indexA -= 1
    else:
      # Copy Element
      A[last] = B[indexB]
      indexB -= 1
    # Move indices
    last-= 1
  return A
  
print(mergeBintoA(A, B, elementsA, elementsB))