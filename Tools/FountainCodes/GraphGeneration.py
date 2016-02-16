import GraphStructure
import random
import math


def randsoliton(parameter_max_int):
    """
    Method randsoliton requires one argument, parameter_max_int, and returns a random integer that is generated
    according to the ideal soliton distribution. This method relies on random.random() and math.ceil().
    :param parameter_max_int: Maximum integer for soliton distribution
    :return: Random integer according to ideal soliton distribution
    """
    randuniform = random.random()
    if randuniform is 0.0:
        return 1
    else:
        inversevalue = int(math.ceil(1 / randuniform))
        if inversevalue <= parameter_max_int:
            return inversevalue
        else:
            return 1


def idealsolitongraph(number_check_nodes, number_variable_nodes):
    """
    Method idealsolitongraph returns a dictionary containing the check nodes and variable nodes created by
    generating a graph with numCheckNodes check nodes and numVariableNodes variable nodes.
    :param number_check_nodes: Number of check nodes
    :param number_variable_nodes: Number of variable nodes
    :return: Soliton graph with soliton variable-node degree distribution and IID assignment
    """
    # Create list of VariableNodes and CheckNodes
    variable_node_list = list(GraphStructure.VariableNode(i) for i in range(0, number_variable_nodes))
    check_node_list = list(GraphStructure.CheckNode(i) for i in range(0, number_check_nodes))
    for node_identity in range(0, number_check_nodes):
        number_neighbors = randsoliton(number_variable_nodes)
        random_neighbors = random.sample(variable_node_list, number_neighbors)
        for neighbor in random_neighbors:
            check_node_list[node_identity].addneighbor(neighbor.getid())
            variable_node_list[neighbor.getid()].addneighbor(node_identity)
    return {"CheckNodes": check_node_list, "VariableNodes": variable_node_list}

