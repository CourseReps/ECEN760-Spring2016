__author__ = 'PRANAY KUMAR EEDARA'


import networkx as nx
from networkx.algorithms import bipartite
from random import randint
import numpy as np
import math


class Decoder:

    def __init__(self,encoded_Graph,encoded_values):

        self.encoded_Graph = encoded_Graph
        self.encoded_values = encoded_values
        src_node_set, encoded_node_set = bipartite.sets(encoded_Graph)
        self.total_src_packets = len(src_node_set)


    def get_check_nodes(self,encoded_Graph):

            cur_src_node_set, cur_encoded_node_set = bipartite.sets(encoded_Graph)
            cur_encoded_node_list = list(cur_encoded_node_set)
            num_recovered_packets = self.total_src_packets - len(cur_src_node_set)

            #find check nodes in the graph
            check_node_list =[]

            for j in cur_encoded_node_list:
                if encoded_Graph.degree(j) == 1 :
                       check_node_list.append(j)
                       #print j

            return check_node_list, num_recovered_packets


    def modify_connected_nodes(self, check_node_src , check_node):

                        # 2. store the identified source node's value as check node value
                        self.decoded_src_values[check_node_src-1] = self.encoded_values[check_node-self.total_src_packets-1]

                        # 3. Identify encoded nodes connected to the identified src node
                        nodes_with_src = self.encoded_Graph.neighbors(check_node_src)
                        if len(nodes_with_src):

                            # 4. Add the src node value to the identified encoded node values
                            for k in nodes_with_src:
                                self.encoded_values[k-self.total_src_packets-1] =  (self.encoded_values[k-self.total_src_packets-1]+ self.decoded_src_values[check_node_src-1])%2

                        # 5. remove src node and check node from the graph
                        self.encoded_Graph.remove_node(check_node_src)



    def Decode(self, N):

        total_src_packets = self.total_src_packets
        self.decoded_src_values= np.zeros(self.total_src_packets)

        num_recovered_packets = 0
        recovrd_pkts_with_len = np.zeros(N+1)
        prev_utilised_nodes =0
        cur_utilised_nodes = 0 #For calculating utilised encoded nodes

        while(num_recovered_packets<(total_src_packets)):

            #get the check nodes in the graph
            check_node_list, num_recovered_packets = self.get_check_nodes(self.encoded_Graph)

            recovrd_pkts_with_len[prev_utilised_nodes:cur_utilised_nodes] = num_recovered_packets

            if len(check_node_list):

                prev_utilised_nodes = cur_utilised_nodes+1
                cur_utilised_nodes += len(check_node_list)

                # 1. find the source node of the identified check nodes
                for j in check_node_list:

                    check_node_src_list = self.encoded_Graph.neighbors(j)
                    if len(check_node_src_list):

                            self.modify_connected_nodes(check_node_src_list[0],j)

                    self.encoded_Graph.remove_node(j)

            else:
                print "case with no check node at " + str(total_src_packets-num_recovered_packets)
                return self.decoded_src_values, recovrd_pkts_with_len,cur_utilised_nodes



        return self.decoded_src_values, recovrd_pkts_with_len,cur_utilised_nodes

