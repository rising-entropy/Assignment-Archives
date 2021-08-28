# Q) Given an array A[0…n-1] , where each element of the array represents a vote in the election.
# Assume that each vote is given as an integer representing the ID of the chosen candidate. Given an
# algorithm for determining who wins the election.

A = [1, 3, 4, 1, 1, 3, 4, 5, 3, 4, 5, 2, 3, 1, 1]

def whoWinsTheElection(A):
  A.sort()
  maxCount = -1
  prev = None
  val = None
  currentCount = 0
  for ele in A:
    if prev != ele:
      if currentCount > maxCount:
        val = prev
        maxCount = currentCount
      currentCount = 1
    else:
      currentCount += 1
    prev = ele
  if currentCount > maxCount:
    val = prev
    maxCount = currentCount
  return val

print(whoWinsTheElection(A))