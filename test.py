yu = int(input())
for yu in range(yu):
  s = input().split()
  numberOfPeople = int(s[0])
  relationsCount = int(s[1])
  peoples = {}
  # ini......
  for i in range(1, numberOfPeople+1):
    peoples[i] = []
    
  #relations...
  for qw in range(relationsCount):
     s = input().split()
     friend1 = int(s[0])
     friend2 = int(s[1])
     peoples[friend1].append(friend2)
     peoples[friend2].append(friend1)
  #print(peoples)
  
  #...........1
  tentativeAnswer = peoples[1]
  #peopleToDelete = []
  
  # 2............
  for theFriend in tentativeAnswer:
    if theFriend in peoples[2]:
       tentativeAnswer.remove(theFriend)
  #print(tentativeAnswer)
  mutualsOfStudent2 = []
  for friendsOf2 in peoples[2]:
     for friendOfTheFriend in peoples[friendsOf2]:
       mutualsOfStudent2.append(friendOfTheFriend)
       
  mutualsOfStudent2 = list(set(mutualsOfStudent2))
  
  for ans in tentativeAnswer:
    if ans in mutualsOfStudent2:
      tentativeAnswer.remove(ans)
  
  
  #.........
  if 1 in tentativeAnswer:
    tentativeAnswer.remove(1)
    
  if 2 in tentativeAnswer:
    tentativeAnswer.remove(2)
  
  
  #...........
  if len(tentativeAnswer) == 0:
    print("-1")
  else:
    for theAns in tentativeAnswer:
      print(theAns, end=' ')
    print()