from GraphUtilities import *

print("\nOriginal graph")
es = [['a','b'],['b','c'], ['a','c']]
X = Graph(es)
X.printGraph()

print("\nRemove edge a ---- b")
X.removeEdge(['a','b'])
X.printGraph()

print("\nRemove node a")
X.removeNode('a')
X.printGraph()

print("\nAdd back a with edges")
X.addNode('a')
X.addEdge(['a','b'])
X.addEdge(['a','c'])
print(X)
