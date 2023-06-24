#TODO LowestCostFrom(node, to:Node)
# Add a vertex/node: Add a new vertex or node to the graph.
# Remove a vertex/node: Remove an existing vertex or node from the graph.
# Add an edge: Create a connection between two vertices in the graph, forming an edge.
# Remove an edge: Remove the connection between two vertices, removing an edge from the graph.
# Check if a vertex/node exists: Verify if a specific vertex or node exists in the graph.
# Check if an edge exists: Determine if an edge exists between two given vertices.
# Get the neighbors of a vertex: Retrieve the adjacent vertices connected to a specific vertex.
# Get the degree of a vertex: Count the number of edges incident to a particular vertex.
# Find a path between two vertices: Discover a path that connects two given vertices in the graph.
# Perform graph traversal: Traverse or visit all the vertices in the graph, such as Depth-First Search (DFS) or Breadth-First Search (BFS).

from vertice import Vertex  

class Graph:
    def __init__(self, vertices:list = None):
        self.vertices = set() #ensure unique vertices
        
        if vertices :
            self.add_vertices(*vertices)

    def add_vertices(self, *vertices):
        if len({type(vertice) for vertice in vertices}) != 1: #check if all elements are of the same type
            raise TypeError("Vertices need to be of the same type")
                
        self.vertices.update(map(Vertex.vertex, vertices))

    def remove_vertices(self, *vertices):
            for vertex in vertices:
                for edge in [edge for edge in self.vertices if vertex in edge]:
                    edge.remove(vertex)

            list(map(self.vertices.discard, vertices))

    def add_edge(self, vertex1, vertex2):#add adds an edge from vertex1 to the vertex2
        self.get_vertex(vertex1).add(vertex2) if vertex2 in self else raise ValueError(f"{vertex2} not in graph")

    def remove_edge(self, vertex1, vertex2):#remove edge between vertex1 and vertex2
        self.get_vertex(vertex1).remove(vertex2)

    def check_edge(self, vertex1, vertex2):#Determine if an edge exists between two given vertices.
        return vertex2 in self.get_vertex(vertex1)

    def get_neighbors(self, vertex): #etrieve the adjacent vertices connected to a specific vertex.
        return self.get_vertex(vertex).get()
    
    def path(self, vertex1, vertex2):
        v1 = self.get_vertex(vertex1)
        v2 = self.get_vertex(vertex2)


    def get_vertex(self, value):
        if value not in self:
            raise ValueError(f"{value} is not in list")
        for vertex in self.vertices:
            if vertex == value:
                return vertex    

    def check(self, value):
        if self.vertices:
            for sample in self.vertices:
                return sample.check(value)
        else:
            return Vertex.vertex(value)

    def __contains__(self, vertex) -> bool:
        return Vertex.vertex(vertex) in self.vertices
    
    def __str__(self):
        return str(self.vertices)
    
    def __repr__(self) -> str:
        return str(self.vertices)
    
    @staticmethod
    def get_path(vertex1, vertex2): #Find a path between two vertices: Discover a path that connects two given vertices in the graph.
        path = [vertex1]
        if vertex1 != vertex2: