from graph import Graph
from curriculum import courses


def semesters(graph, done=None, max_hours=30):
    semester = []
    total = 0
    done = done or set()
    available = {v for v in graph.vertices
                 if not graph.predecessors(v)}

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
    cco = Graph(courses, {(r, c)
                          for c in courses
                          for r in c.requirements})

    for semester in semesters(cco):
        print(sum(c.hours for c in semester))
        for course in semester:
            print(course.hours, course.code, course.name)
        print()
