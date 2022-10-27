# Exercícios

**Nota:** para cada exercício, existe um script na pasta [atividades](../gabarito). Esse script gera o banco de dados 
novamente. Ou seja, cada exercício é independente do outro.

**Nota 2:** o script [main.py](../gabarito/main.py) possui a criação de tabelas e inserção de tuplas. 

1. Selecione todas as disciplinas que o professor Fábio dá aula.

```sqlite
select p.nome, m.nome
from professores as p
inner join professores_para_materias as ppm on p.id_professor = ppm.id_professor
inner join materias m on ppm.id_materia = m.id_materia
where p.nome = 'Fábio'
```

2. Selecione todas as disciplinas que o professor Henry dá aula.

```sqlite
select p.nome, m.nome
from professores as p
inner join professores_para_materias as ppm on p.id_professor = ppm.id_professor
inner join materias m on ppm.id_materia = m.id_materia
where p.nome = 'Henry'
```

3. Selecione todas as disciplinas que o professor Rafael dá aula.

```sqlite
select p.nome, m.nome
from professores as p
inner join professores_para_materias as ppm on p.id_professor = ppm.id_professor
inner join materias m on ppm.id_materia = m.id_materia
where p.nome = 'Rafael'
```

4. Selecione todas as disciplinas que atualmente não possuem nenhum professor atribuído.

```sqlite
select p.nome, m.nome
from materias as m
left join professores_para_materias ppm on m.id_materia = ppm.id_materia
left join professores p on ppm.id_professor = p.id_professor
where p.nome is null
```

5. Selecione todas as disciplinas que possuem exatamente um professor atribuído.

Opção 1:

```sqlite
select p.nome, count(m.nome) as numero_materias
from materias as m
inner join professores_para_materias ppm on m.id_materia = ppm.id_materia
inner join professores p on ppm.id_professor = p.id_professor
group by p.nome
having numero_materias = 1
```

Opção 2:

```sqlite
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

6. Selecione todas as disciplinas que já tiveram mais que um professor atribuído.

```sqlite
select m.nome, count(p.nome) as numero_professores
from materias as m
inner join professores_para_materias ppm on m.id_materia = ppm.id_materia
inner join professores p on ppm.id_professor = p.id_professor
group by m.nome
having numero_professores > 1
```

7. Selecione todas as disciplinas que já tiveram mais que um professor atribuído, e **ordene-as em ordem cronológica 
   inversa** (do professor que está dando a disciplina atualmente até o professor que deu a disciplina há mais tempo).

```sqlite
select m.nome, ppm.data_inicio, ppm.data_fim
from materias as m
inner join professores_para_materias ppm on m.id_materia = ppm.id_materia
inner join professores p on ppm.id_professor = p.id_professor
group by m.nome
having count(m.nome) > 1
order by ppm.data_inicio DESC
```

8. Selecione todas as disciplinas em que dois professores estão atribuídos à ela **ao mesmo tempo**.
9. Insira o professor Zolin no banco de dados. Atribua a disciplina de `Sociologia` à ele.
10. Remova todos os professores do banco de dados que não possuem nenhuma disciplina atribuída.
11. Usando os comandos `INNER JOIN` e `UNION`, faça um full outer join entre as tabelas professores e materias.
12. Usando a biblioteca [mermaid](https://mermaid-js.github.io/mermaid/#/), desenhe um diagrama de classes para a 
    estrutura do banco de dados disponibilizado. 
    * **Dica:** você pode usar o [mermaid.live](https://mermaid.live) para desenhar o diagrama. Depois você só
      copia-e-cola o código no arquivo [diagrama.md](../gabarito/diagrama.md). O Pycharm também possui um plugin com suporte ao
      mermaid, mas precisa ser baixado antes (este ícone aparecerá quando você abrir o arquivo [diagrama.md](../gabarito/diagrama.md)):
    
      ![mermaid](../imagens/mermaid.png)