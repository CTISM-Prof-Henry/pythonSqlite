import sqlite3
import os
from datetime import datetime as dt


def data_para_string(data: dt) -> str:
    """
    Converte uma data para uma string, no formato ANO-MÊS-DIA.
    """
    string = data.strftime('%Y-%m-%d')
    return string


def string_para_data(string: str) -> dt:
    """
    Converte uma string no formato ANO-MÊS-DIA para uma data.
    """
    data = dt.strptime(string, '%Y-%m-%d')
    return data


def cria_tabelas(cur: sqlite3.Cursor) -> sqlite3.Cursor:
    """
    Cria as tabelas do banco de dados.

    :param cur: um cursor para o banco de dados.
    :return: um cursor para o banco de dados.
    """

    cur.execute('''
        CREATE TABLE IF NOT EXISTS materias (
            id_materia INTEGER NOT NULL,
            nome TEXT NOT NULL,
            PRIMARY KEY (id_materia)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id_professor INTEGER NOT NULL,
            nome TEXT NOT NULL,
            PRIMARY KEY (id_professor)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS professores_para_materias (
            id_professor INTEGER NOT NULL,
            id_materia INTEGER NOT NULL,
            data_inicio TEXT NOT NULL DEFAULT '2022-04-11',
            data_fim TEXT NOT NULL DEFAULT '2023-02-15',
            PRIMARY KEY (id_professor, id_materia, data_inicio, data_fim),
            FOREIGN KEY (id_professor) REFERENCES professores(id_professor),
            FOREIGN KEY (id_materia) REFERENCES materias(id_materia)
        )
    ''')

    return cur


def insere_tuplas(cur: sqlite3.Cursor) -> sqlite3.Cursor:
    """
    Cria as tabelas do banco de dados.

    :param cur: um cursor para o banco de dados.
    :return: um cursor para o banco de dados.
    """

    cur.execute('''INSERT INTO professores(id_professor, nome) VALUES (1, 'Fábio');''')
    cur.execute('''INSERT INTO professores(id_professor, nome) VALUES (2, 'Henry');''')
    cur.execute('''INSERT INTO professores(id_professor, nome) VALUES (3, 'Rafael Pereira');''')
    cur.execute('''INSERT INTO professores(id_professor, nome) VALUES (4, 'Lairane');''')
    cur.execute('''INSERT INTO professores(id_professor, nome) VALUES (5, 'Mário');''')
    cur.execute('''INSERT INTO professores(id_professor, nome) VALUES (6, 'Gustavo');''')
    cur.execute('''INSERT INTO professores(id_professor, nome) VALUES (7, 'Karina');''')
    cur.execute('''INSERT INTO professores(id_professor, nome) VALUES (8, 'Roberto');''')
    cur.execute('''INSERT INTO professores(id_professor, nome) VALUES (9, 'Priscila');''')
    cur.execute('''INSERT INTO professores(id_professor, nome) VALUES (10, 'Shirley');''')

    cur.execute('''INSERT INTO materias(id_materia, nome) VALUES (1, 'Internet das Coisas');''')
    cur.execute('''INSERT INTO materias(id_materia, nome) VALUES (2, 'Banco de Dados');''')
    cur.execute('''INSERT INTO materias(id_materia, nome) VALUES (3, 'Desenvolvimento de Sistemas');''')
    cur.execute('''INSERT INTO materias(id_materia, nome) VALUES (4, 'Sociologia')''')
    cur.execute('''INSERT INTO materias(id_materia, nome) VALUES (5, 'Física')''')
    cur.execute('''INSERT INTO materias(id_materia, nome) VALUES (6, 'Princípios de Gestão')''')

    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia) VALUES (1, 1);''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia) VALUES (1, 2);''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia) VALUES (2, 3);''')

    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (4, 5, '2022-04-11', '2022-05-11');''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (5, 5, '2022-05-11', '2022-06-11');''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (6, 5, '2022-06-11', '2023-02-15');''')

    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (7, 6, '2022-04-11', '2022-05-11');''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (8, 6, '2022-05-11', '2022-06-11');''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (9, 6, '2022-06-11', '2023-02-15');''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (10, 6, '2022-06-11', '2023-02-15');''')

    return cur


def main(database_path: str = None):
    # pega o caminho absoluto do arquivo do banco de dados
    # por exemplo, se o banco.db estiver na pasta C:\Users\aluno,
    # database_path vai ser C:\Users\aluno\banco.db
    if database_path is None:
        database_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'banco.db')

    # se o banco de dados existir, deleta-o
    # isso facilita a vida na hora que formos re-gerar o banco, pois evita que tuplas
    # com ID repetido sejam inseridas novamente
    if os.path.exists(database_path):
        os.remove(database_path)

    # cria o arquivo do banco se ele não existe
    # ou se conecta ao arquivo se existir
    with sqlite3.connect(database_path) as con:
        # pega um cursor para executar as operações
        # um cursor é uma conexão para o banco de dados (e.g. cria, deleta, insere, etc)
        cur = con.cursor()

        cur = cria_tabelas(cur)
        cur = insere_tuplas(cur)

        # salva as modificações feitas no banco
        con.commit()


if __name__ == '__main__':
    main()
