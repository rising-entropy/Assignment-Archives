
def compareStrings(str1, str2):
  i = 0
  while i < len(str1) - 1 and str1[i] == str2[i]:
      i += 1
  if str1[i] > str2[i]:
      return -1

  return str1[i] < str2[i]
  
def searchStr(arr, string, first, last):
  try:
    if first > last:
        return -1
      
    # Middle point
    mid = (last + first) // 2

    # If mid is empty - we look for the closest non-empty element
    if len(arr[mid]) == 0:
        # If mid is empty, search in both sides of mid and find the closest non-empty string, and set mid w.r.t. that.
        left, right = mid - 1, mid + 1
        while True:
          
            if left < first and right > last:
                return -1
                  
            if right <= last and len(arr[right]) != 0:
                mid = right
                break
              
            if left >= first and len(arr[left]) != 0:
                mid = left
                break
              
            right += 1
            left -= 1
  
    # If str is found at mid
    if compareStrings(string, arr[mid]) == 0:
        return mid

    # If str is greater than mid
    if compareStrings(string, arr[mid]) < 0:
        return searchStr(arr, string, mid+1, last)

    # If str is smaller than mid
    return searchStr(arr, string, first, mid-1)
  
  except:
    return -1


theList = ["at", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
stringToSearch = "mom"


ans = searchStr(theList, stringToSearch, 0, len(theList))
if ans == -1:
  print("String is not present in the List.")
else:
  print("String present at index: "+str(ans))