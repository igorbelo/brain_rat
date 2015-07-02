<h2>Identificação</h2>
<strong>Aluno:</strong> Igor Coura Belo

<strong>Período:</strong> 6

<strong>Disciplina:</strong> Técnicas de Programação Avançada (TPA)

<h2>Problema</h2>
O rato Brain precisa sair de um labirinto, e da melhor maneira possível (utilizando o menor caminho para o mesmo).
O labirinto é uma matriz de de 0 e 1, onde 0 representa parede e 1, caminho possível. A matriz também possui S e F, onde S é a posição inicial do rato, e F é a saída do labirinto.
Além disso, o labirinto possui uma matriz de custo associada, e essa será considerada por Brain para saber qual a rota de menor custo possível até a saída F.

Um agravante é o gato, que aparece aleatoriamente em alguma posição possível antes de cada movimento do rato.
Brain deve evitar as rotas que passam por onde o gato está, indo por outras rotas as quais não passam pelo gato, sempre considerando a rota de menor custo.
Caso não possua nenhuma outra rota, o jogo acaba, e infelizmente Brain não conseguirá chegar ao seu destino.

A entrada das matrizes de posição e custo serão em arquivo texto.

A proposta é desenvolver um sistema que ajude Brain a sair do labirinto, pela melhor rota possível, evitando o gato no caminho.

<h2>Solução</h2>
<ul>
  <li>Primeiramente encontrar a posição de saída do labirinto, representada pela letra F.
Basicamente percorrer todas as posições da matriz e retornar a posição que contém a letra F como valor.
Função: `exit_position`</li>
  <li>Utilizando a mesma idéia, encontrar também a posição inicial do rato, representada pela letra S.</li>

  <li>A partir da matriz de posições, matriz de custos e posição de saída, calcular todos os custos das rotas que chegam ao fim.
Essa implementação deve ser recursiva, que recebe uma posição, a posição anterior, o custo acumulado e as rotas.</li>
  <ul>
    <li>Adiciona à estrutura de rotas (Hash) uma chave que é a posição atual, essa chave recebe as rotas possíveis com seus devidos custos acumulados.</li>
    <li>Para cada posição anterior encontrada, repete-se a operação acima</li>
  </ul>
  Exemplo de estrutura de saída:
  { (0, 0): { (0, 1): 5, (1, 0): 9 } }
  
  Isso quer dizer que saindo da posição (0, 0), Brain pode tomar as rotas passando por (0, 1) e (1, 0), porém a que o levará para o final mais rápido é a rota passando por (0, 1)
  <li>Agora, se obtém quais são as posições possíveis no labirinto, o que será útil para escolher onde o gato irá cair. Basicamente percorrer a matriz, e acrescentar em um array as posições que têm valor 1.</li>
  <li>Implementa-se também a função que gera uma posição aleatória a partir das posições disponíveis</li>
  <li>Implementa-se a função que põe o gato em uma posição sorteada. A partir dessa posição, atualiza-se todas as rotas que passam por essa posição recursivamente, elevando o custo das mesmas para o infinito. `put_cat`</li>
  <li>E por último, implementa-se a função que tenta movimentar o rato, a partir da posição em que o rato se encontra. Para o rato se movimentar, deve existir uma rota que não tenha o custo infinito.</li>
  <li>Enquanto o rato não estiver na posição final:</li>
  <ul>
    <li>Move o gato para uma posição aleatória</li>
    <li>Fim de jogo se o gato caiu exatamente em cima do rato</li>
    <li>Tenta mover o rato</li>
    <li>Fim de jogo se o rato não tem pra onde ir</li>
  </ul>
</ul>

<h2>Análise de complexidade</h2>
<h3>available_positions</h3>
Esse algoritmo possui a complexidade O(m.n), onde m é o número de linhas, e n é o número de colunas da matriz de posições possíveis.
Também é um algoritmo ótimo, visto que todas as posições da matriz precisam ser visitadas para validar se é uma posição possível ou não

<h2>Testes realizados</h2>
Foram implementados testes automatizados de todas as funções implementadas.
Foi utilizada a biblioteca unittest do Python. Abaixo, o link para a implementação dos testes.
<ul>
  <li><a href="https://github.com/igorbelo/brain_rat/blob/master/test/available_positions.py">available_positions</a></li>
  <li><a href="https://github.com/igorbelo/brain_rat/blob/master/test/exit_position.py">exit_position</a></li>
  <li><a href="https://github.com/igorbelo/brain_rat/blob/master/test/fill_routes.py">fill_routes</a></li>
  <li><a href="https://github.com/igorbelo/brain_rat/blob/master/test/go_rat.py">go_rat</a></li>
  <li><a href="https://github.com/igorbelo/brain_rat/blob/master/test/possible_back_moves.py">possible_back_moves</a></li>
  <li><a href="https://github.com/igorbelo/brain_rat/blob/master/test/put_cat.py">put_cat</a></li>
  <li><a href="https://github.com/igorbelo/brain_rat/blob/master/test/rat_start_position.py">rat_start_position</a></li>
</ul>
Comando para rodar os testes no diretório raíz do projeto:
```python -m unittest discover -s test/ -p '*.py'```

<h2>Conclusão</h2>

<h2>Referências</h2>
Documentação Oficial do Python: https://docs.python.org/2/
