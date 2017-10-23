from graph import Graph
from cco import Curriculum


def semesters(graph, done=None, max_hours=30):
    semester = []
    total = 0
    done = done or set()
    available = {v for v in graph.vertices - done
                 if graph.predecessors(v).issubset(done)}

    while available:
        v = available.pop()
        semester.append(v)
        total += v.hours

        if not available or all(total + v.hours >= max_hours
                                for v in available):
            done.update(semester)
            for r in semester:
                for c in graph.successors(r) - done:
                    if graph.predecessors(c).issubset(done):
                        available.add(c)

            yield semester.copy()
            semester.clear()
            total = 0


if __name__ == '__main__':
    vertices = {c.value for c in Curriculum}
    edges = {(r, c) for c in vertices for r in c.requirements}
    cco_graph = Graph(vertices, edges)

    for i, semester in enumerate(semesters(cco_graph)):
        print(f'{i+1}º Semestre ({sum(c.hours for c in semester)} horas)')
        for course in semester:
            print(f'   [{course.code}] {course.name}')
        print()
