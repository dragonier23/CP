import re
import math

def splitAction(action):
    if re.search(r":", action):
        print("reached")
        return action.split(":")
    return action

def setCombinations(combination):
    product = 1
    for i in range(4):
        product *= (combination[i][1] - combination[i][0] + 1)
    return product

def main():
    filename = 'problemstatement.txt' #'test.txt' #

    file = open(filename, 'r').readlines()

    workflow = dict()
    for line in file:
        #we need to look for the blank line
        if not(line.strip()):
            break
        #so we want to break down each line
        breakDown = re.search(r"(\w+){(.+)}", line).groups()
        #print(breakDown[1].split(","))
        workflow[breakDown[0]] = [check.split(":") for check in breakDown[1].split(",")]

    #so how will our solution work? 
    # we basically need to keep track of the subsets, splitting them slowly until we get the sets which have only As 
    #for ease of searching, i think we will do it as such
    #the subsets will be structured as [(x-range), (m-range), (a-range), (s-range), workflow, stage]
    #we run through this subset until it runs out, every time the subset splits we add a copy to the 
    #combinations list 
    combinations = [[(1, 4000), (1, 4000), (1, 4000), (1, 4000), 'in', 0]]
    ans = 0
    categories = {'x': 0, 'm': 1, 'a': 2, 's':3}
    while combinations:
        #print(combinations)
        current = combinations.pop(0)
        xRange, mRange, aRange, sRange, key, stage = current
        curr = current.copy()
        if key == 'A':
            ans += setCombinations(curr)
            continue
        if key == 'R':
            continue
        if len(workflow[key][stage]) == 1:
            curr[4] = workflow[key][stage][0]
            curr[5] = 0
            combinations.append(curr)
            continue
        #if we reach this point this must be some sort of comparison, hence, we need to split the range
        category = workflow[key][stage][0][0]
        sign = workflow[key][stage][0][1]
        bound = int(workflow[key][stage][0][2:])

        lowerCopy = current.copy()
        upperCopy = current.copy()
        #if the bound in within the range of the curr combination, we need to split it
        if bound > curr[categories[category]][0] and bound < curr[categories[category]][1]:
            if sign == '>': #if it is a more than, we need to change the upperCopy
                upperCopy[categories[category]] = (bound+1, curr[categories[category]][1])
                upperCopy[4] = workflow[key][stage][1]
                upperCopy[5] = 0
                combinations.append(upperCopy)
                lowerCopy[categories[category]] = (curr[categories[category]][0], bound)
                lowerCopy[5] += 1
                combinations.append(lowerCopy)
            else:
                lowerCopy[categories[category]] = (curr[categories[category]][0], bound-1)
                lowerCopy[4] = workflow[key][stage][1]
                lowerCopy[5] = 0
                combinations.append(lowerCopy)
                upperCopy[categories[category]] = (bound, curr[categories[category]][1])
                upperCopy[5] += 1
                combinations.append(upperCopy)
        #so what if the bound is outside the range, or on the border 
        elif bound == curr[categories[category]][0]:
            if sign == '>':
                upperCopy[categories[category]] = (bound+1, curr[categories[category]][1])
                upperCopy[4] = workflow[key][stage][1]
                upperCopy[5] = 0
                combinations.append(upperCopy)
                lowerCopy[categories[category]] = (curr[categories[category]][0], bound)
                lowerCopy[5] += 1
                combinations.append(lowerCopy)
        elif bound == curr[categories[category]][1]:
            if sign == '<':
                lowerCopy[categories[category]] = (curr[categories[category]][0], bound-1)
                lowerCopy[4] = workflow[key][stage][1]
                lowerCopy[5] = 0
                combinations.append(lowerCopy)
                upperCopy[categories[category]] = (bound, curr[categories[category]][1])
                upperCopy[5] += 1
                combinations.append(upperCopy)
        else:
            curr[5] += 1
            combinations.append(curr)    

    print(ans)

if __name__ == '__main__':
    main()