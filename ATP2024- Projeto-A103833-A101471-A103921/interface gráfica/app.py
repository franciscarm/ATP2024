import PySimpleGUI as sg
import tarefas
import graficos

sg.theme("NeutralBlue")

dataset = []

layout = [
    [sg.Text("ATA MÉDICA", font = ("Helvetica", 20), justification ="center", size = (30, 1))], 
    [sg.Button("Iniciar", size = (50, 2), key = "-INICIAR-")],
    [sg.Button("Sair", size = (50, 2), key = "-SAIR-")]
]

window = sg.Window("ATA MÉDICA", layout, size = (400, 150), finalize = True)  

stop = False
while not stop:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "-SAIR-":
        stop = True
    elif event == "-INICIAR-":
        window.close()

        menu_layout = [
            [sg.Button("Carregar BD", key = "-CARREGAR-")],
            [sg.Button("Gravar BD", key = "-GRAVAR-", disabled = True)],
            [sg.Button("Criar uma publicação", key =  "-CRIAR-", disabled = True)],
            [sg.Button("Remover uma publicação", key = "-REMOVER-", disabled = True)],
            [sg.Button("Atualizar publicação", key = "-ATUALIZAR-", disabled = True)],
            [sg.Button("Listar publicações", key = "-LISTAR-", disabled = True)],
            [sg.Button("Consultar publicações por um parâmetro específico", key = "-CONSULTAR-", disabled = True)],
            [sg.Button("Análise de publicações por autor", key = "-A_AUTOR-" , disabled = True)],
            [sg.Button("Análise de publicações por palavras-chave", key = "-A_PALACHAVE-", disabled = True)],
            [sg.Button("Exportar publicações", key = "-EXPORTAR-", disabled = True)],
            [sg.Button("Importar publicações", key = "-IMPORTAR-", disabled = True)],
            [sg.Button("Relatório", key = "-RELATORIO-", disabled = True)],
            [sg.Button("Sair", key = "-SAIR-")]
        ]

        data_viewer_column = [
            [sg.Text("Selecione a opção", size = (40,1), key = "-OPCAO-")],
            [sg.Text(size = (50,1), key = "-DADOS-", auto_size_text = True)],
            [sg.Text("Não se esqueça de carregar a base de dados primeiro!", size = (40,1), key = "-BD-")]
        ]

        layout = [
            [sg.Column(menu_layout, element_justification='left'),
             sg.VSeparator(),
             sg.Column(data_viewer_column)]
        ]

        window = sg.Window("Menu", layout, location=(40,40), font=("Helvetica", 15), size=(1800,900))
        carregou_BD = False 

        stop = False
        while not stop:
            event, values = window.read()
            if event in [sg.WINDOW_CLOSED, '-SAIR-']:
                stop = True

            elif event == '-CARREGAR-':
                ficheiro = sg.popup_get_file("Selecione o ficheiro json", file_types = (("fichriro json", "*.json"),)) #1º parentese é um tuplo, logo meto o primeiro parãmetro e como não meto segundo apenas coloco uma virgula. dentro do 2º paranteses tenno um label e um padrão
                if ficheiro:
                    dataset = tarefas.carregar_dataset(ficheiro)
                    window["-DADOS-"].update(f"Foram carregados {len(dataset)} registos")
                    window["-BD-"].update(" ")
                    carregou_bd=True
                if carregou_bd==True:
                    for key in ["-GRAVAR-", "-CRIAR-", "-REMOVER-", "-ATUALIZAR-", "-LISTAR-", "-CONSULTAR-", "-A_AUTOR-", "-A_PALACHAVE-", "-RELATORIO-", "-EXPORTAR-", "-IMPORTAR-"]:
                        window[key].update(disabled=False)

            elif event == '-CRIAR-':
                window["-DADOS-"].update("A criar uma nova tarefa...")
                
                tamanho_inicial = len(dataset)  
                tarefas.criarPubli(dataset, ficheiro)
                tamanho_final = len(dataset)  

                if tamanho_inicial == tamanho_final:  # Nenhuma publicação foi adicionada
                    window["-DADOS-"].update('A publicação não foi executada!')
                else:
                    window["-DADOS-"].update('Publicação registada com sucesso!')

            elif event == '-REMOVER-':
                window["-DADOS-"].update("Uma publicação está a ser removida, aguarde!")
                remove = tarefas.removerPubli(dataset)
                if remove in [False, 'Cancelar']:
                    window["-DADOS-"].update('Remoção da publicação foi cancelada!')
                else:
                    window["-DADOS-"].update('Publicação removida com sucesso!') 

            elif event == '-ATUALIZAR-':
                window["-DADOS-"].update("Uma publicação está a atualizar!")
                sucesso = tarefas.atualizarPubli(dataset)
                if not sucesso :
                    window["-DADOS-"].update("A atualização foi cancelada!")
                else:
                    window["-DADOS-"].update("A atualização foi executada com sucesso!")

            elif event == '-GRAVAR-':
                window["-DADOS-"].update("A gravar a BD, aguarde!")
                event_gravarTarefa, values_gravarTarefa = tarefas.guardarDataset(dataset)
                if event_gravarTarefa == 'Cancelar':
                    window["-DADOS-"].update('A operação foi cancelada!')
                else:
                    window["-DADOS-"].update('Os dados foram guardados com sucesso!')

            elif event == '-LISTAR-':
                window["-DADOS-"].update("A listar as publicações, aguarde!")
                tarefas.listar_publicacoes(dataset)

            elif event == '-CONSULTAR-':
                window["-DADOS-"].update("A consultar publicações")
                layout_consulta = [
                    [sg.Text("Que parâmetro quer selecionar?")],
                    [sg.Button("Consultar publicações por identificador", key = "-P_IDENTIFICADOR-")],
                    [sg.Button("Consultar publicações por título", key = "-P_TITULO-")],
                    [sg.Button("Consultar publicações por autor", key = "-P_AUTOR-")],
                    [sg.Button("Consultar publicações por afiliação", key = "-P_AFILIACAO-")],
                    [sg.Button("Consultar publicações por palavra_chave", key = "-P_PALACHAVE-")],
                    [sg.Button("Consultar publicações por data de publicação", key = "-P_DATA-")],
                    [sg.Button("Fechar", key = "-FECHAR_PUB-")]
                ]
                window_consultas = sg.Window("Consultas", layout_consulta)
                
                cons_ativa = True
                while cons_ativa:
                    event_consultas, values_consultas = window_consultas.read()
                    if event_consultas in ("-FECHAR_PUB-", sg.WIN_CLOSED):
                        cons_ativa = False
                        window["-DADOS-"].update("Janela foi fechada!")
                    elif event_consultas == "-P_IDENTIFICADOR-":
                        tarefas.listar_publicacoes_identificador(dataset)
                    elif event_consultas == "-P_TITULO-":
                        tarefas.listar_publicacoes_titulo(dataset)
                    elif event_consultas == "-P_AUTOR-":
                        tarefas.listar_publicacoes_aut(dataset)
                    elif event_consultas == "-P_AFILIACAO-":
                        tarefas.listar_publicacoes_afliacao(dataset)
                    elif event_consultas == "-P_PALACHAVE-":
                        tarefas.listar_publicacoes_palavras_chave(dataset)
                    elif event_consultas == "-P_DATA-":
                        tarefas.listar_publicacoes_data_publicacao(dataset)
                window_consultas.close()


            elif event == "-A_AUTOR-":
                layout_autor = [
                    [sg.Text("Quer analisar os autores por ordem alfabética ou por frequência?")],
                    [sg.Button("Por ordem alfabética", key = "-ALFABETICA-")],
                    [sg.Button("Por frequência de artigos publicados", key = "-FREQUENCIA-")],
                    [sg.Button("Fechar", key = "-FECHAR_AUTOR-")]
                ]
                window_autor = sg.Window("Análise por autor", layout_autor)

                autor = True
                while autor:
                    event_autor, values_autor = window_autor.read()
                    if event_autor in ("-FECHAR_AUTOR-", sg.WIN_CLOSED):
                        autor = False
                        window["-DADOS-"].update("Janela foi fechada!")
                    elif event_autor == "-ALFABETICA-":
                        tarefas.listar_por_autor_ordem_alfabetica(dataset)
                    elif event_autor == "-FREQUENCIA-":
                        tarefas.listar_por_autor_frequencia_publicacoes(dataset)
                window_autor.close()

            elif event == "-A_PALACHAVE-":
                layout_palachave = [
                    [sg.Text("Quer analisar por palavras chaves de que modo?")],
                    [sg.Button("Por ordem alfabética", key = "-PALA_ALFABETICA-")],
                    [sg.Button("Por ocorrência nos artigos", key = "-PALA_FREQUENCIA-")],
                    [sg.Button("Fechar", key = "-FECHAR_PALACHAVE-")]
                ]
                window_palachave = sg.Window("Análise por palavras-chave", layout_palachave)

                palachave = True
                while palachave:
                    event_palachave, values_palachave = window_palachave.read()
                    if event_palachave in ("-FECHAR_PALACHAVE-", sg.WIN_CLOSED):
                        palachave = False
                        window["-DADOS-"].update("Janela foi fechada!")
                    elif event_palachave == "-PALA_ALFABETICA-":
                        tarefas.listar_por_palavra_chave_ordem_alfabetica(dataset)
                    elif event_palachave == "-PALA_FREQUENCIA-":
                        tarefas.listar_publicacao_por_palavra_chave_freq(dataset)
                window_palachave.close()

            elif event == '-EXPORTAR-':
                window["-DADOS-"].update("A exportar informação!")
                exp = tarefas.exportacao_por_pesquisa(dataset)
                if exp in [False, 'Cancelar']:
                    window["-DADOS-"].update('A exportação foi cancelada.')
                else:
                    window["-DADOS-"].update('A exportação foi realizada com sucesso.')

            elif event == '-IMPORTAR-':
                window["-DADOS-"].update("A importar informação!")
                imp = tarefas.adicionar_bd(dataset)
                if imp in [dataset, 'Cancelar']:
                    window["-DADOS-"].update('A importação foi cancelada.')
                else:
                    window["-DADOS-"].update('A importação foi realizada com sucesso.')

            elif event == '-RELATORIO-':
                window["-DADOS-"].update("A mostrar o relatório de estatísticas!")
                
                layout_relatorio = [
                    [sg.Text("Escolha o gráfico que deseja ver")],
                    [sg.Button("Publicações por ano", key = "-P_ANO-")],
                    [sg.Button("Publicações por mês de um ano específico", key = "-P_ANOESP-")],
                    [sg.Button("Número de publicações por autor", key = "-P_AUTOR20-")],
                    [sg.Button("Publicações de um autor por ano", key = "-P_AUTORANO-")],
                    [sg.Button("Distribuição de palavras-chaves", key = "-D_PALACHAVE-")],
                    [sg.Button("Palavras chaves mais frequentes por ano", key = "-PALACHAVE_ANO-")],
                    [sg.Button("Fechar", key = "-FECHARRELA-")]
                ]
                window_relatorio = sg.Window("Relatório de estatísticas", layout_relatorio)
                
                cons_ativa = True
                while cons_ativa:
                    event_relatorio, values_relatorio = window_relatorio.read()
                    if event_relatorio in ("-FECHARRELA-", sg.WIN_CLOSED):
                        cons_ativa = False
                        window["-DADOS-"].update("Janela foi fechada!")

                    elif event_relatorio == "-P_ANO-":
                        graficos.publicacoes_por_ano(dataset)

                    elif event_relatorio == "-P_ANOESP-":
                        if dataset:
                            ano_especifico = sg.popup_get_text("Qual ano é que deseja observar?", title = "Ano")
                            if ano_especifico:
                                graficos.publicacoes_por_mes(dataset,ano_especifico)
                    
                    elif event_relatorio == "-P_AUTOR20-":
                        graficos.publicacoes_por_autor(dataset)
                    
                    elif event_relatorio == "-P_AUTORANO-":
                        if dataset:
                            nome_autor = sg.popup_get_text("Qual o nome do autor que pretende analisar?", title = "Autor")
                            if nome_autor:
                                graficos.publicacoes_de_autor_por_ano(dataset, nome_autor)

                    elif event_relatorio == "-D_PALACHAVE-":
                        graficos.palavras_chave_mais_frequentes(dataset)

                    elif event_relatorio == "-PALACHAVE_ANO-":
                        graficos.palavras_chave_por_ano_pie(dataset)

                window_relatorio.close()

window.close()




