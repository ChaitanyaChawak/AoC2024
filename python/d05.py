input = '/home/chai/Documents/AoC2024/puzzles/d05.txt'

with open(input, 'r') as file:
    input_lines = [line.strip() for line in file]

count = 0
count2 = 0

empty_index = input_lines.index('')
rules = input_lines[:empty_index]
pages = input_lines[empty_index + 1:]

rules_dict = {}

def checkorder(elementlist, rulesdict):
    for element in elementlist:
        ind = elementlist.index(element)
        remaining_elements = elementlist[ind + 1:]
        for i in rulesdict.get(element, []):
            if (i in elementlist) and (i not in remaining_elements) : return False
    
    return True

def fixorder(elementlist, rulesdict):
    for element in elementlist:
        ind = elementlist.index(element)
        remaining_elements = elementlist[ind + 1:]
        for i in rulesdict.get(element, []):
            if (i in elementlist) and (i not in remaining_elements) :
                index1, index2 = elementlist.index(element), elementlist.index(i) 
                elementlist[index1], elementlist[index2] = elementlist[index2], elementlist[index1]

    if checkorder(elementlist, rulesdict): return True
    else: fixorder(elementlist, rulesdict)


for i in rules:
    before, after = i.split('|')
    if before in rules_dict: rules_dict[before].append(after)
    else: rules_dict[before] = [after]

for this in pages:
    pages_to_update = this.split(',')
    if checkorder(pages_to_update, rules_dict): count += int(pages_to_update[len(pages_to_update) // 2])
    else:
        fixorder(pages_to_update, rules_dict)
        count2 += int(pages_to_update[len(pages_to_update) // 2])

print(count)
print(count2)