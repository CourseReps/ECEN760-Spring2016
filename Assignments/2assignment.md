# Assignment 2


## Graphs and Peeling Algorithms

Fountain codes or rateless codes are a class of codes that can be employed to protect an information message against erasures.
In this paradigm, a source produces and streams a succession of coded packets.
An interested devices can start listening to this stream of information at any point in time.
Once it has acquired enough packets from the source, this device can decode the original message with high probability.

The structures of fountain codes admit bipartite graph representations.
In a typical representation, the nodes on the left side of the graph or variable nodes contain fragments of the original message.
The nodes on the right side of the graph or check nodes, are formed by adding a small number of variable nodes over the binary field, GF(2).
