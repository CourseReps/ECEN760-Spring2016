"""Bipartite graph file.
Contains Variable and Check Node classes, and Bipartite Graph class.

"""

from GraphUtilities import Graph, Node

class VariableNode(Node):
	"""Variable node class based on Node class"""

	def __init__(self, name):
		"""Constructor. Variable node is assumed to be of type "a". Value initialized to '?'. Takes a node ID"""
		Node.__init__(self, name)
		self.type="a"
		self.value='?'

	def getType(self):
		"""Returns type"""
		return self.type

	def setValue(self,val):
		"""Sets node value"""
		self.value=val

	def getValue(self):
		"""Returns node value"""
		return self.value


class CheckNode(Node):
	def __init__(self, name):
		"""Constructor. Check node is assumed to be of type "b". Value initialized to 0. Takes a node ID"""
		Node.__init__(self, name)
		self.type="b"
		self.value=0

	def getType(self):
		"""Returns type"""
		return self.type

	def setValue(self, val):
		"""Sets node value"""
		self.value=val

	def getValue(self):
		"""Returns node value"""
		return self.value


class BipartiteGraph(Graph):
	"""Bipartite Graph class based on Graph class"""
	def __init__(self, an, bn, es):
		"""Constructor. Takes a list of a nodes, a list of b nodes, and a list of edge primitives(list of two node IDs).
		Note that the lists of nodes should be existing nodes, not node IDs.
		"""
		Graph.__init__(self, [])
		self.aNodes={}
		self.bNodes={}
		for a in an:
			self.aNodes[a.getID()]=a
			self.nodes[a.getID()]=a
		for b in bn:
			self.bNodes[b.getID()]=b
			self.nodes[b.getID()]=b
		for e in es:
			self.addEdge(e)

	def getANodes(self):
		"""Returns list of a nodes"""
		return self.aNodes

	def getBNodes(self):
		"""Returns list of b nodes"""
		return self.bNodes

	def addANodes(self, ans):
		"""Adds a list of a nodes"""
		for n in ans:
			self.aNodes[n.getID()]=n
			self.nodes[n.getID()]=n

	def addBNodes(self, bns):
		"""Adds a list of b nodes"""
		for n in bns:
			self.bNodes[n.getID()]=n
			self.nodes[n.getID()]=n



