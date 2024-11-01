# TESTE DE AFERIÇÃO

No tpc1 respondi às questões com listas em compreensão. 
Na alínea a) faz-se a dição de duas listas, onde a primeira continha todos os elementos da lista1 que não se encontravam na lista2 e na segunda acontecia o contrário.
Na alínea b) seleciona-se as palavras da frase que são compostas por mais de 3 letras, mas primeiro faz-se um split da frase para depois conseguir percorrer palavra por palavra.
Na alíneas c) cria-se um tuplo dentro da lista onde vai fornecer o índice da palavra de uma lista já fornecida.

No tpc2 escrevi os algoritmos específicos para cada problema.
Na alínea a) cria-se um *cont* para guardar as vezes em que a substring aparece na string, e depois percorre a palavra letra por letra com o comprimento da substring. Se fossem iguais o *cont* aumenta mais um se não permanece igual.
Na alínea b) utiliza-se o *sorted* para ordenar uma lista e depois usa-se os três primeiros elementos da mesma para realizar a multiplicação mais baixa possível.
Na alínea c) cria-se uma variàvel *res* que tem como valor o número fornecido. Enquanto que o comprimento da string de *res* seja diferente de 1 cria-se um lista *soma* em que se encontram lá dentro todos os números da string de *res* e essa passa a ter o valor de *soma[0]* e por cada valor presente na lista, sem ser o primeiro, vai-se adicionar esse número ao res anterior.
Na alínea d) o algoritmo vai percorrer todo o comprimento da string - o comprimento da string2 + 1 e depois comparar se essa palavra na string1 é igual à da string2. Se for vai haver retorno do índice da primeira ocorrência de string2, e não devolve -1.

No tpc3 tínhamos uma lista de dicionários onde temos de tirar certas informações.
Na alínea a) apenas é necessário fazer o *return* do *len* da lista.
Na alínea b) tem de se criar um lista vazia e depois para cada elemento da lista verifica-se se tem 'autor' e se esse é igual ao dado pelo utilizador. Depois se tiver 'conteudo' no elemnto vai adicionar-se à lista o valor desse conteudo. E fazer a mesma coisa para os comentarios do autor.
Na alínea c) criou-se uma lista vazia para colocar os autores. Por cada elemento presente na lista, se o 'autor' está no elemento, faz-se um *append* do nome do autor. Tmabém tem de se fazer a mesma coisa com os comentarios e se tiver outros autores estes também vão ser adicionados à lista. No final faz-se um *return* do *sorted* da lista, uma vez que pedem a lista de autores por ordem alfabetica.
Na alínea d) 
Na alínea e) percorre-se a lista e se o 'id' se encontra no elemento, e o valor deste for igual ao *id* dado faz-se o *remove* desse elemento.
Na alínea f) cria-se um dicionário vazio no início e por cada elemento na lista vai-se verificar se tem um 'autor' e se este é igual ao dado inicialmente. Se esse 'autor' já etsiver no dicionário adiciona-se mais um ao valor dele, se não esse passa a ser um. Fazer a mesma coisa para os comentários presentes nos elementos da lista.
Na alínea g) inicialmente cria-se uma lista vazia. Em seguida tem-se de ir aos comentários de cada elemento da lista e verificar se o autor fornecido é igual ao autor presente nos comentários. Se isso aconetecer adiciona-se à lista o conteúdo que se encontra no comentário.
