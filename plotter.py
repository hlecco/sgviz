# this code generates an svg file from gPos.txt
# each blue strip represents how much a node is related to the group

file = open("gPos.txt","r")
size = int(file.readline())
layers = int(file.readline())
edges = file.readline()
labels = []
for i in range(size):
    labels.append(file.readline())
positions = file.read().split()
file.close()

radius = size/6000

file = open("Graph.svg","w")

# plotting header
file.write("<svg width=\"3000\" height=\"3000\" viewBox=\"-1.1 -1.1 2.2 2.2\">\n")

# plotting reference disks
file.write("<circle cx=\"0\" cy=\"0\" r=\""+str(1/layers)+"\" fill=\"rgb(63,63,255)\" />\n")
for i in range(1,layers):
    file.write("<circle cx=\"0\" cy=\"0\" r=\""+str(i/layers)+"\" ")
    file.write("stroke=\"rgb("+str(int(255*(0.25+(i/layers)*0.75)))+","+str(int(255*(0.25+(i/layers)*0.75)))+",255)\" stroke-width=\""+str(1/layers+0.001)+"\" fill=\"none\" />\n")

# plotting edges
for i in range(size):
    for j in range(i,size):
        if int(edges[i*size+j]) == 1:
            file.write("<line x1=\""+str(positions[2*i])+"\" y1=\""+str(positions[2*i+1]))
            file.write("\" x2=\""+str(positions[2*j])+"\" y2=\""+str(positions[2*j+1]))
            file.write("\" style=\"stroke:rgb(0,0,0);stroke-width:0.0005\" />\n")

# plotting nodes
for i in range(size):
    file.write("<circle cx=\""+str(positions[2*i])+"\" cy=\""+str(positions[2*i+1]))
    file.write("\" r=\""+str(radius)+"\" stroke=\"red\" stroke-width=\"0.001\" fill=\"black\" />\n")

# plotting labels
for i in range(size):
    file.write("<text x=\""+str(float(positions[2*i])+radius)+"\" y=\""+str(float(positions[2*i+1])-radius)+"\" fill = \"black\" stroke=\"white\" stroke-width=\"0.0002\" font-size=\"0.008\">")
    file.write(labels[i])
    file.write("</text>\n")

# closing svg
file.write("</svg>")

file.close()

