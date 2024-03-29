from os import path
from typing import Generic, List, Optional, TypeVar
from data_structures.simple_graph.edge import Edge

# https://mypy.readthedocs.io/en/latest/generics.html#defining-generic-classes
V = TypeVar('V')  # type of the vertices in the graph
class Graph(Generic[V]):

    def __init__(self, vertices: List[V]=None):
        self._vertices = vertices if vertices else []
        """
        'Our specific representation uses a list of lists of edges, so for
        every vertex there is a list of edges via which the vertex is connected to other vertices.
        _edges is this list of lists.'
        """
        self._edges: List[List[Edge]] = [[] for _ in self._vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)  # Number of vertices

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))  # Number of edges

    @property
    def vertices(self) -> List[V]:
        return self._vertices

    # Add a vertex to the graph and return its index
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])  # Add empty list for containing edges
        return self.vertex_count - 1  # Return index of added vertex

    # This is an undirected graph, so we always add edges in both directions
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # Add an edge using vertex indices (convenience method)
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge = Edge(u, v)
        self.add_edge(edge)

    # Add an edge by looking up vertex indices (convenience method)
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u = self._vertices.index(first)
        v = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # Find the vertex at a specific index
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    # Find the index of a vertex in the graph
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    # Find the vertices that a vertex at some index is connected to
    def neighbors_for_index(self, index) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    # Look up a vertice's index and find its neighbors (convenience method)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    # Return all of the edges associated with a vertex at some index
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    # Look up the index of a vertex and return its edges (convenience method)
    def edges_for_vertex(self, vertex) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    # Make it easy to pretty-print a Graph
    def __str__(self) -> str:
        desc = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc

    def dump(self, file_name: str = None) -> None:
        s = ""
        for v in sorted(self._vertices):
            s += f"{v}\n"
            edges = sorted(self.vertex_at(e.v)
                           for e in self.edges_for_vertex(v))
            for edge in edges:
                s += f"\t-> {edge}\n"
        if file_name:
            # If there's a tilde, expand it, else no change
            file_name = path.expanduser(file_name)
            with open(file_name, 'w') as f:
                f.write(s)
        else:
            print(s)


class Digraph(Graph):

    # This is a directed graph, so we add edges in just one direction.
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
