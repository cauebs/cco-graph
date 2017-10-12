from graph import Graph
from curriculum import courses


cco = Graph(courses, {(r, c)
                      for c in courses
                      for r in c.requirements})
