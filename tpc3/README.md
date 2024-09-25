## Jogo dos 21 fosforos 

Nos dois modos faz-se import random, para utilizar na vez do computador e a variével *n_fosforos* é inicializada a 21.


No primeiro modo o jogador é o primeiro a retirar um número, de 1 a 4, de fósforos. Retira-se então esse número ao número de fósforos que ainda sobram no momento. Só acontece enquanto o *n_fosforos* for maior que zero e se ainda não houver um perdedor.
Se o utilizador não colocar nenhum desses números, o programa pede para que este volte a tentar escrever um número apropriado.
Se o *n_fosforos* chegar a zero o jogador perdedor passa a ser o jogador, uma vez que foi o último a retirar um fósforo. Se não acontecer, é a vez do computador jogar.

Na vez do computador, este vai retirar um número de 1 a 4 random, caso o *n_fosforos* menos um seja divisível por cinco e o resto seja zero. Contrariamente a isso, irá dar o *n_fosforos* menos 1 a dividir por cinco.
Retira-se ao *n_fosforos* do momento o número que o computador escolheu.

Por fim, quando chegar a zero fosforos, o *jogador_per* terá um nome e irá ser apresentado na interface.



No segundo modo o computador é o primeiro a jogar. Este vai escolher um número random entre 1 e 4 e se o número que ele escolherk for maior que o *n_fosforos* a variável onde ele escolhe o número passa a ter um intervalo entre 1 e *n_fosforos* mais 1. 

Retira-se ao *n_fosforos* o número que ele escolheu. 
Se o *n_fosforos* for igual a zero o *jogador_per* passa a ser o computador, se não é a vez do jogador fazer a sua jogada. 
Caso o número colocado seja menor que 1, maior que 4 ou maior que o *n_fosforos* o programa vai pedir ao jogador para tentar escrever um número novamente. Em seguida retira-se ao *n_fosforos* o número escolhido pelo jogador. Ficando a variável igual a zero o *jogador_per* passa a ser o jogador, pois foi o último a retirar fósforos.
No final acontece um print de quem perdeu o jogo.