# Given a sorted array of string which is interspersed with empty string, write a method to find the
# location of a given string.

theList = ["at", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
stringToSearch = "ball"

def searchString(theList, stringToSearch):  
  for i in range(len(theList)):
    if theList[i] == stringToSearch:
      return i
  return -1

ans = searchString(theList, stringToSearch)
if ans == -1:
  print("String is not present in the List.")
else:
  print("String present at index: "+str(ans))