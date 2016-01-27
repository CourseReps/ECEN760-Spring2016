import GraphUtilities
import random
import math

graph1 = GraphUtilities.Graph([])
graph1.addNode(0)
TotalNumberNodes1 = 10

for NodeIndex1 in range(1, TotalNumberNodes1):
    attachment1 = random.randrange(0, NodeIndex1)
    graph1.addNode(NodeIndex1)
    endpoint1 = [NodeIndex1, attachment1]
    graph1.addEdge(endpoint1)

#graph1.printGraph()


graph2 = GraphUtilities.Graph([])
graph2.addNode(0)
ActiveSet2 = [0]
TotalNumberNodes2 = 1000

for NodeIndex2 in range(1, TotalNumberNodes2):
    attachment2 = random.choice(ActiveSet2)
    graph2.addNode(NodeIndex2)
    endpoint2 = [NodeIndex2, attachment2]
    graph2.addEdge(endpoint2)
    if random.random() < 0.25:
        ActiveSet2.remove(attachment2)
    ActiveSet2.append(NodeIndex2)

#graph2.printGraph()

graph3 = GraphUtilities.Graph([])
graph3.addNode(0)
TotalNumberNodes3 = 30

for NodeIndex3 in range(1, TotalNumberNodes3):
    attachment3 = random.randrange(0, NodeIndex3)
    graph3.addNode(NodeIndex3)
    endpoint3 = [NodeIndex3, attachment3]
    graph3.addEdge(endpoint3)



graph4 = GraphUtilities.Graph([])
graph4.addNode(0)
ActiveSet4 = [0]
TotalNumberNodes4 = 1000

for NodeIndex4 in range(1, TotalNumberNodes4):
    attachment4 = random.choice(ActiveSet4)
    graph4.addNode(NodeIndex4)
    endpoint4 = [NodeIndex4, attachment4]
    graph4.addEdge(endpoint4)
    if random.random() < 0.45:
        ActiveSet4.remove(attachment4)
    ActiveSet4.append(NodeIndex4)

f1 = open("../Graphs/Assignment1_graph1.txt", 'w')
f1.write(GraphUtilities.Utils.graphToText(graph1))
f1.close

f2 = open("../Graphs/Assignment1_graph2.txt", 'w')
f2.write(GraphUtilities.Utils.graphToText(graph2))
f2.close

f3 = open("../Graphs/Assignment1_graph3.txt", 'w')
f3.write(GraphUtilities.Utils.graphToText(graph3))
f3.close

f4 = open("../Graphs/Assignment1_graph4.txt", 'w')
f4.write(GraphUtilities.Utils.graphToText(graph4))
f4.close