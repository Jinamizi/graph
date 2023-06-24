import unittest
from vertice import Vertex
from graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.vertex1 = Vertex(1)
        self.vertex2 = Vertex(2)
        self.vertex3 = Vertex(3)
        self.vertex4 = Vertex(4)
        self.graph = Graph([self.vertex1, self.vertex2, self.vertex3])

    def test_add_vertices(self):
        self.assertEqual(len(self.graph.vertices), 3)

        # Add a new vertex
        self.graph.add_vertices(self.vertex4)
        self.assertEqual(len(self.graph.vertices), 4)
        self.assertIn(self.vertex4, self.graph.vertices)

        # Adding vertices of different types should raise a TypeError
        with self.assertRaises(TypeError):
            self.graph.add_vertices(self.vertex1, self.vertex2, self.vertex3, "5")

    def test_remove_vertices(self):
        self.assertEqual(len(self.graph.vertices), 3)

        # Remove an existing vertex
        self.graph.remove_vertices(self.vertex2)
        self.assertEqual(len(self.graph.vertices), 2)
        self.assertNotIn(self.vertex2, self.graph.vertices)

        # Remove a non-existing vertex should not raise an error
        self.graph.remove_vertices(self.vertex4)
        self.assertEqual(len(self.graph.vertices), 2)

    def test_add_edge(self):
        self.assertEqual(len(self.graph.get_vertex(self.vertex1).edges), 0)

        # Add an edge between vertex1 and vertex2
        self.graph.add_edge(self.vertex1, self.vertex2)
        self.assertEqual(len(self.graph.get_vertex(self.vertex1).edges), 1)
        self.assertIn(self.vertex2, self.graph.get_vertex(self.vertex1).edges)

        # Adding an edge with a vertex not in the graph should raise a ValueError
        with self.assertRaises(ValueError):
            self.graph.add_edge(self.vertex1, self.vertex4)

    def test_remove_edge(self):
        self.graph.add_edge(self.vertex1,self.vertex2)
        self.graph.add_edge(self.vertex1,self.vertex3)
        self.assertEqual(len(self.graph.get_vertex(self.vertex1).edges), 2)

        # Remove an existing edge
        self.graph.remove_edge(self.vertex1, self.vertex2)
        self.assertEqual(len(self.graph.get_vertex(self.vertex1).edges), 1)
        self.assertNotIn(self.vertex2, self.graph.get_vertex(self.vertex1).edges)

        # Remove a non-existing edge should not raise an error
        self.graph.remove_edge(self.vertex1, self.vertex4)
        self.assertEqual(len(self.graph.get_vertex(self.vertex1).edges), 1)

    def test_get_vertex(self):
        # Get an existing vertex
        vertex = self.graph.get_vertex(self.vertex1)
        self.assertEqual(vertex, self.vertex1)

        # Get a non-existing vertex should raise a ValueError
        with self.assertRaises(ValueError):
            self.graph.get_vertex(self.vertex4)


if __name__ == '__main__':
    unittest.main()
