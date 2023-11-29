import sys
sys.path.append('..')
from LinkedLists.doublyLinked import DoublyLinked
class Graph:
    #i gotta create a list which looks like this: [[Edge, [Connections]]]
    def __init__(self, number_of_verts):
        self.edgeNo = 0
        self.vertNo = number_of_verts
        self.list = []
        self.size = 0

        for i in range(0, number_of_verts):
            node = [i, DoublyLinked()]
            self.list = self.list + [node]
            self.size += 1
        print(self.list)

    def add_vertex(self):
        node = [self.vertNo, DoublyLinked()]
        self.vertNo += 1
        self.size += 1
        self.list = self.list + [node]


    def add_edge(self, from_idx, to_idx, weight=1):
        #if either of the vertices are invalid, or edge exists, return False do nothing                
        self.show_list()
        flag1 = False
        flag2 = False
        copy1 = None
        for i in self.list:
            if i[0] == from_idx:
                flag1 = True
                copy1 = i[0]
            if i[0] == to_idx:
                flag2 = True
        if(not(flag1 and flag2)):
            return False

        #now we need to know if the edge exists
        #we need to search the linked list for the edge
        if self.list[copy1][1].search(to_idx) is not None:
            return False        
        #otherwise, create directed edge and return true

        self.list[copy1][1].push_back([to_idx, weight])
        self.edgeNo += 1
        return True
    
    def num_edges(self):
        return self.edgeNo
    def num_verts(self):
        return self.vertNo
    
    def edge_weight(self, from_idx, to_idx):
        pass

    def show_list(self):
        for i in self.list:
            print(i[0], i[1])
        print()

    def has_edge(self, from_idx, to_idx):
        if from_idx >= self.vertNo or to_idx >= self.vertNo:
            return False

        for vertex, edges in self.list:
            if vertex == from_idx:
                return edges.search(to_idx) is not None

        return False
    
    def edge_weight(self, from_idx, to_idx):
        if from_idx >= self.vertNo or to_idx >= self.vertNo:
            return None

        for vertex, edges in self.list:
            if vertex == from_idx:
                edge = edges.search(to_idx)
                return None if edge is None else edge[1]  # Return the weight if the edge exists

        return None
    
    def get_connected(self, v):
        
        if v >= self.vertNo:
            return []
        
        connected = []
        connectedListSize = 0
        for vertex, edges in self.list:
            if vertex == v:
                current = edges.head
                while current is not None:
                    connected = connected + [(current.data[0], current.data[1])]
                    current = current.next
                    connectedListSize += 1

        return connected





