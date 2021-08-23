theCircusArtists = [(85, 100), (60, 150), (87, 90), (65,190), (54, 95), (70, 110)]

def sizeOfTallestRoutine(theCircusArtists):
  
  # sort with 1st param then 2nd
  theCircusArtists = sorted(theCircusArtists, key=lambda element: (element[0], element[1]))
  
  theCount = 0
  prev1, prev2 = -1, -1
  for theCircusArtist in theCircusArtists:
    if theCircusArtist[0] > prev1 and theCircusArtist[1] > prev2:
      theCount += 1
      prev1, prev2 = theCircusArtist[0], theCircusArtist[1]
      
  return theCount

print(sizeOfTallestRoutine(theCircusArtists))