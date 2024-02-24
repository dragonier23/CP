import re
from collections import deque
import random

filename = 'problemstatement.txt' #  'test.txt' #
file = open(filename, 'r').readlines()

#problems is apparently a min cut problem
# REF: KARGER ALGORITHM

#key question is how to structure my data:
#because we are merging, we need to keep track of the nodes that are merged together, and the links to adjacent nodes
#so we could have a 2d list [set of nodes merged, set of adjacent nodes], and the key dosent really matter --> so maybe we 
#should have a list of these things instead
# we just need to be cautious about find the neighbour

nodes = dict()
for line in file:
    origin, dest = line.strip().split(": ")
    dest = dest.split(" ")
    if not(origin in nodes):
        nodes[origin] = set()
    for node in dest:
        nodes[origin].add(node)
        if not(node in nodes):
            nodes[node] = set()
        nodes[node].add(origin)

#now we can just convert it into a list, lets do that
nodeList = []
for node in nodes:
    nodeList.append([{node}, set(nodes[node])])
first = random.choice(nodeList)
#print(first)
#print(random.choice(list(first[1])))

while True:
    #algo existingly goes: choose a node randomly. Choose a neighbour randomly, and merge the 2
    #new combined node has links to all other nodes that were joined previously
    #we should be trying to count the nodes on one side and the nodes on the other side --> maybe lets identify the bridges
    nodeListCopy = nodeList.copy()
    while len(nodeListCopy) > 2:
        first = random.choice(nodeListCopy)
        secondNode = random.choice(list(first[1]))
        #so now we have chosen a node and its neighbour, lets merge it
        #first we need to remove both of them from the list
        for i in range(len(nodeListCopy)):
            if nodeListCopy[i] == first:
                nodeListCopy.pop(i)
                break
        for i in range(len(nodeListCopy)):    
            if secondNode in nodeListCopy[i][0]:
                second = nodeListCopy.pop(i)
                break
        #we now have removed both of them from the list, time to combine. 
        combined = []
        combined.append(first[0].union(second[0]))
        combined.append(set([node for node in first[1].union(second[1]) if not(node in combined[0])]))
        nodeListCopy.append(combined)
    if len(nodeListCopy[0][1]) == 3:
        print(len(nodeListCopy[0][0]) * len(nodeListCopy[1][0]))
        break


        