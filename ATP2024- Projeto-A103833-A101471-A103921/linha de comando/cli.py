from datetime import datetime
from prettytable import PrettyTable
from unidecode import unidecode
import funcoes
import json

def linha(file):
    stop = False
    print("BEM VINDO À ATA MÉDICA")
    while not stop:
        print("\nEscreva 'help' para ver a lista de comandos ou '16' para sair.")
        comando = input("Escolha um comando: ").strip().lower().replace("'", "").replace('"', "")
        if comando=="help":
            print_help()
        elif comando == "1": #funciona
            criar(file)
        elif comando == "2": #funciona
            consultar(file)
        elif comando == "3": #funciona, colocar sem aspas
            consultar_doi(file)
        elif comando== "4": #funciona, colocar sem aspas
            consultar_titulo(file)
        elif comando == "5": #funciona, colocar sem aspas
            consultar_autor(file)
        elif comando == "6":#funciona, colovar sem aspas
            consultar_afiliacao(file)
        elif comando == "7":#funciona, colovar sem aspas
            consultar_keywords(file)
        elif comando == "8":#funciona, colovar sem aspas
            consultar_data(file)
        elif comando == "9": #funciona
            listar_autores(file)
        elif comando == "10": #funciona
            relatorio_estatisticas_freq_key(file)
        elif comando == "11": #funciona
            relatorio_estatisticas_pub_autor(file)
        elif comando == "12":#funciona
            relatorio_estatisticas_pub_ano(file)
        elif comando == "13":#funciona
            eliminar_pub(file)
        elif comando == "14":#funciona
            importar_novos_dados(file)
        elif comando== "15": #funciona, novo ficheiro é criado
            guardar_dataset(file)
        elif comando == "16":#funciona
            print("Saiu do programa")
            stop = True
        else:
            print("Instrução inválida") #funciona



def print_help():
    print("Comandos disponíveis:")
    print("  1 - Cria uma nova publicação.")
    print("  2 - Consultar publicações.")
    print("  3 - Consulta de publicação com o identificador.")
    print("  4 - Consultar publicações por título.")
    print("  5 - Consultar publicações por autor.")
    print("  6 - Consultar publicações por afiliação.")
    print("  7 - Consultar publicações por palavras-chave.")
    print("  8 - Consultar publicações por data de publicação.")
    print("  9 - Listar Autores.")
    print("  10 - Relatório de Estatísticas - Frequência de Palavras-Chave.")
    print("  11 - Relatório de Estatísticas - Pubicações por Autor.")
    print("  12 - Relatório de Estatísticas - Publicações por Ano.")
    print("  13 - Eliminar publicação.")
    print("  14 - Importar novos dados.")
    print("  15 - Guardar informação em memória.")
    print("  16 - Sai do programa.")
    print("  help - Exibe esta mensagem de ajuda.")



    
def criar(publicacoes):
    """
    Adiciona uma nova publicação à lista de publicações existente.
    """
    criada = False
    while not criada:
        print("Iniciando o processo de criação de uma nova publicação...")

        titulo = input("Escreva o título da publicação: ").strip()
        data_publicacao = None
        while not data_publicacao:
            data_str = input("Escreva a data da publicação (formato ANO-MES-DIA): ").strip()
            try:
                data_publicacao = datetime.strptime(data_str, "%Y-%m-%d").date()
            except ValueError:
                print("Formato de data inválido. Tente novamente.")

        autores_lista = []
        while not autores_lista:
            autores_input = input("Escreva os nomes dos autores (separados por vírgula): ").strip()
            autores_lista = [autor.strip() for autor in autores_input.split(",") if autor.strip()]
            if not autores_lista:
                print("Você deve informar pelo menos um autor.")

        afiliacoes_lista = []
        while not afiliacoes_lista or len(afiliacoes_lista) != len(autores_lista):
            afiliacoes_input = input(f"Escreva as afiliações dos autores (separadas por vírgula, uma para cada autor): ").strip()
            afiliacoes_lista = [afiliacao.strip() for afiliacao in afiliacoes_input.split(",") if afiliacao.strip()]
            if len(afiliacoes_lista) != len(autores_lista):
                print(f"O número de afiliações ({len(afiliacoes_lista)}) não corresponde ao número de autores ({len(autores_lista)}). Tente novamente.")

        resumo_publicacao = input("Escreva o resumo da publicação: ").strip()
        while not resumo_publicacao:
            print("O resumo não pode estar vazio. Tente novamente.")
            resumo_publicacao = input("Escreva o resumo da publicação: ").strip()

        palavras_chave_lista = []
        while not palavras_chave_lista:
            try:
                num_palavras = int(input("Quantas palavras-chave tem a publicação? "))
                palavras_chave_lista = [input(f"Escreva a palavra-chave {i + 1}: ").strip() for i in range(num_palavras)]
                palavras_chave_lista = [p for p in palavras_chave_lista if p]
                if not palavras_chave_lista:
                    print("Nenhuma palavra-chave válida foi inserida. Tente novamente.")
            except ValueError:
                print("Número inválido. Tente novamente.")

        pdf_publicacao = input('Escreva o link do PDF da publicação: ').strip()
        doi_publicacao = input('Escreva o DOI da publicação: ').strip()
        url_publicacao = input('Escreva o URL da publicação: ').strip()

        nova_publicacao = {
            "title": titulo,
            "publish_date": str(data_publicacao),
            "authors": [{"name": autores_lista[i], "affiliation": afiliacoes_lista[i]} for i in range(len(autores_lista))],
            "abstract": resumo_publicacao,
            "keywords": palavras_chave_lista,
            "pdf": pdf_publicacao,
            "doi": doi_publicacao,
            "url": url_publicacao,
        }

        publicacoes.append(nova_publicacao)
        criada = True
        print("Publicação criada com sucesso!")
    
def ver_publicacoes(file):
    linhas = []
    for publicacao in file:
        linha = [
            publicacao["title"], 
            publicacao["publish_date"],
            publicacao["keywords"],
            ", ".join([autor['name'] for autor in publicacao["authors"]]),  
            publicacao["doi"],
            publicacao["url"]
        ]
        linhas.append(linha)
    return linhas

def truncar_texto(texto, limite):
    """Trunca o texto se exceder o limite de caracteres."""
    return texto if len(texto) <= limite else texto[:limite] + "..."

def consultar(file):
    """Exibe os dados no formato de tabela com melhorias de exibição."""
    tabela = PrettyTable(['#', 'Title', 'Publish Date', 'Keywords', 'Authors', 'DOI', 'URL'])
    tabela.align = "l"  
    tabela.align['DOI'] = "r"  
    tabela.align['URL'] = "r"  
    
    for idx, linha in enumerate(ver_publicacoes(file), start=1):
        tabela.add_row([
            idx,
            truncar_texto(linha[0], 15),  
            truncar_texto(linha[1], 10),
            truncar_texto(linha[2], 10),  
            truncar_texto(linha[3], 25),  
            truncar_texto(linha[4], 15),  
            truncar_texto(linha[5], 15)   
        ])
    print(tabela)


def verificar_doi(file):
    """Retorna a lista de DOIs presentes no arquivo."""
    return [publicacao['doi'] for publicacao in file if 'doi' in publicacao]

def encontra_publicacao_doi(file, doi):
    """Encontra uma publicação específica usando o DOI."""
    publicacoes_doi = []
    for publicacao in ver_publicacoes(file):
        if publicacao[4] == doi:  
            publicacoes_doi.append(publicacao)
    return publicacoes_doi

def consultar_doi(file):
    """Consulta a publicação com o DOI fornecido pelo utilizador."""
    feito = False
    while not feito:
        doi_utilizador = input('Escreva o DOI da publicação (sem "https://doi.org/"):').strip()
        
        # Adiciona o prefixo "https://doi.org/" ao DOI inserido, se necessário
        doi_publicacao = "https://doi.org/" + doi_utilizador
        
        # Verifica se o DOI fornecido (com o prefixo "https://doi.org/") existe no arquivo
        if doi_publicacao not in verificar_doi(file):
            print("DOI inválido.")
        else:
            feito = True
    
    print("Publicação: \n")
    publicacao = encontra_publicacao_doi(file, doi_publicacao)[0]  
    tabela = PrettyTable(['#', 'Title', 'Publish Date', 'Keywords', 'Authors', 'DOI', 'URL'])
    tabela.align = "l" 
    tabela.align['DOI'] = "r"  
    tabela.align['URL'] = "r"  

    tabela.add_row([  
        1,  # Número da publicação
        truncar_texto(publicacao[0], 20),  
        truncar_texto(publicacao[1], 10),  
        truncar_texto(publicacao[2], 20),  
        truncar_texto(publicacao[3], 25),  
        truncar_texto(publicacao[4], 15),  
        truncar_texto(publicacao[5], 15)   
    ])
    
    print(tabela)
    

def verificar_titulo(file):
    """Retorna a lista de títulos presentes no arquivo para comparação exata."""
    titulo = []
    for publicacao in file:
        if publicacao['title'] not in titulo:
            titulo.append(publicacao['title'])
    return titulo

def encontra_publicacao_titulo(file, titulo):
    """Encontra uma publicação específica usando o título como string exata."""
    publicacoes_titulo = []
    for publicacao in file:
        if publicacao['title'] == titulo: 
            publicacoes_titulo.append(publicacao)
    return publicacoes_titulo

def consultar_titulo(file):
    """Consulta a publicação com o título fornecido pelo utilizador."""
    feito = False
    while not feito:
        titulo_publicacao = input("Escreva o título da publicação:")
        if titulo_publicacao not in verificar_titulo(file):
            print("Título inválido.")
        else:
            feito = True
    
    print("Publicação: \n")
    publicacao = encontra_publicacao_titulo(file, titulo_publicacao)[0]  
    tabela = PrettyTable(['Title', 'Publish Date', 'Keywords', 'Authors', 'DOI', 'URL'])
    tabela.align = "l"  
    tabela.align['DOI'] = "r"  
    tabela.align['URL'] = "r"  

    tabela.add_row([  
        truncar_texto(publicacao["title"],20),  
        truncar_texto(publicacao["publish_date"], 10),  
        truncar_texto(publicacao["keywords"], 20),  
        truncar_texto(", ".join([autor['name'] for autor in publicacao["authors"]]), 25),  
        truncar_texto(publicacao["doi"], 15),  
        truncar_texto(publicacao["url"], 15)   
    ])
    
    print(tabela)

def verificar_autor(file):
    """Retorna a lista de autores presentes no arquivo para comparação exata."""
    autores = []
    for publicacao in file:
        for autor in publicacao["authors"]:
            nome_autor = autor['name']
            if nome_autor not in autores:
                autores.append(nome_autor)
    return autores

def encontra_publicacao_autor(file, nome_autor):
    """Encontra as publicações de um autor específico usando o nome do autor."""
    publicacoes_autor = []
    for publicacao in file:
        for autor in publicacao["authors"]:
            # Comparação exata 
            if nome_autor.strip().lower() == autor['name'].strip().lower():  
                publicacoes_autor.append(publicacao)
    return publicacoes_autor

def consultar_autor(file):
    """Consulta as publicações de um autor fornecido pelo utilizador."""
    feito = False
    while not feito:
        nome_autor = input("Escreva o nome do autor do qual pretende consultar a publicação:")
        if nome_autor.strip().lower() not in [autor.lower() for autor in verificar_autor(file)]:
            print("Autor inválido.")
        else:
            feito = True
    
    print("Publicações do autor: \n")
    publicacoes = encontra_publicacao_autor(file, nome_autor) 
    if not publicacoes:
        print("Nenhuma publicação encontrada para o autor.")
        return

    tabela = PrettyTable(['Title', 'Publish Date', 'Keywords', 'Authors', 'DOI', 'URL'])
    tabela.align = "l"  
    tabela.align['DOI'] = "r"  
    tabela.align['URL'] = "r"  

    for publicacao in publicacoes:  # Agora percorremos a lista de publicações
        tabela.add_row([  
            truncar_texto(publicacao["title"],20),  
            truncar_texto(publicacao["publish_date"], 10),  
            truncar_texto(publicacao["keywords"], 20),  
            truncar_texto(", ".join([autor['name'] for autor in publicacao["authors"]]), 25),  
            truncar_texto(publicacao["doi"], 15),  
            truncar_texto(publicacao["url"], 15)   
        ])
    
    print(tabela)
    


def verificar_afiliacao(file):
    """Retorna a lista de afiliações presentes no arquivo para comparação."""
    afiliacoes = []
    for publicacao in file:
        for aut in publicacao["authors"]:
            afiliacao = aut["affiliation"]
            if afiliacao not in afiliacoes:
                afiliacoes.append(afiliacao)
    return afiliacoes

def encontra_publicacao_afiliacao(file, afiliacao):
    """Encontra as publicações associadas a uma afiliação específica."""
    res = []
    for publicacao in file:
        for afi in publicacao["authors"]:
            if afi["affiliation"] == afiliacao:  
                res.append(publicacao)
    return res

def consultar_afiliacao(file):
    """Consulta a publicação com a afiliação fornecida pelo utilizador."""
    feito = False
    while not feito:
        afiliacao_publicacao = input("Escreva a afiliação da publicação que pretende consultar:").strip()
        if afiliacao_publicacao not in verificar_afiliacao(file):
            print("Afiliação inválida.")
        else:
            feito = True
    
    print("Publicações dessa afiliação: \n")
    publicacoes = encontra_publicacao_afiliacao(file, afiliacao_publicacao)
    if not publicacoes:
        print("Nenhuma publicação encontrada para a afiliação.")
        return

    tabela = PrettyTable(['Title', 'Publish Date', 'Keywords', 'Authors', 'DOI', 'URL'])
    tabela.align = "l"  
    tabela.align['DOI'] = "r"  
    tabela.align['URL'] = "r"  

    for publicacao in publicacoes:  
        tabela.add_row([  
            truncar_texto(publicacao["title"],20),  
            truncar_texto(publicacao["publish_date"], 10),  
            truncar_texto(publicacao["keywords"], 20),  
            truncar_texto(", ".join([autor['name'] for autor in publicacao["authors"]]), 25),  
            truncar_texto(publicacao["doi"], 15),  
            truncar_texto(publicacao["url"], 15)   
        ])
    
    print(tabela)
    
    
def verificar_keywords(file):
    palavras_chave_unicas = set()  
    # Separar palavras-chave e adicioná-las ao conjunto
    for publicacao in file:
        if "keywords" in publicacao:
            if isinstance(publicacao["keywords"], list):
                for palavra in publicacao["keywords"]:
                    palavras_chave_unicas.add(palavra.strip())  
            elif isinstance(publicacao["keywords"], str):
                palavras_chave = publicacao["keywords"].split(",")  
                for palavra in palavras_chave:
                    palavras_chave_unicas.add(palavra.strip())  
    return palavras_chave_unicas

def encontra_publicacao_keywords(file, keyw):
    publicacoes = []  
    for publicacao in file:
        if "keywords" in publicacao:
            if isinstance(publicacao["keywords"], list):
                if keyw in [palavra.strip() for palavra in publicacao["keywords"]]: 
                    publicacoes.append(publicacao)  
            elif isinstance(publicacao["keywords"], str):
                palavras_chave = publicacao["keywords"].split(",")  
                if keyw in [palavra.strip() for palavra in palavras_chave]:  
                    publicacoes.append(publicacao)  
    return publicacoes

def consultar_keywords(file):
    feito = False
    while not feito:
        keyword_publicacao = str(input("Escreva uma palavra-chave: ")).strip()
        if keyword_publicacao not in verificar_keywords(file):
            print("Palavra-chave inválida.")
        else:
            feito = True
            
    print("Publicações com a palavra-chave:", keyword_publicacao, "\n")
    publicacoes = encontra_publicacao_keywords(file, keyword_publicacao)
    
    if not publicacoes: 
        print("Nenhuma publicação encontrada para a palavra-chave.")
        return
    
    # Exibe as publicações encontradas
    tabela = PrettyTable(['Title', 'Publish Date', 'Keywords', 'Authors', 'DOI', 'URL'])
    tabela.align = "l"  
    tabela.align['DOI'] = "r"  
    tabela.align['URL'] = "r"  

    for publicacao in publicacoes: 
        keywords_truncado = ", ".join(publicacao["keywords"]) if isinstance(publicacao["keywords"], list) else publicacao["keywords"]
        
        tabela.add_row([  
            truncar_texto(publicacao["title"], 15),  
            truncar_texto(publicacao["publish_date"], 10),  
            truncar_texto(keywords_truncado, 20),  
            truncar_texto(", ".join([autor['name'] for autor in publicacao["authors"]]), 20),  
            truncar_texto(publicacao["doi"], 10),  
            truncar_texto(publicacao["url"], 10)   
        ])
    
    print(tabela)

def verificar_data(file):
    """Extrai todas as datas de publicação disponíveis no arquivo."""
    datas = set()  
    for publicacao in file:
        if "publish_date" in publicacao:
            datas.add(publicacao["publish_date"].replace("-", "").strip())
    return datas


def encontra_publicacao_data_publicacao(file, data):
    """Encontra publicações que correspondem à data fornecida."""
    res = []
    for publicacao in file:
        if "publish_date" in publicacao and publicacao["publish_date"].replace("-", "").strip().upper() == data.upper():
            res.append(publicacao)
    return res


def consultar_data(file):
    feito = False
    while not feito:
        data_publicacao = input("Escreva a data de publicação da publicação que pretende consultar (YYYY-MM-DD): ").strip().replace("-", "")
        if data_publicacao not in verificar_data(file):
            print("Data inválida. Tente novamente.")
        else:
            feito = True
    
    print("Publicações com a data de publicação:", data_publicacao, "\n")    
    publicacoes = encontra_publicacao_data_publicacao(file, data_publicacao)

    if not publicacoes:  
        print("Nenhuma publicação encontrada para a data fornecida.")
        return

    
    tabela = PrettyTable(['Title', 'Publish Date', 'Keywords', 'Authors', 'DOI', 'URL'])
    tabela.align = "l" 
    tabela.align['DOI'] = "r"  
    tabela.align['URL'] = "r"  
    for publicacao in publicacoes:  
        if isinstance(publicacao, dict):  
            tabela.add_row([  
                truncar_texto(publicacao["title"], 20),  
                truncar_texto(publicacao["publish_date"], 10),  
                truncar_texto(publicacao["keywords"], 20),  
                truncar_texto(", ".join([autor['name'] for autor in publicacao["authors"]]), 25),  
                truncar_texto(publicacao["doi"], 15),  
                truncar_texto(publicacao["url"], 15)   
            ])
        else:
            print(f"A publicação {publicacao} não é um dicionário válido.")
    
    print(tabela)



def listar_autores(file):
    """Lista todos os autores e as suas publicações associadas."""
    autores_publicacoes = {}

    # Construindo o dicionário de autores e as suas publicações
    for publicacao in file:
        for autor in publicacao.get("authors", []):
            nome_autor = autor.get("name", "N/A")
            if nome_autor not in autores_publicacoes:
                autores_publicacoes[nome_autor] = []
            autores_publicacoes[nome_autor].append(publicacao.get("title", "N/A"))

    # Exibindo o resultado em formato de tabela
    print("\nLista de Autores e Titulos das Publicações:\n")
    tabela = PrettyTable(['Authors', 'Title'])
    for autor, publicacoes in autores_publicacoes.items():
        # Truncar o nome do autor e os títulos das publicações
        autor_truncado = truncar_texto(autor, 40)
        titulos_truncados = ", ".join([truncar_texto(titulo, 70) for titulo in publicacoes])

        # Adicionando os dados na tabela
        tabela.add_row([ autor_truncado, titulos_truncados])

    print(tabela)


def relatorio_estatisticas_freq_key(file):
    """
    Gera estatísticas sobre a frequência de palavras-chave nas publicações.
    """
    contador_palavras = {}
    for publicacao in file:
        if isinstance(publicacao["keywords"], list):
            palavras = publicacao["keywords"]
        elif isinstance(publicacao["keywords"], str):
            palavras = publicacao["keywords"].split(",")  
        else:
            palavras = []  

        # Contabiliza as palavras-chave
        for palavra in palavras:
            palavra = palavra.strip()  
            if palavra:  
                if palavra in contador_palavras:
                    contador_palavras[palavra] += 1
                else:
                    contador_palavras[palavra] = 1

    # Ordenar palavras-chave por frequência (decrescente)
    palavras_chave_ordenadas = sorted(contador_palavras.items(), key = lambda x: x[1], reverse = True)
    
    print("\nRelatório de Frequência de Palavras-Chave:\n")
    for palavra, freq in palavras_chave_ordenadas:
        print(f"{palavra}: {freq} ocorrências")
        

def relatorio_estatisticas_pub_autor(file):
    """
    Gera estatísticas sobre o número de publicações por autor.
    """
    autores_freq = {}
    for publicacao in file:
        for autor in publicacao["authors"]:
            nome = autor["name"]
            if nome in autores_freq:
                autores_freq[nome] += 1
            else:
                autores_freq[nome] = 1
                
    autores_ordenados = sorted(autores_freq.items(), key = lambda x: x[1], reverse = True)
                
    print("\nRelatório de Frequência de Publicações por Autor:\n")
    for palavra, freq in autores_ordenados:
        print(f"{palavra}: {freq} ocorrências")
    
    
def relatorio_estatisticas_pub_ano(file):
    """
    Gera estatísticas sobre o número de publicações por ano.
    """
    anos_freq = {}
    for publicacao in file:
        if "publish_date" in publicacao:
            ano = publicacao["publish_date"].split("-")[0]  # Extrair o ano
            if ano in anos_freq:
                anos_freq[ano] += 1
            else:
                anos_freq[ano] = 1

    # Ordenar anos por número de publicações (decrescente)
    anos_ordenados = sorted(anos_freq.items(), key = lambda x: x[1], reverse = True)
    
    print("\nRelatório de Frequência de Publicações por Ano:\n")
    for palavra, freq in anos_ordenados:
        print(f"{palavra}: {freq} ocorrências")

def eliminar_pub(file):
    """
    Elimina uma publicação com base no título fornecido diretamente do dataset.
    """
    feito = False
    while not feito:
        titulo_eliminar = input("Escreva o título da publicação que pretende eliminar: ").strip()
        titulos_existentes = verificar_titulo(file)

        if titulo_eliminar not in titulos_existentes:
            print("Título inválido. Tente novamente.")
        else:
            feito = True

    i = 0
    while i < len(file):  
        if file[i]['title'] == titulo_eliminar:
            file.pop(i)
            print(f"A publicação '{titulo_eliminar}' foi eliminada definitivamente do dataset.")
        else:
            i += 1
    with open('ata_medica_teste1.json', 'w', encoding = 'utf-8') as f:
        json.dump(file, f, indent = 2, ensure_ascii = False)

    print("\nPublicações Existentes:\n")
    tabela = PrettyTable(['Title', 'Publish Date', 'Keywords', 'Authors', 'DOI', 'URL'])

    for publicacao in file: 
        keywords = ", ".join(publicacao["keywords"]) if isinstance(publicacao["keywords"], list) else publicacao["keywords"]

        tabela.add_row([
            truncar_texto(publicacao["title"], 20),  
            truncar_texto(publicacao["publish_date"], 10),  
            truncar_texto(keywords, 20),  
            truncar_texto(", ".join([autor['name'] for autor in publicacao["authors"]]), 20),  
            truncar_texto(publicacao["doi"], 15),  
            truncar_texto(publicacao["url"], 15)   
        ])

    print(tabela)


def carregar_dataset(ficheiro):
    res = []
    try:
        with open(ficheiro, encoding = 'UTF-8') as f: #igual a ter f = open(ficheiro) mas este fecha o ficheiro automaticamente
            res = json.load(f)
            print(f"Dataset carregado com sucesso!\n Foram lidos {len(res)} registos.")
    except Exception as e:
        print(f"Erro ao carregar o dataset: {e}")
    return res


def importar_novos_dados(file):
    novo_arquivo = input("Insira o caminho ou nome do arquivo JSON com os novos dados: ").strip()

    identificadores = {publicacao["doi"] for publicacao in file if "doi" in publicacao}
    novos_dados = carregar_dataset(novo_arquivo)
    
    if not novos_dados:
       print("Falha ao carregar ou o arquivo está vazio.")
    else:
        # Adicionar as novas publicações à base de dados existente
        for nova_publicacao in novos_dados:
            if "doi" in nova_publicacao:
                if nova_publicacao["doi"] not in identificadores:
                    file.append(nova_publicacao)  
                    identificadores.add(nova_publicacao["doi"])  
                    
    print("\nPublicações Atualizadas:\n")
    tabela = PrettyTable(['Title', 'Publish Date', 'Keywords', 'Authors', 'DOI', 'URL'])
    for publicacao in file:
        # Usando .get() para garantir que não ocorra um KeyError se a chave estiver ausente
        title = truncar_texto(publicacao.get("title", "Título não disponível"), 20)
        publish_date = truncar_texto(publicacao.get("publish_date", "Data não disponível"), 10)
        keywords = truncar_texto(", ".join(publicacao.get("keywords", "").split(',')), 20)
        authors = truncar_texto(", ".join([autor.get('name', 'Autor não disponível') for autor in publicacao.get("authors", [])]), 20)
        doi = truncar_texto(publicacao.get("doi", "DOI não disponível"), 15)
        url = truncar_texto(publicacao.get("url", "URL não disponível"), 15)

        tabela.add_row([title, publish_date, keywords, authors, doi, url])
    
    print(tabela)
    
    
def guardar_dataset(file):
    nome = input("Digite o nome do arquivo (sem extensão .json): ").strip()
    if nome.endswith(".json"):  # Verifica se o nome já contém a extensão
        nome = nome[:-5]  # Remove a extensão se estiver presente
    fnome = nome + ".json"  

    try:
        with open(fnome, "w", encoding = "utf-8") as fout:
            json.dump(file, fout, indent = 4, ensure_ascii = False) 
        print(f"Dataset guardado com sucesso no arquivo: {fnome}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

    return fnome  



def carregar_arquivo(file_name):
    """Carrega o arquivo JSON e retorna uma lista de publicações."""
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)

ficheiro = carregar_arquivo('ata_medica_teste2.json')
linha(ficheiro)