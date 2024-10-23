def menu ():
    print ("--------------- MENU ----------------")
    print ("\n (1) - Guardar tabela num ficheiro \n (2) - Carregar tabela de num ficheiro \n (3) - Temperatura média de cada dia \n (4) - Temperatura mínima da tabela \n (5) - Amplitude térmica \n (6) - Dia com maior precipitação \n (7) - Dia com precipitação mais alta que x \n (8) - Dias consecutivos com precipitação mais baixa que x \n (9) - Gráfico da temperatura mínina, máxima e pluviosidade \n (10) - Ver tabela de meteorologia \n (0) - Sair")

menu ()

cond = True
while cond:
    opcao = int(input("Escolha a opção que quer fazer: "))
    if opcao == 0:
        print ("Você saiu do programa!! \n Até breve!!")
        cond = False
    elif opcao == 1:
        tabMeteo = input("Introduza o nome do ficheiro: ")
        n = int(input("Quantos dias tem a tabela? "))
        i = 0
        t = []
        while i < n:
            dia = int(input("Introduza o dia: "))
            mes = int(input("Introduza o mes: "))
            ano = int(input("Introduza o ano: "))
            data = (dia,mes,ano)
            min = float(input("Introduza a temperatura mínima: "))
            max = float(input("Introduza a temperatura máxima: "))
            prec = float(input("Introduza a precipitação: "))
            t.append((data,min,max,prec))
            i =  i + 1
        file = open(tabMeteo,"w")
        file.write("DATA --- TEMPMIN --- TEMPMAX --- PRECIPITACAO")
        file.write("\n")
        for data,min,maz,prec in t:
            file.write(str(data) + " | " + str(min) + " | " + str(max) + " | " + str(prec))
            file.write("\n")
        file.close()
        print ("--------------- MENU ----------------")
        print ("\n (1) - Guardar tabela num ficheiro \n (2) - Carregar tabela de num ficheiro \n (3) - Temperatura média de cada dia \n (4) - Temperatura mínima da tabela \n (5) - Amplitude térmica \n (6) - Dia com maior precipitação \n (7) - Dia com precipitação mais alta que x \n (8) - Dias consecutivos com precipitação mais baixa que x \n (9) - Gráfico da temperatura mínina, máxima e pluviosidade \n (10) - Ver tabela de meteorologia \n (0) - Sair")
        
    elif opcao == 2:
        res = []
        tabMeteo = input("Introduza o nome do ficheiro que quer carregar: ")
        file = open(tabMeteo,"r")
        for linha in file:
            campos = linha.strip().split("|") #split devolve uma lista
            if len(campos) == 4:
                data = campos[0]
                TempMin,TempMax,precipitacao = map(float,campos[1:])
                previsao = (data,TempMin,TempMax,precipitacao)
                res.append(previsao)
        print(res)
        print ("--------------- MENU ----------------")
        print ("\n (1) - Guardar tabela num ficheiro \n (2) - Carregar tabela de num ficheiro \n (3) - Temperatura média de cada dia \n (4) - Temperatura mínima da tabela \n (5) - Amplitude térmica \n (6) - Dia com maior precipitação \n (7) - Dia com precipitação mais alta que x \n (8) - Dias consecutivos com precipitação mais baixa que x \n (9) - Gráfico da temperatura mínina, máxima e pluviosidade \n (10) - Ver tabela de meteorologia \n (0) - Sair")
    elif opcao == 3:
        lista = []
        for data,min,max,_ in res:
            tempmedia = (min + max)/2
            lista.append((data,tempmedia))
        print(lista)
        print ("--------------- MENU ----------------")
        print ("\n (1) - Guardar tabela num ficheiro \n (2) - Carregar tabela de num ficheiro \n (3) - Temperatura média de cada dia \n (4) - Temperatura mínima da tabela \n (5) - Amplitude térmica \n (6) - Dia com maior precipitação \n (7) - Dia com precipitação mais alta que x \n (8) - Dias consecutivos com precipitação mais baixa que x \n (9) - Gráfico da temperatura mínina, máxima e pluviosidade \n (10) - Ver tabela de meteorologia \n (0) - Sair")
    elif opcao == 4:
        minima = res[0][1]
        for _,min,_,_ in res:
            if min < minima:
                minima = min
        print("A temperatura mínima da tabela toda é na data:",data,"e é:",minima)
        print ("--------------- MENU ----------------")
        print ("\n (1) - Guardar tabela num ficheiro \n (2) - Carregar tabela de num ficheiro \n (3) - Temperatura média de cada dia \n (4) - Temperatura mínima da tabela \n (5) - Amplitude térmica \n (6) - Dia com maior precipitação \n (7) - Dia com precipitação alta baixa que x \n (8) - Dias consecutivos com precipitação mais baixa que x \n (9) - Gráfico da temperatura mínina, máxima e pluviosidade \n (10) - Ver tabela de meteorologia \n (0) - Sair")
    elif opcao == 5:
        lista1 = []
        amplitude = 0
        for data,min,max,_ in res:
            amplitude = max - min
            lista1.append((data,amplitude))
        print(lista1)
        print ("--------------- MENU ----------------")
        print ("\n (1) - Guardar tabela num ficheiro \n (2) - Carregar tabela de num ficheiro \n (3) - Temperatura média de cada dia \n (4) - Temperatura mínima da tabela \n (5) - Amplitude térmica \n (6) - Dia com maior precipitação \n (7) - Dia com precipitação alta baixa que x \n (8) - Dias consecutivos com precipitação mais baixa que x \n (9) - Gráfico da temperatura mínina, máxima e pluviosidade \n (10) - Ver tabela de meteorologia \n (0) - Sair")
    elif opcao == 6:
        prec_max = res[0][3]
        for data,_,_,prec in res:
            if prec > prec_max:
                prec_max = prec
        print("A precipitação máxima ocorreu na data",data,"e é de",prec_max)
        print ("--------------- MENU ----------------")
        print ("\n (1) - Guardar tabela num ficheiro \n (2) - Carregar tabela de num ficheiro \n (3) - Temperatura média de cada dia \n (4) - Temperatura mínima da tabela \n (5) - Amplitude térmica \n (6) - Dia com maior precipitação \n (7) - Dia com precipitação alta baixa que x \n (8) - Dias consecutivos com precipitação mais baixa que x \n (9) - Gráfico da temperatura mínina, máxima e pluviosidade \n (10) - Ver tabela de meteorologia \n (0) - Sair")
    elif opcao == 7:
        p = float(input("Introduza o limite x: "))
        lista2 = []
        for data,_,_,prec in res:
            if prec > p:
                lista2.append((data,prec))
        print(lista2)
        print ("--------------- MENU ----------------")
        print ("\n (1) - Guardar tabela num ficheiro \n (2) - Carregar tabela de num ficheiro \n (3) - Temperatura média de cada dia \n (4) - Temperatura mínima da tabela \n (5) - Amplitude térmica \n (6) - Dia com maior precipitação \n (7) - Dia com precipitação alta baixa que x \n (8) - Dias consecutivos com precipitação mais baixa que x \n (9) - Gráfico da temperatura mínina, máxima e pluviosidade \n (10) - Ver tabela de meteorologia \n (0) - Sair")
    elif opcao == 8:
        p = float(input("Introduza o limite x: "))
        max_local = 0
        max_global = 0
        for _,_,_,prec in res:
            if prec < p:
                max_local = max_local + 1
            else:
                if max_local > max_global:
                    max_global = max_local
                max_local = 0
        if (max_local > max_global):
            max_global = max_local
        print(max_global)
        print ("--------------- MENU ----------------")
        print ("\n (1) - Guardar tabela num ficheiro \n (2) - Carregar tabela de num ficheiro \n (3) - Temperatura média de cada dia \n (4) - Temperatura mínima da tabela \n (5) - Amplitude térmica \n (6) - Dia com maior precipitação \n (7) - Dia com precipitação alta baixa que x \n (8) - Dias consecutivos com precipitação mais baixa que x \n (9) - Gráfico da temperatura mínina, máxima e pluviosidade \n (10) - Ver tabela de meteorologia \n (0) - Sair")
    elif opcao == 9:
        import matplotlib.pyplot as plt
        datas = [f"{(data[0])}-{(data[1])}-{(data[2])}" for data, *_ in res]
        temp_min = [min for _,min,*_ in res]
        temp_max = [max for _,_,max,_ in res]
        preci = [prec for _,_,_,prec in res]
        plt.plot(datas,temp_min, label="Temp Mínima") #recebe um x e um y
        plt.plot(datas,temp_max, label="Temp Máxima") 
        plt.plot(datas,preci, label="Precipitacao") 
        plt.xlabel("DATA")
        plt.ylabel("TEMPERATURA ºC")
        plt.title("Temperatura Mínima, Máxima e Precipitação")
        plt.legend()
        plt.show()
        print ("--------------- MENU ----------------")
        print ("\n (1) - Guardar tabela num ficheiro \n (2) - Carregar tabela de num ficheiro \n (3) - Temperatura média de cada dia \n (4) - Temperatura mínima da tabela \n (5) - Amplitude térmica \n (6) - Dia com maior precipitação \n (7) - Dia com precipitação alta baixa que x \n (8) - Dias consecutivos com precipitação mais baixa que x \n (9) - Gráfico da temperatura mínina, máxima e pluviosidade \n (10) - Ver tabela de meteorologia \n (0) - Sair")
    elif opcao == 10:
        for data,min,max,prec in res:
            print("DATA ----------- TEMP MIN --- TEMP MAX --- PREC")
            print(data, "      ", min, "   ", max, "     ", prec)
        
