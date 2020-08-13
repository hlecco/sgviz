# this code gets the info from gInfo.txt and sets coordinates for the nodes
# everything is then saved to gPos.txt
# later, run plotter.py to generate the svg file

import random
import math

class Node:
    # vertex class
    def __init__(self, num):
        self.Id = num
        self.label = ""
        self.edge = set()
        self.x = random.random()-0.5
        self.y = random.random()-0.5

# read size of the graph and relations between each vertex
file = open("gInfo.txt","r")
size = int(file.readline())
edges = file.readline()
labels = file.readlines()
file.close()

vx = []
for i in range(size):
    # create new vertices and put the information in them
    vx.append(Node(i))
# edge relations
for i in range(size):
    for j in range(i,size):
        if int(edges[size*i+j]) == 1:
            # this is saying the vertices i and j are connected
            vx[i].edge.add(j)
            vx[j].edge.add(i)

# how many nodes are connected to the node with most neighbors?
most = 1
for vertex in vx:
    if len(vertex.edge) > most:
        most = len(vertex.edge)

# positioning the vertices
for i in range(size):
    # setting coordinates as mean of the connected ones
    counter = 1
    for j in range(i):
        if j in vx[i].edge:
            vx[i].x += vx[j].x
            vx[i].y += vx[j].y
            counter+=1
    vx[i].x = vx[i].x / counter
    vx[i].y = vx[i].y / counter

    # setting the distance to the center
    # the more vertices are connected, more centralized it is
    dist = math.sqrt(math.pow(vx[i].x,2) + math.pow(vx[i].y,2))
    if dist!=0:
        vx[i].x *= (1-len(vx[i].edge)/most) / dist
        vx[i].y *= (1-len(vx[i].edge)/most) / dist

    # introducing some perturbation
    vx[i].x = random.uniform(vx[i].x-dist/10, vx[i].x+dist/10)
    vx[i].y = random.uniform(vx[i].y-dist/10, vx[i].y+dist/10)
# with everyone set, repeat a couple of times
for k in range(size):

    for p in range(size):
        for i in range(size):
                # setting coordinates as mean of the connected ones
                counter = 1
                if j in vx[i].edge:
                    vx[i].x += vx[j].x
                    vx[i].y += vx[j].y
                    counter+=1
                vx[i].x = vx[i].x / counter
                vx[i].y = vx[i].y / counter
    for i in range(size):
        # setting the distance to the center
        # the more vertices are connected, more centralized it is
        dist = math.sqrt(vx[i].x**2 + vx[i].y**2)
        if dist!=0:
            vx[i].x *= (1-len(vx[i].edge)/(most)) / dist
            vx[i].y *= (1-len(vx[i].edge)/(most)) / dist

        # introducing some perturbation
        vx[i].x = random.uniform(vx[i].x-dist/100, vx[i].x+dist/100)
        vx[i].y = random.uniform(vx[i].y-dist/100, vx[i].y+dist/100)




file = open("gPos.txt","w")
file.write(str(size) + "\n")
file.write(str(most) + "\n")
file.write(str(edges))
for i in range(size):
    file.write(labels[i])
for i in range(size):
    file.write(str(vx[i].x) + " " + str(vx[i].y) + "\n")
file.close()





