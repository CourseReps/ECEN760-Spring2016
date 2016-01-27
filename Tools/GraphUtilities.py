import numpy


class UndirectedEdge:

	def __init__(self, n1, n2):
		self.node1=n1
		self.node2=n2

	def getNodes(self):
		return [self.node1, self.node2]

	def hasNodes(self, n1, n2):
		if(self.node1==n1 and self.node2==n2):
			return True

		if(self.node1==n2 and self.node2==n1):
			return True

		return False


class Node:

	def __init__(self, name):
		self.ID=name
		self.neighbors=[]

	def addNeighbors(self, nbs):
		for i in range(0, len(nbs)):
			if(not nbs[i] in self.neighbors):
				self.neighbors.append(nbs[i])

	def replaceNeighbors(self, nbs):
		self.neighbors=nbs

	def removeNeighbor(self, nb):
		if(nb in self.neighbors):
			self.neighbors.remove(nb)

	def getID(self):
		return self.ID

	def getNeighbors(self):
		return self.neighbors


class Graph:

	def __init__(self, eds):
		self.size = 0
		self.nodes = []
		self.edges = []
		for i in range(0, len(eds)):
			self.addEdge(eds[i])

	def containsNode(self, name):
		for i in range(0, len(self.nodes)):
			if(self.nodes[i].getID()==name):
				return True
		return False

	def containsEdge(self, edgep):
		for e in self.edges:
			if(e.hasNodes(edgep[0], edgep[1])):
				return True

		return False

	def getNode(self, name):
		for i in range(0, len(self.nodes)):
			if(self.nodes[i].getID()==name):
				return self.nodes[i]
		newNode = Node(name)
		self.nodes.append(newNode)
		return self.nodes[len(self.nodes)-1]

	def addNode(self, name):
		newNode = Node(name)
		self.nodes.append(newNode)


	def addEdge(self, edgep):
		if(not self.containsEdge(edgep)):
			no1 = self.getNode(edgep[0])
			no2 = self.getNode(edgep[1])
			newEdge = UndirectedEdge(edgep[0], edgep[1])
			self.edges.append(newEdge)
			no1.addNeighbors([no2.getID()])
			no2.addNeighbors([no1.getID()])

	def removeEdge(self, edgep):
		for i in range(0, len(self.edges)):
			if(self.edges[i].hasNodes(edgep[0], edgep[1])):
				self.edges.pop(i)
				break
		no1 = self.getNode(edgep[0])
		no2 = self.getNode(edgep[1])
		no1.removeNeighbor(edgep[1])
		no2.removeNeighbor(edgep[0])

	def removeNode(self, name):
		no = self.getNode(name)
		nbs = no.getNeighbors()
		while(len(nbs)>0):
			self.removeEdge([name, nbs[0]])
			nbs=no.getNeighbors()
		self.nodes.remove(no)

	def updateNeighbors(self):
		#Remove all neighbors
		for i in range(0, len(self.nodes)):
			self.nodes[i].replaceNeighbors([])

		#Add new neighbors for each edge
		for i in range(0, len(self.edges)):
			currentNodes = self.edges[i].getNodes()
			no1 = self.getNode(currentNodes[0])
			no2 = self.getNode(currentNodes[1])
			no1.addNeighbors(no2.getID())
			no2.addNeighbors(no1.getID())

	def printGraph(self):
		print("\n\tNODES:")
		for i in range(0, len(self.nodes)):
			print(str(self.nodes[i].getID())+"\t"+str(self.nodes[i].getNeighbors()))
		print("\n\tEDGES:")
		for i in range(0, len(self.edges)):
			currentNodes = self.edges[i].getNodes()
			print(str(currentNodes[0])+" ---- "+str(currentNodes[1]))

	def __str__(self):
		fullstring = "\n\tNODES:\n"
		for i in range(0, len(self.nodes)):
			fullstring+=(str(self.nodes[i].getID())+"\t"+str(self.nodes[i].getNeighbors())+"\n")
		fullstring+="\n\tEDGES:\n"
		for i in range(0, len(self.edges)):
			currentNodes = self.edges[i].getNodes()
			fullstring+=(str(currentNodes[0])+" ---- "+str(currentNodes[1])+"\n")
		return fullstring


class Utils:
	def getGraph(textrep):
		tokens = textrep.split()
		if(len(tokens)%2 != 0):
			print("File not formatted correctly: detected an odd number of tokens")
			return Graph([])
		edgs = []
		i = 2
		while(i<len(tokens)-1):
			currentEdge = [tokens[i], tokens[i+1]]
			edgs.append(currentEdge)
			i+=2
		Gr = Graph(edgs)
		return Gr

	def graphToText(graph):
		totalstring = ""
		totalstring+=(str(len(graph.nodes))+"\n")
		totalstring+=(str(len(graph.edges))+"\n")
		for e in graph.edges:
			currentNodes = e.getNodes()
			totalstring+=(str(currentNodes[0])+" "+str(currentNodes[1])+"\n")

		return totalstring




