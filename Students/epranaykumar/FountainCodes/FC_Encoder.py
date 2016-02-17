__author__ = 'PRANAY KUMAR EEDARA'


import networkx as nx
from networkx.algorithms import bipartite
from random import randint
import numpy as np
import math


class Encoder:

    def __init__(self,src_values,err_bound, c):

        self.src_values = src_values
        self.err_bound = err_bound
        self.c = c
        self.total_src_packets = len(src_values)


    def get_ideal_distribution(self,total_src_packets):

        # for the ideal distribution, calculate the probabilities for K number of degrees
        ideal_distribution = [1.0/total_src_packets]
        for i in range(2,total_src_packets+1):
            probability_i = 1.0/(i*(i-1))
            ideal_distribution.append(probability_i)

        return ideal_distribution


    def get_robust_distribution(self, total_src_packets,err_bound, c):

        # for the robust distribution, calculate the probabilities for K number of degrees
        robust_factor = c*math.log(total_src_packets/err_bound)* math.sqrt(total_src_packets)
        robust_distribution = []

        for i in range(1,total_src_packets+1):
            if i<(total_src_packets/float(robust_factor)):
                  probability_i = robust_factor/float((total_src_packets*i))

            elif i == (total_src_packets/float(robust_factor)):
                  probability_i = (robust_factor/float(total_src_packets))*math.log(robust_factor/err_bound)
            else :
                  probability_i = 0.0

            robust_distribution.append(probability_i)

        return robust_distribution


    def get_degree_distribution(self,total_src_packets,err_bound, c):

        ideal_distribution = self.get_ideal_distribution(total_src_packets)
        robust_distribution = self.get_robust_distribution(total_src_packets,err_bound, c)

        degree_distribution = np.array(ideal_distribution) + np.array(robust_distribution)
        degree_distribution = np.cumsum(degree_distribution)

        return degree_distribution


    def Encode(self, N):

        total_src_packets = self.total_src_packets

        #get degree distribution
        degree_distribution = self.get_degree_distribution(self.total_src_packets,self.err_bound, self.c)

        # generate N encoded values
        src_nodes = range(1,total_src_packets+1)
        encoded_nodes = range(total_src_packets+1, total_src_packets+N+1)

        #print src_nodes
        #print encoded_nodes
        # creating bipartite graph with src nodes  and encoded nodes
        encoded_Graph = nx.Graph()
        encoded_Graph.add_nodes_from(encoded_nodes, bipartite=0) # Add the node attribute "bipartite"
        encoded_Graph.add_nodes_from(src_nodes, bipartite=1)

        #encoded values
        encoded_values=[]

        for i in encoded_nodes:
            ## choosing random degree according to the distribution
            random_degree = np.argmax(degree_distribution>np.random.uniform(0,1)) + 1
            #print i
            ## pick random source nodes uniformly
            edge_list = [(i,randint(1,total_src_packets)) for p in range(random_degree)]
            #print edge_list
            encoded_Graph.add_edges_from(edge_list)

            ## assign encode value
            sum=0
            for j in range(0,random_degree):
                sum = sum + self.src_values[edge_list[j][1]-1]

            encoded_values.append(sum%2)

        #print bipartite.sets(encoded_Graph)

        # check whether the source nodes have atleast one encoded node
        for j in src_nodes:
                if encoded_Graph.degree(j) == 0 :
                     print "Source Nodes left empty",j
                     encoded_Graph.add_edge(randint(total_src_packets+1, total_src_packets+N),j)

        #print bipartite.sets(encoded_Graph)

        return encoded_Graph, encoded_values
