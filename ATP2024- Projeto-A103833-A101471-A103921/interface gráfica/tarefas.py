import PySimpleGUI as sg
import json
from datetime import datetime

def carregar_dataset(ficheiro):
    res = []
    try:
        with open(ficheiro, encoding = 'UTF-8') as f: # igual a ter f = open(ficheiro) mas este fecha o ficheiro automaticamente
            res = json.load(f)
            sg.popup(f"Dataset carregado com sucesso!\n Foram lidos {len(res)} registos.", title = 'Sucesso')
    except Exception as e:
        sg.popup(f"Erro ao carregar o dataset: {e}", title = 'Erro')
    return res

def guardarDataset(bd):
    formLayout = [[sg.Text('Introduza o nome do ficheiro para guardar os dados')],
          [sg.Text('Nome', size = (10, 1)), sg.InputText(key='-FNOME-'),sg.Text('.json', size = (5, 1)) ],
          [sg.Button('Inserir'), sg.Button('Cancelar')]]

    wform = sg.Window('Guardar Dataset', formLayout, location = (200,300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)
    nome=inputValues['-FNOME-']
    if nome[-5:] == ".json":
        nome = nome[:-5]
    fnome = nome + ".json"
    fout = open(fnome,"w", encoding = 'utf-8')
    json.dump(bd, fout, indent = 4, ensure_ascii = False)
    fout.close()
    return inputEvent, inputValues


def criarPubli(dataset, ficheiro):

    layout = [
        [sg.Text("abstract: "), sg.InputText(do_not_clear = False, key = "-ABSTRACT-")],
        [sg.Text("keywords: "), sg.InputText(do_not_clear = False, key = "-KEYWORDS-")],
        [sg.Text("authors (separados por ;): "), sg.InputText(do_not_clear = False, key = "-AUTORES-")],
        [sg.Text("afilliation (separado por ;): "), sg.InputText(do_not_clear = False, key = "-AFILIACAO-")],
        [sg.Text("doi: "), sg.InputText(do_not_clear = False, key = "-DOI-")],
        [sg.Text("pdf: "), sg.InputText(do_not_clear = False, key = "-PDF-")],
        [sg.Text("publish_date: "),
         sg.Text("Ano"), sg.Combo([str(ano) for ano in range(2024, 2026)], key = "-ANO-", size = (7, 2), default_value = "2024"),
         sg.Text("Mês"), sg.Combo([f"{mes:02d}" for mes in range(1, 13)], key = "-MES-", size = (6, 1), default_value = "01"),
         sg.Text("Dia"), sg.Combo([f"{dia:02d}" for dia in range(1, 32)], key = "-DIA-", size = (6, 1), default_value = "01"),
         ],
        [sg.Text("title: "), sg.InputText(do_not_clear = False, key = "-TITULO-")],
        [sg.Text("url: "), sg.InputText(do_not_clear = False, key = "-URL-")],
        [sg.Button("Salvar"), sg.Button("Cancelar")]
    ]
    window = sg.Window("Criar publicação", layout, location = (100, 100), font = ('Helvetica', 15))

    stop = False
    while not stop:
        event, values = window.read()
        if event in ["Cancelar", sg.WINDOW_CLOSED]:
            stop = True
        else:
            autores = values["-AUTORES-"].split(";")
            afiliacoes = values["-AFILIACAO-"].split(";")

            lista = [{"name": autor.strip(), "affiliation": afiliacao.strip()}
                     for autor, afiliacao in zip(autores, afiliacoes)]
            publi = {
                "abstract": values["-ABSTRACT-"],
                "keywords": values["-KEYWORDS-"],
                "authors": lista,
                "doi": values["-DOI-"],
                "pdf": values["-PDF-"],
                "publish_date": f'{values["-ANO-"]}-{values["-MES-"]}-{values["-DIA-"]}',
                "title": values["-TITULO-"],
                "url": values["-URL-"],
            }

            dataset.append(publi)

            try:
                with open(ficheiro, "w", encoding = "UTF-8") as file_out:
                    json.dump(dataset, file_out, indent = 4, ensure_ascii = False)
                sg.popup("Publicação criada e salva com sucesso!", title = "Sucesso")
            except Exception as e:
                sg.popup(f"Erro ao salvar a publicação: {e}", title = "Erro")

            stop = True  

    window.close()
    return dataset



def removerPubli(dataset):
    titulos = [publicacao['title'] for publicacao in dataset]

    if not titulos:
        sg.popup("Não existe nenhuma publicação disponível para a remoção", font = ("Helvetica", 15))
        return False
    
    layout = [
        [sg.Text("Selecione o título da publicação que deseja remover.", font = ("Helvetica", 15))],
        [sg.Combo(titulos, key = '-TITULO-', size = (50,1), readonly = True)],
        [sg.Button("Confirmar"), sg.Button("Cancelar")]
    ]

    window = sg.Window("Remover publicação", layout, location = (200, 300), font = ("Helvetica", 15))

    while True:
        event, values = window.read()
        if event in ("Cancelar", sg.WIN_CLOSED):
            window.close()
            return False
        elif event == "Confirmar":
            titulo_selc = values['-TITULO-']
            if titulo_selc:
                for i, publicacao in enumerate(dataset):
                    if publicacao.get('title') == titulo_selc:
                        del dataset[i]
                        sg.popup(f"Publicação {titulo_selc} removida com sucesso!", font = ("Helvetica", 15))
                        window.close()
                        return True
            else:
                sg.popup("Não foi selecionado nenhum título!", font = ("Helvetica", 15))

def listar_publicacoes(bd):
    # criei uma tabela iterativa, se carregar numa linha, abre uma janela pop up com as informaçoes
    linhas = []
    for publicacao in bd:
        linha = [
            publicacao["title"], 
            publicacao["publish_date"],
            publicacao["keywords"],
            ", ".join([autor['name'] for autor in publicacao["authors"]]),
            publicacao["doi"],
            publicacao["url"]
        ]
        linhas.append(linha)

    col_widths = [30, 15, 20, 25, 20, 25]

    layout = [
        [sg.Text("Selecione uma publicação para ver mais detalhes:", font = ("Helvetica", 15))],
        [
            sg.Table(
                values = linhas,
                headings = ['Title', 'Publish Date', 'Keywords', 'Authors', 'DOI', 'URL'],
                col_widths = col_widths,
                auto_size_columns=False,
                justification = 'middle',
                num_rows = min(len(linhas), 15),
                enable_events = True,
                key = '-TABELA-',
                font = ("Helvetica", 12),
                select_mode = sg.TABLE_SELECT_MODE_BROWSE
            )
        ],
        [sg.Button('Fechar')]
    ]

    wform = sg.Window("Publicações", layout, location = (100, 100), size = (1200, 600), font = ("Helvetica", 12))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent == sg.WIN_CLOSED or inputEvent == 'Fechar':
            wform.close()

    if inputEvent == '-TABELA-' and inputValues['-TABELA-']:
        index_selecionado = inputValues['-TABELA-'][0]  # Índice da linha selecionada
        publicacao_selecionada = bd[index_selecionado]

        sg.popup_scrolled(
            f"Título: {publicacao_selecionada['title']}\n\n"
            f"Autores: {', '.join([autor['name'] for autor in publicacao_selecionada['authors']])}\n\n"
            f"Resumo:\n{publicacao_selecionada['abstract']}\n\n"
            f"Publicado em: {publicacao_selecionada['publish_date']}\n\n"
            f"DOI: {publicacao_selecionada['doi']}\n\n"
            f"URL: {publicacao_selecionada['url']}",
            title="Detalhes da Publicação",
            font=("Helvetica", 12),
            size=(80, 20)
            )

    return


def atualizarPubli(dataset):
    # Listar títulos disponíveis
    titulos = [publicacao['title'] for publicacao in dataset]

    if not titulos:
        sg.popup("Não existem publicações disponíveis para atualização.", title = "Erro")
        return False

    # Layout para selecionar o título
    layout_titulo = [
        [sg.Text("Selecione o título da publicação que deseja atualizar:")],
        [sg.Combo(titulos, key = '-TITULO-', size = (50, 1), readonly = True)],
        [sg.Button("Confirmar"), sg.Button("Cancelar")]
    ]

    window_titulo = sg.Window("Selecionar Publicação", layout_titulo)
    event, values = window_titulo.read()

    if event == "Cancelar" or event == sg.WIN_CLOSED:
        sg.popup("Atualização cancelada.", title = "Cancelado")
        window_titulo.close()
        return False

    titulo_selecionado = values['-TITULO-']
    window_titulo.close()

    if not titulo_selecionado:
        sg.popup("Nenhum título selecionado!", title = "Erro")
        return False

    publicacao = next((pub for pub in dataset if pub['title'] == titulo_selecionado), None)

    if not publicacao:
        sg.popup(f"Publicação com título '{titulo_selecionado}' não encontrada.", title="Erro")
        return False

    opcoes = [
        ["Data de Publicação", publicacao.get("publish_date", "")],
        ["Resumo", publicacao.get("abstract", "")],
        ["Palavras-chave", publicacao.get("keywords", "")],
        ["Autores", ", ".join([autor.get("name", "") for autor in publicacao.get("authors", [])])],
        ["Afiliações", ", ".join([autor.get("affiliation", "") for autor in publicacao.get("authors", [])])]
    ]

    layout_selecao = [
        [sg.Text("Selecione o campo que deseja atualizar:")],
        [sg.Table(
            values=opcoes,
            headings=["Campo", "Valor Atual"],
            col_widths=[20, 50],
            auto_size_columns=False,
            justification = "left",
            enable_events = True,
            key = "-TABELA-",
            num_rows = min(len(opcoes), 10)
        )],
        [sg.Button("Confirmar"), sg.Button("Cancelar")]
    ]

    window_selecao = sg.Window("Selecionar Campo", layout_selecao, modal=True)
    event, values = window_selecao.read()

    if event == "Cancelar" or event == sg.WIN_CLOSED:
        sg.popup("Atualização cancelada.", title="Cancelado")
        window_selecao.close()
        return False

    selecionados = values["-TABELA-"]
    window_selecao.close()

    if not selecionados:
        sg.popup("Nenhum campo selecionado!", title="Erro")
        return False

    indice_escolhido = selecionados[0]
    campo_escolhido, valor_atual = opcoes[indice_escolhido]

    layout_atualizacao = [
        [sg.Text(f"Insira o novo valor para {campo_escolhido}:")],
        [sg.InputText(valor_atual, key="-NOVO_VALOR-")],
        [sg.Button("Salvar"), sg.Button("Cancelar")]
    ]

    window_atualizacao = sg.Window("Atualizar Campo", layout_atualizacao, modal=True)
    event, values = window_atualizacao.read()

    if event == "Salvar":
        novo_valor = values["-NOVO_VALOR-"]
        if campo_escolhido == "Data de Publicação":
            publicacao["publish_date"] = novo_valor
        elif campo_escolhido == "Resumo":
            publicacao["abstract"] = novo_valor
        elif campo_escolhido == "Palavras-chave":
            publicacao["keywords"] = novo_valor
        elif campo_escolhido == "Autores":
            nomes = novo_valor.split(", ")
            for i, autor in enumerate(publicacao.get("authors", [])):
                if i < len(nomes):
                    autor["name"] = nomes[i]
        elif campo_escolhido == "Afiliações":
            afiliacoes = novo_valor.split(", ")
            for i, autor in enumerate(publicacao.get("authors", [])):
                if i < len(afiliacoes):
                    autor["affiliation"] = afiliacoes[i]

        sg.popup("Publicação atualizada com sucesso!", title="Sucesso")
        window_atualizacao.close()
        return True

    elif event == "Cancelar" or event == sg.WIN_CLOSED:
        sg.popup("Atualização cancelada!", title="Cancelado")
        window_atualizacao.close()
        return False
    return True
    
def listar_publicacoes_identificador(bd):
    publicacoes = []
    identificadores = [publicacao['doi'] for publicacao in bd if "doi" in publicacao]
    
    formLayout = [[sg.Text('Introduza o identificador da publicação que pretende consultar: ')],
          [sg.Text('Identificador (doi)', size = (6, 1)), sg.Combo(identificadores, key = "-IDENTIFICADOR-", readonly = True)],
          [sg.Button('Inserir'), sg.Button('Cancelar')]]

    wform = sg.Window('Consulta por identificador', formLayout, location = (200,300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent == "Cancelar" or inputEvent == sg.WIN_CLOSED: 
        wform.close()
    
    elif inputEvent == "Inserir":
        identificador_escolhido = inputValues['-IDENTIFICADOR-']
        for publicacao in bd:
            if identificador_escolhido == (publicacao['doi']):
                publicacoes.append(publicacao)
        if publicacoes:
            listar_publicacoes(publicacoes)
        else:
            sg.popup("Não existem publicações com o identificador fornecido.", font = ("Helvetica", 15))
    return publicacoes

def listar_publicacoes_titulo(bd):
    publicacoes=[]
    titulo=[]
    for publicacao in bd:
        if publicacao["title"] not in titulo:
            titulo.append(publicacao["title"])

    formLayout = [[sg.Text('Introduza o título da publicação que pretende consultar: ')],
          [sg.Text('Título', size = (6, 1)), sg.Combo(titulo, key = "-TITULO-", readonly = True)],
          [sg.Button('Inserir'), sg.Button('Cancelar')]]

    wform = sg.Window('Consulta por título', formLayout, location = (200,300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent == "Cancelar" or inputEvent == sg.WIN_CLOSED: 
        wform.close()
    
    elif inputEvent == "Inserir":
        titulo = inputValues['-TITULO-']
        for publicacao in bd:
            if titulo == (publicacao['title']):
                publicacoes.append(publicacao)
        if publicacoes:
            listar_publicacoes(publicacoes)
        else:
            sg.popup("Não existem publicações com o título fornecido.", font = ("Helvetica", 15))
    return publicacoes


def listar_publicacoes_aut(bd):
    publicacoes = []
    autores = []
    for publicacao in bd:
        for aut in publicacao["authors"]:
            if aut["name"] not in autores:
                autores.append(aut["name"])

    formLayout = [[sg.Text('Insira o nome do autor cujas publicações pretende consultar: ')],
          [sg.Text('Autor', size = (6, 1)), sg.Combo(autores, key = "-AUTOR-", readonly = True)],
          [sg.Button('Inserir'), sg.Button('Cancelar')]]

    wform = sg.Window('Consulta por autor', formLayout, location = (200,300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent == "Cancelar" or inputEvent == sg.WIN_CLOSED: 
        wform.close()
    
    elif inputEvent == "Inserir":
        autor_escolhido = inputValues['-AUTOR-']
        for publicacao in bd:
            for aut in publicacao["authors"]:
                if autor_escolhido == (aut["name"]):
                    publicacoes.append(publicacao)
        if publicacoes:
            listar_publicacoes(publicacoes)
        else:
            sg.popup("Não existem publicações para o autor fornecido.", font = ("Helvetica", 15))
    return publicacoes

def listar_publicacoes_afliacao(bd):
    publicacoes = []
    afiliacoes = []
    for publicacao in bd:
        for aut in publicacao["authors"]:
            if aut["affiliation"] not in afiliacoes:
                afiliacoes.append(aut["affiliation"])

    formLayout = [[sg.Text('Insira o nome da afiliação que pretende consultar: ')],
          [sg.Text('Afiliação', size = (6, 1)), sg.Combo(afiliacoes, key = "-AFILIACAO-", readonly = True)],
          [sg.Button('Inserir'), sg.Button('Cancelar')]]

    wform = sg.Window('Consulta por afiliação', formLayout, location = (200,300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent == "Cancelar" or inputEvent == sg.WIN_CLOSED: 
        wform.close()
    
    elif inputEvent == "Inserir":
        afiliacao_escolhida = inputValues['-AFILIACAO-']
        for publicacao in bd:
            for aut in publicacao["authors"]:
                if afiliacao_escolhida == (aut["affiliation"]):
                    publicacoes.append(publicacao)
        if publicacoes:
            listar_publicacoes(publicacoes)
        else:
            sg.popup("Não existem publicações com a afiliação inserida.", font = ("Helvetica", 15))
    return publicacoes

def listar_publicacoes_palavras_chave(bd):
    
    publicacoes = []
    palavras_chave_unicas = set()  
    
    # Separar palavras-chave e adicioná-las ao conjunto
    for publicacao in bd:
        if "keywords" in publicacao:
            palavras_chave = publicacao["keywords"].split(",")  
            for palavra in palavras_chave:
                palavras_chave_unicas.add(palavra.strip()) 
   
    palavras_chave_unicas = sorted(palavras_chave_unicas)

    formLayout = [
        [sg.Text('Introduza a palavra-chave relacionada com as publicações que pretende consultar: ')],
        [sg.Text('Palavra-chave', size = (12, 1)), sg.Combo(palavras_chave_unicas, key = "-PALAVRA-CHAVE-", readonly = True)],
        [sg.Button('Inserir'), sg.Button('Cancelar')]
    ]

    wform = sg.Window('Consulta por palavra-chave', formLayout, location = (200, 300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent == "Cancelar" or inputEvent == sg.WIN_CLOSED: 
        wform.close()
    
    elif inputEvent == "Inserir":
        palavra_chave_escolhida = inputValues['-PALAVRA-CHAVE-']
        for publicacao in bd:
            if palavra_chave_escolhida in publicacao.get('keywords', '').split(","):
                publicacoes.append(publicacao)
        
        if publicacoes:
            listar_publicacoes(publicacoes)  
        else:
            sg.popup("Não existem publicações com a palavra-chave selecionada.", font = ("Helvetica", 15))
    
    return publicacoes

def listar_publicacoes_data_publicacao(bd):
    publicacoes=[]
    formLayout = [[sg.Text('Introduza a data da publicação que petende consultar: ')],
          [sg.Text("Data da publicação:"),
            sg.Text("Ano"), sg.Combo([str(ano) for ano in range(1900, 2026)], key = "-ANO-", size = (6, 1), default_value = "2024"),
            sg.Text("Mês"), sg.Combo([f"{mes:02d}" for mes in range(1, 13)], key = "-MES-", size = (4, 1), default_value = "01"),
            sg.Text("Dia"), sg.Combo([f"{dia:02d}" for dia in range(1, 32)], key = "-DIA-", size = (4, 1), default_value = "01"),
        ],
          [sg.Button('Inserir'), sg.Button('Cancelar')]]

    wform = sg.Window('Consulta por data de publicação', formLayout, location = (200,300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent == "Cancelar" or inputEvent == sg.WIN_CLOSED: 
        wform.close()
    
    elif inputEvent == "Inserir":
        data = f"{inputValues['-ANO-']}-{inputValues['-MES-']}-{inputValues['-DIA-']}"
        for publicacao in bd:
            if data == (publicacao["publish_date"]):
                publicacoes.append(publicacao)
        if publicacoes:
            listar_publicacoes(publicacoes)
        else:
            sg.popup("Não existem publicações com a data de publicação fornecida.", font = ("Helvetica", 15))
    return publicacoes


def listar_por_autor_frequencia_publicacoes(bd):
    # Contar a frequência de publicações de cada autor
    contador_autores = {}
    for publicacao in bd:
        for autor in publicacao["authors"]:
            nome_autor = autor["name"]
            if nome_autor in contador_autores:
                contador_autores[nome_autor] += 1
            else:
                contador_autores[nome_autor] = 1

    # Ordenar autores por frequência de publicações (decrescente)
    autores_ordenados = sorted(contador_autores.items(), key=lambda x: x[1], reverse=True)

    # Criar uma lista de opções com autores e  a sua contagem
    opcoes_autores = [f"{autor} ({freq} publicação/publicações)" for autor, freq in autores_ordenados]

    # Layout do formulário para selecionar autor
    formLayout = [
        [sg.Text('Selecione um autor para consultar as suas publicações:', font = ("Helvetica", 15))],
        [sg.Combo(opcoes_autores, key = "-AUTOR-", size = (50, 1), readonly = True)],
        [sg.Button('Inserir'), sg.Button('Cancelar')]
    ]

    wform = sg.Window('Consulta de publicações por autor', formLayout, location = (200, 300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent == "Cancelar" or inputEvent == sg.WIN_CLOSED:
        wform.close()
        return

    if inputEvent == "Inserir":
        autor_selecionado = inputValues["-AUTOR-"]
        if autor_selecionado:
            # Extrair o nome do autor selecionado 
            nome_autor = autor_selecionado.split(" (")[0]

            # Filtrar publicações do autor selecionado manualmente
            publicacoes = []
            for publicacao in bd:
                encontrou_autor = False
                for autor in publicacao["authors"]:
                    encontrou_autor = encontrou_autor or (autor["name"] == nome_autor)
                if encontrou_autor:
                    publicacoes.append(publicacao)

            # Exibir publicações ou mensagem de erro
            if publicacoes:
                listar_publicacoes(publicacoes)
            else:
                sg.popup("Não existem publicações para o autor fornecido.", font = ("Helvetica", 15))
    return


def listar_por_autor_ordem_alfabetica(bd):
    autores = []
    for publicacao in bd:
        for aut in publicacao["authors"]:
            if aut["name"] not in autores:
                autores.append(aut["name"])
                
    # Ordenar autores por ordem alfabetica 
    autores_ordenados_alfabetica = sorted(autores)

    # Criar uma lista de opções com autores 
    opcoes_autores_alfabetica = [f"{autor}" for autor in autores_ordenados_alfabetica]


    formLayout = [
        [sg.Text('Selecione um autor para consultar as suas publicações:', font = ("Helvetica", 15))],
        [sg.Combo(opcoes_autores_alfabetica, key = "-AUTOR-", size = (50, 1), readonly = True)],
        [sg.Button('Inserir'), sg.Button('Cancelar')]
    ]

    wform = sg.Window('Consulta de publicações por autor', formLayout, location = (200, 300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent == "Cancelar" or inputEvent == sg.WIN_CLOSED: 
        wform.close()

    elif inputEvent == "Inserir":
        autor_selecionado = inputValues["-AUTOR-"]
        if autor_selecionado:
            # Extrair apenas o nome do autor selecionado 
            nome_autor = autor_selecionado.split(" (")[0]

            # Filtrar publicações do autor selecionado
            publicacoes = [
                publicacao for publicacao in bd if any(autor["name"] == nome_autor for autor in publicacao["authors"])
            ] 
            if publicacoes:
                listar_publicacoes(publicacoes)
            else:
                sg.popup("Não existem publicações para o autor fornecido.", font = ("Helvetica", 15))

    return 


def listar_publicacao_por_palavra_chave_freq(bd):

    # prodecimento utilizado para obter as publicações por freq
    contador_palavras = {}
    for publicacao in bd:
        palavras = publicacao["keywords"].split(",")
        for palavra in palavras:
            palavra = palavra.strip()  
            if palavra in contador_palavras:
                contador_palavras[palavra] += 1
            else:
                contador_palavras[palavra] = 1


    palavras_ordenadas = sorted(contador_palavras.items(), key = lambda x: x[1], reverse = True)

    # Criar uma lista de opções com palavras-chave e as ocorrencias
    opcoes_palavras = [f"{palavra} ({freq} ocorrência/ocorrências)" for palavra, freq in palavras_ordenadas]

    
    formLayout = [
        [sg.Text('Selecione uma palavra-chave para consultar as publicações associadas:', font = ("Helvetica", 15))],
        [sg.Combo(opcoes_palavras, key = "-PALAVRA-", size = (50, 1), readonly = True)],
        [sg.Button('Inserir'), sg.Button('Cancelar')]
    ]

    wform = sg.Window('Consulta por Palavra-Chave', formLayout, location = (200, 300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent in ("Cancelar", sg.WIN_CLOSED):
        return  # Fechar a janela sem executar nada

    if inputEvent == "Inserir":
        palavra_selecionada = inputValues["-PALAVRA-"]
        if palavra_selecionada:
            # Extrair apenas a palavra-chave selecionada (removendo a contagem entre parênteses)
            palavra_chave = palavra_selecionada.split(" (")[0]

            # Filtrar publicações com a palavra-chave selecionada
            publicacoes = [
                publicacao for publicacao in bd if palavra_chave in publicacao["keywords"]
            ]

            if publicacoes:
                listar_publicacoes(publicacoes)
            else:
                sg.popup("Não existem publicações com a palavra-chave fornecida.", font = ("Helvetica", 15))

    return

def listar_por_palavra_chave_ordem_alfabetica(bd):
    palavras_chave = {}

    # Contagem das palavras-chave
    for publicacao in bd:
        palavras = publicacao["keywords"].split(",")  
        for palavra in palavras:
            palavra = palavra.strip()  
            if palavra in palavras_chave:
                palavras_chave[palavra] += 1
            else:
                palavras_chave[palavra] = 1

    
    palavras_ordenadas_alfabetica = sorted(palavras_chave.keys())

    opcoes_palavras_alfabetica = [f"{palavra}" for palavra in palavras_ordenadas_alfabetica]

    # Layout do formulário para selecionar palavra-chave
    formLayout = [
        [sg.Text('Selecione a palavra-chave para consultar as publicações associadas:', font = ("Helvetica", 15))],
        [sg.Combo(opcoes_palavras_alfabetica, key = "-PALAVRA-CHAVE-", size = (50, 1), readonly = True)],
        [sg.Button('Inserir'), sg.Button('Cancelar')]
    ]

    wform = sg.Window('Consulta de publicações por palavra-chave', formLayout, location = (200, 300), font = ("Helvetica", 15))
    inputEvent, inputValues = wform.read(close = True)

    if inputEvent == "Cancelar" or inputEvent == sg.WIN_CLOSED:
        wform.close()

    elif inputEvent == "Inserir":
        palavra_selecionada = inputValues["-PALAVRA-CHAVE-"]
        if palavra_selecionada:
            # Filtrar publicações com a palavra-chave selecionada
            publicacoes = [
                publicacao for publicacao in bd if palavra_selecionada in publicacao["keywords"]
            ]
            if publicacoes:
                listar_publicacoes(publicacoes)  
            else:
                sg.popup("Não existem publicações para a palavra-chave fornecida.", font = ("Helvetica", 15))

    return


def exportacao_por_pesquisa(dataset):
    # Solicitar ao usuário um critério de exportação
    formLayout = [
        [sg.Text("Selecione o tipo de filtro para a pesquisa:")],
        [sg.Button("Pesquisar por Título", key = "-TITULO-")],
        [sg.Button("Pesquisar por Autor", key = "-AUTOR-")],
        [sg.Button("Pequisar por Afiliação", key = "-AFILIACAO-")],
        [sg.Button("Pesquisar por Palavras-chave", key = "-PALAVRAS-CHAVE-")],
        [sg.Button("Pesquisar por Data de Publicação", key = "-DATA-")],
        [sg.Button("Pesquisar por Identificador", key = "-IDENTIFICADOR-")],
        [sg.Button("Cancelar")]
    ]

    window = sg.Window('Exportação por Pesquisa', formLayout, modal = True)
    event, _ = window.read(close = True)

    if event == 'Cancelar' or event == sg.WINDOW_CLOSED:
        sg.popup('Exportação cancelada.', title = 'Cancelado')
        return False

    criterio = event

    # Obter os valores disponíveis com base no critério selecionado
    opcoes = []
    if criterio == "-TITULO-":
        opcoes = sorted(set(publicacao.get('title', '') for publicacao in dataset if publicacao.get('title', '')))
    elif criterio == "-AUTOR-":
        opcoes = sorted(set(autor.get('name', '') for publicacao in dataset for autor in publicacao.get('authors', []) if autor.get('name', '')))
    elif criterio == "-AFILIACAO-":
        opcoes = sorted(set(autor.get('affiliation', '') for publicacao in dataset for autor in publicacao.get('authors', []) if autor.get('affiliation', '')))
    elif criterio == "-PALAVRAS-CHAVE-":
        opcoes = sorted(set(keyword.strip() for publicacao in dataset for keyword in publicacao.get('keywords', '').split(',') if keyword.strip()))
    elif criterio == "-DATA-":
        opcoes = sorted(set(publicacao.get('publish_date', '') for publicacao in dataset if publicacao.get('publish_date', '')))
    elif criterio == "-IDENTIFICADOR-":
        opcoes = sorted(set(publicacao.get('doi', '') for publicacao in dataset if publicacao.get('doi', '')))

    if not opcoes:
        sg.popup('Não há valores disponíveis para o critério selecionado.', title = 'Erro')
        return False

    layout_opcoes = [
        [sg.Text('Selecione uma opção:')],
        [sg.Listbox(values = opcoes, size = (40, 10), key = '-VALOR-')],
        [sg.Button('Confirmar'), sg.Button('Cancelar')]
    ]

    window_opcoes = sg.Window('Seleção de Valor', layout_opcoes, modal = True)
    event_opcoes, values_opcoes = window_opcoes.read(close = True)

    if event_opcoes == 'Cancelar' or not values_opcoes.get('-VALOR-'):
        sg.popup('Nenhum valor selecionado!', title = 'Erro')
        return False

    valor = values_opcoes['-VALOR-'][0]

    # Filtrar o dataset com base no critério fornecido
    publicacoes_filtradas = []

    for publicacao in dataset:
        if criterio == "-TITULO-":
            if valor.lower() == publicacao.get('title', '').lower():
                publicacoes_filtradas.append(publicacao)
        elif criterio == "-AUTOR-":
            autores = [autor.get('name', '').lower() for autor in publicacao.get('authors', [])]
            if valor.lower() in autores:
                publicacoes_filtradas.append(publicacao)
        elif criterio == "-AFILIACAO-":
            afiliacoes = [autor.get('affiliation', '').lower() for autor in publicacao.get('authors', [])]
            if valor.lower() in afiliacoes:
                publicacoes_filtradas.append(publicacao)
        elif criterio == "-PALAVRAS-CHAVE-":
            if valor.lower() in publicacao.get('keywords', '').lower():
                publicacoes_filtradas.append(publicacao)
        elif criterio == "-DATA-":
            if valor == publicacao.get('publish_date', ''):
                publicacoes_filtradas.append(publicacao)
        elif criterio == "-IDENTIFICADOR-":
            if valor == publicacao.get('doi', ''):
                publicacoes_filtradas.append(publicacao)

    if not publicacoes_filtradas:
        sg.popup('Nenhuma publicação encontrada com os critérios fornecidos.', title = 'Erro')
        return False

   
    salvarLayout = [
        [sg.Text('Introduza o nome do arquivo para exportar os dados:')],
        [sg.InputText(key = '-ARQUIVO-')],
        [sg.Button('Salvar'), sg.Button('Cancelar')]
    ]

    salvarWindow = sg.Window('Salvar Exportação', salvarLayout, modal = True)
    salvarEvent, salvarValues = salvarWindow.read(close = True)

    if salvarEvent == 'Cancelar' or salvarEvent == sg.WINDOW_CLOSED:
        sg.popup('Exportação cancelada.', title='Cancelado')
        return False

    arquivo = salvarValues['-ARQUIVO-']
    if not arquivo:
        sg.popup('Nome do arquivo não fornecido!', title = 'Erro')
        return False

    if ".json" not in arquivo[-5:]:
        arquivo += '.json'

    try:
        with open(arquivo, 'w', encoding = 'utf-8') as f:
            json.dump(publicacoes_filtradas, f, ensure_ascii = False, indent = 4)
        sg.popup(f'Exportação realizada com sucesso! Arquivo salvo como {arquivo}', title = 'Sucesso')
        return True
    except Exception as e:
        sg.popup(f'Erro ao salvar o arquivo: {e}', title = 'Erro')
        return False



def adicionar_bd(bdexistente):
    """
    Adiciona novas publicações da base de dados `bdnova` ao banco de dados `bdexistente`,
    com a opção de importar novas publicações a partir de um arquivo JSON.
    """
    
    identificadores = {publicacao["doi"] for publicacao in bdexistente if "doi" in publicacao}

    # Interface para selecionar o arquivo de novas publicações
    formLayout = [
        [sg.Text("Escolha o arquivo com as novas publicações (JSON):")],
        [sg.InputText(key = "-FICHEIRO-", enable_events = True), sg.FileBrowse(file_types = (("JSON Files", "*.json"),))],
        [sg.Button("Importar"), sg.Button("Cancelar")]
    ]

    wform = sg.Window("Importar Publicações", formLayout, location = (200, 300), font = ("Helvetica", 15))
    
    while True:
        inputEvent, inputValues = wform.read()
        
        if inputEvent == sg.WIN_CLOSED or inputEvent == "Cancelar":
            wform.close()
            return bdexistente  

        if inputEvent == "Importar":
            novo_arquivo = inputValues["-FICHEIRO-"]
            if not novo_arquivo:
                sg.popup_error("Nenhum arquivo foi selecionado. Operação cancelada.")
            else:
                # Carregar os novos dados do arquivo JSON
                novos_dados = carregar_dataset(novo_arquivo)

                # Verificar se o arquivo contém dados válidos
                if not novos_dados:
                    sg.popup_error("Falha ao carregar ou o arquivo está vazio.")
                else:
                    for nova_publicacao in novos_dados:
                        if "doi" in nova_publicacao:
                            if nova_publicacao["doi"] not in identificadores:
                                bdexistente.append(nova_publicacao)  
                                identificadores.add(nova_publicacao["doi"])  
                    listar_publicacoes(bdexistente)

            wform.close()
            return bdexistente  


