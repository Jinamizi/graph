import unittest
from functools import total_ordering
from vertice import Vertex

@total_ordering
class VerticeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        v1 = Vertex(1)
        v2 = Vertex(2)
        v3 = 3
        v4 = Vertex("test")
        v5 = test

    def test_add_and_remove_edge(self):        
        self.v1.add_edge(v2)
        self.v1.add_edge(v3)
        
        self.assertIn(self.v2, self.v1, "V2 should be in v1")
        self.assertIn(self.v3, self.v1, "V3 should be in v1")
        self.assertRaises(TypeError, self.v1.add_edge, v4, "Should not accept vertext with different value")
        self.assertRaises(TypeError, self.v1.add_edge, "test", "Should not accept vertext with different value")

        self.v1.remove_edge(v2)
        self.v1.remove_edge(v3)
        self.assertNotIn(self.v2, self.v1, "V2 should have been removed")
        self.assertNotIn(self.v3, self.v1, "V2 should have been removed")
        self.assertRaises(ValueError, self.v1.remove_edge, "test", "Should Raise Value error for value with no edge")
    
    def test_ordering(self):        
        self.assertEqual(self.v1, self.v1)
        self.assertNotEqual(self.v1, self.v2)

if __name__ == '__main__':
    unittest.main()
