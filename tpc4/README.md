# Aplicação

O objetivo deste trabalho de casa era fazer uma pequena aplicação com vários tipo de operações onde usamos manipulação de listas.
Para tal, realizou-se a aplicação em python, para também aprendermos como se usa o terminal.

Para casa operação/tarefa é associada um número que o utilizador pode selecionar para escolher o que deseja fazer. 

Inicialmente cria-se o menu, onde se coloca que tarefa corresponde a *x* número e a *cond* inicial é True.
Escolhendo o número 1 o ciclo vai permitir com que o programa faça uma lista com *n* quantidade de números, escolhidos pelo utilizador, onde os números lá colocados iram ser random mas dentro do intervalo de 1 a 100.
Escolhendo o número 2, vai ser lida uma lista, onde esta é toda escrita pelo utilizador. Este vai escolher quantos números a lista terá e quais seram esses números.
Ao selecionar o número 3, o programa vai realizar a soma dos elementos da última lista que ficou guardada no sistema. Ou seja por cada elemento da lista, este vai somar ao valor da soma anterior, até não haver mais elementos.
Na opção 4 pode-se realizar a média dos valores presentes da última lista guardada. Para tal realiza-se a soma dos elementos, e depois dividimos essa soma pela quantidade de números que a lista tem (contamos quantos ciclos acontecem).
Com o número 5 a aplicação vai mostrar ao utilizador qual é que é o maior número presente na lista. Vai-se fazer uma comparação entre todos os valores da lista e o maior irá ficar guardado como tal e irá ser mostrado na interface no final de se percorrer toda a lista.
Com o número 6, o menor número da lista irá ser apresentado. Compara-se também todos os elemntos da lista com o primeiro valor desta. Se um número encontrado for menor que o inicial, esse irá passar a ser o menor, fazendo este ciclo até acabar a lista.
Selecionando o número 7, o programa vai copiar a lista existente numa nova variável. Em seguida organiza-se a lista por ordem crescente e depois compara-se com a lista inicial. Se elas forem iguais, o programa imprime que a  lista encontra-se ordenada de forma crescente.
Na opção 8, o programa vai copiar a lista existente numa nova variável. Em seguida organiza-se a lista por ordem crescente e depois inverte-se a mesma. Compara-se as listas e o programa diz se a lista está ordenada de forma descrescente ou não.
Ao selecionar o número 9 o utilizador escolhe um número para verificar se esse se encontra na lista guardada. Se o encontrar o programa imprime o número e a posição dele na lista, se não imprime *-1*.
Escolhendo o número 0, o programa irá fechar e apresenta uma mensagem que transmite essa mesma informação (*cond=False*).

No final de todos os *elif* coloca-se outra vez o print do menu para o utilizador escolher se quer fazer mais alguma coisa ou se deseja sair da aplicação.