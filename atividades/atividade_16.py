import os
import sqlite3
import sys


def trickery(database_path: str):
    """
    Uma função que permite que o código rode tanto pelo Pycharm, quanto pelo VS Code, quanto pela linha de comando.

    Também remove o banco de dados antigo e gera um novo.
    """
    cur_path = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    cur_path = os.path.join(cur_path, os.sep.join(['atividades']))
    os.chdir(cur_path)

    project_path = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    sys.path.append(project_path)

    from atividades.main import main as gera_banco
    gera_banco(database_path)


def main():
    database_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'banco.db')
    trickery(database_path)

    with sqlite3.connect('banco.db') as con:
        # pega um cursor para executar as operações
        # um cursor é uma conexão para o banco de dados (e.g. cria, deleta, insere, etc)
        cur = con.cursor()

        # seleciona todas as tuplas da tabela materias
        materias = cur.execute('''SELECT id_materia, nome FROM materias''').fetchall()

        for linha in materias:
            id_materia = linha[0]
            nome_materia = linha[1]
            print('id_materia: {0} nome: {1}'.format(id_materia, nome_materia))


if __name__ == '__main__':
    main()
