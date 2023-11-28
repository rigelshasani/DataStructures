import sys
sys.path.append('..')
from LinkedLists.doublyLinked import DoublyLinked
class Graph:
    #i gotta create a list which looks like this: [[Edge, [Connections]]]
    def __init__(self, number_of_verts):
        self.edgeNo = 0
        self.vertNo = number_of_verts
        self.list = []

        for i in range(0, number_of_verts):
            node = [i, DoublyLinked()]
            self.list.append(node)

    def add_vertex(self):
        self.vertNo += 1
        node = [self.vertNo, DoublyLinked()]
        self.list.append(node)

    def add_edge(self, from_idx, to_idx, weight=1):
        #if either of the vertices are invalid, or edge exists, return False do nothing                
        flag1 = False
        flag2 = False
        copy1 = None
        for i in self.list:
            if i[0] == from_idx:
                flag1 = True
                copy1 = i[0]
            elif i[0] == to_idx:
                flag2 = True
        if(not(flag1 and flag2)):
            return False
        #now we need to know if the edge exists
        #we need to search the linked list for the edge
        if self.list[copy1][1].search(to_idx) == True:
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
            print(i)
        print()


graph1 = Graph(5)
graph1.show_list()
graph1.add_vertex()
graph1.show_list()


