from functools import total_ordering

class Vertex:
    def __init__(self, value) -> None:
        self.value = value
        self.edges = {}

    def check(self, value) -> Vertex:
        if not isinstance(data, Vertex) and type(data) != type(self.value):
            raise TypeError("Invalid data type. Expected {}.".format(type(self.value).__name__))
        elif isinstance(data, Vertex) and type(data.value) != type(self.value):
            raise TypeError("Invalid data type. Expected {}.".format(type(self.value).__name__))
        
        return value if isinstance(value, Vertex) else Vertex(value)

    def add_edge(self, vertex):
        #vertices = [self.check(vertice) for vertice in (vertices if isinstance(vertices, (list, tuple, set)) else iter([vertices]))]
        #condition = lambda obj: obj not in self
        #vertices = list(filter(self.__contains__, vertices))
        self.edges.add(self.check(vertex))

    def remove_edge(self, vertex):
        if vertex in self: #check if ver
            self.edges.remove(Vertex.vertex(vertex))
        raise ValueError(": Vertex.remove(vertex): vertex not in list")

    def get_vertex(self, value) -> Vertex:
        for vertice in self.edges:
            if vertice == value:
                return vertice
        return None

    def __hash__(self) -> int:
        return hash(self.value)

        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self.value)

    def __eq__(self, other):
        return self.value == Vertex.vertex(other).value
    
    def __contains__(self, vertex) -> bool:
        return Vertex.vertex(vertex) in self.edges
       # return any(v == vertex for v in self.edges)

    @classmethod
    def vertex(cls, value) -> Vertex:
        return value if isinstance(value, Vertex) else Vertex(value) 


