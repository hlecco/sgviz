sgviz stands for "Simple Graph Visualizer"
It generates graphs in svg format.

How to use:
Create a directory named src in the folder
Create a file src/entries.txt containing all nodes of the graph (i.e. each node name, one per line)
For each node, create a file "src/<nodename>" containing all nodes that it is connected to.

The graph won't be directed so, for instance, if nodes "node1" and "node2" are connected, there's no need to
put node1 on src/node2 and node2 in src/node1, only one of them

./getgraph.py will generate a file gInfo.txt that contains the amount of graphs, the edges (as a string of 0 and 1) and each label
./parser.py will read gInfo.txt and generate a file gPos.txt that contains the position for each node.

The position is set following two rules:
 - The more edges a node has, the more inner it will be
 - It'll try to place nodes near to the ones that are connected to it

The first condition is stronger that the second.

Finally, run ./parser to generate Graph.svg


Please note: the included directory src and files gPos.txt, gInfo.txt and Graph.svg refer to brazilian airports and existing flight operated by a specific company.
For different plots, it suffices to change the src directory contents.
