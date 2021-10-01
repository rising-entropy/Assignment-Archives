lstOfGroups = []
numberOfPins = 0
while(True):
    s = input()
    if s.isnumeric():
        numberOfPins = int(s)
        break
    lstOfGroups.append(s)

pins = []
for p in range(numberOfPins):
    s = input()
    pins.append(s)
    lstOfGroups.remove(s)

pins += lstOfGroups

for p in pins:
    print(p)