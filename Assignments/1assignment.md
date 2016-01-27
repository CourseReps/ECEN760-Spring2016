# Assignment 1


## Handling Graphs

The purpose of this first assignment is to get familiar with handling graphs from a computational perspective.
To be software agnostic, graphs are specified in text files, each with a simple format.
For students who intend to use [Python](https://www.python.org), sample code is available under [Tools](../Tools).
Using the ```classes``` and ```methods``` provided therein, it is possible to import the text files associated with this assignment into your program.

### Action Items

The format for the trees is as follows.
The first line is the number of nodes.
The second line is the number of edges.
Every subsequent line denotes an edge, and it specifies its endpoints using unique identifiers for the nodes.
 * [Tree 1](../Graphs/Assignment1_graph1.txt)
 * [Tree 2](../Graphs/Assignment1_graph2.txt)
 * [Tree 3](../Graphs/Assignment1_graph3.txt)
 * [Tree 4](../Graphs/Assignment1_graph4.txt)

For each tree, compute the following attributes.
 * __Depth__: Maximum depth of the tree, as seen from the root.
 * __Ancestry__: Number of ancestors for every node.
 * __Graph Radius__: Radius when tree seen as undirected graph.
 * __Nodes per Level__: Number of nodes per level.
 * __Degree Distribution__: Degree distribution from node perspective when tree seen as undirected graph.

