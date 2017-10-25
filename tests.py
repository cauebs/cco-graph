from graph import Digraph


def test_add_vertex():
    vertices = [ None ]
    g = Digraph(vertices, [])

    assert None in g.vertices
    assert len(g) == 1

    for i in range(10):
        g.add_vertex(i)
        assert len(g) == i + 2
        assert i in g.vertices


def test_remove_vertex():
    vertices = [ 0, 1, 2, 3 ]
    edges = [ (0, 1), (1, 2), (2, 3), (3, 0) ]
    g = Digraph(vertices, edges)

    assert len(g) == 4

    g.remove_vertex(0)
    assert len(g) == 3
    assert 0 not in g.vertices
    assert len(g.edges) == 2
    assert g.edges == { (1, 2), (2, 3) }
    assert g.successors(3) == set()
    assert g.predecessors(1) == set()

    try:
        g.remove_vertex(-1)
    except Exception as e:
        if not isinstance(e, KeyError):
            raise e


def test_add_edge():
    vertices = [ 0, 1, 2, 3, 4 ]
    g = Digraph(vertices, [])

    assert g.edges == set()

    edges = { (0, i) for i in range(1, 5) }
    for i in edges:
        g.add_edge(*i)
    assert g.successors(0) == { 1, 2, 3, 4 }
    assert len(g.edges) == len(edges)
    assert g.edges == edges

    for i in range(1, 5):
        assert g.predecessors(i) == { 0 }

    try:
        g.add_edge(-1, 3)
    except KeyError as e:
        pass

    assert g.edges == edges


def test_remove_edge():
    total = 4
    vertices = [ i for i in range(total) ]
    edges = { (i, (i + 1) % total) for i in range(total) }
    g = Digraph(vertices, edges)

    assert g.edges == edges
    for i in range(total):
        assert g.successors(i) == { (i + 1) % total }
        assert g.predecessors(i) == { (i - 1) % total }

    g.remove_edge(0, 1)
    assert (0, 1) not in g.edges
    assert g.successors(0) == set()
    assert g.predecessors(1) == set()
    assert g.edges == edges - { (0, 1) }


def test_vertices():
    vertices = { i for i in range(10000) }
    g = Digraph(vertices, [])
    assert g.vertices == vertices

    g.remove_vertex(55)
    assert g.vertices == vertices - { 55 }


def test_edges():
    total = 100
    vertices = { i for i in range(total) }
    edges = { (i, (i + 1) % total) for i in range(total) }
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

    assert g.successors(0) == { 1, 2, 3 }

    g.remove_edge(0, 1)
    assert g.successors(0) == { 2, 3 }

    for i in range(1, 4):
        assert g.successors(i) == set()


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

    assert len(g.edges) == 0


def test_indegree():
    total = 10
    vertices = ( i for i in range(total) )
    edges = ( (0, i) for i in range(1, total) )
    g = Digraph(vertices, edges)

    assert g.indegree(0) == 0
    for i in range(1, total):
        assert g.indegree(i) == 1

    g.remove_vertex(0)
    for i in range(1, total):
        assert g.indegree(i) == 0


def test_outdegree():
    total = 10
    vertices = ( i for i in range(total + 1) )
    edges = ( (0, (i + 1) % total) for i in range(total) )
    g = Digraph(vertices, edges)

    assert g.outdegree(0) == total
    for i in range(1, total + 1):
        assert g.outdegree(i) == 0

    g.remove_vertex(1)
    assert g.outdegree(0) == total - 1

    assert g.outdegree(5) == 0


def test_is_complete():
    total = 100
    vertices = { 0, 1, 2 }
    edges = { (0, 1), (0, 2), (1, 2) }
    loops = { (0, 0), (1, 1), (2, 2) }
    g = Digraph(vertices, edges)

    assert g.is_complete() == True

    g.remove_edge(0, 1)
    g.remove_edge(1, 0)
    assert g.is_complete() == False


def test_transitive_closure():
    vertices = { 0, 1, 2, 3 }
    edges = [ (0, 1), (0, 2), (0, 3) ]
    g = Digraph(vertices, edges)

    assert g.transitive_closure(0) == vertices

    g.remove_edge(0, 1)
    assert g.transitive_closure(0) == vertices - { 1 }
    assert g.transitive_closure(1) == { 1 }


def test_is_connected():
    vertices = { 0, 1, 2, 3 }
    edges = [ (0, 1), (0, 2), (0, 3) ]
    g = Digraph(vertices, edges)

    assert g.is_connected() == True

    g.remove_edge(0, 1)
    assert g.is_connected() == False


def test_is_tree():
    vertices = { 0, 1, 2, 3, 4, 5 }
    edges = [ (0, 1), (0, 2), (1, 3), (3, 4), (4, 5) ]
    g = Digraph(vertices, edges)

    assert g.is_tree() == True

    g.add_edge(5, 0)
    assert g.is_tree() == False
    g.remove_edge(5, 0)
    assert g.is_tree() == True


def test_topological_sorting():
    vertices = { 0, 1, 2, 3, 4, 5 }
    edges = [ (0, 1), (0, 2), (1, 4), (4, 3), (3, 5) ]
    g = Digraph(vertices, edges)

    assert g.topological_sorting() == [ 0, 1, 2, 4, 3, 5 ]


def test_depth_first():
    vertices = { 0, 1, 2, 3, 4 }
    edges = { (0, 1), (1, 2), (2, 3), (2, 4) }
    g = Digraph(vertices, edges)


    assert set(g.depth_first()) == vertices
    assert g.depth_first(0) in ( [ 0, 1, 2, 3, 4 ], [ 0, 1, 2, 4, 3 ] )
    assert g.depth_first(3) == [ 3 ]
    assert g.depth_first(4) == [ 4 ]

    g.remove_edge(0, 1)
    assert g.depth_first(0) == [ 0 ]
    assert g.depth_first(1) in ( [ 1, 2, 3, 4 ], [ 1, 2, 4, 3 ] )


def test_breadth_first():
    vertices = { 0, 1, 2, 3, 4 }
    edges = { (0, 1), (0, 2), (2, 3), (2, 4) }
    g = Digraph(vertices, edges)


    assert set(g.breadth_first()) == vertices
    assert g.breadth_first(0) in ( [ 0, 1, 2, 3, 4 ], [ 0, 2, 1, 3, 4 ],
                                   [ 0, 1, 2, 4, 3 ], [ 0, 2, 1, 4, 3 ] )
    assert g.breadth_first(2) in ( [ 2, 3, 4 ], [ 2, 4, 3 ] )
    assert g.breadth_first(3) == [ 3 ]
    assert g.breadth_first(4) == [ 4 ]

    g.remove_edge(0, 1)
    assert g.breadth_first(0) == [ 0, 2, 3, 4 ]
    assert g.breadth_first(1) == [ 1 ]
