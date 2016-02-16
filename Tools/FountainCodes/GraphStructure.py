class VariableNode:
    """
    A variable node contains an information symbol.
    """

    def __init__(self, variablenodeid, neighborlist=None):
        self.__ID = variablenodeid
        self.__NeighborList = []

        if neighborlist is not None:
            self.__NeighborList = neighborlist

    def getid(self):
        return self.__ID

    def getneighborcount(self):
        return len(self.__NeighborList)

    def getneighborlist(self):
        return self.__NeighborList

    def setneighborlist(self, neighborlist):
        self.__NeighborList = neighborlist

    def removeneighbor(self, variablenode):
        self.__NeighborList.remove(variablenode)

    def addneighbor(self, neighbor):
        self.__NeighborList.append(neighbor)


class CheckNode:
    """
    A check node represents a coded symbol.
    """

    def __init__(self, checknodeid, neighborlist=None):
        self.__ID = checknodeid
        self.__NeighborList = []

        if neighborlist is not None:
            self.__NeighborList = neighborlist

    def getid(self):
        return self.__ID

    def getneighborcount(self):
        return len(self.__NeighborList)

    def getneighborlist(self):
        return self.__NeighborList

    def setneighborlist(self, neighborlist):
        self.__NeighborList = neighborlist

    def removeneighbor(self, checknode):
        self.__NeighborList.remove(checknode)

    def addneighbor(self, neighbor):
        self.__NeighborList.append(neighbor)
