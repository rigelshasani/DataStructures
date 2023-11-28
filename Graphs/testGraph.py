
import unittest
from graphs3 import Graph

class A2_PartB_TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a2"""
    
    def test_init(self):
        the_graph = Graph(10)
        self.assertEqual(the_graph.num_edges(), 0)
        self.assertEqual(the_graph.num_verts(), 10)



    def test_add_vertex(self):
        the_graph = Graph(10)
        the_graph.add_vertex()
        self.assertEqual(the_graph.num_verts(), 11)
        the_graph.add_vertex()
        self.assertEqual(the_graph.num_verts(), 12)

    def test_add_edge(self):
        the_graph = Graph(10)

        rc = the_graph.add_edge(0,10)
        self.assertEqual(rc, False)

        rc = the_graph.add_edge(10, 7)
        self.assertEqual(rc, False)

        rc = the_graph.add_edge(-1,10)
        self.assertEqual(rc, False)

        rc = the_graph.add_edge(12,10)
        self.assertEqual(rc, False)

        the_graph.add_vertex()
        self.assertEqual(the_graph.num_verts(), 11)

        rc = the_graph.add_edge(0,10,5)
        self.assertEqual(rc, True)

        rc = the_graph.add_edge(10, 7)
        self.assertEqual(rc, True)

        rc = the_graph.add_edge(12,10)
        self.assertEqual(rc, False)

        rc = the_graph.add_edge(0,10)
        self.assertEqual(rc, False)

        rc = the_graph.add_edge(10, 7,3)
        self.assertEqual(rc, False)

        rc = the_graph.add_edge(7, 10, 3)
        self.assertEqual(rc, True)

        for i in range(0,10):
            rc = the_graph.add_edge(0,i)
            self.assertEqual(rc, True)

unittest.main()