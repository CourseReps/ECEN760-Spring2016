# Assignment 2


## Graphs and Peeling Algorithms

Fountain codes or rateless codes are a class of codes that can be employed to protect an information message against erasures.
In this paradigm, a source produces and streams a succession of coded packets.
An interested device can start listening to this stream of information at any point in time.
Once it has acquired enough packets from the source, this device can decode the original message with high probability.
The structure of fountain codes admits bipartite graph representations.
In a typical representation, the nodes on the left side of the graph or variable nodes contain fragments of the original message.
The nodes on the right side of the graph or check nodes, are formed by adding a small number of variable nodes over the binary field, GF(2). [David MacKay](http://www.inference.phy.cam.ac.uk/mackay/) offers an excellent introduction to digital fountain codes in his [book](http://www.inference.phy.cam.ac.uk/mackay/DFountain.html) (Chapter 50), which is available online.


### Action Items
* __Read__: [Digital Fountain Codes](http://www.inference.phy.cam.ac.uk/mackay/DFountain.html).
* __Implement__: A class that can generate abstract graphical representations of fountain codes.
* __Implement__: A class that tracks the evolution of a peeling decoder on a fountain code.
* __Graph__: Number of recovered packets as a function of codelength ```N in range(0,2000)``` for a code with ```K = 1000```.
You should run multiple trials to get statistically significant results.


### Questions
* Exercise 50.1 [Digital Fountain Codes](http://www.inference.phy.cam.ac.uk/mackay/DFountain.html).
* Optimize the degree distribution of a digital fountain code for a file of K = 1000 packets.
The objective function for this optimization, should be the mean of N, the number of packets required for complete decoding. 
Report performance with confidence interval.
* Exercise 50.11 [Digital Fountain Codes](http://www.inference.phy.cam.ac.uk/mackay/DFountain.html).
