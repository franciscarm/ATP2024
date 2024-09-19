# Jogo do adivinha

O primeiro código tem o algoritmo onde o computador tenta acertar o número que o utilizador está a pensar.
Fiz import random e criei duas variáveis, o *min = 0* e o "*max = 100*. Inicialmente o computador vai apresentar na interface o seu primeiro palpite (irá ser um número random). 
O utilizador, após esse palpite, irá escrever *m*, *n* ou *i* de acordo com o número que o computador referiu, e os palpites vão ser iguais a 1.
Se o utilizador escrever *m* adiciona-se um aos palpites e a variável *min* vai passar a ser o número dado pelo computador mais um, reduzindo assim o intervalo de número que ainda podem ser possíveis escolher. Acontecendo isto, o computador imprime novamente um novo número e continua assim até acertar.
Se for escrito *n* adiciona-se um aos palpites e o *max* vai passar a ser o palpite que o computador forneceu, diminuindo as suas possibilidades de resposta. Acontecendo isto, o computador imprime novamente um novo número e continua assim até acertar.
Quando acertar o utilizador escreve *i* e aparecerá qual era o número correto e quantas tentativas é que o computador demorou para chegar ao mesmo.

O segundo código corresponde ao jogo onde é o utilizador que tenta adivinhar o que o computador pensou.
Crei uma variével onde o computador escolhe um número random, e os palpites são zero inicialmente. Em seguida o utilizador pode digitar o número que acha que é o correto. 
Enquanto que o palpite do utilizador não for igual ao do computador o número de palpites aumenta. 
Se o palpite for maior que o número irá aparecer na interface que é preciso adivinhar um número mais baixo que aquele. Caso seja menor, é preciso adivinhar um número mais alto.
No final irá aparecer que acertou o número e quantas tentativas levou a tal.