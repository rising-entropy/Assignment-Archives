combinedList = []

s1 = input()
while(True):
    try:
        vart = input().split()
        vartDic = {
            "name": vart[0],
            "number": vart[1],
            "whatToDisplay": vart[0]+" - Vartika "+vart[1]
        }
        combinedList.append(vartDic)
    except:
        break
while(True):
    try:
        vaib = input().split()
        vaibDic = {
            "name": vaib[0],
            "number": vaib[1],
            "whatToDisplay": vaib[0]+" - Vartika "+vaib[1]
        }
        combinedList.append(vaibDic)
    except:
        break

combinedList = sorted(combinedList, key=lambda x : x['whatToDisplay'])

for li in combinedList:
    print(li['whatToDisplay'])