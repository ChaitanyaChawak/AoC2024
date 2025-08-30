import re

input = '/home/chai/Documents/AoC2024/puzzles/d03.txt'

with open(input, 'r') as file:
    input_lines = [line.strip() for line in file]

pattern = r"mul\((\-?\d+(\.\d+)?),(\-?\d+(\.\d+)?)\)"
pattern_remove_between = r"don't\(\).*?do\(\)"

sum = 0
sum2 = 0

fullcontent = ''

for i in input_lines:
    matches = re.findall(pattern, i)
    for match in matches:

        num1 = match[0]
        num2 = match[2]
        
        sum += int(num1) * int(num2)

    fullcontent += i

new_inp = re.sub(pattern_remove_between, "", fullcontent)
matches2 = re.findall(pattern, new_inp)
for match in matches2:

    num1 = match[0]
    num2 = match[2]
    
    sum2 += int(num1) * int(num2)

print(sum)
print(sum2)
