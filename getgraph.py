# opens file entries.txt and saves its contents to 'nodes'
file = open("src/entries.txt","r")
nodes = file.read().split()
file.close()


# initialize all edges (set as not related)
edges=[]
for i in range(len(nodes)**2):
    edges.append(0)

# for each entry (node) open its file and copy its contents
for name in nodes:
    file = open("src/"+name,"r")
    related = file.read().split()
    file.close()
    # if a label is on the file and is on the entries file, then set the edges appropriately
    for dest in related:
        if dest in nodes:
            edges[nodes.index(name)*len(nodes) + nodes.index(dest)] = 1
            edges[nodes.index(dest)*len(nodes) + nodes.index(name)] = 1

# store all information in gInfo.txt
# that is, the amount of nodes, the edges and the labels
file = open("gInfo.txt","w")
file.write(str(len(nodes))+"\n")
for i in edges:
    file.write(str(i))
file.write("\n")
for name in nodes:
    file.write(name+"\n")
file.close()
