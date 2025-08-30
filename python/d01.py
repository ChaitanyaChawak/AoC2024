input = '/home/chai/Documents/AoC2024/puzzles/d01.txt'

with open(input, 'r') as file:
  input_lines = [line.strip() for line in file]

#initializations
left = []
right = []
sum = 0
part2 = 0

#parsing
for i in input_lines:
  l, r = i.split('   ')
  left.append(l)
  right.append(r)

left.sort()
right.sort()

for i in range(0, len(left)):
  lint = int(left[i])
  rint = int(right[i])
  if lint>rint:
    sum += (lint-rint)
  else: sum += (rint-lint)

for i in left:
  count = 0
  if i in right:
    count += right.count(i)
  part2 += count*int(i)

print(sum)
print(part2)
