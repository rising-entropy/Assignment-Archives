# Write a method to sort an array of string so that all the anagrams are next to each other.

theList = ["ars", "che", "sar", "mci", "mun", "rmd", "icm", "num", "kim", "mik"]

def isAnagram(a, b):
  a = [ch for ch in a]
  b = [ch for ch in b]
  a.sort()
  b.sort()
  if a == b:
    return True
  return False

def sortListOfStringsAnagrams(theList):
  theList.sort()
  anagramDic = {}
  for ele in theList:
    c=0
    for k in anagramDic.keys():
      if isAnagram(k, ele):
        anagramDic[k].append(ele)
        c+=1
        break
    if c == 0:
      anagramDic[ele] = [ele]
  anagramSequence = list(anagramDic.keys())
  anagramSequence.sort()
  finalList = []
  for seq in anagramSequence:
    specificAnagramList = anagramDic[seq]
    specificAnagramList.sort()
    finalList += specificAnagramList
    
  return finalList
    
print(sortListOfStringsAnagrams(theList))