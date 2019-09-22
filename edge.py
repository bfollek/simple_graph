class Edge:

    def __init__(self, u: int, v:int):
        self.u = u  # the "from" vertex
        self.v = v  # the "to" vertex

    def reversed(self):
        return Edge(self.v, self.u)

    def __str__(self):
        return f"{self.u} -> {self.v}"

    def __repr__(self):
        return f"Edge(u={self.u}, v={self.v})"
