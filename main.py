from graph import Digraph
from cco import Curriculum


def semesters(graph, done=None, max_hours=30):
    """
    Considere um grafo cujos vértices são disciplinas de um currículo e cujas
    arestas (v, w) indicam que ter sido aprovado em v é pré-requisito para
    cursar w. Esta função gera uma sequência de semestres respeitando os
    pré-requisitos e o máximo de horas-aula por semestre. Adicionalmente, ela
    aceita como parâmetro um conjunto de disciplinas já cursadas. O algoritmo
    usado é uma versão do algoritmo de Kahn modificada para respeitar as
    restrições impostas pelo problema em questão. O não-determinismo da função
    é consequência da implementação de conjuntos no Python.
    """

    # pequena otimização: mantém-se uma contagem de horas no semestre atual
    # para que não seja necessário calculá-la em cada iteração
    total = 0
    semester = []
    done = set(done or [])

    # disciplinas disponíveis para serem cursadas: todas do currículo cujos
    # pré-requisitos são um subconjunto das já cursadas, exceto elas próprias
    available = {v for v in graph.vertices - done
                 if graph.predecessors(v).issubset(done)}

    while available:
        v = available.pop()
        semester.append(v)
        total += v.hours

        # checamos se não há mais disciplinas disponíveis para este semestre
        # ou se todas as disponíveis têm uma carga horária grande demais
        if not available or all(total + v.hours >= max_hours
                                for v in available):
            # adicionamos as disciplinas do semestre ao conjunto das cursadas
            done.update(semester)

            # verificamos se as disciplinas desbloquearam outras disciplinas
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
    cco_graph = Digraph(vertices, edges)

    for i, semester in enumerate(semesters(cco_graph)):
        print(f'{i+1}º Semestre ({sum(c.hours for c in semester)} horas)')
        for course in semester:
            print(f'   [{course.code}] {course.name}')
        print()
