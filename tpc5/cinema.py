def menu():
    print("""Menu: 
    (1) Reset
    (2) Criar sessão
    (3) Remover sessão
    (4) Listar Filmes
    (5) Consultar Filmes    
    (6) Verificar disponibilidade total
    (7) Comprar bilhete
    (8) Verificar disponibilidade de um lugar
    (9) Devolver bilhete
    (0) Sair
    """)

menu()


def inserirSala( cinema, sala):
    cinema.append(sala)
    return cinema

def listar(cinema):
    print("---------------Em exibição---------------")
    for sala in cinema:
        print("Filme: ", sala[2])
    print("-----------------------------------------")
    return 

def disponivel(cinema, filme, lugar):
    cond = False
    for sala in cinema:
        if (sala[2] == filme):
            if lugar not in sala[1]:
                cond = True 

    return cond

def vendeBilhete(cinema, filme, lugar):
    if disponivel(cinema, filme, lugar):
        for sala in cinema:
            if (sala[2] == filme):
                sala[1].append(lugar)
    return (cinema)

def listarDisponibilidades(cinema):
    print("---------------Em exibição---------------")
    for sala in cinema:
        nlugaresdisponiveis = sala[0]-len(sala[1])
        print("Filme: ", sala[2],"  |  Número lugares disponíveis: ", nlugaresdisponiveis)
    print("-----------------------------------------")
    return 

def devolveBilhete(cinema, filme, lugar):
    for sala in cinema:
        if sala[2] == filme:
            sala[1].remove(lugar)
    return cinema

def listarSala(cinema, filme):
    for sala in cinema:
        if sala[2] == filme:
            print("---------------Filme ", sala[2], "---------------")
            print("Nome: ", sala[2],"  |  Número lugares: ", sala[0], "  |  Lugares ocupados: ", sala[1])
            print("--------------------------------------")
            
    return


def criaSala(cinema, filme, nlugares):
    sala=(nlugares, [], filme)
    cinema.append(sala)
    return (cinema)

def removeSala(cinema, filme):
    for sala in cinema:
        if sala[2] == filme:
            if sala[1] == []:
                cinema.remove(sala)
            else:
                print("Não foi possível remover o parque escolhido pois este tem lugares ocupados.")

    return (cinema)

def menu():
    print("""Menu: 
    (1) Reset
    (2) Criar sessão
    (3) Remover sessão
    (4) Listar Filmes
    (5) Consultar Filmes    
    (6) Verificar disponibilidade total
    (7) Comprar bilhete
    (8) Verificar disponibilidade de um lugar
    (9) Devolver bilhete
    (0) Sair
    """)

opcao=1
sala1 = [150, [], "Twilight"]
sala2 = [200, [], "Hannibal"]
sala3 = [75, [], "It end with us"]
cinema1 = []
cinema1 = inserirSala(cinema1,sala1)
cinema1 = inserirSala(cinema1,sala2)
cinema1 = inserirSala(cinema1,sala3)

while opcao != '0':
    menu()
    opcao = input("Introduza uma opção (número de 0 a 9): ")
    if opcao=="1":
        cinema1=[]
    elif opcao=="2":
        nlugares = int(input("Número de lugares na sala: "))
        filme = input("Nome do filme: ")
        sala = (nlugares, [], filme)
        cinema = inserirSala(cinema1, sala)
    elif opcao=="3":
        filme=input("Insira o nome do filme que pretende remover: ")
        removeSala(cinema1, filme)
    elif opcao=="4":
        listar(cinema1)
    elif opcao=="5":
        filme=input("Insira o nome do filme que pretende consultar: ")
        listarSala(cinema1, filme)
    elif opcao=="6":
        listarDisponibilidades(cinema1)
    elif opcao=="7":
        filme=input("Insira o nome do filme para o qual pretende comprar bilhete: ")
        lugar=int(input("Insira o lugar que pretende comprar: "))
        vendeBilhete(cinema1, filme, lugar)
    elif opcao=="8":
        filme=input("Insira o nome do filme que pretende consultar: ")
        lugar=int(input("Insira o lugar que pretende consultar a disponibilidade: "))
        print(disponivel(cinema1, filme, lugar))
    elif opcao=="9":
        filme=input("Insira o nome do filme para o qual pretende realizar a devolução do bilhete: ")
        lugar=int(input("Insira o lugar que pretende devolver: "))
        devolveBilhete(cinema1, filme, lugar)
    else:
        print("Escolheu sair. A atual lista de filmes é: ")
        listar(cinema1)