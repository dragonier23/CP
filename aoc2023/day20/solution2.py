import re
import math
#so here, we know rx is inputted by mg, and mg has a few inputs
#for a low to rx, all to mg must be high, so we should search for that instead and look for the 
#lcm of this

def main():
    filename = 'problemstatement.txt'
    file = open(filename, 'r').readlines()

    config = dict()
    for line in file:
        workflow = re.findall(r'[a-z%&]+', line)
        if workflow[0] == 'broadcaster':
            config['broadcaster'] = [2, workflow[1:]]
        if workflow[0][0] == '%':
            config[workflow[0][1:]] = [1, workflow[1:], 0]       
        if workflow[0][0] == '&':
            config[workflow[0][1:]] = [0, workflow[1:], dict()]
    
    for module in config: #module is the key
        for dest in config[module][1]:
            if dest in config:
                if not(config[dest][0]): 
                    config[dest][2][module] = 0
    
    calcAns = {origin: 0 for origin in config['mg'][2]}
    remaining = [module for module in calcAns]

    buttonPress = 0
    while remaining:
        buttonPress += 1
        queue = [('broadcaster', 0)]
        while queue:
            currAddress, pulse = queue.pop(0)
            if config[currAddress][0] == 2: # we first check if this is a broadcaster unit
                for dest in config[currAddress][1]:
                    if dest in config:
                        if not(config[dest][0]): #if it is a conjunction, edit its memory
                            config[dest][2][currAddress] = pulse
                        queue.append((dest, pulse))
            elif config[currAddress][0]: # so if it is a flip flop module
                if not(pulse): #only react if it is a low pulse
                    config[currAddress][2] = 0 if config[currAddress][2] else 1
                    for dest in config[currAddress][1]:
                        if dest in config:
                            if not(config[dest][0]): #if it is a conjunction, edit its memory
                                config[dest][2][currAddress] = config[currAddress][2]
                            queue.append((dest, config[currAddress][2]))
            else: #hence, it must be a conjunction unit
                rmbLow = False
                for origin in config[currAddress][2]:
                    if not(config[currAddress][2][origin]):
                        rmbLow = True 
                        break
                if currAddress in remaining:
                    if rmbLow: #if we are sending a high
                        calcAns[currAddress] = buttonPress
                        remaining.pop(remaining.index(currAddress))
                for dest in config[currAddress][1]:
                    if dest in config:
                        if not(config[dest][0]): #if it is a conjunction, edit its memory
                            config[dest][2][currAddress] = 1 if rmbLow else 0 
                        queue.append((dest, 1 if rmbLow else 0))
    ans = [calcAns[key] for key in calcAns]
    finalAns = 1
    for element in ans:
        finalAns = math.lcm(element, finalAns)
    print(finalAns)
                        
if __name__ == '__main__':
    main()