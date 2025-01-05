import json
import os
from datetime import datetime


import os
import json

def criar_publicacao(file, ti, data, aut, afi, res, pal_cha, pdf_pub, doi_pub, url_pub):
    """
    Adiciona uma nova publicação a um arquivo JSON no formato fornecido.

    Parâmetros:
        file (str): Nome do arquivo JSON onde as publicações serão salvas.
        ti (str): Título da publicação.
        data (str): Data de publicação no formato 'YYYY-MM-DD'.
        aut (list): Lista de nomes dos autores.
        afi (list): Lista de afiliações correspondentes aos autores.
        res (str): Resumo da publicação.
        pal_cha (list): Lista de palavras-chave.
        pdf_pub (str): Link do PDF da publicação.
        doi_pub (str): DOI da publicação.
        url_pub (str): URL da publicação.
    """

    if not isinstance(file, str):
        raise TypeError(f"O argumento 'file' deve ser uma string, mas recebeu {type(file).__name__}.")
    
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)

    # Inicializa o conteúdo do arquivo
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="UTF-8") as fread:
            try:
                publicacoes = json.load(fread)
            except json.JSONDecodeError:
                print(f"Arquivo {file} está corrompido. Inicializando como vazio.")
                publicacoes = []
    else:
        publicacoes = []  # Inicializa vazio caso o arquivo não exista
        
    pal_cha_str = ", ".join(pal_cha) 
    # Normaliza autores e afiliações
    autores = []
    for i, autor in enumerate(aut):
        afiliacao = afi[i] if i < len(afi) else "N/A"  
        autores.append({"name": autor, "affiliation": afiliacao})

    # Adiciona a nova publicação
    publi = {
        "abstract": res,
        "keywords": pal_cha_str,
        "authors": autores,
        "doi": doi_pub,
        "pdf": pdf_pub,
        "publish_date": data,
        "title": ti,
        "url": url_pub,
    }
    publicacoes.append(publi)

    # Salva no arquivo JSON
    with open(file_path, "w", encoding="UTF-8") as fwork:
        json.dump(publicacoes, fwork, indent=2, ensure_ascii=False)

    print(f"Publicação '{ti}' adicionada com sucesso ao arquivo {file}.")
    
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
    