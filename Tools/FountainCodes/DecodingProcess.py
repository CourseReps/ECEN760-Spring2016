def peeling_iteration(variable_node_identity, variable_node_list, check_node_list, check_node_singletons):
    """
    Function peeling_iteration performs a peeling iteration by removing variable_node_identity from its of neighbors.
    It uses variable_node_list and check_node_list to access the nodes of the graph. No value is returned.

    :param variable_node_identity: Identity of variable node under consideration.
    :param variable_node_list: List of variable nodes.
    :param check_node_list: List of check nodes.
    :param check_node_singletons: Set of check nodes with degree one.
    :return: void
    """
    check_node_neighbors = variable_node_list[variable_node_identity].getneighborlist()
    for check_node_identity in check_node_neighbors:
        if check_node_identity < len(check_node_list):
            if variable_node_identity in check_node_list[check_node_identity].getneighborlist():
                check_node_list[check_node_identity].removeneighbor(variable_node_identity)
            if check_node_list[check_node_identity].getneighborcount() is 1:
                check_node_singletons.add(check_node_identity)
            elif check_node_list[check_node_identity].getneighborcount() is 0:
                check_node_singletons.discard(check_node_identity)


def continue_decoding(variable_node_list, decoded_variable_nodes, remaining_check_nodes, new_check_nodes):
    """
    Function continue_decoding performs a peeling process to decode a partially decoded graph.

    :param variable_node_list:
    :param decoded_variable_nodes:
    :param remaining_check_nodes:
    :param new_check_nodes:
    :return:
    """
    for check_node_identity in range(len(new_check_nodes)):
        for variable_node_identity in range(len(decoded_variable_nodes)):
            if decoded_variable_nodes[variable_node_identity] in new_check_nodes[check_node_identity].getneighborlist():
                new_check_nodes[check_node_identity].removeneighbor(decoded_variable_nodes[variable_node_identity])
            remaining_check_nodes.append(new_check_nodes[check_node_identity])
            check_node_neighbors = new_check_nodes[check_node_identity].getneighborlist()
            for variable_node_identity2 in range(len(check_node_neighbors)):
                variable_node_list[variable_node_identity2].addneighbor(len(remaining_check_nodes) - 1)
    return decode_graph(variable_node_list, remaining_check_nodes)


def decode_graph(variable_node_list, check_node_list):
    """
    Function decode_graph performs a peeling process to decode a graph passed in as variable_node_list and
    check_node_list. It returns a list of variable_nodes_decoded and check_nodes_remaining

    :param variable_node_list: List of variable nodes
    :param check_node_list: List of check nodes
    :return: variable_nodes_decoded and check_nodes_remaining
    """
    variable_nodes_decoded = []
    check_node_singletons = set([])
    check_nodes_remaining = []

    for check_node in check_node_list:
        if check_node.getneighborcount() is 1:
            check_node_singletons.add(check_node.getid())

    while len(check_node_singletons) is not 0:
        check_node_identity = check_node_singletons.pop()
        check_node_neighbors = check_node_list[check_node_identity].getneighborlist()
        variable_nodes_decoded.append(check_node_neighbors[0])
        peeling_iteration(check_node_neighbors[0], variable_node_list, check_node_list, check_node_singletons)

    for variable_node_identity in range(len(check_node_list)):
        if check_node_list[variable_node_identity].getneighborcount() > 1:
            check_nodes_remaining.append(check_node_list[variable_node_identity])

    return {"DecodedVariableNodes": variable_nodes_decoded, "RemainingCheckNodes": check_nodes_remaining}
