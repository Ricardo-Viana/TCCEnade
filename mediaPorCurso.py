import pandas as pd
import numpy as np
import requests
from io import BytesIO
from zipfile import ZipFile
import os
import re

def processa_respostas(ano, cod_grupo, valores_na, tipo_questao):
    if ano == 2021:
        url = 'https://download.inep.gov.br/microdados/microdados_enade_2021.zip'
    else:
        url = f'https://download.inep.gov.br/microdados/microdados_enade_{ano}_LGPD.zip'

    dir_path = f'./enade{ano}'
    if not os.listdir(dir_path):
        os.makedirs(dir_path)
    
        filebytes = BytesIO(
            requests.get(url).content
        )

        myzip = ZipFile(filebytes)
        myzip.extractall(dir_path)    

    if ano == 2021:
        df = pd.read_csv('enade2021/microdados_Enade_2021/2. DADOS/microdados2021_arq1.txt', delimiter = ';')
    else:
        df = pd.read_csv(f'enade{ano}/microdados_Enade_{ano}_LGPD/2. DADOS/microdados{ano}_arq1.txt', delimiter = ';')
    filtered_df = df[df['CO_GRUPO'] == cod_grupo]
    unique_courses = filtered_df['CO_CURSO'].unique()

    if tipo_questao == 'pandemia':
        
        if ano == 2021:
            files = os.listdir('enade2021/microdados_Enade_2021/2. DADOS')
            files_sorted_by_number = sorted(files, key=lambda x: int(re.search(fr'microdados2021_arq(\d+)', x).group(1)))
            latest_file = files_sorted_by_number[-1]
            df_respostas = pd.read_csv(f'enade2021/microdados_Enade_2021/2. DADOS/{latest_file}', delimiter = ';')
        elif ano > 2021:
            files = os.listdir(f'enade{ano}/microdados_Enade_{ano}/2. DADOS')
            files_sorted_by_number = sorted(files, key=lambda x: int(re.search(fr'microdados{ano}_arq(\d+)', x).group(1)))
            latest_file = files_sorted_by_number[-1]    
            df_respostas = pd.read_csv(f'enade{ano}/microdados_Enade_{ano}_LGPD/2. DADOS/{latest_file}', delimiter = ';')
        else:
            raise Exception('Ano não está incluso na pandemia')

        df_respostas_filtered = df_respostas[df_respostas['CO_CURSO'].isin(unique_courses)]

        colunas_respostas = [col for col in df_respostas_filtered.columns if col.startswith('QE_')]

        novos_nomes_colunas = [f"QE_{i+1}" for i in range(len(colunas_respostas))]

        renomear_dict = dict(zip(colunas_respostas, novos_nomes_colunas))

        df_respostas_filtered.rename(columns=renomear_dict, inplace=True)

        colunas_respostas = novos_nomes_colunas

    elif tipo_questao == 'percepção prova':

        if ano == 2021:
            df_respostas = pd.read_csv(f'enade2021/microdados_Enade_2021/2. DADOS/microdados2021_arq3.txt', delimiter = ';')
        else:    
            df_respostas = pd.read_csv(f'enade{ano}/microdados_Enade_{ano}_LGPD/2. DADOS/microdados{ano}_arq3.txt', delimiter = ';')
        
        df_respostas_filtered = df_respostas[df_respostas['CO_CURSO'].isin(unique_courses)]

        colunas_respostas = [col for col in df_respostas_filtered.columns if col.startswith('CO_RS')]

        df_respostas_filtered[colunas_respostas] = df_respostas_filtered[colunas_respostas].replace({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5})


    elif tipo_questao == 'processo formativo':
        if ano == 2021:
            df_respostas = pd.read_csv(f'enade2021/microdados_Enade_2021/2. DADOS/microdados2021_arq4.txt', delimiter = ';')
        else:
            df_respostas = pd.read_csv(f'enade{ano}/microdados_Enade_{ano}_LGPD/2. DADOS/microdados{ano}_arq4.txt', delimiter = ';')

        df_respostas_filtered = df_respostas[df_respostas['CO_CURSO'].isin(unique_courses)]

        colunas_respostas = [col for col in df_respostas_filtered.columns if col.startswith('QE_')]
        
    df_respostas_filtered[colunas_respostas] = df_respostas_filtered[colunas_respostas].replace(valores_na, np.nan)

    df_respostas_filtered = df_respostas_filtered.dropna(how='all', subset=colunas_respostas)

    media_respostas = df_respostas_filtered.groupby('CO_CURSO')[colunas_respostas].mean().reset_index()

    media_respostas['CO_GRUPO'] = cod_grupo

    return media_respostas

anos_input = input("Digite os anos a serem analisados (separados por vírgula, ex: 2019,2021,2022): ")
anos_list = [int(ano.strip()) for ano in anos_input.split(',')]

valores_na_input = input("Digite os valores a serem substituídos por NaN (separados por vírgula, ex: '*', '.'): ")
valores_na = [valor.strip().strip("'") for valor in valores_na_input.split(',')]

tipo_questao = input("Digite qual tipo de questão você quer gerar um relatório (pandemia, percepção prova ou processo formativo): ").lower()

df_cinerotulo = pd.read_csv('cinerotuloenade.csv')

metricas = pd.DataFrame()

for ano in anos_list:
    df_enade = df_cinerotulo[f'cod_enade_{ano}'].dropna() # Alterar para uma lista circular futuramente
    for cod_grupo in df_enade:
        resultado = processa_respostas(ano, cod_grupo, valores_na, tipo_questao)
        metricas = pd.concat([metricas, resultado], ignore_index=True)
    else:
        print(f"Ano {ano} não está disponível para análise.")

# Substituir pontos por vírgulas nos números
metricas = metricas.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

# Exportar o resultado
metricas.to_csv("Metricas_todos_cursos.csv", index=False, sep=';')