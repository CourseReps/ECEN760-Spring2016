__author__ = 'pranaykumar'


import networkx as nx
import csv

# creating empty graph with no nodes and edges
undirected_Graph =nx.Graph()
directed_Graph = nx.DiGraph()

# get edges into a list from the text file
graphfile = open("../../../Graphs/Assignment1_graph4.txt")

totalnodes = int(graphfile.readline())
totaledges = int(graphfile.readline())

print totalnodes, totaledges
edge_list = []

for line in graphfile:
        edge = line.split()
        edge_list.append([int(edge[0]),int(edge[1])])

print "edge list \n", edge_list
graphfile.close()


# add edge_list to undirected and directed graphs
undirected_Graph.add_edges_from(edge_list)
directed_Graph.add_edges_from(edge_list)

undir_node_list = undirected_Graph.nodes()
dir_node_list = directed_Graph.nodes()



# calculate the maximum distance from root 0 to all other nodes in G = depth, eccentricity
depth = nx.eccentricity(undirected_Graph, 0)
print depth

# get the ancestors for each node in G.
number_of_ancestors = []
for j in dir_node_list:
    print directed_Graph.predecessors(j)
    number_of_ancestors.append( len(directed_Graph.predecessors(j)) )

#Radius is the minimum eccentricity.
print nx.radius(undirected_Graph)

# degree of a node is the number of edges that contain the node n
degree_list =[]
for j in undir_node_list:
    degree_list.append( undirected_Graph.degree(j) )
    print  undirected_Graph.degree(j)


# Nodes per level - first calculate the level for each node and store the node in corresponding level
nodes_in_level = [[] for _ in range(depth+1)]

for j in undir_node_list:
    short_path = nx.shortest_path(undirected_Graph,0,j)
    nodes_in_level[len(short_path)-1].append(j)

print nodes_in_level

totalnodes_level = []
for j in range(depth+1):
    totalnodes_level.append(len(nodes_in_level[j]))


# store attributes to a csv file
myfile = open("graph_attributes.csv", 'a')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

wr.writerow([])
wr.writerow([])
wr.writerow(["Graph4"])
wr.writerow([])
wr.writerow(["Depth", depth])

wr.writerow(["Radius",nx.radius(undirected_Graph)])

wr.writerow(["Node"] + dir_node_list)

wr.writerow(["Number of Ancestors"]+ number_of_ancestors)

wr.writerow(["Degree"] + degree_list)

wr.writerow(["Nodes_Per_Level"]+totalnodes_level)
