from enum import Enum
from typing import NamedTuple, Tuple


class Course(NamedTuple):
    code: str
    name: str
    hours: int
    requirements: Tuple['Course']

    def __repr__(self):
        return self.code


class Curriculum(Enum):
    EEL5105 = Course('EEL5105',
                     'Circuitos e Técnicas Digitais', 5, ())

    INE5401 = Course('INE5401',
                     'Introdução à Computação', 2, ())

    INE5402 = Course('INE5402',
                     'Programação Orientada a Objetos I', 6, ())

    INE5403 = Course('INE5403',
                     'Fundamentos de Matemática Discreta para COMPUTAÇÃO', 6, ())

    MTM3100 = Course('MTM3100',
                     'Pré-Cálculo', 4, ())

    MTM3101 = Course('MTM3101',
                     'Cálculo 1', 4, (MTM3100,))

    INE5404 = Course('INE5404',
                     'Programação Orientada a Objetos II', 6, (INE5402,))

    INE5405 = Course('INE5405',
                     'Probabilidade e Estatística', 5, (MTM3101,))

    INE5406 = Course('INE5406',
                     'Sistemas Digitais', 5, (EEL5105,))

    INE5407 = Course('INE5407',
                     'Ciência, Tecnologia e Sociedade', 3, ())

    MTM3102 = Course('MTM3102',
                     'Cálculo 2', 4, (MTM3101,))

    MTM5512 = Course('MTM5512',
                     'Geometria Analítica', 4, ())

    INE5408 = Course('INE5408',
                     'Estruturas de Dados', 6, (INE5404,))

    INE5409 = Course('INE5409',
                     'Cálculo Numérico para Computação', 4, (MTM5512, MTM3102))

    INE5410 = Course('INE5410',
                     'Programação Concorrente', 4, (INE5404,))

    INE5411 = Course('INE5411',
                     'Organização de Computadores I', 6, (INE5406,))

    MTM5245 = Course('MTM5245',
                     'Álgebra Linear', 4, (MTM5512,))

    INE5412 = Course('INE5412',
                     'Sistemas Operacionais I', 4, (INE5410, INE5411))

    INE5413 = Course('INE5413',
                     'Grafos', 4, (INE5403, INE5408))

    INE5414 = Course('INE5414',
                     'Redes de Computadores I', 4, (INE5404,))

    INE5415 = Course('INE5415',
                     'Teoria da Computação', 4, (INE5403, INE5408))

    INE5416 = Course('INE5416',
                     'Paradigmas de Programação', 5, (INE5408,))

    INE5417 = Course('INE5417',
                     'Engenharia de Software I', 5, (INE5408,))

    INE5418 = Course('INE5418',
                     'Computação Distribuída', 4, (INE5412, INE5414))

    INE5419 = Course('INE5419',
                     'Engenharia de Software II', 4, (INE5417,))

    INE5420 = Course('INE5420',
                     'Computação Gráfica', 4, (INE5408, MTM3102, MTM5245))

    INE5421 = Course('INE5421',
                     'Linguagens Formais e Compiladores', 4, (INE5415,))

    INE5422 = Course('INE5422',
                     'Redes de Computadores II', 4, (INE5414,))

    INE5423 = Course('INE5423',
                     'Banco de Dados I', 4, (INE5408,))

    INE5424 = Course('INE5424',
                     'Sistemas Operacionais II', 4, (INE5412,))

    INE5425 = Course('INE5425',
                     'Modelagem e Simulação', 4, (INE5405,))

    INE5426 = Course('INE5426',
                     'Construção de Compiladores', 4, (INE5421,))

    INE5427 = Course('INE5427',
                     'Planejamento e Gestão de Projetos', 4, (INE5417,))

    INE5430 = Course('INE5430',
                     'Inteligência Artificial', 4, (INE5405, INE5413, INE5416))

    INE5453 = Course('INE5453',
                     'Introdução ao TCC', 1, (INE5417,))

    INE5428 = Course('INE5428',
                     'Informática e Sociedade', 4, (INE5407,))

    INE5429 = Course('INE5429',
                     'Segurança em Computação', 4, (INE5403, INE5414))

    INE5431 = Course('INE5431',
                     'Sistemas Multimídia', 4, (INE5414,))

    INE5432 = Course('INE5432',
                     'Banco de Dados II', 4, (INE5423,))

    INE5433 = Course('INE5433',
                     'TCC I', 6, (INE5427, INE5453))

    INE5434 = Course('INE5434',
                     'TCC II', 9, (INE5433,))
