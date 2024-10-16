def menu():
    print ("-----------------Menu-----------------")
    print("\n (1)-Criar uma turma \n (2)-Inserir aluno na turma \n (3)-Listar a turma \n (4)-Consultar aluno por id \n (5)-Consultar aluno por nome \n (6)-Guardar a turma \n (7)-Carregar uma turma \n (0)-Sair da aplicação")

menu()

cond = True 
while cond:
    opcao = int(input("Selecione o que deseja fazer. "))
    if opcao == 0:
        print ("Você saiu da aplicação!! Até breve.")
        cond = False
    elif opcao == 1:
        turma = []
        n = int(input("Quantos alunos tem a turma. "))
        i = 0
        while i < n:
            nome = input("Coloque o nome do aluno. ")
            id = int(input("Introduza o número de aluno. "))
            notaTPC = int(input("Nota dos trabalhos de casa. "))
            notaProj = int(input("Nota do projeto. "))
            notaTeste = int(input("Nota do teste. "))
            notas = [notaTPC,notaProj,notaTeste]
            turma.append((nome,id,notas))
            i = i + 1
        print ("-----------------Menu-----------------")
        print("\n (1)-Criar uma turma \n (2)-Inserir aluno na turma \n (3)-Listar a turma \n (4)-Consultar aluno por id \n (5)-Consultar aluno por nome \n (6)-Guardar a turma \n (7)-Carregar uma turma \n (0)-Sair da aplicação")
    elif opcao == 2:
        nome = input("Coloque o nome do aluno. ")
        id = int(input("Introduza o número de aluno. "))
        notaTPC = int(input("Nota dos trabalhos de casa. "))
        notaProj = int(input("Nota do projeto. "))            
        notaTeste = int(input("Nota do teste. "))
        notas = [notaTPC,notaProj,notaTeste]
        turma.append((nome,id,notas))
        print ("-----------------Menu-----------------")
        print("\n (1)-Criar uma turma \n (2)-Inserir aluno na turma \n (3)-Listar a turma \n (4)-Consultar aluno por id \n (5)-Consultar aluno por nome \n (6)-Guardar a turma \n (7)-Carregar uma turma \n (0)-Sair da aplicação")
    elif opcao == 3:
        print(turma)
        print ("-----------------Menu-----------------")
        print("\n (1)-Criar uma turma \n (2)-Inserir aluno na turma \n (3)-Listar a turma \n (4)-Consultar aluno por id \n (5)-Consultar aluno por nome \n (6)-Guardar a turma \n (7)-Carregar uma turma \n (0)-Sair da aplicação")
    elif opcao == 4:
        id_recebido = int(input("Introduza o id do aluno. "))
        for item in turma:
            if item[1] == id_recebido:
                print(item)
        print ("-----------------Menu-----------------")
        print("\n (1)-Criar uma turma \n (2)-Inserir aluno na turma \n (3)-Listar a turma \n (4)-Consultar aluno por id \n (5)-Consultar aluno por nome \n (6)-Guardar a turma \n (7)-Carregar uma turma \n (0)-Sair da aplicação")
    elif opcao == 5:
        nome_recebido = input("Introduza o nome do aluno. ")
        for item in turma:
            if item[0] == nome_recebido:
                print(item)
        print ("-----------------Menu-----------------")
        print("\n (1)-Criar uma turma \n (2)-Inserir aluno na turma \n (3)-Listar a turma \n (4)-Consultar aluno por id \n (5)-Consultar aluno por nome \n (6)-Guardar a turma \n (7)-Carregar uma turma \n (0)-Sair da aplicação")
    elif opcao == 6:
        nome = input("Escreva o nome do ficheiro ")
        file = open(nome,"w")
        for elem in turma:
            file.write(str(elem))
            file.write("\n")
        file.close()
        print ("-----------------Menu-----------------")
        print("\n (1)-Criar uma turma \n (2)-Inserir aluno na turma \n (3)-Listar a turma \n (4)-Consultar aluno por id \n (5)-Consultar aluno por nome \n (6)-Guardar a turma \n (7)-Carregar uma turma \n (0)-Sair da aplicação")
    elif opcao == 7:
        nome = input("Escreva o nome do ficheiro ")
        file = open(nome,"r")
        i=1
        for linha in file:
            print(str(i) + " :: " + linha, end='')
            i = i+1
        file.close()
        print ("-----------------Menu-----------------")
        print("\n (1)-Criar uma turma \n (2)-Inserir aluno na turma \n (3)-Listar a turma \n (4)-Consultar aluno por id \n (5)-Consultar aluno por nome \n (6)-Guardar a turma \n (7)-Carregar uma turma \n (0)-Sair da aplicação")
