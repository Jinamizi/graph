#TODO allow Vertex of Vertices i.e a Vertex whose value is other Vertices
#TODO implement undirectional vertex

from functools import total_ordering

class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = set()

    def check(self, data):
        if not isinstance(data, Vertex) and type(data) != type(self.value):
            raise TypeError("Invalid data type. Expected {}.".format(type(self.value).__name__))
        elif isinstance(data, Vertex) and type(data.value) != type(self.value):
            raise TypeError("Invalid data type. Expected {}.".format(type(self.value).__name__))
        
        return self.vertex(data)

    def add(self, *vertices): 
        self.edges.update(map(self.check, vertices))

    def remove(self, *vertices):
        list(map(self.edges.discard, vertices)) #should remove a list of edges

    def get(self, value=None):
        if value is None:
            return list(self.edges)
        if value in self.edges:
            for vertice in self.edges:
                if vertice == value:
                    return vertice
        raise ValueError(f"{value} is not an edge")

    def __hash__(self) -> int:
        return hash(self.value)
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self.value)

    def __eq__(self, other):
        return self.value == self.vertex(other).value
    
    def __contains__(self, vertex) -> bool:
        return self.vertex(vertex) in self.edges

    @staticmethod
    def vertex(value): #return a vertex from the value or values
        return value if isinstance(value, Vertex) else Vertex(value)

     


