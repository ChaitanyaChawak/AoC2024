input = '/home/chai/Documents/AoC2024/puzzles/d02.txt'

with open(input, 'r') as file:
  input_lines = [line.strip() for line in file]

#initializations
line = []
count = 0
count2 = 0

def checkasc(this):
  this = [int(a) for a in this]
  sortthis = sorted(this)
  sortthisrev = sorted(this, reverse=True)
  if this == sortthis or this == sortthisrev:
    return True
  else: return False

def checkdist(this):
  this = [int(a) for a in this]
  for i in range(0, len(this)-1):
    if (abs(int(this[i+1]) - int(this[i])) > 3) or (abs(int(this[i+1]) - int(this[i])) < 1):
      return False
            
  return True

#parsing
for i in input_lines:
  linee = list(i.split(' '))

  if checkasc(linee) and checkdist(linee): count += 1

  for j in range(0,len(linee)):
    linerem = linee[:]
    linerem.pop(j)
    if checkasc(linerem) and checkdist(linerem):
      count2 += 1
      break


print(count)
print(count2)
