import GraphUtilities
import random
import math

graph1 = GraphUtilities.Graph([])
graph1.addNode(0)
TotalNumberNodes1 = 100

for NodeIndex1 in range(1, TotalNumberNodes1):
    attachment1 = random.randrange(0, NodeIndex1)
    graph1.addNode(NodeIndex1)
    endpoint1 = [NodeIndex1, attachment1]
    graph1.addEdge(endpoint1)
# graph1.printGraph()


graph2 = GraphUtilities.Graph([])
graph2.addNode(0)
ActiveSet2 = [0]
TotalNumberNodes2 = 100

for NodeIndex2 in range(1, TotalNumberNodes2):
    attachment2 = random.choice(ActiveSet2)
    graph2.addNode(NodeIndex2)
    endpoint2 = [NodeIndex2, attachment2]
    graph2.addEdge(endpoint2)
    if random.random() < 0.25:
        ActiveSet2.remove(attachment2)
    ActiveSet2.append(NodeIndex2)
graph2.printGraph()

