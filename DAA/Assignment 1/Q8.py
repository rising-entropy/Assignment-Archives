def getRankOfNumber(stream, num):
  stream.sort()
  dic = {}
  for s in stream:
    if s in dic.keys():
      dic[s] += 1
    else:
      dic[s] = 1
  for i in range(len(stream)):
    if stream[i] == num:
      return i+(dic[num]-1)
    if stream[i] > num:
      return i
  if num > stream[len(stream)-1]:
    return len(stream)
  return 0

stream = [1, 1, 3, 4, 5, 7, 7, 10, 3]

print(getRankOfNumber(stream, 1))
print(getRankOfNumber(stream, 3))
print(getRankOfNumber(stream, 4))