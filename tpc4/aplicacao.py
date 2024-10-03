def menu ():
    print ("--------------- MENU ----------------")
    print ("(1) - Criar Lista \n (2) - Ler Lista \n (3) - Soma \n (4) - Média \n (5) - Maior Número \n (6) - Menor Número \n (7) - Ordenada por ordem crescente \n (8) - Ordenada por ordem decrescente \n (9) - Procurar um elemento \n (0) - Sair")

menu ()

import random
cond = True
while cond:
    opcao = int(input("Escolha a opção que quer fazer: "))
    if opcao == 0:
        print ("Você saiu do programa!! \n Até breve!!")
        cond = False
    elif opcao == 1:
        n = int(input("Introduza o número de elementos pretendidos: "))
        lista = []
        while len(lista) < n:
            num = random.randrange(1,101)
            lista.append (num)
        print(lista)
        print ("--------------- MENU ----------------")
        print ("(1) - Criar Lista \n (2) - Ler Lista \n (3) - Soma \n (4) - Média \n (5) - Maior Número \n (6) - Menor Número \n (7) - Ordenada por ordem crescente \n (8) - Ordenada por ordem decrescente \n (9) - Procurar um elemento \n (0) - Sair")
    elif opcao == 2:
        lista = []
        x = int(input("Introduza quantos elementos deseja na lista: "))
        i = 0
        while i < x:
                l = int(input("Introduza os núemros que deseja que a lista tenha: "))
                lista.append(l)
                i = i + 1
        print (lista)
        print ("--------------- MENU ----------------")
        print ("(1) - Criar Lista \n (2) - Ler Lista \n (3) - Soma \n (4) - Média \n (5) - Maior Número \n (6) - Menor Número \n (7) - Ordenada por ordem crescente \n (8) - Ordenada por ordem decrescente \n (9) - Procurar um elemento \n (0) - Sair")
    elif opcao == 3:
        soma = 0
        for elem in lista:
             soma = soma + elem
        print ("A soma é:", soma)
        print ("--------------- MENU ----------------")
        print ("(1) - Criar Lista \n (2) - Ler Lista \n (3) - Soma \n (4) - Média \n (5) - Maior Número \n (6) - Menor Número \n (7) - Ordenada por ordem crescente \n (8) - Ordenada por ordem decrescente \n (9) - Procurar um elemento \n (0) - Sair")
    elif opcao == 4:
        soma = 0
        x = 0
        for elem in lista:
            soma = soma + elem
            x = x + 1
        media = soma / x
        print("A média é:", media)
        print ("--------------- MENU ----------------")
        print ("(1) - Criar Lista \n (2) - Ler Lista \n (3) - Soma \n (4) - Média \n (5) - Maior Número \n (6) - Menor Número \n (7) - Ordenada por ordem crescente \n (8) - Ordenada por ordem decrescente \n (9) - Procurar um elemento \n (0) - Sair")
    elif opcao == 5:
        maior = 0
        for elem in lista:
            if elem > maior:
                maior = elem
        print("O maior número é:", maior)
        print ("--------------- MENU ----------------")
        print ("(1) - Criar Lista \n (2) - Ler Lista \n (3) - Soma \n (4) - Média \n (5) - Maior Número \n (6) - Menor Número \n (7) - Ordenada por ordem crescente \n (8) - Ordenada por ordem decrescente \n (9) - Procurar um elemento \n (0) - Sair")
    elif opcao == 6:
        menor = lista[0]
        for elem in lista:
            if elem < menor:
                menor = elem
        print("O menor número é", menor)
        print ("--------------- MENU ----------------")
        print ("(1) - Criar Lista \n (2) - Ler Lista \n (3) - Soma \n (4) - Média \n (5) - Maior Número \n (6) - Menor Número \n (7) - Ordenada por ordem crescente \n (8) - Ordenada por ordem decrescente \n (9) - Procurar um elemento \n (0) - Sair")
    elif opcao == 7:
        lista_ord = lista.copy()
        lista_ord.sort ()
        if lista == lista_ord:
            print("Sim está ordenada por ordem crescente.")
        else:
            print("Não se encontra ordenada por ordem crescente.")
        print ("--------------- MENU ----------------")
        print ("(1) - Criar Lista \n (2) - Ler Lista \n (3) - Soma \n (4) - Média \n (5) - Maior Número \n (6) - Menor Número \n (7) - Ordenada por ordem crescente \n (8) - Ordenada por ordem decrescente \n (9) - Procurar um elemento \n (0) - Sair")
    elif opcao == 8:
        lista_ord = lista.copy()
        lista_ord.sort()
        lista_ord.reverse()
        if lista_ord == lista:
            print("Sim está ordenada de forma decrescente.")
        else:
            print("Não se encontra ordenada de forma decrescente.")
        print ("--------------- MENU ----------------")
        print ("(1) - Criar Lista \n (2) - Ler Lista \n (3) - Soma \n (4) - Média \n (5) - Maior Número \n (6) - Menor Número \n (7) - Ordenada por ordem crescente \n (8) - Ordenada por ordem decrescente \n (9) - Procurar um elemento \n (0) - Sair")
    elif opcao == 9:
        el = int(input("Introduza o elemento que quer ver se está na lista: "))
        posicao = lista.index(el)
        if el in lista:
            print("O",el,"encontra-se na lista, na posicao", posicao + 1)
        else:
            print ("-1")
        print ("--------------- MENU ----------------")
        print ("(1) - Criar Lista \n (2) - Ler Lista \n (3) - Soma \n (4) - Média \n (5) - Maior Número \n (6) - Menor Número \n (7) - Ordenada por ordem crescente \n (8) - Ordenada por ordem decrescente \n (9) - Procurar um elemento \n (0) - Sair")

