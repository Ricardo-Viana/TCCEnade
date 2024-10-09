import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import wget

def relacionarTabelas(ano):
    dir_path = f'./ConceitoEnade'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if not os.path.exists(f"ConceitoEnade/ConceitoEnade{ano}.xls"):
        # URL da página web que contém os links de download
        url = f'https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-de-qualidade-da-educacao-superior/{ano}' # Link fixo só muda o último componente que depende do ano

        # Fazer a solicitação HTTP
        response = requests.get(url)

        # Verificar se a solicitação foi bem-sucedida
        if response.status_code == 200:
            # Parsear o conteúdo HTML com BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Encontrar todos os links de download (normalmente, estão em tags <a>)
            links = soup.find_all('a', href=True)

            # Iterar sobre os links encontrados e exibir ou filtrar os links de download
            for link in links:
                href = link['href']
                # Filtrar os links que contenham a palavra "download" ou outro critério desejado
                if 'download' in href and (href.endswith('.xlsx') or href.endswith('.xls')):  # Exemplo de filtro
                    wget.download(href, f"ConceitoEnade/ConceitoEnade{ano}.xls")
                    break

if __name__ == '__main__':
    relacionarTabelas(2021)