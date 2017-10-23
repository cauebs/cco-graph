from collections import defaultdict, deque


class Digraph:
    def __init__(self, vertices, edges=None):
        self.vertices = set(vertices)
        self._successors = defaultdict(set)
        self._predecessors = defaultdict(set)
        for (v, w) in edges or {}:
            self.add_edge(v, w)

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def remove_vertex(self, vertex):
        self._successors.pop(vertex)
        self._predecessors.pop(vertex)
        for w in self._predecessors[vertex]:
            self.remove_edge(w, vertex)
        self.vertices.remove(vertex)

    def add_edge(self, v, w):
        self._successors[v].add(w)
        self._predecessors[w].add(v)

    def remove_edge(self, v, w):
        self._successors[v].remove(w)
        self._predecessors[w].remove(v)

    def __len__(self):
        return len(self.vertices)

    def order(self):
        return len(self)

    def one_vertex(self):
        v = self.vertices.pop()
        self.vertices.add(v)
        return v

    def successors(self, vertex):
        return self._successors[vertex]

    def predecessors(self, vertex):
        return self._predecessors[vertex]

    def indegree(self, vertex):
        return len(self.predecessors(vertex))

    def outdegree(self, vertex):
        return len(self.successors(vertex))

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
