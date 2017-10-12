from typing import NamedTuple, Tuple


class Course(NamedTuple):
    code: str
    name: str
    bla: int
    requirements: Tuple['Course']

    def __repr__(self):
        return self.code


eel5105 = Course('EEL5105',
                 'Circuitos e Técnicas Digitais', 5, ())

ine5401 = Course('INE5401',
                 'Introdução à Computação', 2, ())

ine5402 = Course('INE5402',
                 'Programação Orientada a Objetos I', 6, ())

ine5403 = Course('INE5403',
                 'Fundamentos de Matemática Discreta para Computação', 6, ())

mtm3100 = Course('MTM3100',
                 'Pré-Cálculo', 4, ())

mtm3101 = Course('MTM3101',
                 'Cálculo 1', 4, (mtm3100))

ine5404 = Course('INE5404',
                 'Programação Orientada a Objetos II', 6, (ine5402))

ine5405 = Course('INE5405',
                 'Probabilidade e Estatística', 5, (mtm3101))

ine5406 = Course('INE5406',
                 'Sistemas Digitais', 5, (eel5105))

ine5407 = Course('INE5407',
                 'Ciência, Tecnologia e Sociedade', 3, ())

mtm3102 = Course('MTM3102',
                 'Cálculo 2', 4, (mtm3101))

mtm5512 = Course('MTM5512',
                 'Geometria Analítica', 4, ())

ine5408 = Course('INE5408',
                 'Estruturas de Dados', 6, (ine5404))

ine5409 = Course('INE5409',
                 'Cálculo Numérico para Computação', 4, (mtm5512, mtm3102))

ine5410 = Course('INE5410',
                 'Programação Concorrente', 4, (ine5404))

ine5411 = Course('INE5411',
                 'Organização de Computadores I', 6, (ine5406))

mtm5245 = Course('MTM5245',
                 'Álgebra Linear', 4, (mtm5512))

ine5412 = Course('INE5412',
                 'Sistemas Operacionais I', 4, (ine5410, ine5411))

ine5413 = Course('INE5413',
                 'Grafos', 4, (ine5403, ine5408))

ine5414 = Course('INE5414',
                 'Redes de Computadores I', 4, (ine5404))

ine5415 = Course('INE5415',
                 'Teoria da Computação', 4, (ine5403, ine5408))

ine5416 = Course('INE5416',
                 'Paradigmas de Programação', 5, (ine5408))

ine5417 = Course('INE5417',
                 'Engenharia de Software I', 5, (ine5408))

ine5418 = Course('INE5418',
                 'Computação Distribuída', 4, (ine5412, ine5414))

ine5419 = Course('INE5419',
                 'Engenharia de Software II', 4, (ine5417))

ine5420 = Course('INE5420',
                 'Computação Gráfica', 4, (ine5408, mtm3102, mtm5245))

ine5421 = Course('INE5421',
                 'Linguagens Formais e Compiladores', 4, (ine5415))

ine5422 = Course('INE5422',
                 'Redes de Computadores II', 4, (ine5414))

ine5423 = Course('INE5423',
                 'Banco de Dados I', 4, (ine5408))

ine5424 = Course('INE5424',
                 'Sistemas Operacionais II', 4, (ine5412))

ine5425 = Course('INE5425',
                 'Modelagem e Simulação', 4, (ine5405))

ine5426 = Course('INE5426',
                 'Construção de Compiladores', 4, (ine5421))

ine5427 = Course('INE5427',
                 'Planejamento e Gestão de Projetos', 4, (ine5417))

ine5430 = Course('INE5430',
                 'Inteligência Artificial', 4, (ine5405, ine5413, ine5416))

ine5453 = Course('INE5453',
                 'Introdução ao TCC', 1, (ine5417))

ine5428 = Course('INE5428',
                 'Informática e Sociedade', 4, (ine5407))

ine5429 = Course('INE5429',
                 'Segurança em Computação', 4, (ine5403, ine5414))

ine5431 = Course('INE5431',
                 'Sistemas Multimídia', 4, (ine5414))

ine5432 = Course('INE5432',
                 'Banco de Dados II', 4, (ine5423))

ine5433 = Course('INE5433',
                 'TCC I', 6, (ine5427, ine5453))

ine5434 = Course('INE5434',
                 'TCC II', 9, (ine5433))


courses = (eel5105, ine5401, ine5402, ine5403, mtm3100, mtm3101,
           ine5404, ine5405, ine5406, ine5407, mtm3102, mtm5512,
           ine5408, ine5409, ine5410, ine5411, mtm5245,
           ine5412, ine5413, ine5414, ine5415, ine5416, ine5417,
           ine5418, ine5419, ine5420, ine5421, ine5422, ine5423,
           ine5424, ine5425, ine5426, ine5427, ine5430, ine5453,
           ine5428, ine5429, ine5431, ine5432, ine5433,
           ine5434)
