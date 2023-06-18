#TODO LowestCostFrom(node, to:Node)

from vertice import Vertice  
class Graph:
    def __init__(self, vertices = None):
        self.vertices = []
        if vertices:
            vertices = vertices if isinstance(vertices, (list, tuple, set)) else iter([vertices]) #convert to an iter
            if len({type(vertice) for vertice in vertices} != 1): #check if all elements are of the same type
                raise TypeError("Vertices need to be of the same type")
            self.vertices = vertices if isinstance(vertices[0], Vertice) else list(map(Vertice, vertices)) 

    def add(self, vertices):
        vertices = vertices if isinstance(vertices, (list, tuple, set)) else iter([vertices]) #convert to an iter
        if self.vertices:
            self.vertices.extend(list(map(ver)))
        if len({type(vertice) for vertice in vertices} != 1): #check if all elements are of the same type
            raise TypeError("Vertices need to be of the same type")
        self.vertices = vertices if isinstance(vertices[0], Vertice) else list(map(Vertice, vertices))
