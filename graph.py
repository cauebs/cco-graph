from collections import defaultdict


class Graph:
    def __init__(self, vertices, edges=None):
        self.vertices = set(vertices)
        self._edges = defaultdict(set)
        self._reversed_edges = defaultdict(set)
        for (v, w) in edges or {}:
            self.add_edge(v, w)

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def remove_vertex(self, vertex):
        self._edges.pop(vertex)
        for w in self._reversed_edges[vertex]:
            self.remove_edge(w, vertex)
        self.vertices.remove(vertex)

    def add_edge(self, v, w):
        self._edges[v].add(w)
        self._reversed_edges[w].add(v)

    def remove_edge(self, v, w):
        self._edges[v].remove(w)
        self._reversed_edges[w].remove(v)

    def __len__(self):
        return len(self.vertices)

    def one_vertex(self):
        for v in self.vertices:
            return v

    def successors(self, vertex):
        return self._edges[vertex]

    def predecessors(self, vertex):
        return self._reversed_edges[vertex]

    def adjacents(self, vertex):
        return set.union(self.predecessors(vertex),
                         self.successors(vertex))

    def indegree(self, vertex):
        return len(self.predecessors(vertex))

    def outdegree(self, vertex):
        return len(self.successors(vertex))

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
                for w in self.successors(v):
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
                for w in self.successors(v):
                    pending.add(w)
        return True
