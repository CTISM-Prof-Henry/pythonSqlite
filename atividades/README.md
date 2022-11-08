# Exercícios

## Pré-requisitos

Fazer a configuração disponível na página inicial, seja para o [Pycharm](../README.md#configurando-no-Pycharm) ou
para a [linha de comando](../README.md#configurando-pela-linha-de-comando).

Será preciso também se [desconectar do banco de dados](../README.md#deletando-o-banco-de-dados) a cada nova atividade 
realizada.

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
materias = cur.execute('''
    SELECT nome, periodos FROM materias;
''').fetchall()

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

1. Usando a biblioteca [mermaid](https://mermaid-js.github.io/mermaid/#/), e a ferramenta online 
   [mermaid.live](mermaid.live), desenhe um diagrama de classes para a estrutura do banco de dados 
   disponibilizado.
2. Selecione todas as disciplinas que o professor Fábio dá aula.
3. Selecione todas as disciplinas que o professor Henry dá aula.
4. Selecione todas as disciplinas que o professor Rafael Pereira dá aula.
5. Selecione todos os professores que possuem cabelo mas não possuem barba.
6. Selecione todos os professores que possuem barba mas não possuem cabelo.
7. Selecione todos os professores que não possuem nem cabelo e nem barba.
8. Selecione todos os professores que possuem cabelo ou possuem barba.
9. Selecione todas as matérias que possuem exatamente um período.
10. Selecione todas as matérias que possuem entre um e dois períodos, e.g. 1 ≤ períodos ≤ 2.
11. Selecione todas as matérias que possuem um ou três períodos.
12. Selecione todas as disciplinas que possuem apenas um período ou o professor não tem cabelo nem barba.
13. Selecione todas as disciplinas que atualmente não possuem nenhum professor atribuído.
14. Selecione todos os professores que já deram aula de Princípios de Gestão, e **ordene-os em ordem cronológica 
    inversa** (do professor que está dando a disciplina atualmente até o professor que deu a disciplina há mais tempo).
15. Selecione todas as disciplinas que possuem exatamente um professor atribuído.
16. Selecione todas as disciplinas que já tiveram mais que um professor atribuído.
17. Selecione o nome do professor, o nome da disciplina, a data de início de atuação do professor na disciplina, 
    a data de fim de atuação do professor da disciplina, de todas as disciplinas que possuem dois professores atribuídos
    à ela **ao mesmo tempo**.
18. Insira o professor Zolin no banco de dados. Atribua a disciplina de `Sociologia` à ele.
19. Remova todos os professores do banco de dados que não possuem nenhuma disciplina atribuída.
20. Usando os comandos `INNER JOIN` e `UNION`, faça um full outer join entre as tabelas professores e materias.