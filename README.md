# pythonSqlite

Este repositório organiza o conhecimento necessário para trabalhar com sqlite em Python.

## Sumário

* [Sumário](#sumário)
* [Configurando no Pycharm](#configurando-no-pycharm)
  * [Executando um comando SQL](#executando-um-comando-sql)
  * [Gerando o diagrama do banco de dados](#gerando-o-diagrama-do-banco-de-dados)

## Configurando no Pycharm

1. Crie o banco de dados (por exemplo, executando o script [atividades/main.py](atividades/main.py))
2. Clique duas vezes sobre o arquivo do banco de dados (por exemplo, `banco.db`)
3. Talvez seja necessário baixar um plugin para conseguir manipular o banco de dados pelo Pycharm. Se for o caso, clique
   no link do lado do sinal de ⚠️
4. Certifique-se que o caminho dado no campo `file` está apontando para o arquivo banco.db:

   ![sqlite_2.png](imagens/sqlite_2.png)

5. Clique ok
6. Uma nova aba se abrirá no Pycharm, com o nome `console`. Também se abrirá uma janela lateral de nome `database`. Na
   aba `console` você executará comandos SQL, enquanto na janela `database` você pode ver a estrutura do banco de dados.

### Executando um comando SQL

Após fazer o passo-a-passo da seção [Configurando no Pycharm](#configurando-no-Pycharm), você pode digitar um comando
SQL na janela console, e executá-lo clicando no botão verde ▶️ , ou então entrando com o comando `CTRL + Enter`.

### Gerando o diagrama do banco de dados

Após fazer o passo-a-passo da seção [Configurando no Pycharm](#configurando-no-Pycharm), na janela `database`, clique 
com o botão direito em cima do nome do banco de dados (por exemplo, `banco`), selecione a opção `Diagrams`, e depois
`Show Visualization`:

   ![sqlite_3.png](imagens/sqlite_3.png)
   
Abaixo é mostrado o diagrama do banco de dados disponibilizado nas [Atividades](atividades/README.md):

   ![sqlite_4.png](imagens/sqlite_4.png)
   
A tabela `sqlite_master` é uma tabela de controle criada pelo sqlite para anotar metadados sobre o banco de dados (como 
por exemplo o número de tabelas presentes). 

## Configurando pela linha de comando

1. Crie o banco de dados (por exemplo, executando o script [atividades/main.py](atividades/main.py))
2. Pela linha de comando, navegue até a pasta do banco de dados (por exemplo, `cd C:\Users\aluno\pythonSqlite\atividades`)
3. Digite o comando `sqlite3 <nome do arquivo>`, onde `<nome do arquivo>` é o nome do arquivo do banco de dados
   * Por exemplo `sqlite3 banco.db`
4. Você pode rodar comandos SQL normalmente agora:

   ![sqlite_5.png](imagens/sqlite_5.png)

5. Para sair dessa tela, pressione `CTRL + D` (Linux) ou `CTRL + C` (Windows).