from collections import defaultdict


class Graph:
    def __init__(self, vertices, edges=None, directed=True):
        self.vertices = set(vertices)
        self._directed = directed

        self._successors = defaultdict(set)
        self._predecessors = defaultdict(set)
        for (v, w) in edges or {}:
            self.add_edge(v, w)

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def remove_vertex(self, vertex):
        for w in self._predecessors[vertex]:
            self.remove_edge(w, vertex)
        for w in self._successors[vertex]:
            self.remove_edge(vertex, w)
        self.vertices.remove(vertex)

    def add_edge(self, v, w):
        if not (v in self.vertices and w in self.vertices):
            raise KeyError

        self._successors[v].add(w)
        self._predecessors[w].add(v)

        if not self._directed:
            self._successors[w].add(v)
            self._predecessors[v].add(w)

    def remove_edge(self, v, w):
        self._successors[v].remove(w)
        self._predecessors[w].remove(v)

        if not self._directed:
            self._successors[w].remove(v)
            self._predecessors[v].remove(w)

    def __len__(self):
        return len(self.vertices)

    def one_vertex(self):
        v = self.vertices.pop()
        self.vertices.add(v)
        return v

    def successors(self, vertex):
        return self._successors[vertex]

    def predecessors(self, vertex):
        return self._predecessors[vertex]

    def adjacents(self, vertex):
        return set.union(self._successors[vertex],
                         self._predecessors[vertex])

    def indegree(self, vertex):
        return len(self._predecessors[vertex])

    def outdegree(self, vertex):
        return len(self._successors[vertex])

    def degree(self, vertex):
        return len(self.adjacents(vertex))

    def is_regular(self):
        return len({self.degree(v) for v in self.vertices}) == 1

    def is_complete(self):
        return all(self.degree(v) >= len(self) - 1
                   for v in self.vertices)

    def transitive_closure(self, vertex):
        closure = set()
        pending = {vertex}
        while pending:
            v = pending.pop()
            if v not in closure:
                closure.add(v)
                for w in self._successors[v]:
                    pending.add(w)
        return closure

    def is_connected(self):
        return self.transitive_closure(self.one_vertex()) == self.vertices

    def is_tree(self):
        visited = set()
        pending = {self.one_vertex()}
        while pending:
            v = pending.pop()
            if v in visited:
                return False
            else:
                visited.add(v)
                for w in self._successors[v]:
                    pending.add(w)
        return True


if __name__ == '__main__':
    vertices = {(x, y)
                for x in range(8)
                for y in range(8)}

    edges = {(v, w)
             for v in vertices
             for w in vertices
             if abs(v[0] - w[0]) == 1 and abs(v[1] - w[1]) == 2
             or abs(v[0] - w[0]) == 2 and abs(v[1] - w[1]) == 1}

    g = Graph(vertices, edges, directed=False)
