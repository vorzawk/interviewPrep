class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = {}

class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, vertName):
        vertex = Vertex(vertName)
        self.vertices.append(vertex)

    def get_vertex(self, vertName):
        """ Returns the vertex if it is present in the graph, returns None if not """
        for vertex in self.vertices:
            if vertex.name == vertName:
                return vertex

    def add_edge(self, fromVertex, toVertex, weight):
        """ Add a weighted edge between fromVertex and toVertex. Raise exceptions if the vertices are not part of the graph """
        if not self.get_vertex(fromVertex):
            raise NameError('vertex {} not found in the graph'.format(fromVertex))
        if not self.get_vertex(toVertex):
            raise NameError('vertex {} not found in the graph'.format(toVertex))
        v1 = self.get_vertex(fromVertex)
        v1.edges[toVertex] = weight

    def get_vertices(self):
        return self.vertices


