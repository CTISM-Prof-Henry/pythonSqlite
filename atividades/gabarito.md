# Exercícios

## Pré-requisitos

Fazer a configuração disponível na página inicial, seja para o [Pycharm](../README.md#configurando-no-Pycharm) ou
para a [linha de comando](../README.md#configurando-pela-linha-de-comando).

## Modo de resolver

Com o banco de dados aberto (seja pelo Pycharm ou pela linha de comando), descubra o comando SQL que resolve o exercício.
Após descobri-lo, cole-o no script correspondente à atividade, e adapte o código-fonte Python para imprimir na tela os
dados retornados.

**Exemplo:** se quisermos selecionar o nome e o número de períodos das matérias elencadas na tabela `materias`, o 
comando SQL que faz esta consulta é

```sql
select nome, periodos
from materias;
```

Portanto, precisamos colar este comando no arquivo Python correspondente, e adaptar o código para imprimir as 
informações corretamente:

```python
materias = cur.execute('''SELECT nome, periodos FROM materias;''').fetchall()

for linha in materias:
    nome = linha[0]
    periodos = linha[1]
    print('nome: {0} periodos: {1}'.format(nome, periodos))
```

Existe um arquivo Python para cada exercício, na pasta [atividades](.). Esse script gera o banco de dados 
novamente. Ou seja, cada exercício é independente do outro.

**Nota 2:** o script [main.py](main.py) possui os comandos de criação de tabelas e inserção de tuplas. 
                                   
**Nota 3:** o gabarito está [aqui](gabarito.md).

## Enunciados

1. Usando a biblioteca [mermaid](https://mermaid-js.github.io/mermaid/#/), desenhe um diagrama de classes para a 
   estrutura do banco de dados disponibilizado. 
    
   ```mermaid
   classDiagram
       class professores {
           INTEGER id_professor PK
           TEXT nome,
           TEXT cabelo,
           TEXT barba
       }
       
       class materias {
           INTEGER id_materia PK
           TEXT nome
           INTEGER periodos
       }
       
       class professores_para_materias {
           INTEGER id_professor PK FK
           INTEGER id_materia PK FK
           TEXT data_inicio
           TEXT data_fim 
       }
       
       professores -- professores_para_materias : id_professor
       materias -- professores_para_materias : id_materia
   ```

2. Selecione todas as disciplinas que o professor Fábio dá aula.

   ```sql
   select p.nome, m.nome
   from professores as p
   inner join professores_para_materias as ppm on p.id_professor = ppm.id_professor
   inner join materias m on ppm.id_materia = m.id_materia
   where p.nome = 'Fábio'
   ```

3. Selecione todas as disciplinas que o professor Henry dá aula.

   ```sql
   select p.nome, m.nome
   from professores as p
   inner join professores_para_materias as ppm on p.id_professor = ppm.id_professor
   inner join materias m on ppm.id_materia = m.id_materia
   where p.nome = 'Henry'
   ```

4. Selecione todas as disciplinas que o professor Rafael Pereira dá aula.

   ```sql
   select p.nome, m.nome
   from professores as p
   left join professores_para_materias as ppm on p.id_professor = ppm.id_professor
   left join materias m on ppm.id_materia = m.id_materia
   where p.nome = 'Rafael Pereira'
   ```

5. Selecione todos os professores que possuem cabelo mas não possuem barba.

   ```sql
   select nome
   from professores
   where cabelo = 'sim' and barba = 'não';
   ```

6. Selecione todos os professores que possuem barba mas não possuem cabelo.

   ```sql
   select nome
   from professores
   where cabelo = 'não' and barba = 'sim';
   ```

7. Selecione todos os professores que não possuem nem cabelo e nem barba.

   ```sql
   select nome
   from professores
   where cabelo = 'não' and barba = 'não';
   ```

8. Selecione todos os professores que possuem cabelo ou possuem barba.

   ```sql
   select nome
   from professores
   where cabelo = 'sim' or barba = 'sim';
   ```

9. Selecione todas as matérias que possuem exatamente um período.

   ```sql
   select nome
   from materias
   where periodos = 1;
   ```

10. Selecione todas as matérias que possuem entre um e dois períodos, e.g. 1 ≤ períodos ≤ 2.

    ```sql
    select nome
    from materias
    where periodos >= 1 and periodos <= 2;
    ```

11. Selecione todas as matérias que possuem um ou três períodos.

   ```sql
   select nome
   from materias
   where periodos = 1 or periodos = 3;
   ```

12. Selecione todas as disciplinas que possuem apenas um período ou o professor não tem cabelo nem barba.

   ```sql
    select m.nome, m.periodos, p.nome, p.cabelo, p.barba
    from materias as m
    left join professores_para_materias ppm on m.id_materia = ppm.id_materia
    left join professores p on ppm.id_professor = p.id_professor
    where (m.periodos = 1) or (p.cabelo = 'não' and p.barba = 'não')
   ```

13. Selecione todas as disciplinas que atualmente não possuem nenhum professor atribuído.

    ```sql
    select p.nome, m.nome
    from materias as m
    left join professores_para_materias ppm on m.id_materia = ppm.id_materia
    left join professores p on ppm.id_professor = p.id_professor
    where p.nome is null
    ```

14. Selecione todos os professores que já deram aula de Princípios de Gestão, e **ordene-os em ordem cronológica 
    inversa** (do professor que está dando a disciplina atualmente até o professor que deu a disciplina há mais tempo).

    ```sql
    select p.nome, date(ppm.data_inicio) as d_data_inicio, date(ppm.data_fim) as d_data_fim
    from professores as p
    inner join professores_para_materias ppm on p.id_professor = ppm.id_professor
    inner join materias m on m.id_materia = ppm.id_materia
    where m.nome = 'Princípios de Gestão'
    order by d_data_fim desc
    ```

15. Selecione todas as disciplinas que possuem exatamente um professor atribuído.

    **Opção 1:**

    ```sql
    select p.nome, count(m.nome) as numero_materias
    from materias as m
    inner join professores_para_materias ppm on m.id_materia = ppm.id_materia
    inner join professores p on ppm.id_professor = p.id_professor
    group by p.nome
    having numero_materias = 1
    ```

    **Opção 2:**

    ```sql
    select *
    from (
        select p.nome, count(m.nome) as numero_materias
        from materias as m
        inner join professores_para_materias ppm on m.id_materia = ppm.id_materia
        inner join professores p on ppm.id_professor = p.id_professor
        group by p.nome
    )
    where numero_materias = 1
    ```

16. Selecione todas as disciplinas que já tiveram mais que um professor atribuído.

    ```sql
    select m.nome, count(p.nome) as numero_professores
    from materias as m
    inner join professores_para_materias ppm on m.id_materia = ppm.id_materia
    inner join professores p on ppm.id_professor = p.id_professor
    group by m.nome
    having numero_professores > 1
    ```

17. Selecione o nome do professor, o nome da disciplina, a data de início de atuação do professor na disciplina, 
    a data de fim de atuação do professor da disciplina, de todas as disciplinas que possuem dois professores atribuídos
    à ela **ao mesmo tempo**.

    **Opção 1:** sem criar tabela temporária (precisa refazer a busca três vezes)

    ```sql
    select p.nome, m.nome, date(ppm.data_inicio) as d_data_inicio, date(ppm.data_fim) as d_data_fim
    from professores as p
    inner join professores_para_materias as ppm on p.id_professor = ppm.id_professor
    inner join materias as m on ppm.id_materia = m.id_materia
    where m.nome in (
        select m.nome
        from professores_para_materias ppm
        inner join materias m on ppm.id_materia = m.id_materia
        group by m.nome, date(data_inicio), date(data_fim)
        having count(*) > 1
    ) and d_data_inicio in (
        select date(data_inicio)
        from professores_para_materias ppm
        inner join materias m on ppm.id_materia = m.id_materia
        group by m.nome, date(data_inicio), date(data_fim)
        having count(*) > 1
    ) and d_data_fim in (
        select date(ppm.data_fim)
        from professores_para_materias ppm
        inner join materias m on ppm.id_materia = m.id_materia
        group by m.nome, date(data_inicio), date(data_fim)
        having count(*) > 1
    )
    ```

    **Opção 2:** criando tabela temporária (evita refazer a mesma consulta três vezes)

    ```sql
    -- cria tabela temporária
    create temporary table if not exists temp as
        select m.nome, date(data_inicio) as d_data_inicio, date(data_fim) as d_data_fim
        from professores_para_materias ppm
        inner join materias m on ppm.id_materia = m.id_materia
        group by m.nome, date(data_inicio), date(data_fim)
        having count(*) > 1;
   
    -- seleciona as informações requisitas que também se encontram na tabela temporária
    select p.nome, m.nome, date(ppm.data_inicio) as d_data_inicio, date(ppm.data_fim) as d_data_fim
    from professores as p
    inner join professores_para_materias as ppm on p.id_professor = ppm.id_professor
    inner join materias as m on ppm.id_materia = m.id_materia
    where m.nome in (
        select nome from temp
    ) and d_data_inicio in (
        select d_data_inicio from temp
    ) and d_data_fim in (
        select d_data_fim from temp
    );
   
    -- opcional: deleta a tabela temporária
    drop table temp;
    ```

18. Insira o professor Zolin no banco de dados. Atribua a disciplina de `Sociologia` à ele.

    ```sql
    insert into professores (id_professor, nome) values (11, 'Zolin');
    insert into professores_para_materias (id_professor, id_materia) values (11, 4);
    ```

19. Remova todos os professores do banco de dados que não possuem nenhuma disciplina atribuída.

    ```sql
    delete from professores
    where id_professor in (
        select p.id_professor
        from professores as p
        left join professores_para_materias ppm on p.id_professor = ppm.id_professor
        left join materias m on ppm.id_materia = m.id_materia
        where m.nome is null
    )
    ```

20. Usando os comandos `INNER JOIN` e `UNION`, faça um full outer join entre as tabelas professores e materias.

    ```sql
    select p.nome, m.nome
    from professores as p
    left join professores_para_materias ppm on p.id_professor = ppm.id_professor
    left join materias m on m.id_materia = ppm.id_materia
    union
    select p.nome, m.nome
    from materias as m
    left join professores_para_materias ppm on ppm.id_materia = m.id_materia
    left join professores as p on p.id_professor = ppm.id_professor
    ```