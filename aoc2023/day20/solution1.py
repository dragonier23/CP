import re
# i think we need to do 2 things: 
# we need a hash table with the modules, storing the data:
# for flip-flop: [0, (list of output), state (0 for low, 1 for high)]
# for conjunction: [1, (list of output), (dictionary of input and state)], rmb initial is low
# for broadcast: [2, (list of outputs)]

#so we should have a queue that keeps track of the things to check. Structure of this should be
# [(location, strength (0 or 1))]

def main():
    filename = 'problemstatement.txt' #'test1.txt' #
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

    lowCount, highCount = (0, 0)
    
    for i in range(240853):
        queue = [('broadcaster', 0)]
        lowCount += 1
        while queue:
            #print(queue)
            currAddress, pulse = queue.pop(0)
            
            if config[currAddress][0] == 2: # we first check if this is a broadcaster unit
                for dest in config[currAddress][1]:
                    if pulse:
                        highCount += 1
                    else: 
                        lowCount += 1 
                    if dest in config:
                        if not(config[dest][0]): #if it is a conjunction, edit its memory
                            config[dest][2][currAddress] = pulse
                        queue.append((dest, pulse))
            elif config[currAddress][0]: # so if it is a flip flop module
                if not(pulse): #only react if it is a low pulse
                    config[currAddress][2] = 0 if config[currAddress][2] else 1
                    for dest in config[currAddress][1]:
                        if config[currAddress][2]:
                            highCount += 1
                        else: 
                            lowCount += 1
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
                for dest in config[currAddress][1]:
                    if rmbLow:
                        highCount += 1
                    else: 
                        lowCount += 1
                    if dest in config:
                        if not(config[dest][0]): #if it is a conjunction, edit its memory
                            config[dest][2][currAddress] = 1 if rmbLow else 0 
                        queue.append((dest, 1 if rmbLow else 0))
    print(highCount)
    print(lowCount)
    print(lowCount * highCount)

if __name__ == '__main__':
    main()