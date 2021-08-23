# Given a sorted theListay of n integers that has been rotated an unknown number of times, write code to
# find an element in the theListay. You may assume that the theListay was originally sorted in increasing order.

theList = [5, 6, 7, 8, 1, 2]
ele = 8

def searchElement(theList, l, h, ele):
  try:
    if l > h:
        return -1
    
    mid = (l + h) // 2
    if theList[mid] == ele:
        return mid

    # sub-array is sorted
    if theList[l] <= theList[mid]:
        if ele >= theList[l] and ele <= theList[mid]:
            return searchElement(theList, l, mid-1, ele)
        return searchElement(theList, mid + 1, h, ele)

    # sub-array is not sorted, the other side of it must be sorted
    if ele >= theList[mid] and ele <= theList[h]:
        return searchElement(theList, mid + 1, h, ele)
    return searchElement(theList, l, mid-1, ele)
  
  except:
    return -1

val = searchElement(theList, 0, len(theList), ele)
if val == -1:
  print("Element Does not exist in the list")
else:
  print("Element exists at index: "+str(val))
