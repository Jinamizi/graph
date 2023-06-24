import unittest
from vertice import Vertex

class VerticeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.v1 = Vertex(1)
        cls.v2 = Vertex(2)
        cls.v3 = 3
        cls.v4 = Vertex("test")
        cls.v5 = "test"

    def test_add_and_remove_edge(self):        
        self.v1.add(self.v2)
        self.v1.add(self.v3)
        
        self.assertIn(self.v2, self.v1, "V2 should be in v1")
        self.assertIn(self.v3, self.v1, "V3 should be in v1")
        self.assertRaises(TypeError, self.v1.add, self.v4, "Should not accept vertext with different value")
        self.assertRaises(TypeError, self.v1.add, "test", "Should not accept value with different value")

        self.v1.remove(self.v2)
        self.v1.remove(self.v3)
        self.assertNotIn(self.v2, self.v1, "V2 should have been removed")
        self.assertNotIn(self.v3, self.v1, "V2 should have been removed")
        self.assertRaises(ValueError, self.v1.remove, "test")
    
    def test_ordering(self):        
        self.assertEqual(self.v1, self.v1)
        self.assertNotEqual(self.v1, self.v2)

if __name__ == '__main__':
    unittest.main()
