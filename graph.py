from collections import deque


class Digraph:
    def __init__(self, vertices, edges):
        self._successors = {}
        self._predecessors = {}
        for v in vertices:
            self.add_vertex(v)
        for (v, w) in edges:
            self.add_edge(v, w)

    def add_vertex(self, v):
        self._successors[v] = set()
        self._predecessors[v] = set()

    def remove_vertex(self, v):
        for w in self._predecessors[v]:
            self._successors[w].remove(v)
        self._successors.pop(v)
        self._predecessors.pop(v)

    def add_edge(self, v, w):
        if not (v in self.vertices and w in self.vertices):
            raise KeyError
        self._successors[v].add(w)
        self._predecessors[w].add(v)

    def remove_edge(self, v, w):
        if not (v in self.vertices and w in self.vertices):
            raise KeyError
        self._successors[v].remove(w)
        self._predecessors[w].remove(v)

    @property
    def vertices(self):
        return set(self._successors.keys())

    def __len__(self):
        return len(self.vertices)

    @property
    def order(self):
        return len(self)

    def one_vertex(self):
        v = self.vertices.pop()
        return v

    def successors(self, v):
        return self._successors[v]

    def predecessors(self, v):
        return self._predecessors[v]

    def indegree(self, v):
        return len(self.predecessors(v))

    def outdegree(self, v):
        return len(self.successors(v))

    def is_complete(self):
        return all(self.degree(v) >= len(self) - 1
                   for v in self.vertices)

    def transitive_closure(self, v):
        closure = set()
        pending = {v}
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

    def topological_sorting(self):
        sorting = []
        done = set()
        available = {v for v in self.vertices
                     if not self.predecessors(v)}

        while available:
            v = available.pop()
            sorting.append(v)
            done.add(v)

            for w in self.successors(v):
                if self.predecessors(w).issubset(done):
                    available.add(w)

        return sorting

    def depth_first(self, root=None):
        root = root or self.one_vertex()
        stack = deque([root])
        in_order = []
        discovered = set()

        while stack:
            v = stack.pop()
            if v not in discovered:
                discovered.add(v)
                in_order.append(v)
                for w in self.successors(v):
                    stack.append(w)

        return in_order

    def breadth_first(self, root=None):
        root = root or self.one_vertex()
        queue = deque([root])
        in_order = [root]
        discovered = {root}

        while queue:
            v = queue.popleft()
            for w in self.successors(v):
                if w not in discovered:
                    discovered.add(w)
                    in_order.append(w)
                    queue.append(w)

        return in_order
