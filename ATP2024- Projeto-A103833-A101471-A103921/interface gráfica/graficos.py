import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def JanelaGrafico(plt):
    layout = [[sg.Canvas(key='-CANVAS-')],
              [sg.Button('OK')]]

    window = sg.Window('Gráfico', layout, location = (300,25), finalize = True, font = ("Helvetica", 15))

    canvas_elem = window['-CANVAS-']
    canvas = FigureCanvasTkAgg(plt.gcf(), canvas_elem.Widget)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    event, values = window.read()

    window.close()
    return


# 1. Distribuição de publicações por ano
def publicacoes_por_ano(bd):
    contagem_anos = {}
    for pub in bd:
        if 'publish_date' in pub:
            ano = pub['publish_date'].split('-')[0]
            if ano in contagem_anos:
                contagem_anos[ano] += 1
            else:
                contagem_anos[ano] = 1

    anos = []
    quantidades = []
    for ano, quantidade in contagem_anos.items():
        anos.append(ano)
        quantidades.append(quantidade)

    plt.figure(figsize = (10, 6))
    plt.bar(anos, quantidades, color = 'lightblue')
    plt.title('Distribuição de Publicações por Ano', fontdict = {'fontname': 'Arial Rounded MT Bold', 'fontsize': 12})
    plt.xlabel('Ano', fontdict = {'fontname': 'Arial Rounded MT Bold'})
    plt.ylabel('Número de Publicações', fontdict = {'fontname': 'Arial Rounded MT Bold'})
    plt.xticks(fontname = 'Arial Rounded MT Bold')
    plt.yticks(fontname = 'Arial Rounded MT Bold')
    plt.tight_layout()
    plt.show()

# 2. Distribuição de publicações por mês num ano específico
def publicacoes_por_mes(bd, ano_especifico):
    contagem_meses = {}
    for pub in bd:
        if 'publish_date' in pub:
            partes_data = pub['publish_date'].split('-')
            ano = partes_data[0]
            if ano == ano_especifico:
                mes = partes_data[1]
                if mes in contagem_meses:
                    contagem_meses[mes] += 1
                else:
                    contagem_meses[mes] = 1

    meses = []
    quantidades = []
    for mes, quantidade in contagem_meses.items():
        meses.append(mes)
        quantidades.append(quantidade)

    plt.figure(figsize = (10, 6))
    plt.bar(meses, quantidades, color = 'blue')
    plt.title(f'Distribuição de Publicações por Mês em {ano_especifico}', fontdict = {'fontname': 'Arial Rounded MT Bold', 'fontsize': 12})
    plt.xlabel('Mês', fontdict = {'fontname': 'Arial Rounded MT Bold'})
    plt.ylabel('Número de Publicações', fontdict = {'fontname': 'Arial Rounded MT Bold'})
    plt.xticks(fontname = 'Arial Rounded MT Bold')
    plt.yticks(fontname = 'Arial Rounded MT Bold')
    plt.tight_layout()
    plt.show()

# 3. Número de publicações por autor (top 20)
def publicacoes_por_autor(bd):
    contagem_autores = {}
    for pub in bd:
        if 'authors' in pub:
            for autor in pub['authors']:
                nome = autor['name']
                if nome in contagem_autores:
                    contagem_autores[nome] += 1
                else:
                    contagem_autores[nome] = 1

    autores_ordenados = sorted(contagem_autores.items(), key = lambda x: x[1], reverse = True)
    top_20 = autores_ordenados[:20]

    nomes = []
    quantidades = []
    for autor, quantidade in top_20:
        nomes.append(autor)
        quantidades.append(quantidade)

    plt.figure(figsize = (10, 6))
    plt.bar(nomes, quantidades, color = 'darkcyan')
    plt.title('Top 20 Autores com Mais Publicações', fontdict = {'fontname': 'Arial Rounded MT Bold', 'fontsize': 12})
    plt.xlabel('Autores', fontdict = {'fontname': 'Arial Rounded MT Bold'})
    plt.ylabel('Númerp de publicações', fontdict = {'fontname': 'Arial Rounded MT Bold'})
    plt.xticks(fontname = 'Arial Rounded MT Bold')
    plt.yticks(fontname = 'Arial Rounded MT Bold')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

# 4. Distribuição de publicações de um autor por ano
def publicacoes_de_autor_por_ano(bd, nome_autor):
    contagem_anos = {}
    for pub in bd:
        if 'authors' in pub:
            for autor in pub['authors']:
                if nome_autor.lower() in autor['name'].lower():
                    ano = pub['publish_date'].split('-')[0]
                    if ano in contagem_anos:
                        contagem_anos[ano] += 1
                    else:
                        contagem_anos[ano] = 1

    anos = []
    quantidades = []
    for ano, quantidade in contagem_anos.items():
        anos.append(ano)
        quantidades.append(quantidade)

    plt.figure(figsize = (10, 6))
    plt.bar(anos, quantidades, color = 'lightpink')
    plt.title(f'Distribuição de Publicações do Autor "{nome_autor}" por Ano', fontdict = {'fontname': 'Arial Rounded MT Bold', 'fontsize': 12})
    plt.xlabel('Ano', fontdict = {'fontname': 'Arial Rounded MT Bold'})
    plt.ylabel('Número de Publicações', fontdict = {'fontname': 'Arial Rounded MT Bold'})
    plt.xticks(fontname = 'Arial Rounded MT Bold')
    plt.yticks(fontname = 'Arial Rounded MT Bold')
    plt.tight_layout()
    plt.show()

# 5. Distribuição de palavras-chave (top 20)
def palavras_chave_mais_frequentes(bd):
    contagem_palavras = {}
    for pub in bd:
        if 'keywords' in pub:
            palavras = pub['keywords'].split(',')
            for palavra in palavras:
                palavra = palavra.strip()
                if palavra in contagem_palavras:
                    contagem_palavras[palavra] += 1
                else:
                    contagem_palavras[palavra] = 1

    palavras_ordenadas = sorted(contagem_palavras.items(), key = lambda x: x[1], reverse=True)
    top_20 = palavras_ordenadas[:20]

    palavras = []
    frequencias = []
    for palavra, frequencia in top_20:
        palavras.append(palavra)
        frequencias.append(frequencia)

    plt.figure(figsize = (10, 6))
    plt.bar(palavras, frequencias, color = 'cyan')
    plt.title('Palavras-chave Mais Frequentes (Top 20)', fontdict = {'fontname': 'Arial Rounded MT Bold', 'fontsize': 12})
    plt.xlabel('Palvras-chave', fontdict = {'fontname': 'Arial Rounded MT Bold'})
    plt.ylabel('Frequência', fontdict = {'fontname': 'Arial Rounded MT Bold'})
    plt.xticks(fontname = 'Arial Rounded MT Bold')
    plt.yticks(fontname = 'Arial Rounded MT Bold')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

# 6. Palavras-chave mais frequentes por ano
def palavras_chave_por_ano_pie(bd):
    # Coleta todos os anos disponíveis no dataset
    anos_disponiveis = []
    for pub in bd:
        if 'publish_date' in pub:
            ano = pub['publish_date'].split('-')[0]
            if ano not in anos_disponiveis:  
                anos_disponiveis.append(ano)
    
    anos_disponiveis.sort() 

    # Cria uma janela para o usuário selecionar o ano
    layout = [
        [sg.Text("Selecione o ano para gerar o gráfico:")],
        [sg.Combo(values = anos_disponiveis, size = (10, 1), key = "-ANO-", readonly = True)],
        [sg.Button("OK"), sg.Button("Cancelar")]
    ]
    window = sg.Window("Seleção de Ano", layout)

    ano_selecionado = None
    consulta_ativa = True
    while consulta_ativa:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            consulta_ativa = False
        elif event == "OK" and values["-ANO-"]:
            ano_selecionado = values["-ANO-"]
            consulta_ativa = False

    window.close()

    # Se nenhum ano foi selecionado, encerra a função
    if not ano_selecionado:
        return

    # Gera o gráfico apenas para o ano selecionado
    palavras_por_ano = {}
    for pub in bd:
        if 'publish_date' in pub and 'keywords' in pub:
            ano = pub['publish_date'].split('-')[0]
            if ano == ano_selecionado:
                palavras = pub['keywords'].split(',')
                if ano not in palavras_por_ano:
                    palavras_por_ano[ano] = {}
                for palavra in palavras:
                    palavra = palavra.strip()
                    if palavra in palavras_por_ano[ano]:
                        palavras_por_ano[ano][palavra] += 1
                    else:
                        palavras_por_ano[ano][palavra] = 1

    # Seleciona as 5 palavras mais frequentes para o ano escolhido
    palavras = []
    frequencias = []
    if ano_selecionado in palavras_por_ano:
        palavras_ordenadas = sorted(palavras_por_ano[ano_selecionado].items(), key = lambda x: x[1], reverse = True)
        top_palavras = palavras_ordenadas[:5]

        palavras = [item[0] for item in top_palavras]
        frequencias = [item[1] for item in top_palavras]

    # Gera o gráfico de pizza
    if palavras and frequencias:
        plt.figure(figsize=(8, 8))
        plt.pie(frequencias, labels = palavras, autopct = '%1.1f%%', startangle = 90, colors = ['blue', 'cyan', 'lightblue', 'darkblue', 'skyblue'])
        plt.title(f'Top Palavras-chave Mais Frequentes em {ano_selecionado}', fontdict = {'fontname': 'Arial Rounded MT Bold', 'fontsize': 12})
        plt.show()
    else:
        sg.popup(f"Não há dados de palavras-chave para o ano {ano_selecionado}.", title = "Erro")


