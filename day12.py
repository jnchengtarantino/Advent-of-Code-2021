import numpy as np 
# file = open("testinput.txt")
file = open("day12input.txt")

def traverse(graph, paths, node, currentPath):
    currentPath = currentPath+"," + node
    temp = currentPath.split(",")
    flag = False
    for n in temp:
        flag = (not n.isupper() and temp.count(n) > 1) or flag
    if node == "end":
        paths.append(currentPath[1:])
        return
    for n in graph[node]:
        if n!= "start" and not (n in temp and not n.isupper() and flag):
            traverse(graph,paths,n,currentPath)

graph = {}
paths=[]
lines = file.readlines()
for line in lines:
    v1, v2 = line.strip().split("-")
    if v1 not in graph:
        graph[v1] = []
    if v2 not in graph:
        graph[v2] = []
    graph[v1].append(v2)
    graph[v2].append(v1)
traverse(graph,paths,"start","")
# print(paths)
print(len(paths))
file.close()