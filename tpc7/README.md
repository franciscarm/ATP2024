# Aplicação com funções da aula prática 7

Começou-se por criar a função *menu* para o utilizador conseguir interagir com a interface e para que seja possível observar quais as opções que pode-se escolher.

Coloca-se uma uma condição inicial *cond = True* e inicia-se um ciclo while. Se a opçaõ escolhida for a 0, a condição muda, *cond = False* e o programa fecha.

Escolhendo-se a opção 1 um novo ficheiro é criado (onde o utilizador dá o nome a tal) e vai-se poder escrever nele. O utilizador vai poder criar uma tabela de meteorologia. Esta vai ser guardada numa lista. Cada elemento da lista irá ter uma data, a temperatura mínima desse dia, a temperatura máxima e a precipitação e para tal o utilizador escreve os valores de cada um dos parâmetros. 
Para uma melhor organização é criada uma maneira de separar melhor os parâmetros no ficheiro de texto.

Com a opção 2 vai ser possível carregar para o progrma um ficehiro, já existente, onde tem uma tabela meteorológica. É apresentada na interface a lista com as informações desse ficheiro.

Com a opção 3 é possível fazer a média das temperaturas de todas as datas disponíveis. Este vai realizar a soma entre as temperatutas mínimas e máximas e dividir por 2. O resultado é apresentado em formato de tuplo com a data e o valor pretendido.

Selecionando a opção 4 percorre toda a lista e vai apresentar em que dia é que houve a temperatura mínima mais baixa. Para tal inicia-se uma variável *minima* que corresponde á primiera temperatura mínima da lista, e depois é comparada com as outras. A menor é a que fica guardada e depois é apresentada. 

A opção 5 calcula a apmlitude térmica de todas as datas. Esta consite na diferença entre a temperatura máxima e a temperatura mínima de um certo dia. 

Escolhendo a opção 6 vai ser possível ver qual é o dia em que a precipitação foi maior. Cria-se uma variável que tem como valor a precipitação do primeiro elemento. Em seguida vai comparar com os outros valores e o maior fica guardado na variável e é apresentado.

Com a opção 7 o utilizador vai dar um limite de precipitação e o programa vai apresentar uma lista com as datas que possuem uma precipitação superior ao valor apresentado pelo limite.

Selecionando a opção 8 o utilizador vai fornecer também um limite, mas a resposta vai ser o número de dias consecutivos em que o valor da precipitação foi menor que esse limite.

A opção 9 vai apresentar a temperatura mínima, máxima e pluviosidade em formato de gráfico. Para tal houve um *import matplotlib.pyplot as plt* para que seja possível a apresentação dos gráfico na interface. 

Por fim acrescentei uma opção que vai mostrar na interface os parâmetros e as informações deles. Desta forma é mais fácil observar a tabela da meteorologia.