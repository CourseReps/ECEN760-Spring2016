import DecodingProcess
import GraphGeneration

graph = GraphGeneration.idealsolitongraph(1200, 1000)

check_node_list = graph["CheckNodes"]
variable_node_list = graph["VariableNodes"]

print "Number of Check Nodes: " + repr(len(check_node_list))
print "Number of Variable Nodes: " + repr(len(variable_node_list))

NoNeighbors = 0
for checknode in check_node_list:
    if checknode.getneighborcount() is 0:
        print "Empty Check Node ID: " + repr(checknode.getid())
        NoNeighbors += 1
print "Empty space: " + repr(NoNeighbors)

results = DecodingProcess.decode_graph(variable_node_list, check_node_list)
variable_nodes_decoded = results["DecodedVariableNodes"]
check_nodes_remaining = results["RemainingCheckNodes"]

print " ******************************** \n\n"
print repr(sorted(variable_nodes_decoded)) + "\n"
print repr((float(len(variable_nodes_decoded)) / float(len(variable_node_list))))
