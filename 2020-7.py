import sys
import re
from typing import NamedTuple

class Node(NamedTuple):
    bag: str
    num: int
    children: list = None

def buildnode(str):
    '''create a Node object from an input line'''
    # input spec:
    # <color> bags contain ([<number> <color> bag[s],]* [<number> <color> bag[s].)
    #                      no other bags.
    # returned Node always has a 0 for the num
    # returned Node's children are also Nodes, with the number set but always with no children
    # there's got to be a fancy regex for this

    # [container color, containees string]
    tuple1 = str.split('bags contain')
    container = tuple1[0].strip()
    # list of ["<number> <color>"] or "no other" extracted from containees string
    list1 = [re.match('(.*)bag', bag.strip()).group(1).strip() for bag in tuple1[1].split(',')]
    node = Node(container, 0, [])
    for contains in list1:
        # extract <number> and <color> for each containee
        # no regex match means "no other", so the container remains with no children
        z = re.match('(\d*) (.*)', contains)
        if z:
            node.children.append(Node(z.group(2), int(z.group(1))))
    return node

def buildreversegraph(lines):
    '''{str:[Node]} from from bag name to list of bags that can contain it'''
    graph = {}
    for line in lines:
        node = buildnode(line)
        # print(node)
        for child in node.children:
            containers = graph.get(child.bag, [])
            if not containers:
                # the graph key is the child (containee),
                # the value is bags found (containers) that contain this child
                # containers (children) in this graph have no further children
                graph[child.bag] = containers
            containers.append(Node(node.bag, child.num))
    return graph

def buildgraph(lines):
    '''{str:[Node]} from from bag name to list of bags contained within it'''
    # the graph key is the container, the value is all containees ()
    # this structure is the same as the input
    # containees (children) in this graph have no further children
    return {node.bag: node.children for node in (buildnode(line) for line in lines)}

def findcontainable(bag, graph, found=set()):
    '''find set of all bags that can contain (at any level) the given bag name'''
    containers = [c.bag for c in graph.get(bag, [])]
    # I'm assuming no loops
    for container in containers:
        found.add(container)
        findcontainable(container, graph, found)
    return found

def countcontents(bag, graph):
    '''count total number of bags contained in the given bag name'''
    count = 0
    # I'm assuming no loops
    for child in graph.get(bag, []):
        count += child.num + child.num * countcontents(child.bag, graph)
    return count

input = [line.strip() for line in sys.stdin]

# part 1 - 103
graph = buildreversegraph(input)
print(len(findcontainable('shiny gold', graph)))

# part 2 - 1469
graph = buildgraph(input)
print(countcontents('shiny gold', graph))
