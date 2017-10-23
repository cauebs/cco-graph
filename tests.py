from graph import Digraph


def test_add_vertex():
    vertices = [ None ]
    g = Digraph(vertices, [])
    assert len(g) == 1

    for i in range(10):
        g.add_vertex(i)
        assert len(g) == i + 2


def test_remove_vertex():
    vertices = [ 0, 1, 2, 3 ]
    edges = [ (0, 1), (1, 2), (2, 3), (3, 0) ]
    g = Digraph(vertices, edges)

    assert len(g) == 4
    for i in g.vertices:
        assert g.successors(i) == { (i + 1) % len(g.vertices) }
        assert g.predecessors(i) == { (i - 1) % len(g.vertices) }

    g.remove_vertex(0)
    assert 0 not in g.vertices
    assert g.successors(3) == set()
    assert g.predecessors(1) == set()

    try:
        g.remove_vertex(-1)
    except Exception as e:
        if not isinstance(e, KeyError):
            raise e


def test_add_edge():
    vertices = [ 0, 1, 2, 3, 4 ]
    edges = [ (0, i) for i in range(1, 5) ]
    g = Digraph(vertices, [])

    assert g.edges == set()

    for i in edges:
        g.add_edge(*i)
    assert g.successors(0) == { 1, 2, 3, 4 }
    assert len(g.edges) == len(edges)

    for i in range(1, 5):
        assert g.predecessors(i) == { 0 }

    try:
        g.add_edge(-1, 3)
    except Exception as e:
        if not isinstance(e, KeyError):
            raise e


def test_remove_edge():
    vertices = [ 0, 1, 2, 3 ]
    edges = [ (0, 1), (1, 2), (2, 3), (3, 0) ]
    g = Digraph(vertices, edges)

    assert g.edges == set(edges)
    for i in range(4):
        assert g.successors(i) == { (i + 1) % len(vertices) }
        assert g.predecessors(i) == { (i - 1) % len(vertices) }

    g.remove_edge(0, 1)
    assert (0, 1) not in g.edges
    assert g.successors(0) == set()
    assert g.predecessors(1) == set()


def test_vertices():
    vertices = { i for i in range(10000) }
    g = Digraph(vertices, [])
    assert g.vertices == vertices


def test_edges():
    total = 100
    vertices = { i for i in range(total) }
    edges = { (i, (i+1)%total) for i in range(total) }
    g = Digraph(vertices, edges)

    assert edges == g.edges

    g.remove_edge(55, 56)
    assert edges - { (55, 56) } == g.edges


def test_len():
    vertices = { i for i in range(1000) }
    g = Digraph(vertices, [])
    assert len(vertices) == len(g)

    g.remove_vertex(1)
    assert len(vertices) - 1 == len(g)


def test_one_vertex():
    l = [ i for i in range(100) ]
    g = Digraph(l, [])

    for _ in l:
        v = g.one_vertex()
        assert v in g.vertices


def test_order():
    vertices = { i for i in range(1000) }
    g = Digraph(vertices, [])
    assert len(vertices) == g.order

    g.remove_vertex(1)
    assert len(vertices) - 1 == g.order


def test_sucessors():
    vertices = { 0, 1, 2, 3 }
    edges = { (0, 1), (0, 2), (0, 3) }
    g = Digraph(vertices, edges)

    assert g.edges == edges
    for i in range(1, 4):
        assert g.successors(i) == set()

    g.remove_edge(0, 1)
    assert g.successors(0) == { 2, 3 }


def test_predecessors():
    vertices = { 0, 1, 2, 3 }
    edges = { (0, 1), (0, 2), (0, 3) }
    g = Digraph(vertices, edges)

    assert g.edges == edges
    for i in range(1, 4):
        assert g.predecessors(i) == { 0 }

    assert g.predecessors(0) == set()

    g.remove_vertex(0)
    for i in g.vertices:
        assert g.predecessors(i) == set()
