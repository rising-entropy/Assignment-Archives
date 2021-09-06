
theList = [1, 2, 3, 4, 5, 2]

# Modified version of the binary search
def findMaximumElement(theList, low, high):

    # Base Case
    if low == high:
        return theList[low]

    # 2 elements (One of them would be the maximum)
    if high - low == 1:
        if theList[low] > theList[high]:
            return theList[low]
        if theList[low] < theList[high]:
            return theList[high]
    
    # General Case
    mid = (low + high)//2

    # The Peak
    if theList[mid] > theList[mid+1] and theList[mid] > theList[mid-1]:
        return theList[mid]

    # Peak lies to the left
    if theList[mid] < theList[mid-1] and theList[mid] > theList[mid+1]:
        return findMaximumElement(theList, low, mid-1)

    # Peak lies to the right
    if theList[mid] > theList[mid-1] and theList[mid] < theList[mid+1]:
        return findMaximumElement(theList, mid+1, high)

print(findMaximumElement(theList, 0, len(theList)-1))
